from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER


input_file = "akgec_courses.txt"
output_file = "AKGEC_Courses_Branches.pdf"


# Read TXT file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()


# Create PDF
pdf = SimpleDocTemplate(
    output_file,
    pagesize=A4
)


styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.alignment = TA_CENTER

normal_style = styles["Normal"]


content = []


for line in lines:

    line = line.strip()

    if not line:
        content.append(Spacer(1, 8))
        continue

    if line.startswith("AJAY"):
        content.append(Paragraph(line, title_style))

    else:
        content.append(Paragraph(line, normal_style))


pdf.build(content)


print("PDF created successfully!")
print("File:", output_file)