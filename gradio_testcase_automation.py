#!/usr/bin/env python
# coding: utf-8

# In[2]:


#get_ipython().system('pip install openai python-docx python-dotenv')


# In[24]:


#get_ipython().system('pip install openpyxl')


# In[1]:


import os
import json
from dotenv import load_dotenv
#from IPython.display import Markdown, display, update_display
from openai import OpenAI
from docx import Document


# In[38]:


import pandas as pd
import re
import gradio as gr


# In[3]:


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


# In[4]:


# Initialize and constants
load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

if api_key and api_key.startswith('sk-proj') and len(api_key)>10:
    print("API key looks good!")
else:
    print("There might be a problem with your API key. Please check!")
    
MODEL = 'gpt-4o-mini'
openai = OpenAI()


# In[5]:


#Set up system prompt for extracting just the requirements from the document

req_doc_system_prompt = "You are provided with a complete requirements specifications document. \
You are able to decide which content from that document are related to actual requirements, identify each requirement as \
functional or non-functional and list them all.\n"
req_doc_system_prompt += "If the document is empty or do not contain requirements or if you cannot extract them, please respond as such.\
Do not make up your own requirements. \n"
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


# In[39]:


#Set up user prompt, sending in the requirements doc as input and calling the ReqDoc.extract function. Key to note here is the explicit instructions to
#respond in JSON format.

def req_doc_user_prompt(doc):
    user_prompt = "Here is the contents from a requirement document.\n"
    user_prompt += f"{doc.extract()} \n"
    user_prompt += "Please scan through the document and extract only the  actual requirements. For example, ignore sections or \
paragraphs such as Approvers, table of contents and similar sections which are not really requirements.\
You must respond in a JSON format"
    user_prompt += "If the content is empty, respond that there are no valid requirements you could extract and ask for a proper document.\n"
    user_prompt = user_prompt[:25_000] # Truncate if more than 25,000 characters
    return user_prompt


# In[40]:


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


# In[8]:


#Uncomment and run this if you want to see the extracted requriements in json format.
#get_requirements("reqdoc.docx")


# ### Next, we will make another call to gpt-4o-mini

# In[41]:


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
system_prompt += "If you are provided with an empty list, ask for a proper requirement doc\n"


# In[10]:


# Set up user prompt passing in the req doc file. This in turn will call the get_requirements function, which will make a call to chatgpt.

def get_testcase_user_prompt(reqdoc):
    user_prompt = "You are looking at the following list of requirements. \n"
    user_prompt += f"{get_requirements(reqdoc)}\n"
    user_prompt += "Prepare unit test cases for each of these requirements in a table and send that table as response. \n"
    user_prompt += user_prompt[:25000]
    return user_prompt


# In[11]:


# In[55]:


#This is the 2nd call to chatgpt to get test cases. display(Markdown) will take care of producing a neatly formatted table output.
def create_testcase_doc_gradio(response, is_response_ready, is_cleared, file_input):
    if is_cleared or file_input == None:  # Prevent OpenAI call if "Clear" was clicked
        return "", False
    stream = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_testcase_user_prompt(file_input)}
          ],
        stream=True
    )
    #Modified for Gradio
    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        #print(result)
        yield result, False


# In[37]:


# Define this variable and then pass js=force_dark_mode when creating the Interface
force_dark_mode = """
function refresh() {
    const url = new URL(window.location);
    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""


# In[15]:


def show_or_hide_save_button(response, is_response_ready, is_cleared):
    if is_cleared or response == None:
         return "", False
    table_pattern = r"(\|.+\|[\r\n]+)+"
    table_match = re.search(table_pattern, response)
    if table_match:
        return response, True #(response, is_response_ready)
    else:
        return response, False #(response, is_response_ready)


# In[42]:


def extract_table_from_markdown(response):
    # Regular expression to match Markdown tables
    table_pattern = r"(\|.+\|[\r\n]+)+"
    table_match = re.search(table_pattern, response)

    if table_match:
        table_data = table_match.group(0)
        # Process the table into a format pandas can read
        rows = table_data.strip().split("\n")
        data = [row.split("|")[1:-1] for row in rows]  # Split columns by '|'

        # Convert to DataFrame
        df = pd.DataFrame(data[1:], columns=data[0])  # First row is the header

        # Save to Excel
        output_file = "test_cases.xlsx"
        df.to_excel(output_file, index=False)

        return output_file
    else:
        return None


# In[43]:


def extract_and_save_button(response, is_cleared):
    if is_cleared:
       return None  # Do nothing if the file was cleared
    # This function will be triggered when the user clicks "Save as Excel"
    output_file = extract_table_from_markdown(response)
    if output_file:
        return output_file
    else:
        return "No table found in the provided input."


# In[54]:


# Gradio interface
with gr.Blocks(js=force_dark_mode) as demo:
    gr.HTML("<h2 style='text-align: center; color: white;'>📄 Test case automation</h2>")
    with gr.Row():
        file_input = gr.File(label="Upload your requirements docx file", file_types=[".docx"])
    with gr.Row():
        response = gr.Markdown()
    # Button to save the table as Excel file (optional)
    save_button = gr.Button("Download Table as Excel", visible=False)
    file_output = gr.File(label="Download Excel File", visible=False)  
    # State variable to track if response is ready
    is_response_ready = gr.State(False)
    with gr.Row():
        clear_button = gr.Button("Clear")
    # State variable to track if clear button is clicked
    is_cleared = gr.State(False)

    # Function to show "Processing..." message
    def show_processing(is_cleared, file_input):
        if is_cleared or file_input==None:
            return None, False, is_cleared, file_input  # Do nothing if the file was cleared
        #return gr.HTML("<h6 style='text-align: left; color: #ffffffff;'>⌛ Processing your file... Please wait!</h6>"), False, is_cleared, file_input
        return "⌛ Processing your file... Please wait!", False, is_cleared, file_input
    
    # Trigger response only if the file was uploaded and not cleared
    file_input.change(
        lambda _: False,  # Directly set is_cleared to False
        inputs=[file_input],
        outputs=[is_cleared]
    ).then(
        show_processing, inputs=[is_cleared, file_input], outputs=[response, is_response_ready, is_cleared, file_input]
    ).then(
        create_testcase_doc_gradio, inputs=[response, is_response_ready, is_cleared, file_input], outputs=[response, is_response_ready]
    ).then(
        show_or_hide_save_button, inputs=[response, is_response_ready, is_cleared], outputs=[response, is_response_ready]
    ).then(
        lambda _, ready: (gr.update(visible=ready), gr.update(visible=ready)), inputs=[response, is_response_ready], outputs=[save_button,file_output])

    #.then() passes the previous function outputs as inputs to the next function

    # Button action to extract and save table as an Excel file
    save_button.click(extract_and_save_button, inputs=[response, is_cleared], outputs=file_output)
    
    # Clear button resets both file and output while setting is_cleared to True
    clear_button.click(lambda: (None, None, None, True), inputs=None, outputs=[file_input, file_output, response, is_cleared]) 

# Launch Gradio app
demo.launch(share=True)


# In[ ]:




