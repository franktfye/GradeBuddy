import requests
import json
import os
from docx import Document
import csv



  
#dify local deployment
url = "http://localhost/v1/workflows/run"




folder_path = 'data'  # Replace with the path to your folder containing .docx files
csv_file_path = 'evaluations.dify.csv'  # The output CSV file path

#define the API key below
headers = {
    'Authorization': 'Bearer API', #define your Dify workflow API
    'Content-Type': 'application/json',
}


def import_txt(file_name):
    with open(file_name) as f:
        return [line.strip() for line in f]
    
def read_docx(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    print("File read")
    return ''.join(full_text)


rubrics1 = import_txt('rubrics.txt')
rubric = ''.join(rubrics1)
topic1 = import_txt('topic.txt')
topic = ''.join(topic1)

def evaluate_files_in_folder(folder_path):
    evaluations = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".docx"):
            file_path = os.path.join(folder_path, file_name)
            content = read_docx(file_path)
            data = {"inputs": {"input_text": content, "topic":topic, "rubric": rubric}, #define your workflow variables
                    "response_mode": "blocking",
                    "user": "USERNAME" #define your username
                    }
            response = requests.post(url, headers=headers, data=json.dumps(data))
            evaluation1 = response.json()
            evaluation = evaluation1['data']['outputs']['output']
            evaluations.append((file_name, evaluation))
            print(f"Evaluated:{file_name}")
    return evaluations



def write_evaluations_to_csv(evaluations, csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'Evaluation'])
        for evaluation in evaluations:
            writer.writerow(evaluation)

#Run the above tasks
evaluations = evaluate_files_in_folder(folder_path)

write_evaluations_to_csv(evaluations, csv_file_path)

