import sqlite3

# Try importing matplotlib for graphical visualizations
try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    department TEXT NOT NULL,
    email TEXT UNIQUE,
    mark REAL NOT NULL
)
""")
conn.commit()


# Populate mock data
def insert_mock_data():
    mock_students = [
        ("Alice Johnson", 20, "Computer Science", "alice@example.com", 88.5),
        ("Bob Smith", 21, "Mechanical", "bob@example.com", 72.0),
        ("Charlie Davis", 19, "Electronics", "charlie@example.com", 91.0),
        ("Diana Prince", 22, "Computer Science", "diana@example.com", 95.5),
        ("Ethan Hunt", 20, "Civil", "ethan@example.com", 64.0),
        ("Fiona Gallagher", 21, "Electronics", "fiona@example.com", 82.5),
        ("George Miller", 23, "Mechanical", "george@example.com", 58.0),
        ("Hannah Abbott", 19, "Civil", "hannah@example.com", 76.5),
        ("Ian Malcolm", 22, "Computer Science", "ian@example.com", 85.0),
        ("Julia Roberts", 20, "Electronics", "julia@example.com", 89.0),
    ]

    added_count = 0
    for name, age, dept, email, mark in mock_students:
        try:
            cursor.execute("""
            INSERT INTO students (name, age, department, email, mark)
            VALUES (?, ?, ?, ?, ?)
            """, (name, age, dept, email, mark))
            added_count += 1
        except sqlite3.IntegrityError:
            pass  # Skip if already exists

    conn.commit()
    if added_count > 0:
        print(f"Successfully inserted {added_count} mock student record(s)!")
    else:
        print("Mock data already exists or no new records were added.")


# Add student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter name: ").strip()
    age = int(input("Enter age: "))
    department = input("Enter department: ").strip()
    email = input("Enter email: ").strip()
    mark = float(input("Enter mark: "))

    if not name or not department:
        print("Name and department are required.")
        return

    if age <= 0 or not 0 <= mark <= 100:
        print("Invalid age or mark.")
        return

    try:
        cursor.execute("""
        INSERT INTO students (name, age, department, email, mark)
        VALUES (?, ?, ?, ?, ?)
        """, (name, age, department, email, mark))

        conn.commit()
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Email already exists!")


# View all students with formatted table display
def view_students():
    print("\n--- Student Records ---")

    cursor.execute("SELECT id, name, age, department, email, mark FROM students")
    records = cursor.fetchall()

    if not records:
        print("No student records found.")
        return

    header = f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Department':<18} | {'Email':<25} | {'Mark':<6}"
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for r in records:
        print(f"{r[0]:<5} | {r[1]:<20} | {r[2]:<5} | {r[3]:<18} | {r[4]:<25} | {r[5]:<6.2f}")
    print("-" * len(header))


# Search student
def search_student():
    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "SELECT id, name, age, department, email, mark FROM students WHERE id = ?",
        (student_id,)
    )
    student = cursor.fetchone()

    if student:
        print("\nStudent Found:")
        print(f"  ID:         {student[0]}")
        print(f"  Name:       {student[1]}")
        print(f"  Age:        {student[2]}")
        print(f"  Department: {student[3]}")
        print(f"  Email:      {student[4]}")
        print(f"  Mark:       {student[5]}")
    else:
        print("Student not found!")


# Update student
def update_student():
    student_id = int(input("Enter student ID: "))

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if not cursor.fetchone():
        print("Student not found!")
        return

    name = input("Enter new name: ").strip()
    age = int(input("Enter new age: "))
    department = input("Enter new department: ").strip()
    email = input("Enter new email: ").strip()
    mark = float(input("Enter new mark: "))

    if not name or not department or age <= 0 or not 0 <= mark <= 100:
        print("Invalid input.")
        return

    try:
        cursor.execute("""
        UPDATE students
        SET name=?, age=?, department=?, email=?, mark=?
        WHERE id=?
        """, (name, age, department, email, mark, student_id))

        conn.commit()
        print("Student updated successfully!")

    except sqlite3.IntegrityError:
        print("Email already exists!")


# Delete student
def delete_student():
    student_id = int(input("Enter student ID: "))

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if not cursor.fetchone():
        print("Student not found!")
        return

    confirm = input("Are you sure? (yes/no): ")

    if confirm.lower() == "yes":
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print("Student deleted successfully!")
    else:
        print("Deletion cancelled.")


# Calculate average marks
def calculate_average():
    cursor.execute("SELECT AVG(mark), MIN(mark), MAX(mark), COUNT(*) FROM students")
    avg_mark, min_mark, max_mark, count = cursor.fetchone()

    if count == 0 or avg_mark is None:
        print("No student records available.")
    else:
        print("\n--- Mark Summary Statistics ---")
        print(f"Total Students: {count}")
        print(f"Average Mark:   {avg_mark:.2f}")
        print(f"Highest Mark:   {max_mark:.2f}")
        print(f"Lowest Mark:    {min_mark:.2f}")


# Visualize marks with graphs
def show_marks_graph():
    cursor.execute("SELECT name, mark, department FROM students ORDER BY mark DESC")
    records = cursor.fetchall()

    if not records:
        print("No records available to plot.")
        return

    names = [r[0] for r in records]
    marks = [r[1] for r in records]
    departments = [r[2] for r in records]

    # Console Text Histogram fallback / quick preview
    print("\n--- Text Chart (Score out of 100) ---")
    for name, mark in zip(names, marks):
        bar = "█" * int(mark // 5)
        print(f"{name[:15]:<15} | {bar} ({mark:.1f})")

    if not HAS_MATPLOTLIB:
        print("\nNotice: 'matplotlib' is not installed. To see graphical charts, install it using:")
        print("  pip install matplotlib")
        return

    # Graphical Plots with matplotlib
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # 1. Bar Chart: Student Marks
    bars = axes[0].bar(names, marks, color='skyblue', edgecolor='black')
    axes[0].set_title("Student Marks Overview", fontsize=14, fontweight='bold')
    axes[0].set_xlabel("Students")
    axes[0].set_ylabel("Marks (0-100)")
    axes[0].set_ylim(0, 105)
    axes[0].axhline(y=sum(marks)/len(marks), color='red', linestyle='--', label=f'Avg ({sum(marks)/len(marks):.1f})')
    axes[0].tick_params(axis='x', rotation=45)
    axes[0].legend()
    axes[0].grid(axis='y', linestyle=':', alpha=0.7)

    for bar in bars:
        yval = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}", ha='center', va='bottom', fontsize=8)

    # 2. Bar Chart: Department-wise Average
    cursor.execute("SELECT department, AVG(mark) FROM students GROUP BY department")
    dept_data = cursor.fetchall()
    depts = [d[0] for d in dept_data]
    dept_avgs = [d[1] for d in dept_data]

    dept_bars = axes[1].bar(depts, dept_avgs, color='lightgreen', edgecolor='black')
    axes[1].set_title("Department-wise Average Marks", fontsize=14, fontweight='bold')
    axes[1].set_xlabel("Department")
    axes[1].set_ylabel("Average Mark")
    axes[1].set_ylim(0, 105)
    axes[1].tick_params(axis='x', rotation=30)
    axes[1].grid(axis='y', linestyle=':', alpha=0.7)

    for bar in dept_bars:
        yval = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}", ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()


# Main menu
while True:
    print("\n================================")
    print(" STUDENT DATABASE MANAGEMENT ")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average Marks & Stats")
    print("7. Visualize Marks Graph")
    print("8. Load Mock Data")
    print("9. Exit")

    choice = input("Enter your choice: ").strip()

    try:
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average()
        elif choice == "7":
            show_marks_graph()
        elif choice == "8":
            insert_mock_data()
        elif choice == "9":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 9.")

    except ValueError:
        print("Please enter valid numeric values.")
    except sqlite3.Error as error:
        print("Database error:", error)

conn.close()
