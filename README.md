# Quick-Calc

## Project Description
Quick-Calc is a simple calculator application developed for the Advanced Software Engineering course.  
The application performs basic arithmetic operations including addition, subtraction, multiplication, and division.  
It also includes a clear function to reset the calculator state.

The main focus of the project is demonstrating software testing practices, version control workflows, and proper documentation.

---

## Setup Instructions

1. Clone the repository:

git clone https://github.com/yourusername/swe-testing-assignment.git

2. Navigate to the project directory:

cd swe-testing-assignment

3. Install dependencies:

pip install -r requirements.txt

---

## Running the Application

You can run the calculator logic using Python if needed:

python quick_calc/calculator.py

---

## Running the Tests

Run the test suite using:

python -m pytest

All unit and integration tests should execute automatically.

---

## Testing Framework Research

This project compares two popular Python testing frameworks: **pytest** and **unittest**.

### Pytest
Pytest is a modern testing framework known for concise syntax, powerful fixtures, and detailed assertion reporting.  
It allows developers to write tests using simple functions and requires minimal boilerplate code.

### Unittest
Unittest is Python’s built-in testing framework and follows a class-based testing structure similar to JUnit.  
While stable and widely used, it often requires more setup and produces less readable test output compared to pytest.

### Framework Choice
Pytest was selected for this project because of its simplicity and readability.  
It enables clean test design and faster development, which makes it suitable for small to medium-sized applications like Quick-Calc.

---

## Version

Initial release: **v1.0.0**