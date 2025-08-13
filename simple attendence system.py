import csv
from datetime import datetime

FILENAME = "attendance.csv"

# Create CSV file with header if not exists
try:
    with open(FILENAME, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Student ID", "Name", "Status"])
except FileExistsError:
    pass


def mark_attendance(student_id, name, status):
    """Marks attendance for a student"""
    date_today = datetime.now().strftime("%Y-%m-%d")
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_today, student_id, name, status])
    print(f"✅ Attendance marked for {name} as {status}")


def view_attendance(sort_by="Date"):
    """Displays attendance sorted by Date, Name, or Student ID"""
    with open(FILENAME, "r") as file:
        reader = list(csv.reader(file))
        header = reader[0]
        data = reader[1:]

    # Sorting logic
    if sort_by.lower() == "name":
        data.sort(key=lambda x: x[2].lower())  # Sort by Name
    elif sort_by.lower() == "id":
        data.sort(key=lambda x: x[1])  # Sort by Student ID
    else:
        data.sort(key=lambda x: x[0], reverse=True)  # Sort by Date (latest first)

    # Display
    print("\n" + "-" * 40)
    print(", ".join(header))
    print("-" * 40)
    for row in data:
        print(", ".join(row))
    print("-" * 40)


# Main Program Loop
while True:
    print("\n--- Simple Attendance System ---")
    print("1. Mark Attendance")
    print("2. View Attendance (Sorted by Date)")
    print("3. View Attendance (Sorted by Name)")
    print("4. View Attendance (Sorted by Student ID)")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        status = input("Present or Absent? ").capitalize()
        mark_attendance(sid, name, status)

    elif choice == "2":
        view_attendance("date")

    elif choice == "3":
        view_attendance("name")

    elif choice == "4":
        view_attendance("id")

    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
