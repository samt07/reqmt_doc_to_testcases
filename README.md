# req-doc-to-testcases
This repo contains code written in Python to produce test cases from a requirements document.

## Features
- [Input a requirements docx file]
- [Receive a comprehensive list of test cases in a neatly formatted tabe]

## Requirements
To run this project, you need the following installed:
- Python 3.11 or higher
- (Optional) Jupyter Notebook
- Your OpenAI API Secret Key

## Installation

1. **Clone this repository:**
   Open a terminal and run:
   ```bash
   git clone https://github.com/samt07/reqstotestcases.git

2. **Navigate to the project directory**
    ```bash

    cd reqstotestcases

3. **Install required libraries:**
   Run the following command to install all dependencies:
    ```python
       pip install -r requirements.txt

## Usage
# Option 1: Run with Jupyter Notebook (Recommended)
1. Open the Jupyter Notebook:
    ```bash
       jupyter notebook req_to_testdoc_automation.ipynb
2. Follow the instructions in the notebook to execute the code step-by-step.

# Option 2: Run as a Python script
If you cannot install Jupyter Notebook, convert the notebook into a .py file and run it as a script.
    ```bash
        jupyter nbconvert --to script req_to_testdoc_automation.ipynb
        python req_to_testdoc_automation.ipynb
# Option 3: Running on Google Colab (No installation Required)

1. Go to [Google Colab](https://colab.research.google.com/).  
2. Click **File > Upload Notebook** and select `req_to_testdoc_automation.ipynb`.  
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
- `req_to_testdoc_automation.ipynb`: Main notebook containing the code and explanations.
- `requirements.txt`: File listing all required Python libraries.
- `.env`: Environment file for storing the OpenAI API Key (not included in the repository).


































