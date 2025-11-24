import json
import datetime
import os
from collections import defaultdict

class FitnessTracker:
    def _init_(self):
        self.workouts = []  # List of workout dicts
        self.goals = {"weekly_calories": 0, "weekly_workouts": 0}  # Default goals
        self.load_data()

    def log_workout(self, exercise, duration, calories):
        workout = {
            "exercise": exercise,
            "duration": duration,  # in minutes
            "calories": calories,
            "date": datetime.date.today().isoformat()
        }
        self.workouts.append(workout)
        print(f"Workout logged: {exercise} for {duration} min, {calories} cal.")

    def set_goal(self, goal_type, target):
        if goal_type in self.goals:
            self.goals[goal_type] = target
            print(f"Goal set: {goal_type} to {target}.")
        else:
            print("Invalid goal type. Use 'weekly_calories' or 'weekly_workouts'.")

    def get_weekly_summary(self):
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())
        weekly_workouts = [w for w in self.workouts if datetime.date.fromisoformat(w["date"]) >= week_start]
        total_calories = sum(w["calories"] for w in weekly_workouts)
        total_workouts = len(weekly_workouts)
        return total_calories, total_workouts

    def check_goals(self):
        total_calories, total_workouts = self.get_weekly_summary()
        feedback = []
        if total_calories >= self.goals["weekly_calories"]:
            feedback.append("Great job on your calorie goal!")
        else:
            feedback.append(f"You're {self.goals['weekly_calories'] - total_calories} calories away from your goal.")
        if total_workouts >= self.goals["weekly_workouts"]:
            feedback.append("Awesome! You've met your workout count goal.")
        else:
            feedback.append(f"Keep going! {self.goals['weekly_workouts'] - total_workouts} more workouts this week.")
        return feedback

    def visualize_progress(self):
        # Simple text-based bar chart for weekly calories
        total_calories, _ = self.get_weekly_summary()
        bars = int(total_calories / 100)  # 1 bar per 100 calories
        print(f"Weekly Calories Progress: {'█' * bars} ({total_calories} cal)")

    def save_data(self):
        data = {"workouts": self.workouts, "goals": self.goals}
        with open("fitness_data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists("fitness_data.json"):
            with open("fitness_data.json", "r") as f:
                data = json.load(f)
                self.workouts = data.get("workouts", [])
                self.goals = data.get("goals", self.goals)

# CLI Interface
def main():
    tracker = FitnessTracker()
    while True:
        print("\nPersonal Fitness Tracker Menu:")
        print("1. Log Workout")
        print("2. Set Goal")
        print("3. View Weekly Summary")
        print("4. Check Goals")
        print("5. Visualize Progress")
        print("6. Save and Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            exercise = input("Exercise: ")
            duration = int(input("Duration (min): "))
            calories = int(input("Calories burned: "))
            tracker.log_workout(exercise, duration, calories)
        
        elif choice == "2":
            goal_type = input("Goal type (weekly_calories or weekly_workouts): ")
            target = int(input("Target value: "))
            tracker.set_goal(goal_type, target)
        
        elif choice == "3":
            cal, workouts = tracker.get_weekly_summary()
            print(f"This week: {workouts} workouts, {cal} calories burned.")
        
        elif choice == "4":
            feedback = tracker.check_goals()
            for msg in feedback:
                print(msg)
        
        elif choice == "5":
            tracker.visualize_progress()
        
        elif choice == "6":
            tracker.save_data()
            print("Data saved. Exiting.")
            break
        
        else:
            print("Invalid choice.")

if _name_ == "_main_":
    main()
