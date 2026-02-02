import sqlite3

DB_NAME = "workout_log.db"


class Workout:
    def __init__(self, exercise, weight):
        self.exercise = exercise
        self.weight = weight


def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS workouts
                              (exercise TEXT, weight REAL)"""
        )


def add_workout(workout):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO workouts (exercise, weight) VALUES (?, ?)",
            (workout.exercise, workout.weight),
        )
        conn.commit()


def get_all_workouts():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT exercise, weight FROM workouts")
        return cursor.fetchall()


def delete_all_workouts():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM workouts")
        conn.commit()


def main():
    print("--- GYM WORKOUT LOG ---")
    create_table()

    while True:
        try:
            print("\nMenu:")
            print("1. Add a workout")
            print("2. View all workouts")
            print("3. Clear all records")
            print("4. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                exercise = input("Enter exercise name: ")
                weight = float(input("Enter weight lifted (kg): "))
                new_workout = Workout(exercise, weight)
                add_workout(new_workout)
                print("Workout added successfully.")

            elif choice == "2":
                data = get_all_workouts()
                if data:
                    print("\n--- WORKOUT HISTORY ---")
                    for exercise, weight in data:
                        print(f"Exercise: {exercise:<15} | Weight: {weight} kg")
                else:
                    print("\nNo workouts found. Time to hit the gym!")

            elif choice == "3":
                confirm = input("Are you sure you want to delete everything? (y/n): ")
                if confirm.lower() == "y":
                    delete_all_workouts()
                    print("All records deleted.")

            elif choice == "4":
                print("Goodbye! Keep pushing!")
                break
            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()