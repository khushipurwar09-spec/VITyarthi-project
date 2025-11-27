import json
import datetime
import os

class FitnessTracker:
    """
    A Command-Line Fitness Tracking System.
    Tracks workouts, calories, goals, BMI, and workout history
    while saving progress locally in JSON format.
    """

    def __init__(self):
        # List to store workouts 
        self.workouts = []
        # Weekly goals for calories & workout count
        self.goals = {"weekly_calories": 0, "weekly_workouts": 0}
        # Saved progress
        self.load_data()

    def log_workout(self, exercise, duration, calories):
        """Store exercise details with timestamp."""
        workout = {
            "exercise": exercise,
            "duration": duration,   # time spent in minutes
            "calories": calories,   # calories burned
            "date": datetime.date.today().isoformat()  # current date
        }
        self.workouts.append(workout)
        print(f"\n✔ Workout logged: {exercise} for {duration} mins, {calories} calories.")

    def set_goal(self, goal_type, target):
        """Set weekly calorie goal or weekly workout count goal."""
        if goal_type in self.goals:
            self.goals[goal_type] = target
            print(f"\n✔ Goal updated: {goal_type} → {target}")
        else:
            print("\n❌ Invalid goal type. Use: weekly_calories / weekly_workouts")

    def get_weekly_summary(self):
        """Return calories burnt + number of workouts for the current week."""
        today = datetime.date.today()
        # Finding Monday of current week
        week_start = today - datetime.timedelta(days=today.weekday())

        # Filter only this week's logged workouts
        weekly_data = [
            w for w in self.workouts if datetime.date.fromisoformat(w["date"]) >= week_start
        ]

        # Total calories and workout count
        total_calories = sum(w["calories"] for w in weekly_data)
        total_workouts = len(weekly_data)
        return total_calories, total_workouts

    def check_goals(self):
        """Check whether weekly calorie and workout goals have been achieved."""
        calories, workouts = self.get_weekly_summary()
        print("\n----- Goal Status -----")

        # Calorie goal check
        if calories >= self.goals["weekly_calories"]:
            print("Calories Goal: ✔ Achieved")
        else:
            print(f"Calories Goal: ❌ Need {self.goals['weekly_calories'] - calories} more calories")

        # Workout count goal check
        if workouts >= self.goals["weekly_workouts"]:
            print("Workout Count Goal: ✔ Achieved")
        else:
            print(f"Workout Count Goal: ❌ Need {self.goals['weekly_workouts'] - workouts} more workouts")

    def visualize_progress(self):
        """Display progress using bar graph (text only) — 1 block = 100 calories."""
        calories, _ = self.get_weekly_summary()
        bars = int(calories / 100)
        print("\n----- Weekly Calorie Progress -----")
        print("█" * bars, f"({calories} cal)")

    # More Features

    def calculate_bmi(self, weight, height):
        """Calculate BMI from weight (kg) and height (cm)."""
        height_m = height / 100  # convert to meters
        bmi = weight / (height_m ** 2)
        print(f"\nYour BMI: {bmi:.2f}")

        # Health 
        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    def view_history(self):
        """Display full list of saved workouts."""
        if not self.workouts:
            print("\n⚠ No workouts logged yet.")
            return
        print("\n----- Workout History -----")
        for i, w in enumerate(self.workouts, start=1):
            print(f"{i}. {w['date']} → {w['exercise']} | {w['duration']} mins | {w['calories']} cal")

    def delete_workout(self, index):
        """Delete an incorrectly added workout using history index."""
        if 0 <= index < len(self.workouts):
            removed = self.workouts.pop(index)
            print(f"\n✔ Deleted workout: {removed['exercise']} ({removed['date']})")
        else:
            print("\n❌ Invalid index.")

    # Saving & Loading

    def save_data(self):
        """Save workouts & goals in JSON file for future use."""
        data = {"workouts": self.workouts, "goals": self.goals}
        with open("fitness_data.json", "w") as f:
            json.dump(data, f, indent=4)
        print("\n💾 Progress saved.")

    def load_data(self):
        """Load previous progress if JSON exists."""
        if os.path.exists("fitness_data.json"):
            with open("fitness_data.json", "r") as f:
                data = json.load(f)
                self.workouts = data.get("workouts", [])
                self.goals = data.get("goals", self.goals)

# Main App Menu

def main():
    tracker = FitnessTracker()

    while True:
        print("\n===== PERSONAL FITNESS TRACKER =====")
        print("1. Log Workout")
        print("2. Set Goal")
        print("3. View Weekly Summary")
        print("4. Check Goals")
        print("5. Visualize Progress")
        print("6. BMI Calculator")
        print("7. View Workout History")
        print("8. Delete Workout Entry")
        print("9. Save & Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == "1":
                # Input workout details
                ex = input("Exercise: ")
                duration = int(input("Duration (minutes): "))
                calories = int(input("Calories burned: "))
                tracker.log_workout(ex, duration, calories)

            elif choice == "2":
                # Update weekly goals
                g_type = input("Goal type (weekly_calories / weekly_workouts): ")
                val = int(input("Target value: "))
                tracker.set_goal(g_type, val)

            elif choice == "3":
                # Display weekly calories + workout count
                cal, count = tracker.get_weekly_summary()
                print(f"\nWeekly Summary → {count} workouts | {cal} calories burned")

            elif choice == "4":
                # Check goal status
                tracker.check_goals()

            elif choice == "5":
                # Show graphical progress
                tracker.visualize_progress()

            elif choice == "6":
                # BMI calculation
                weight = float(input("Weight (kg): "))
                height = float(input("Height (cm): "))
                tracker.calculate_bmi(weight, height)

            elif choice == "7":
                # Show workout list
                tracker.view_history()

            elif choice == "8":
                # Delete workout
                tracker.view_history()
                idx = int(input("\nEnter workout number to delete: ")) - 1
                tracker.delete_workout(idx)

            elif choice == "9":
                # Save and exit
                tracker.save_data()
                print("\nExiting... Stay consistent & stay fit! 💪")
                break

            else:
                print("\n❌ Invalid choice. Try again.")

        except ValueError:
            print("\n❌ Input must be a number. Try again.")

if __name__ == "__main__":
    main()
