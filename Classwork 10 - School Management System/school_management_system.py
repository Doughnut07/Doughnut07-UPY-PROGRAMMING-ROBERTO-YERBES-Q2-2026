#INPUT
users = {
    'rherrera':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Rafita Herrera'
    },
    'ccalderon':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Clarissa Calderon'
    },
    'vcervantes':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Venus Cervantes'
    },
    'anava':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Arturito Nava'
    },
    'mvilchis':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Melany Vilchis'
    },
    'mjimenez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mareli Jimenez'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}
 
subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)
 
notes = {
    'rherrera': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'ccalderon': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'vcervantes': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'anava': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'mvilchis': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'mjimenez': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}
#PROCESS
logged = False
current_user = ""

while logged == False:
    user = input("User: ")
    password = input("Password: ")
    
    if user in users:
        if users[user]['password'] == password:
            logged = True
            current_user = user
        else:
            print("\nIncorrect password. Try again.\n")
    else:
        print("\nWrong User/Password. Try again.\n")

user_role = users[current_user]['rol']

#OUTPUT
print(f"\nWelcome, {users[current_user]['name']} ({user_role})")

if user_role == 'student':
    print(f"\nReport card for {users[current_user]['name']}")
    aprobadas = set()
    pendientes = set()
    
    for subject_name in subjects:
        grade = notes[current_user][subject_name]
        print(f"{subject_name}: {grade}")
        
        if grade >= 7.0:
            aprobadas.add(subject_name)
        else:
            pendientes.add(subject_name)
            
    print(f"\nPassed subjects: {aprobadas}")
    print(f"Pending subjects: {pendientes}")

elif user_role == 'professor':
    print("\nStudent list:")
    for student_key in users:
        if users[student_key]['rol'] == 'student':
            print(f"- {student_key} ({users[student_key]['name']})")
            
    student_to_grade = input("\nStudent (username): ")
    
    if student_to_grade == 'exit':
        print("\nExiting program.")
    elif student_to_grade in notes:
        print("\nAvailable subjects:")
        for subject_name in subjects:
            print(f"- {subject_name}")
            
        subject_to_grade = input("\nSubject to modify: ")
        
        if subject_to_grade == 'exit':
            print("\nExiting program.")
        elif subject_to_grade in subjects:
            new_grade_input = input("New grade: ")
            
            if new_grade_input == 'exit':
                print("\nExiting program.")
            else:
                new_grade = float(new_grade_input)
                confirmation = input("Are you sure you want to modify it? (yes/no): ")
                
                if confirmation == 'exit':
                    print("\nExiting program.")
                elif confirmation == 'yes':
                    notes[student_to_grade][subject_to_grade] = new_grade
                    print("\nGrade updated.")
                elif confirmation == 'no':
                    print("\nModification cancelled.")
                else:
                    print("\nInvalid option. Modification cancelled.")
                    
        else:
            print("\nSubject not found.")
    else:
        print("\nStudent not found.")

elif user_role == 'coordinator':
    print("\nTeacher list:")
    for prof_key in users:
        if users[prof_key]['rol'] == 'professor':
            print(f"- {users[prof_key]['name']}")
            
    print("\nSubject list:")
    for subj in subjects:
        print(f"- {subj}")
        
    print("\nStudents and their grades:")
    for stu_key in notes:
        print(f"\n{users[stu_key]['name']}:")
        for subj in subjects:
            print(f"  {subj}: {notes[stu_key][subj]}")