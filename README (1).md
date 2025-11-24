# fitness-tracker
🚀 P Y T H O N - F I T N E S S - T R A C K E R 🚀

💪 Your Command-Line Companion for Crushing Goals!

Welcome to the Personal Fitness Tracker, a simple but powerful Command Line Interface (CLI) application built in Python. Designed for rapid logging and weekly progress tracking, this app helps you stay accountable and hit your fitness milestones!

✨ Features at a Glance

Emoji

Feature

Description

📝

Log Everything

Quickly record Exercise Type, Duration (minutes), and Calories Burned for every session.

🎯

Set Weekly Goals

Define targets for total Calories burned and total Workouts completed each week.

📊

Progress Visualization

Get an instant, simple text-based bar chart view of your weekly calorie burn.

📅

Weekly Summary

See your accumulated stats for the current Monday-Sunday week.

✅

Goal Check-In

Receive motivational feedback on how close you are to achieving your targets.

💾

Data Persistence

All your data is safely saved to a fitness_data.json file between sessions.

🛠️ Getting Started

Prerequisites

Python 3.x installed on your system.

Installation & Run

Save the Code: Ensure the provided Python code is saved as fitness_tracker.py.

Open Terminal: Navigate to the directory containing the file.

Execute: Run the application using the Python interpreter:

python fitness_tracker.py


🏃 Usage Guide

Once running, the app presents a clear menu. Simply enter the corresponding number for the action you want to take!

Main Menu

Personal Fitness Tracker Menu:
1. Log Workout 📝
2. Set Goal 🎯
3. View Weekly Summary 📅
4. Check Goals ✅
5. Visualize Progress 📊
6. Save and Exit 🚪


1. Log Workout (📝)

This is where you record your activity.

Input Field

Example Input

Notes

Exercise

Cycling

Any descriptive text for your workout.

Duration (min)

45

Time spent working out, in whole minutes.

Calories burned

450

Estimated calories burned.

2. Set Goal (🎯)

Define your weekly targets. The supported goal keys are:

weekly_calories

weekly_workouts

Example:
Goal type: weekly_calories
Target value: 2500

6. Save and Exit (🚪)

🚨 IMPORTANT: Always use option 6 to exit the application. This ensures your latest workouts and any new goal settings are written to fitness_data.json and not lost!

⚙️ How Data Works

The tracker automatically calculates your weekly progress by finding the start of the current week (Monday) and aggregating all logged workouts from that date forward.

File Name: fitness_data.json

Storage: The file is created and maintained in the same directory as the fitness_tracker.py script.

Structure: It stores both your workouts history and your current goals.

{
    "workouts": [
        {
            "exercise": "Weightlifting",
            "duration": 60,
            "calories": 400,
            "date": "2025-11-20"
        }
        // ... more workouts
    ],
    "goals": {
        "weekly_calories": 2500,
        "weekly_workouts": 3
    }
}


Happy Tracking! Keep pushing toward those personal bests! 🥇
