#!/usr/bin/env python
# coding: utf-8

# In[2]:

import os
import json
from dotenv import load_dotenv
from IPython.display import Markdown, display, update_display
from openai import OpenAI
from docx import Document

# In[3]:
#tabulate is needed only for running this in terminal as python script
get_ipython().system('pip install tabulate python-dotenv openai python-docx')

# In[4]:

class ReqDoc:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        """
        Reads the content of a .docx file and returns the paragraphs as a list of strings.
        """
        try:
            # Check if the file exists
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"The file {self.file_path} was not found.")

            # Attempt to open and read the document
            doc = Document(self.file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text

        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# In[5]:

# Initialize and constants

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj') and len(api_key)>10:
    print("API key looks good so far")
else:
    print("There might be a problem with your API key. Please check!")
    
MODEL = 'gpt-4o-mini'
openai = OpenAI()

# In[6]:

#Set up system prompt for extracting just the requirements from the document

req_doc_system_prompt = "You are provided with a complete requirements specifications document. \
You are able to decide which content from that document are related to actual requirements, identify each requirement as \
functional or non-functional and list them all.\n"
req_doc_system_prompt += "You should respond in JSON as in this example:"
req_doc_system_prompt += """
{
    "requirements": [
        {"RequirementNo": "FR-01", "Requirement Description": "description of this functional requirement goes here"},
        {"RequirementNo": "FR-02": "Requirement Description": "description of this functional requirement goes here"},
        {"RequirementNo": "NFR-01": "Requirement Description": "description of this non-functional requirement goes here"},
        {"RequirementNo": "NFR-02": "Requirement Description": "description of this non-functional requirement goes here"}
    ]
}
"""

# In[7]:

#Set up user prompt, sending in the requirements doc as input and calling the ReqDoc.extract function. Key to note here is the explicit instructions to
#respond in JSON format.

def req_doc_user_prompt(doc):
    user_prompt = "Here is the contents from a requirement document.\n"
    user_prompt += f"{doc.extract()} \n"
    user_prompt += "Please scan through the document and extract only the  actual requirements. For example, ignore sections or \
paragraphs such as Approvers, table of contents and similar sections which are not really requirements.\
You must respond in a JSON format"
    user_prompt = user_prompt[:25_000] # Truncate if more than 25,000 characters
    return user_prompt

# In[8]:

#Function to call chatgpt-4o-mini model with the user and system prompts set above and returning the json formatted result obtained from chatgpt

def get_requirements(doc):
    reqdoc = ReqDoc(doc)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": req_doc_system_prompt},
            {"role": "user", "content": req_doc_user_prompt(reqdoc)}
        ],
      response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)


# In[9]:


#get_requirements("requirements.docx")


# ### Next, we will make another call to gpt-4o-mini

# In[10]:


#Set up system prompt to ask for test cases in table format

system_prompt = "You are an assitant that receives a list of functional and non functional requirements in JSON format. You are the expert in generating unit test cases for each requirement. \
You will create as many different test cases as needed for each requirement and produce a result in a table. Order the table by requirement No. Provide clear details on test case pass criteria. \
The table will contain the following columns. \
1.S No\
2.Requirement No\
3.Requirement Description\
4.Test Case ID\
5.Test case summary\
6.Test case description\
7.Success criteria \n"

# In[11]:


# Set up user prompt passing in the req doc file. This in turn will call the get_requirements function, which will make a call to chatgpt.

def get_testcase_user_prompt(reqdoc):
    user_prompt = "You are looking at the following list of requirements. \n"
    user_prompt += f"{get_requirements(reqdoc)}\n"
    user_prompt += "Prepare unit test cases for each of these requirements in a table and send that table as response. \n"
    user_prompt += user_prompt[:25000]
    return user_prompt


# In[12]:


#This is the 2nd call to chatgpt to get test cases. display(Markdown) will take care of producing a neatly formatted table output.
def create_testcase_doc(reqdoc):
    stream = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_testcase_user_prompt(reqdoc)}
          ],
        stream=True
    )
    response = ""
    #The below code is modified for running this as ipython script on the terminal.
    
    from tabulate import tabulate
    table_data = []
    
    for chunk in stream:
        # Append the content of the current chunk
        response += chunk.choices[0].delta.content or ''
        # Remove unwanted markers
        response = response.replace("```", "").replace("markdown", "")    
        # Assuming `response` contains rows of the table as comma-separated values (modify as needed)
        rows = response.split("\n")
        table_data = [row.split("|") for row in rows if row.strip()]  # Convert rows to lists for tabulate
    
        # Clear the console and print the updated table
        print("\033[H\033[J")  # Clear the terminal (works on most terminals)
        print(tabulate(table_data, headers="firstrow", tablefmt="plain"))  # Use `grid` style for better visuals

# In[13]:

#Final step is to prompt the user to provide the path to .docx file and call the function above
#The below code is modified for running this as ipython script on the terminal.
if __name__ == "__main__":
    input_file = input("Enter the path to the .docx file: ")
    create_testcase_doc(input_file)

# In[ ]:




