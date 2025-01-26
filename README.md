# Automate Test case creation using ChatGPT
This repo contains code written in Python to produce test cases from a requirements document using the gpt-4o-mini model.

## Features
- Input your requirements in a ".docx" file
- Receive a comprehensive list of test cases in a neatly formatted tabe

## Requirements
To run this project, you need the following:
- Python 3.11 or higher
- (Optional) Jupyter Notebook
- (Optional) Google Colab account
- Your OpenAI API Secret Key

## Installation

1. **Clone this repository:**
   Open a terminal and run:
   ```bash
   git clone [https://github.com/samt07/req_doc_to_testcases.git](https://github.com/samt07/req_doc_to_testcases.git)

2. **Navigate to the project directory**
    ```bash

    cd req_doc_to_testcases

3. **Install required libraries:**
   Run the following command to install all dependencies:
    ```python
       pip install -r requirements.txt

## Usage
# Option 1: Run with Jupyter Notebook (Recommended)
1. Open the Jupyter Notebook:
    ```bash
       jupyter notebook testcase_automation.ipynb
2. Follow the instructions in the notebook to execute the code step-by-step.

# Option 2: Running on Google Colab (No installation Required)

1. Go to [Google Colab](https://colab.research.google.com/).  
2. Click **File > Upload Notebook** and select `testcase_automation.ipynb`.  
3. Install any required libraries by adding the following code cell at the top of the notebook:
   ```python
   !pip install -r requirements.txt
4. Handle env variable
    ```python
    import os
    os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
  
5. Run the Notebook step-by-step by pressing Shift+Enter

## Setting Up Environment Variables
1. Create a .env file in the project directory.
2. Add the Open AI Key value. Dont include any quotes. Just paste the key value after the =:
OPENAI_API_KEY=
3. Save the file. Ensure the file extension is .env. It should not be ".env.txt" for example.

## File Structure
- `testcase_automation.ipynb`: Main notebook containing the code and explanations.
- `requirements.txt`: File listing all required Python libraries.
- `.env`: Environment file for storing the OpenAI API Key (not included in the repository).


































