def pad(string, length):
    new_length = length - len(string)
    return string + new_length * ' '

class Course:
    def __init__(self, c, tt, type, cd_hr=0, sms=0):
        self.code = c
        self.title = tt
        self.type = type
        self.credit_hrs = cd_hr
        self.semester = sms

    def __str__(self):
        if len(self.code)>8 :
            self.code=(input('enter new code (8) length : '))
            s=f'{pad(self.code, 8)}{pad(self.title, 40)}{pad(str(self.credit_hrs), 15)}{pad(self.type, 10)}{pad(str(self.semester), 9)}'
            return s
        elif len(self.title)>40 :
            self.code=(input('enter new title (40) length : '))
            s=f'{pad(self.code, 8)}{pad(self.title, 40)}{pad(str(self.credit_hrs), 15)}{pad(self.type, 10)}{pad(str(self.semester), 9)}'
            return s
        else:
            return f'{pad(self.code, 8)}{pad(self.title, 40)}{pad(str(self.credit_hrs), 15)}{pad(self.type, 10)}{pad(str(self.semester), 9)}'

courses = [Course('00000000', 'Object Oriented Programming', 'core', 3, 2),
           Course('00000001', 'Digital Logic Design', 'elective', 3, 2),
           Course('00000011', 'Math Deficiency', 'core', 3, 2),
           Course('00000111', 'Applied Physics', 'core', 3, 2)]
s=(f'{pad('CODE',8)}{pad('TITLE',40)}{pad('CREDIT_HOURS',15)}{pad('TYPE',10)}{pad('SEMESTER',9)}')
with open('FixedLengthRecords.txt', 'w') as file:
    file.write(str(s)+'\n')
    for i in courses:
        file.write(str(i) + '\n')

menu = 'a) Add\ns) Search\nd) Delete\nl) List All\ne) Edit\nq) Quit'
while True:
    choice = input('Enter your choice: ')
    if choice == 'a':                                              # Add a new course
        c = Course(input('Enter code: '), input('Enter title: '), input('Enter type: '), int(input('Enter credit_hrs: ')), int(input('Enter semester: ')))
        courses.append(c)
        with open('FixedLengthRecords.txt', 'a') as file:
            file.write(str(c) + '\n')
    elif choice == 's':                                            # Search for a course
        code = input('Enter the code you want to search: ')
        found = False
        with open('FixedLengthRecords.txt', 'r') as file:
            for line in file:
                if line[:8] == code:
                    print(line)
                    found = True
                    break
        if not found:
            print("Course not found.")
    elif choice == 'd':                                             # Delete a course
        code = input('Enter the code you want to delete: ')
        with open('FixedLengthRecords.txt', 'r') as file:
            lines = file.readlines()
        with open('FixedLengthRecords.txt', 'w') as file:
            for line in lines:
                if line[:8] != code:
                    file.write(line)
                else:
                    file.write(pad('??',8) +line[8:82]+'\n')  
    elif choice == 'l':
        with open('FixedLengthRecords.txt', 'r') as file:
            for line in file:                                      # List all courses
                print(line)                                                
    elif choice == 'e':                                            # Edit a course
        code = input('Enter the code you want to edit: ')
        with open('FixedLengthRecords.txt', 'r') as file:
            lines = file.readlines()
        with open('FixedLengthRecords.txt', 'w') as file:
            for line in lines:
                if line[:8] == code:
                    c = Course(input('Enter new code: '), input('Enter new title: '), input('Enter new type: '), int(input('Enter new credit_hrs: ')), int(input('Enter new semester: ')))
                    file.write(str(c) + '\n')
                else:
                    file.write(line)
    elif choice == 'q':# quit
        break
    else:
        print(f'Invalid input\nChoose from the following:\n{menu}')


