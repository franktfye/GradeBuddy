#pip install openai
#pip install python-docx

import os
from docx import Document
import csv

from openai import AzureOpenAI
client = AzureOpenAI(
    api_key= os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

def import_txt(file_name):
    with open(file_name) as f:
        return [line.strip() for line in f]


model="gpt-4"

rubrics = import_txt('rubrics.txt')

instructions = "You will act as a teacher and evaluate students' essays. You will give a score (1 to 8, Higher score means better) for each rubric. After scoring, provide a brief comments about the whole essay."

folder_path = 'data'  # Replace with the path to your folder containing .docx files
csv_file_path = 'evaluations.gpt4.test3.csv'  # The output CSV file path

def evaluate_content(content):
    try:
        response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system", 
                        "content": f"{instructions} Rubrics: {rubrics}"
                    },
                    {
                        "role": "system", 
                        "content": "Please evaluate the following based on rubrics:"
                    },
                    {
                        "role": "user", 
                        "content": f"{content}"
                    }
                        ],
                temperature=0.1,
                top_p=0.9,
                max_tokens=500,
                
            )
        return response.choices[0].message.content 
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Evaluation failed"

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    print("File read")
    return '\n'.join(full_text)
    


def evaluate_files_in_folder(folder_path):
    evaluations = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".docx"):
            file_path = os.path.join(folder_path, file_name)
            content = read_docx(file_path)
            evaluation = evaluate_content(content)
            evaluations.append((file_name, evaluation))
            print(f"Evaluated:{file_name}")
    return evaluations

def write_evaluations_to_csv(evaluations, csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'Evaluation'])
        for evaluation in evaluations:
            writer.writerow(evaluation)


evaluations = evaluate_files_in_folder(folder_path)
write_evaluations_to_csv(evaluations, csv_file_path)
