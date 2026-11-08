# S3-Minor-Cse-Ananya-

  
Student Database Management System
Course: Programming Foundations for Engineers (25MNCST309)
Regulation: 2025
Project type: Project-Based Learning (PBL)
Language: Python 3
Database: SQLite

1. Project overview
The Student Database Management System is a menu-driven Python application that stores and manages student information in an SQLite database. It supports adding, viewing, searching, updating and deleting student records. It also calculates academic statistics, exports records to CSV, generates a text report and visualizes marks using Matplotlib.

This is a local, single-user educational application. It is not a college ERP system and does not include authentication, role-based access or network deployment.

2. Objectives
Apply Python programming fundamentals to a practical problem.
Implement CRUD (Create, Read, Update, Delete) database operations.
Store student data persistently using SQLite.
Calculate average, minimum and maximum marks.
Classify students as Pass or Fail using a configurable pass mark.
Export records and reports for further use.
Visualize individual and department-wise performance.
3. Four-module syllabus mapping
Module 1 — Programming fundamentals
Concepts demonstrated:

Variables and constants: PASS_MARK, MIN_AGE, MAX_MARK.
Data types: strings, integers, floats, booleans and None.
Operators: arithmetic, comparison and logical operators.
Conditional statements: if, elif, else.
Iteration: while and for loops.
Input validation and exception handling: try, except.
Validation of age, marks, names and email input.
Relevant code: configuration constants, input helper functions, classify_result() and the main menu loop.

Module 2 — Functions and standard libraries
Concepts demonstrated:

User-defined functions.
Function parameters and return values.
Local variables and scope.
Type hints using typing.
Standard libraries: sqlite3, csv, os, sys, datetime, logging and math.
Optional third-party library import using try/except.
Relevant functions include get_integer(), get_mark(), initialize_database(), fetch_student() and calculate_statistics().

Module 3 — Data structures, database and file handling
Concepts demonstrated:

Lists: collections of student records and marks.
Tuples: immutable statistical summary and sample records.
Dictionaries: student records and labelled statistics.
Sets: unique department names.
SQLite database creation and SQL operations.
CRUD operations: INSERT, SELECT, UPDATE and DELETE.
Parameterized SQL queries to avoid SQL injection through user input.
CSV export using Python's csv module.
Text report generation.
Error logging using Python's logging module.
Database table:

Column	Type	Description
id	INTEGER	Auto-increment student ID
name	TEXT	Student name
age	INTEGER	Student age
department	TEXT	Department
email	TEXT	Unique email address
mark	REAL	Mark from 0 to 100
created_at	TEXT	Record creation timestamp
Module 4 — Data visualization and version control
Concepts demonstrated:

Matplotlib bar chart for individual marks.
Matplotlib bar chart for department-wise average marks.
Console text histogram as a fallback when Matplotlib is unavailable.
Saving a chart as a PNG file.
Git and GitHub version-control workflow.
4. System requirements
Python 3.9 or later recommended.
Windows, Linux or macOS.
Matplotlib is optional. The database and console functions work without it.
No separate database server is required; SQLite is included with Python.
5. Project structure
student_database_management/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── students.db              # Created automatically
├── logs/
│   └── application.log          # Created automatically
└── reports/
    ├── students_export.csv      # Created by CSV export
    ├── student_report.txt       # Created by report generation
    └── student_marks_charts.png # Created by visualization
The data, logs and reports directories are created automatically when the program starts. Generated database and report files are local runtime data and should not normally be committed to Git.

6. Installation and execution
Step 1 — Install Python
Install Python 3.9 or later and verify:

python --version
On some Linux systems, use:

python3 --version
Step 2 — Open the project directory
cd student_database_management
Step 3 — Optional: install Matplotlib
python -m pip install -r requirements.txt
If you do not want graphical charts, you can run the program without installing Matplotlib.

Step 4 — Run the application
Windows:

python main.py
Linux/macOS:

python3 main.py
The SQLite database is created automatically at data/students.db.

7. Menu options
Option	Operation
1	Add a student
2	View all students
3	Search by student ID
4	Update a student
5	Delete a student after confirmation
6	Calculate academic statistics
7	Display marks charts
8	Insert sample student records
9	Export records to CSV
10	Generate and display a text report
11	Exit
8. Database and data integrity
The database applies these constraints:

Student ID is an auto-increment primary key.
Name and department cannot be blank.
Age must be between 1 and 120.
Email must be unique and is compared case-insensitively.
Mark must be between 0 and 100.
SQL statements use placeholders (?) rather than string concatenation.
Database operations use SQLite connection context managers for transaction handling.
The email validation is a basic format check, not full RFC email validation. A production system would require stronger validation and account verification.

9. Sample data
Choose menu option 8 to insert ten demonstration students. Existing email addresses are skipped, so running the option repeatedly does not duplicate those sample records.

The sample data is fictional and must not be treated as real student information.

10. Testing checklist
Test	Expected result
Add student with valid values	Record is inserted
Add duplicate email	Database rejects the duplicate
Enter age 0	Input is rejected
Enter mark above 100	Input is rejected
Search for existing ID	Student details are displayed
Search for missing ID	Student not found message
Update existing ID	Record is updated
Delete and confirm with YES	Record is deleted
Delete with any other confirmation	Deletion is cancelled
Calculate statistics with no records	No-record message
Export CSV	CSV file is generated
Generate report	Text report is generated
Run charts without Matplotlib	Text histogram is displayed
11. Git and GitHub workflow
Initialize a repository:

git init
git add main.py README.md requirements.txt .gitignore
git commit -m "Initial student database management system"
Create an empty repository on GitHub, then connect it:

git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/student-database-management.git
git push -u origin main
Replace YOUR_USERNAME with your GitHub username.

Do not commit real student personal information, database files, logs or generated reports.

12. Limitations
This is a command-line application, not a web application.
It is designed for local educational use and one user at a time.
It does not implement login, authorization, audit history or encrypted database storage.
SQLite is appropriate for this project, but a multi-user institutional deployment would need a server-side architecture and access controls.
The pass mark of 40 is an example configuration and should be changed to match the institution's assessment rules.
Matplotlib charts are optional.
13. Future enhancements
Add a graphical user interface using Tkinter.
Add subject-wise marks and semester management.
Add grade calculation and configurable pass criteria.
Add login and role-based access.
Add database backup and restore.
Add a web dashboard using Flask or FastAPI.
Add PDF report generation.
14. Conclusion
The project demonstrates the application of Python fundamentals, functions, data structures, database management, file handling, error handling, data analysis and visualization in a single engineering-oriented application. It provides a practical demonstration of the four-module Programming Foundations for Engineers syllabus.

