import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

FILE = "data.json"


def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_session():
    subject = input("Enter subject: ").strip().capitalize()
    try:
        hours = float(input("Enter hours studied: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    entry = {
        "subject": subject,
        "hours": hours,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data = load_data()
    data.append(entry)
    save_data(data)

    print("Study session saved.\n")


def view_summary():
    data = load_data()

    if not data:
        print("No study data found.\n")
        return

    total_hours = sum(d["hours"] for d in data)
    print(f"\nTotal study time: {total_hours:.2f} hours")

    subject_totals = {}
    for d in data:
        subject = d["subject"]
        subject_totals[subject] = subject_totals.get(subject, 0) + d["hours"]

    print("\nTime spent per subject:")
    for subject, hrs in subject_totals.items():
        print(f"{subject}: {hrs:.2f} hours")

    print(f"Total sessions: {len(data)}")

    print()


def show_graph():
    data = load_data()

    if not data:
        print("No data available to display graph.\n")
        return

    subject_totals = {}
    for d in data:
        subject = d["subject"]
        subject_totals[subject] = subject_totals.get(subject, 0) + d["hours"]

    subjects = list(subject_totals.keys())
    hours = list(subject_totals.values())

    plt.bar(subjects, hours)
    plt.xlabel("Subjects")
    plt.ylabel("Hours Studied")
    plt.title("Study Time Distribution")
    plt.tight_layout()
    plt.show()


def main():
    while True:
        print("      Study Tracker      ")
        print("1. Add Study Session")
        print("2. View Summary")
        print("3. Show Graph")
        print("4. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_session()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            show_graph()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
