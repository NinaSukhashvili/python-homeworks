#დაწერეთ პროგრამა, რომელიც ტერმინალში მომხმარებელს გამოუტანს სტუდენტების აიდის (id) სიას, მომხარებელი აირჩევს სტუდენტის აიდის, მიღებული აიდისთვის დაბეჭდავს სტუდენტის მონაცემებს. მონაცემებში უნდა დაიბეჭდოს (სახელი, გვარი, ასაკი და ქულა თითოეული საგნის მიხედვით)

my_dict = {
  "students": [
    {"id": 20,     "name": "Giorgi",  "age": 25},
    {"id": 25,     "name": "Giorgi",  "age": 23},
    {"id": 56,     "name": "Nika",    "age": 25},
    {"id": 100,    "name": "Nika",    "age": 22},
    {"id": 1232,   "name": "Dato",    "age": 22},
    {"id": 846723, "name": "Archili", "age": 32},
  ],
  "subjects": [
    {"id": 1, "name": "Math",      "grades": {"20":"B","25":"A","56":"B","100":"A","1232":"C","846723":"A"}},
    {"id": 2, "name": "Physics",   "grades": {"20":"A","25":"B","56":"B","100":"A","1232":"C","846723":"B"}},
    {"id": 3, "name": "English",   "grades": {"20":"A","25":"A","56":"A","100":"A","1232":"B","846723":"A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20":"B","25":"B","56":"B","100":"A","1232":"A","846723":"A"}},
    {"id": 5, "name": "History",   "grades": {"20":"C","25":"B","56":"B","100":"A","1232":"A","846723":"A"}},
  ]
}


ids = []
for student in my_dict["students"]:
    ids.append(student["id"])
print(f"studentebis ID: {', '.join(map(str, ids))}")

chosen_id = int(input("airchiet studentis ID: "))

found_student = None
for student in my_dict["students"]:
    if student["id"] == chosen_id:
        found_student = student
        break

if found_student is not None:
    print(f"\nstudent information:")
    print(f"ID: {found_student['id']}, Name: {found_student['name']}, Age: {found_student['age']}")
    for subject in my_dict["subjects"]:
        grade = subject["grades"][str(chosen_id)]
        print(f"subject: {subject['name']}, grade: {grade}")
else:
    print("student not found!")