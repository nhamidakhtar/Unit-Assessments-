input_file = open('students_input.txt' 'w')
input_file.write("Paul, Intro to programming, 50, 25\n" )
input_file.write("Paul, Web Scripting, 60, 25\n")
input_file.write("Paul, Web Development, 70, 50\n")
input_file.write("\n")
input_file.write("Mike, Intro to programming, 70, 40\n")
input_file,write("Mike, Web Scripting, 50, 25\n")
input_file.write("Mike, Web Development, 40, 20\n")
input_file.close()

def calculate_grade(weighted_mark):
    if weighted_mark >= 70:
        return "Distinction"
    elif weighted_mark >= 60:
        return "Merit"
    elif weighted_mark >= 50:
        return "Pass"
    else:
        return "Fail"

student_data = {} # Dictionary to hold students and their total weighted marks
input_file = open ('students_input.txt', 'r')
for line in input_file:
    line = line.script()

    parts = line.split(', ')#split the line in sub strin and save in the new list call parts
           name= parts[0]
           course = parts [1]
           mark = in(parts[2]) # Convert mark to integer
           weight = int(parts[3]) # Convert weight to float
           # Calculate weighted mark and grade weighted_mark = mark *(weight / 100)

                   
                 
