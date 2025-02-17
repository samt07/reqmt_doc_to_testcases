# Automate Test case creation using ChatGPT
This repo contains code written in Python to generate test cases automatically from a user uploaded requirements document using OpenAI's gpt-4o-mini model. The generated test cases can be downloaded as an xls file.

## Features
- The code takes in requirements doc as an input file. The document can contain any number of sections which might not be related to actual requirements like Approvers, Table of contents, Appendix etc. It just needs to be in .docx format.
- Generates a comprehensive list of test cases for each requirement in a neatly formatted table as output (streamed like chatgpt interface).
- Download the test cases as .xls file.
- UI is built using Gradio for a rich user experience.
- Also available in [HuggingFace Spaces](https://huggingface.co/spaces/Samhugs07/TestCasesFromBRD)
  
## Requirements
To run this project, you need the following:
- Google account (to run this in Google Colab)
- Jupyter Notebook (to run it locally using Jupyter lab)
- Python 3.11 or higher (to run it locally as python script)
- Your OpenAI API Secret Key. Get one in few secs from [OpenAi](https://platform.openai.com/settings/organization/api-keys)
- Nothing. See this in action on [HuggingFace Spaces](https://huggingface.co/spaces/Samhugs07/TestCasesFromBRD)

## Installation

1. **Clone this repository:**
   Open a terminal and run:
   ```bash
   git clone https://github.com/samt07/reqmt_doc_to_testcases.git

2. **Navigate to the project directory**
    ```bash
    cd reqmt_doc_to_testcases

## Set Up Environment Variables  

1. **Create a `.env` file**  
   - Navigate to the project directory.  
   - Create a new file named `.env`.  

2. **Add the OpenAI API Key**  
   - Open the `.env` file in a text editor.  
   - Add the following line:  
     ```env
     OPENAI_API_KEY=youropenaikey
     ```
   - Ensure:  
     - No spaces before or after the `=`.  
     - No quotes around the value.  

3. **Save the file**  
   - Save it with the exact name `.env`.  
   - Verify that it is not saved as `.env.txt`, `env.env`, or any other variation.  

## Usage
## Option 1 (recommended): Just goto link: [HuggingFace Spaces](https://huggingface.co/spaces/Samhugs07/TestCasesFromBRD)

## Option 2: Run with locally installed Jupyter Notebook 
   1. Open the Jupyter Notebook:
       ```bash
          jupyter lab gradio_testcase_automation.ipynb
   2. Follow the instructions in the notebook to execute the code cell by cell, by using `Shift+Enter` key.

## Option 3: Run this on Google Colab (No installation Required.)

   1. Go to [Google Colab](https://colab.research.google.com/).  
   2. Click **File > Upload Notebook** and select `gradio_testcase_automation_colab.ipynb` from your local cloned repository folder.
   3. Set up env variable. Use Google Colab's Keys (typically found on the left side tool bar with a Key image)
      - 3a. Add `OPENAI_API_KEY` as the Secret name and paste your Open AI API Key. Enable the Notebook access option.  
   4. Run the Notebook cell-by-cell by pressing `Shift+Enter`
   5. At the end, upload your requirement document in Gradio UI.

## Option 3: Run as a standalone .py python script
   1. Create a .env file as mentioned above.
   2. Install dependenices by running this command
      ```bash
       pip install -r requirements.txt
   3. Run the following command
      ```bash
       ipython gradio_testacse_automation.py
   
## File Structure
- `gradio_testcase_automation.ipynb`: Jupyter notebook to run in locally installed jupyter lab.
- `gradio_testcase_automation_colab.ipynb`: Jupyter notebook to run in Google Colab.
-  `gradio_testacse_automation.py`: To run as a standalone python script locally
- `.env`: Environment file for storing the OpenAI API Key (not included in the repository).
- `requirements.txt`: Contains the required dependencies. Needed only for running as local python script
-  `reqdoc.docx`: Sample input requirement document.
-  `Lorem ipsum BRD`: To test invalid requirements document.
