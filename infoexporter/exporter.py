import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_to_excel(data, file_name):
    data.to_excel(file_name, index=False)

def export_to_pdf(data, file_name):
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter
    c.drawString(30, height - 40, f"Report: {file_name}")
    y = height - 60

    for i, row in data.iterrows():
        text = ", ".join([str(item) for item in row.values])
        c.drawString(30, y, text)
        y -= 20
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
