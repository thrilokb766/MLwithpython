with open("tasks.json", "r") as file: import datetime

habits = {}



def add_habit():
    habit_name = input("Enter a new habit to track: ")

    if habit_name in habits:
        print(f"Habit '{habit_name}' already exists.")
    else:
        habits[habit_name] = {
            "log": [],  # Stores completion dates
            "streak": 0  # Tracks number of days in a row
        }
        print(f"Habit '{habit_name}' added successfully!")



def log_habit():
    habit_name = input("Enter the habit you completed today: ")

    if habit_name in habits:
        today = str(datetime.date.today())

        if today in habits[habit_name]["log"]:
            print("You already logged this habit for today!")
        else:
            habits[habit_name]["log"].append(today)
            habits[habit_name]["streak"] += 1
            print(f"Great job! Logged '{habit_name}' for today.")
    else:
        print("Habit not found. Please add it first.")

def view_habits():
    if not habits:
        print("No habits found.")
    else:
        print("\nYour Habits:")
        for name, data in habits.items():
            print(f"- {name}: Streak = {data['streak']}, Log = {data['log']}")


while True:
    print("\n========== Habit Tracker ==========")
    print("1. Add Habit")
    print("2. Log Habit")
    print("3. View Habits")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_habit()
    elif choice == "2":
        log_habit()
    elif choice == "3":
        view_habits()
    elif choice == "4":
        print("Goodbye! Keep tracking your habits! 😊")
        break
    else:
        print("Invalid choice. Please try again.")
