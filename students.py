from datetime import datetime

import syllabus as sbs

students = [
    {"student_id": 1001,
     "name": "",
     "date_of_birth": "",
     "year_joined": None, }
]


def add_student_details(student_id, name, dob, year_joined):
    student_id_valid = False
    for i in range(0, len(students)):
        if students[i]["student_id"] == student_id:
            students[i]["name"] = name
            students[i]["date_of_birth"] = dob
            students[i]["year_joined"] = year_joined
            student_id_valid = True

    if not student_id_valid:
        print("invalid student id")


def get_syllabus_student_id(student_id):
    current_year = datetime.now().year
    success = False
    for i in range(0, len(students)):
        if students[i]["student_id"] == student_id:
            year = (current_year - students[i]["year_joined"])
            sbs.get_syllabus(year)
            success = True
            break
    if not success:
        print("cannot get student id")
