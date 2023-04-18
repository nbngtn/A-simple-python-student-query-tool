# A-simple-python-student-query-tool
Simulate SQL functionality on pandas dataframe

### 5 query functions:
1. Showall(): To show all records in the database
        If executed, it will print the whole dataframe in the output.

2. LastName(lastname): To search for a student with his/her last name  
When executed, the terminal will prompt the user for a last name input. 
        - Step 1) The program will first check/validate the input from the user. The user can type any type of characters but the program will not accept non-alphabet characters. The function will return a message if the input contains non-alphabet characters.
        - Step 2) Once the program validates that the input is correct in format, it will proceed to search the database for the record.

3. GradYr(gradyr): To search for students graduating on a certain year  
When executed, the terminal will prompt the user for a graduate year input.
        - Step 1) The program will first check/validate the input from the user. The user can type any type of characters but the program will not accept non-numeric   characters. The function will return a message if the input contains non-numeric characters. 
        - Step 2) Once the program validates that the input is correct in format, the program returns all the records that match the input.

4. Summary(program, gradyr): To show the percentage of students from a program that graduates on or after a certain year on total number of students
        When executed, the terminal will prompt the user for inputs for program and graduate year.
    - Step 1) The program will first create two sets: Program names, and Years. These sets will be used later.
    - Step 2) The program will check the if the inputs are in the right format. It only accepts alphabet characters for program name and numeric characters for graduate year.
    - Step 3) The progam will check if the year/program name exists in the database by going through the sets made in step 1.
    - Step 4) Once the program is certain that the inputs are in correct format and they do exist in the database, it will start searching for records that match the parameters. 
    - Step 5) From the returned output, it will calculate the number of students and its percentage upon total number of students.

5. newRecord(id,last,first,gradyear,gradterm,program): Add a new record to the database
    Although the process of input quality check is performed during StartProgram(), I will explain it under this function because the inputs are used for this function.
    The input prompt starts with ID and end with Program. The function will stop immediately once an input for a parameter does not meet the format check:
            ID, Gradyear -> only integers
            Lname, Fname, Sem, Prog -> only alphabet characters
    If all the inputs are correct, a new record with those features will be added to the database.
###
StartProgram(): To start the program
1. Ask the user which function does he/she want to use (1-5)
2. Once the input is received, execute the respective functions
