# GradeBuddy
 Meet the Grading Bot, a python script of LLM for providing efficient feedback on student assignments

## Update: With the powerful workflow-based LLM development tool Dify, we can now leverage customized, high-quality LLMs to accurately grade student assignments, including essays.

To get started, simply set up Dify and import the pre-configured "Essay Grading Workflow.yml" file. Then, run the "dify-workflow.py" script, which utilizes the workflow API to streamline the process. The script will automatically generate a output CSV file containing all evaluations, complete with corresponding Student IDs.

For more information, please refer to my blog: https://randomtalktheory.blogspot.com/2024/07/using-llm-workflow-to-evaluate-documents.html
Dify: https://github.com/langgenius/dify
Docker Desktop: https://docs.docker.com/desktop/install

 
## Getting Started
### Prerequisites
- Python 3.x installed on your computer
- An Azure account with Cognitive Services enabled (if you are using Azure)

### 1. Setting Up Python

If Python is not already installed on your computer, follow these steps:
(If you are not using miniconda)

1. Download Python from the [official website](https://www.python.org/downloads/).
2. Run the installer and follow the prompts. Ensure that you check the box to **Add Python to PATH** during installation.
3. To verify the installation, open a terminal or command prompt and type `python --version`. You should see the Python version number.

### 2. Setting Up System Environment Variables for Azure API

To use the Azure API with GradeBuddy, you'll need to set up your API key as a system environment variable:

1. Log in to your Azure portal and navigate to Cognitive Services to find your API key.
2. On Windows:
   - Search for "Environment Variables" in the Start menu and select "Edit the system environment variables."
   - In the System Properties window, click the "Environment Variables" button.
   - Under "System variables," click "New" and add a new variable with the name `AZURE_API_KEY` and your Azure API key as the value.

   On macOS/Linux:
   - Open your terminal.
   - Edit your shell profile file (e.g., `~/.bash_profile`, `~/.zshrc`, etc.) and add the following line: `export AZURE_API_KEY="YourAzureAPIKeyHere"`.
   - Save the file and run `source ~/.bash_profile` (or equivalent) to reload the profile.

3. To verify, restart your terminal or command prompt and type `echo %AZURE_API_KEY%` (Windows) or `echo $AZURE_API_KEY` (macOS/Linux). You should see your Azure API key.

### 3. Running the Script

To run GradeBuddy:

1. Download the GradeBuddy script from the GitHub repository.
2. Place your student essays in the designated data folder. Ensure the files are named appropriately (e.g., student name or ID) for easy identification.
3. Open a terminal or command prompt, navigate to the script's directory, and execute the script by typing:

   ```
   python evaluate.oai.py
   ```

4. The script will process the essays and output a table of scores based on the provided rubrics and content analysis.
