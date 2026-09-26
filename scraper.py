import requests
from bs4 import BeautifulSoup

url = "https://www.akgec.ac.in/courses-offered/"

response = requests.get(url)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

# Find courses table
target_table = None

for table in soup.find_all("table"):
    table_text = table.get_text(" ", strip=True)

    if "Computer Science and Engineering" in table_text:
        target_table = table
        break

if target_table:
    print("Courses table found!")

    rows = target_table.find_all("tr")

    courses = []
    current_program = ""

    for row in rows:

        cells = row.find_all(["th", "td"])

        data = [cell.get_text(" ", strip=True) for cell in cells]

        if not data:
            continue

        # B.Tech / M.Tech / MCA headings
        if len(data) == 1:
            current_program = data[0]
            continue

        # Course + intake
        if len(data) == 2 and data[0] and data[1]:

            # Skip table header
            if data[0] == "Courses" and data[1] == "Sanctioned Intake":
                continue

            course_name = data[0]
            intake = data[1]

            courses.append({
                "program": current_program,
                "course": course_name,
                "intake": intake
            })

    # Save clean data
    with open("akgec_courses.txt", "w", encoding="utf-8") as file:

        file.write("AJAY KUMAR GARG ENGINEERING COLLEGE\n")
        file.write("Courses and Branches\n")
        file.write("=" * 50 + "\n\n")

        for item in courses:

            file.write(f"Program: {item['program']}\n")
            file.write(f"Course: {item['course']}\n")
            file.write(f"Sanctioned Intake: {item['intake']}\n")
            file.write("-" * 50 + "\n")

    print("Clean data saved successfully!")
    print("File: akgec_courses.txt")

else:
    print("Courses table not found!")