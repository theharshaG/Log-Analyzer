# Log-Analyzer
Log Analyzer (Python Project)

## Overview

This project is a simple command-line Log Analyzer implemented in Python. It reads log data from a file and allows users to analyze logs by counting errors, displaying error lines with line numbers, and searching for specific keywords. It uses generators for efficient memory usage.

## Features

Count total error messages
Display error lines with line numbers
Search logs by keyword
Efficient file reading using generator
Simple command-line interface

## Technologies Used

Python
File Handling
Generators (yield)

## How to Run

install python (VS Code)
Ensure log.txt file exists with log data
Run the program: log analyzer.py

## How It Works

Log data is stored in a file (log.txt)
Each line represents a log entry

The program reads the file using a generator function (yield)
This helps process large files efficiently

User can perform the following actions:
Count how many lines contain the word "ERROR"
Display error lines along with their line numbers
Search for any keyword in the logs

Search is case-insensitive
If no match is found, a message is displayed

## Future Improvements

Add log level filtering (INFO, WARNING, ERROR)
Export results to file
Add date-based filtering
Convert to GUI application
Develop web version using Flask
Add real-time log monitoring

## Author
Harsha G
Learning Python | Embedded Systems | IoT
