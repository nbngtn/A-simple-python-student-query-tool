import pandas as pd
import re
# Input the txt file and put into DataFrame
with open('/mnt/42BC914FBC913E7B/Miu/Fordham/Python/Project/student.txt',mode='r',encoding='utf-8') as f:
    data = f.read()

data = data.split('\n') # split data records

# split into column values
for i in range(len(data)):
    data[i] = data[i].split('\t')
cols = data.pop(0)
stu_rec = pd.DataFrame(data,columns=cols)

# Design query tool
def Showall():
    print(stu_rec.to_string())

def LastName(last):
    output = pd.DataFrame() # creating an empty dataframe
    if re.search('[^a-zA-Z]',last): # check the format of user's input
        print('You have entered a wrong name format')
    else:
        for i in range(len(stu_rec.index)):
            if stu_rec.iloc[i]['Last'].lower()==last:
                output = pd.concat([output,stu_rec.iloc[[i]]]) # if the input matches a value in the database, add the whole record to the new dataframe to display
        if output.empty == False:
            print(output) # Print if the dataframe is not empty
        else:
            print('Record not found') # Return message if the input is in correct format but record does not exists in database

def GradYr(year):
    if re.search('[^0-9]',year):
            print('Maybe you have entered a wrong year format') # Return message if user input contains characters other than numeric
    else:
        output = stu_rec.loc[stu_rec['GradYear']==year] # returns all records that matches the input into a new dataframe
        if output.empty == False: 
            print(output) # Print if the dataframe is not empty
        else:
            print('Record not found') # Return message if the input is in correct format but record does not exists in database

def Summary(program,gradyear):
    global stu_rec # declare to use a global variable

    programs = set() # creating a set of program names
    years = set() # creating a set of years
    for i in range(len(stu_rec.index)):
        programs.add(stu_rec.iloc[i]['DegreeProgram'])
        years.add(stu_rec.iloc[i]['GradYear'])

    if re.search('[^A-Za-z]',program) or re.search('[^0-9]',gradyear): # Check input format
        if re.search('[^A-Za-z]',program):
            print('Wrong program name format')
            return
        elif re.search('[^0-9]',gradyear):
            print('Wrong graduate year format')
            return
    elif gradyear not in years or program not in [item.lower() for item in programs]: 
        if gradyear not in years:
            print('Graduate year does not exist')
            return
        if program not in [item.lower() for item in programs]:
            print('Program does not exist')
            return

    years = list(years) # turn back to list to iterate
    years.sort() 
    students = pd.DataFrame() # creating an empty dataframe

    for i in range(len(stu_rec.index)):
        limit = years.index(gradyear)
        for x in range(limit,len(years)):
            if stu_rec.iloc[i]['DegreeProgram'].lower()==program.lower() and stu_rec.iloc[i]['GradYear']==years[x]: # check if there is a record that satisfies the program name and gradyear condition
                students = pd.concat([students,stu_rec.iloc[[i]]])
    if students.empty == False:
        output = pd.DataFrame([[len(students.index), len(students.index)/100]],columns = ['Number of students', '%'])
        print(output)
    else:
        print('Record does not exist')

def newRecord(id,last,first,gradyear,gradterm,program): # to insert a new record into the database
    global stu_rec # declare to use a global variable
    stu_rec.loc[len(stu_rec.index)] = [id,last,first,gradyear,gradterm,program]
    stu_rec.to_csv('/media/Personal/Download/Miu/Fordham/Python/Project/enter the path of the file here.txt',index=False)
    print('Recored saved!')


def StartProgram():
    global stu_rec
    while True:
        try:
            user = int(input('Welcome to the database! What do you want to do? \n1. Show all the students \n2. Search using last name \n3. Search using graduate year \n4. Summary of students graduating at a particular year of a program \n5. Add record \nPress any button to exit \n')) # get input from the user
        except:
            print('Program exit') # Exit the program if the input from user is not a number
            break       
        if user not in [1,2,3,4,5]:
            if user <=0 or user >5: # If the user input is larger than 5 or smaller than 1
                print('Please choose options within 1 to 5')
        else: # If user's input is within the range
            if user == 1:
                Showall()
            elif user == 2:
                lastname = input('Enter student last name: ').lower()
                LastName(lastname)
            elif user == 3:
                gradyear = input('Enter a graduate year: ')
                GradYr(gradyear)
            elif user == 4:
                year = input('Enter a graduate year: ')
                program = input('Enter a program: ').lower()
                Summary(program,year)
            elif user == 5:
                id = input('Enter ID: ')
                if re.search('[^0-9]',id) or id in list(stu_rec['ID']) or not id:
                    if re.search('[^0-9]',id): # Return a value if user input contains decimals or non-digit characters
                        print('ID you have entered is not an integer \nEntry stopped\n')
                    elif not id: # If the string is blank
                        print('Blank entry \nEntry stopped\n')
                    else:
                        print('ID already exists \nEntry stopped\n')
                    continue
                lname = input('Enter Last name: ')
                if re.search('[^A-Za-z]',lname): # Return a value if user input contains non-alphabet characters
                     print('The last name you entered contains non-alphabet characters \nEntry stopped\n')
                     continue
                elif not lname: # If the string is blank
                    print('Blank entry \nEntry stopped\n')
                    continue
                fname = input('Enter First name: ')
                if re.search('[^A-Za-z]',fname): # Return a value if user input contains non-alphabet characters
                     print('The first name you entered contains non-alphabet characters \nEntry stopped\n')
                     continue
                elif not fname: # If the string is blank
                    print('Blank entry \nEntry stopped\n')
                    continue
                gyear = input('Enter graduate year: ')
                if re.search('[^0-9]',gyear): # Return a value if user input contains decimals or non-digit characters
                    print('The year you entered contains non-integer characters \nEntry stopped\n')
                    continue
                elif not gyear: # If the string is blank
                    print('Blank entry \nEntry stopped\n')
                    continue
                sem = input('Enter graduate term: ')
                if re.search('[^A-Za-z]',sem): # Return a value if user input contains non-alphabet characters
                    print('The term you entered contains non-alphabet characters \nEntry stopped\n')
                    continue
                elif not sem: # If the string is blank
                    print('Blank entry \nEntry stopped\n')
                    continue
                prog = input('Enter program: ')
                if re.search('[^A-Za-z]',prog): # Return a value if user input contains non-alphabet characters
                    print('The program you entered contains non-alphabet characters \nEntry stopped\n')
                    continue
                elif not prog: # If the string is blank
                    print('Blank entry \nEntry stopped\n')
                    continue
                newRecord(id,lname,fname,gyear,sem,prog)                
        if input('Do you want to continue? (Press \'y\' to Continue or Any button to Quit) ') != 'y':
            break

StartProgram()
