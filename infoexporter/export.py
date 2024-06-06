# data_exporter/export.py
import csv
import json
import pandas as pd

def export_data(data, file_format, file_path):
    if file_format == 'csv':
        export_to_csv(data, file_path)
    elif file_format == 'json':
        export_to_json(data, file_path)
    elif file_format == 'excel':
        export_to_excel(data, file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

def export_to_csv(data, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def export_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def export_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
