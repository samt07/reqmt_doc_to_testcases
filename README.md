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

3. **Set up Env variable**
   3a. Create a ".env" file in the same path.
   3b. Add OPENAI_API_KEY=youropenaikey
   3c. Ensure there is no space before or after '='. No quotes needed for the value as well.
   3d. Save the file as .env
   3e. Check and ensure it is saved as ".env". It should not look like .env.txt or env.env or anything else. Just .env

## Usage
# Option 1: Run with locally installed Jupyter Notebook (Recommended)
   1. Open the Jupyter Notebook:
       ```bash
          jupyter notebook testcase_automation.ipynb
   2. Follow the instructions in the notebook to execute the code cell by cell, by using Shift+Enter key.

# Option 2: Run this on Google Colab (No installation Required)

   1. Go to [Google Colab](https://colab.research.google.com/).  
   2. Click **File > Upload Notebook** and select `testcase_automation_colab.ipynb` from your local cloned repository folder.
   3. Set up env variable. Use Google Colab's Keys (typically found on the left side tool bar with a Key image)
      3a. Add OPENAI_API_KEY as the Secret name and paste your Open AI API Key. Enable the Notebook access option so that it can be used in the session.  
   4. Run the Notebook cell-by-cell by pressing Shift+Enter
   5. For the final cell, after pressing Shift+Enter, upload your requirement document once it enables up File Upload widget.

# Option 3: Run as a standalone .py python script
   3a. Create a .env file as mentioned in Option 1.
   3b. Run the following command
   ```python
   ipython testcase-automation-script.py
   3c. It will then ask for requriement file path. Provide that.
   3d. Output gets printed. It might look not as appealing as it would in Jupyter notebook, but that can be refined if needed.

## File Structure
- `testcase_automation.ipynb`: Jupyter notebook to run in locally installed jupyter lab.
- `testcase_automation_colab.ipynb`: Jupyter notebook to run in Google Colab.
-  `testcase-automation-script.py`: To run as a standalone python script locally
- `.env`: Environment file for storing the OpenAI API Key (not included in the repository).
-  `requirement doc.docx`: Input requirement document. It can be located anywhere but the code only supports .docx files currently.


































