# Python Command-Line Fitness Tracker

# Project statement

## Problem Statement
Many popular fitness tracking programs are depends on cloud services or closed systems that restrict users' access to and control over their own activity and health data. A lightweight, non-GUI tool that allow users who value privacy, preferences, and a data-driven approach to easily log activities, compute metrics, and produce comprehensive, customised reports directly is frequently lacking.

## Scope of the Project
The project scope is focused on delivering a fully functional, command-line interface (CLI) application built in Python.
- In-Scope
  Data logging for various activities (running, cycling, weightlifting), essential metric calculations (calories burned, pace), data persistence using SQLite or JSON, and real-time visualization of trends and summaries using Matplotlib.
- Out-of-Scope (Initial Phase)
  Developing a Graphical User Interface (GUI), integrating with external fitness APIs (Strava, Fitbit), and implementing machine learning models for prediction or suggestion. These are defined as future enhancements.

## High-Level Features
The application is structured around four core functional pillars:
- Data Logging
  Allows easy input of diverse activities and associated metrics (distance, duration, weight, sets/reps) through simple CLI commands.
- Metric Calculation
  Automatically processes raw data to generate critical fitness metrics, including estimated calorie expenditure (via MET values) and performance pace.
- Data Persistence
  Securely stores and manages all activity logs and body metrics (weight, BMR) in a reliable data store for long-term tracking.
- Visualization and Reporting
  Generates insightful visual outputs (graphs, charts) showing progress over user-defined periods and activity distribution.
