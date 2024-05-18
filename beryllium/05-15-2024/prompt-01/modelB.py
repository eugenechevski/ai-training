def find_top_student(student_list):
    highest_average = 0
    top_student_name = ""
    for student in student_list:
        average = sum(student["grades"].values()) / len(student["grades"])
        if average > highest_average:
            highest_average = average
            top_student_name = student["name"]
    return top_student_name


# Example
student_list = [ 
       {  "name": "Annie",    "grades": {"Math": 90,   "Science": 88,  "English": 92 } },
       {  "name": "Bob",  "grades": {    "Math": 85,   "Science": 92,  "History": 86 }  },
       {  "name": "Charlie",    "grades": {    "Math": 70,   "Art": 90,     "Computer Science": 95 } }
   ]                  
print(find_top_student(student_list))  # Outputs: Charlie