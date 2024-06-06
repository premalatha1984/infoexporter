from .database import fetch_data
from .exporter import export_to_excel, export_to_pdf

def generate_file(table_name, fields, file_format, connection_string):
    data = fetch_data(table_name, fields, connection_string)
    
    if file_format.lower() == 'xlsx':
        file_name = f"{table_name}.xlsx"
        export_to_excel(data, file_name)
    elif file_format.lower() == 'pdf':
        file_name = f"{table_name}.pdf"
        export_to_pdf(data, file_name)
    else:
        raise ValueError("Unsupported file format. Choose either 'xlsx' or 'pdf'.")
    
    return file_name
