import students as std
import syllabus as sbs

sbs.add_syllabus("computer", 1)
sbs.add_syllabus("maths", 1)
sbs.add_syllabus("dsa", 2)
sbs.add_syllabus("lin algebra", 2)
sbs.add_syllabus("calculus", 3)
sbs.add_syllabus("DSAI", 3)
sbs.add_syllabus("Eng", 4)
sbs.add_syllabus("Business", 4)
print(f"Syllabus after adding all of the courses: {sbs.syllabus}")

sbs.delete_syllabus("dsa", 2)
print(f"Syllabus after deleting the mentioned course : {sbs.syllabus}\n")

sbs.get_syllabus(4)


std.add_student_details(1001, "a", "1/1/06", 2021)
print("student database: ", std.students)

print("\nGetting the syllabus for student of id 101 :")
std.get_syllabus_student_id(1001)
