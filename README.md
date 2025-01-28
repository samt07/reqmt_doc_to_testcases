# Automate Test case creation using ChatGPT
This repo contains code written in Python to produce test cases from a user uploaded requirements document using the OpenAI's gpt-4o-mini model.

## Features
- Upload your requirements as it is in a word (.docx) file. It can contain any number of sections which might not be related to actual requirements like Approvers, Table of contents, Appendix etc. Just upload as it is.
- Receive a comprehensive list of test cases for each requirement in a neatly formatted table as output (streamed like chatgpt interface).
  
## Requirements
To run this project, you need the following:
- Your OpenAI API Secret Key. Get one in few secs from [OpenAi](https://platform.openai.com/settings/organization/api-keys)

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
## Option 1: Run with locally installed Jupyter Notebook (Recommended)
   1. Open the Jupyter Notebook:
       ```bash
          jupyter lab testcase_automation.ipynb
   2. Follow the instructions in the notebook to execute the code cell by cell, by using `Shift+Enter` key.

## Option 2: Run this on Google Colab (No installation Required.)

   1. Go to [Google Colab](https://colab.research.google.com/).  
   2. Click **File > Upload Notebook** and select `testcase_automation_colab.ipynb` from your local cloned repository folder.
   3. Set up env variable. Use Google Colab's Keys (typically found on the left side tool bar with a Key image)
      - 3a. Add `OPENAI_API_KEY` as the Secret name and paste your Open AI API Key. Enable the Notebook access option.  
   4. Run the Notebook cell-by-cell by pressing `Shift+Enter`
   5. For the final cell, after pressing `Shift+Enter`, upload your requirement document once it enables up File Upload widget.

## Option 3: Run as a standalone .py python script
   1. Create a .env file as mentioned in Option 1.
   2. Run the following command
    ```python
     ipython testcase-automation-script.py
   3. It will then ask for requriement file path. Provide that.
   4. Output gets printed. It might look not as appealing as it would in Jupyter notebook, but that can be refined if needed.

## File Structure
- `testcase_automation.ipynb`: Jupyter notebook to run in locally installed jupyter lab.
- `testcase_automation_colab.ipynb`: Jupyter notebook to run in Google Colab.
-  `testcase-automation-script.py`: To run as a standalone python script locally
- `.env`: Environment file for storing the OpenAI API Key (not included in the repository).
-  `requirement doc.docx`: Input requirement document. It can be located anywhere but the code only supports .docx files currently.
