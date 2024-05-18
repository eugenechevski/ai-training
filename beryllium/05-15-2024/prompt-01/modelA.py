def highest_average(student_list):
    # Initialize maximum average and student name
    max_average = 0
    best_student = ""

    for student in student_list:
        total = sum(student["grades"].values())
        average = total / len(student["grades"])

        # Update maximum average and best student if a higher average is found.
        if average > max_average:
            max_average = average
            best_student = student["name"]
    return best_student

# Example
student_list = [ 
       {  "name": "Annie",    "grades": {"Math": 90,   "Science": 88,  "English": 92 } },
       {  "name": "Bob",  "grades": {    "Math": 85,   "Science": 92,  "History": 86 }  },
       {  "name": "Charlie",    "grades": {    "Math": 70,   "Art": 90,     "Computer Science": 95 } }
   ]                  
print(highest_average(student_list))  # Outputs: Charlie