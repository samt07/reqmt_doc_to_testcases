# Automate Test case creation using ChatGPT
This repo contains code written in Python to generate test cases automatically from a user uploaded requirements document using OpenAI's gpt-4o-mini model. The generated test cases can then be downloaded as an xls file.

## Features
- The code takes in requirements doc as an input file. The document can contain any number of sections which might not be related to actual requirements like Approvers, Table of contents, Appendix etc. It just needs to be in `.docx` format.
- Generates a comprehensive list of test cases for each requirement in a neatly formatted table as output (streamed like chatgpt interface).
- Download the test cases as `.xls` file.
- UI is built using **Gradio** for a rich user experience.
- Also available in [HuggingFace Spaces](https://huggingface.co/spaces/Samhugs07/TestCasesFromBRD)
  
## Requirements
To run this project, you need the following:
- Google account (to run this in Google Colab)
- Python 3.11 or higher (to run it locally as python script and also for Jupyter Notebook)
- Jupyter Notebook (to run it locally using Jupyter lab)
- Your OpenAI API Secret Key. Get one in few secs from [OpenAi](https://platform.openai.com/settings/organization/api-keys)
- Nothing. Yes, not even OPEN AI Secret Key. See this in action on [HuggingFace Spaces](https://huggingface.co/spaces/Samhugs07/TestCasesFromBRD)

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

## Option 2: Run with locally installed Jupyter Notebook. You must have installed Python already. 
   1. Create a .env file as mentioned above
   2. Open the Jupyter Notebook:
       ```bash
          jupyter lab gradio_testcase_automation.ipynb
   3. Follow the instructions in the notebook to execute the code cell by cell, by using `Shift+Enter` key.
   4. If the Python version is 3.13 or higher, there might be a warning message for some imports. These can be ignored.

## Option 3: Run this on Google Colab (No installation Required.)

   1. Go to [Google Colab](https://colab.research.google.com/).  
   2. Click **File > Upload Notebook** and select `gradio_testcase_automation_colab.ipynb` from your local cloned repository folder.
   3. Set up env variable. Use Google Colab's Keys (typically found on the left side tool bar with a Key image)
      - 3a. Add `OPENAI_API_KEY` as the Secret name and paste your Open AI API Key. Enable the Notebook access option.  
   4. Run the Notebook cell-by-cell by pressing `Shift+Enter`
   5. At the end, upload your requirement document in Gradio UI.

## Option 4: Run as a standalone .py python script
   1. If Python is not installed already, install Python 3.11 or higher version from [here](https://www.python.org/downloads/)
   2. Create a .env file as mentioned above.
   3. Install dependenices by running this command
      ```bash
       pip install -r requirements.txt
   4. Run the following command
      ```bash
       ipython gradio_testcase_automation.py
   
## File Structure
- `gradio_testcase_automation.ipynb`: Jupyter notebook to run in locally installed jupyter lab.
- `gradio_testcase_automation_colab.ipynb`: Jupyter notebook to run in Google Colab.
-  `gradio_testcase_automation.py`: To run as a standalone python script locally
- `.env`: Environment file for storing the OpenAI API Key (not included in the repository).
- `requirements.txt`: Contains the required dependencies. Needed only for running as local python script
-  `reqdoc.docx`: Sample input requirement document.
-  `Lorem ipsum BRD`: To test a sample invalid requirements document.
