

syllabus = [

]


def add_syllabus(course, year):
    course_added = False
    for i in range(0, len(syllabus)):
        if syllabus[i]["year"] == year:
            syllabus[i]["courses"].append(course)
            print(course)
            course_added = True
    if not course_added:
        syllabus.append({"year": year,
                         "courses": [course]})
        print(course)


def delete_syllabus(course, year):
    course_deleted = False
    for i in range(0, len(syllabus)):
        if syllabus[i]["year"] == year and course in syllabus[i]["courses"]:
            syllabus[i]["courses"].remove(course)
            print(course)
            course_deleted = True

    if not course_deleted:
        print("The course cannot be found")


def get_syllabus(year):
    syllabus_available = False
    for i in range(0, len(syllabus)):
        if syllabus[i]["year"] == year:
            print(f"syllabus for  year {year} : {syllabus[i]['courses']}")

            syllabus_available = True
    if not syllabus_available:
        print("Cannot get syllabus")




