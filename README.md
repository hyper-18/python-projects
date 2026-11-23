# python-projects
Python projects from beginner to advanced
## Project 1: Expense Tracker

A Python command-line application for managing personal expenses.

### Features
- Add expenses with amount, category, and description.
- Automatically record expense dates.
- View all recorded expenses.
- Calculate total expenses.
- Delete existing expenses.
- Save and load expenses using JSON.
- Preserve expense history after restarting the application.
- Validate user inputs.
- Display amounts in INR (₹).

### Technologies
- Python
- Object-Oriented Programming
- JSON
- File Handling
- Exception Handling
- DateTime Module

### How to Run

1. Open the `expense-tracker` folder.
2. Run:

bash
python main.py
==================================================
## Project 2: Password Strength Checker

A Python-based command-line application that evaluates password strength using predefined security rules.

### Features
- Password length validation.
- Uppercase and lowercase detection.
- Number and special-character detection.
- Common weak password detection.
- Password strength scoring (0–6).
- Personalized improvement suggestions.
- Interactive command-line interface.

### Technologies
- Python
- Regular Expressions
- String Methods
- Functions
- Conditional Statements

### How to Run

1. Open the project folder.
2. Run:

bash
python main.py
==================================================
## Project 3: Quiz Application

A Python-based command-line quiz application featuring multiple-choice questions, difficulty levels, and timed answers.

### Features
- 15 multiple-choice questions.
- Easy, Medium, and Hard difficulty levels.
- Randomized question order.
- Answer validation.
- 15-second timer per question.
- Automatic score calculation.
- Correct answer display.
- Final percentage and performance feedback.
- Replay functionality.

### Technologies
- Python
- Lists and Dictionaries
- Functions
- Loops and Conditional Statements
- Random Module
- Time Module
- Windows `msvcrt` Module

### How to Run

1. Open the `quiz-application` folder.
2. Run:

bash
python main.py
====================================================
# Project 4 — Contact Management System

A simple Python-based Contact Management System that allows users to store, view, search, update, and delete contact information through a menu-driven interface.

## Features

- **Add Contact:** Save a new contact with details.
- **View Contacts:** Display all saved contacts.
- **Search Contact:** Find contacts using their name.
- **Update Contact:** Modify existing contact information.
- **Delete Contact:** Remove contacts from the system.
- **Menu-Driven Interface:** Navigate through different operations using a simple terminal menu.

## Technologies Used

- Python 3
- Object-Oriented Programming
- Lists and Dictionaries
- Functions and Conditional Statements
- Loops
- CRUD Operations

## Project Structure

```text
contact-management/
│
├── main.py
├── contact.py
└── README.md
```
## How to Run

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd python-projects/contact-management
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Learning Outcomes

Through this project, I practised:

- Creating and working with Python classes and objects.
- Organizing code into multiple files.
- Implementing CRUD operations.
- Managing collections of data.
- Using loops and conditional statements.
- Building menu-driven command-line applications.

## Future Improvements

- Add JSON-based data persistence.
- Prevent duplicate contacts.
- Improve input validation.
- Add search functionality using phone numbers and email addresses.

---

**Project:** 04 / Python Projects Series  
**Language:** Python  
**Difficulty:** Beginner
====================================================
# Project 5 — Library Management System

A Python-based Library Management System that allows users to manage books, track availability, and perform library operations through a menu-driven command-line interface.

## Features

- **Add Book:** Add new books using their title, author, and ISBN.
- **View Books:** Display all books stored in the library.
- **Search Book:** Search for books by title or author.
- **Issue Book:** Issue an available book.
- **Return Book:** Return a previously issued book.
- **Delete Book:** Remove books from the library.
- **Duplicate ISBN Prevention:** Prevent adding books with an existing ISBN.
- **Data Persistence:** Store book information permanently using JSON.
- **Automatic Loading:** Load previously saved books when the application starts.
- **Input Validation:** Handle empty inputs and invalid operations.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Classes and Objects
- Lists and Dictionaries
- JSON
- File Handling
- Exception Handling

## Project Structure

```text
library-management-system/
│
├── main.py
├── book.py
├── library.py
├── books.json
└── README.md
```

## How to Run

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd python-projects/library-management-system
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Data Storage

The application uses `books.json` to store book information.

Each book contains:

- Title
- Author
- ISBN
- Availability status

The application automatically saves changes and restores the saved data when restarted.

## Learning Outcomes

Through this project, I practised:

- Implementing Object-Oriented Programming.
- Creating and managing classes and objects.
- Working with lists and dictionaries.
- Reading and writing JSON files.
- Implementing CRUD operations.
- Handling exceptions and invalid inputs.
- Building a menu-driven Python application.

## Future Improvements

- Add a graphical user interface.
- Track borrower information.
- Add issue and return dates.
- Generate library reports.
- Support multiple library users.

---

**Project:** 05 / Python Projects Series  
**Language:** Python  
**Difficulty:** Beginner to Intermediate
====================================================
# Project 6 — Weather Application

A Python-based Weather Application that fetches real-time weather information for any city using the Open-Meteo API.

The application allows users to search for cities and retrieve current weather conditions through a simple command-line interface.

## Features

- **Search City:** Search for weather information using a city name.
- **Current Temperature:** Display the current temperature.
- **Feels-Like Temperature:** Show the apparent temperature.
- **Weather Conditions:** Display conditions such as clear sky, cloudy, rain, and thunderstorms.
- **Humidity:** Display relative humidity.
- **Wind Speed:** Show current wind speed.
- **Precipitation:** Display current precipitation.
- **Daytime Detection:** Identify whether it is currently daytime or nighttime.
- **Error Handling:** Handle invalid city names, network errors, and API failures.
- **Continuous Search:** Search for multiple cities without restarting the application.

## Technologies Used

- Python 3
- Requests Library
- Open-Meteo API
- HTTP Requests
- JSON Parsing
- Exception Handling
- Python Functions and Dictionaries

## API Used

This project uses the free **Open-Meteo API**.

- Geocoding API: Converts city names into geographical coordinates.
- Weather Forecast API: Retrieves current weather information using latitude and longitude.

No API key is required.

## Project Structure

```text
weather-application/
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd python-projects/weather-application
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Execute the following command:

```bash
python main.py
```

Enter a city name to retrieve its current weather information.

Type `exit` to close the application.

## Learning Outcomes

Through this project, I practised:

- Understanding and integrating external APIs.
- Sending HTTP requests using Python's Requests library.
- Retrieving and processing JSON responses.
- Working with dictionaries and functions.
- Handling API errors and network exceptions.
- Using geographical coordinates to retrieve location-specific information.

## Future Improvements

- Add a graphical user interface.
- Display a five-day weather forecast.
- Add weather icons.
- Support temperature conversion between Celsius and Fahrenheit.
- Add automatic location detection.
- Store recently searched cities.

---

**Project:** 06 / Python Projects Series  
**Language:** Python  
**API:** Open-Meteo  
**Difficulty:** Beginner to Intermediate
====================================================
# Expense Splitter

A command-line Python application that helps a group of people manage shared expenses, calculate individual balances, and determine who owes whom.

## Features

- Add and manage participants.
- Add shared expenses.
- Split expenses equally among selected participants.
- View all recorded expenses.
- Calculate individual balances.
- Generate settlement suggestions.
- Edit existing expenses.
- Delete expenses.
- Save records automatically using JSON.
- Load previously saved data when the application starts.
- Input validation and error handling.

## Project Structure

```text
expense-splitter/
│
├── main.py
├── expense.py
├── splitter.py
├── data.json
└── README.md
```

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Lists and Dictionaries
- Exception Handling

## How to Run

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd expense-splitter
```

**3. Run the application**

```bash
python main.py
```

## How It Works

1. Add participants to the group.
2. Record expenses and specify who paid.
3. Select the participants sharing each expense.
4. The application calculates individual balances.
5. View settlement suggestions to determine who owes money.
6. Your records are automatically saved in `data.json`.

## Concepts Practiced

- Classes and Objects
- Object-Oriented Programming
- Functions and Modules
- Lists and Dictionaries
- JSON Serialization and Deserialization
- File Handling
- CRUD Operations
- Input Validation
- Exception Handling

## Current Limitations

- Expenses are divided equally among selected participants.
- Unequal expense splitting is not supported.
- Settlement suggestions are calculated using net balances.
- Small floating-point rounding differences may occur.

## Learning Outcome

This project helped me understand how to build a multi-file Python application, manage shared financial records, implement CRUD operations, calculate balances, and maintain persistent data using JSON.
====================================================
# Student Grade Management System

A command-line Python application designed to manage student records, store subject-wise marks, calculate percentages, and generate student report cards.

## Features

- Add new students.
- View all registered students.
- Search students using roll numbers.
- Add subject-wise marks.
- Generate individual report cards.
- Calculate total marks and percentages.
- Automatically assign grades.
- Update student names and roll numbers.
- Update existing subject marks.
- Delete student records.
- Sort students by name or percentage.
- Display class performance statistics.
- Automatically save and load records using JSON.
- Input validation and error handling.

## Project Structure

```text
student-grade-management/
│
├── main.py
├── student.py
├── students.json
└── README.md
```

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Dictionaries
- Lists
- Lambda Functions
- Exception Handling

## How to Run

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd student-grade-management
```

**3. Run the application**

```bash
python main.py
```

## How It Works

1. Add students using their names and roll numbers.
2. Enter marks for different subjects.
3. Generate individual student report cards.
4. View calculated totals, percentages, and grades.
5. Update or delete student records when required.
6. Sort students based on names or academic performance.
7. View overall class performance statistics.

All student records are automatically saved in `students.json` and loaded when the application starts.

## Grading System

| Percentage | Grade |
|---|---|
| 90–100% | A+ |
| 80–89% | A |
| 70–79% | B |
| 60–69% | C |
| 50–59% | D |
| Below 50% | F |

## Concepts Practiced

- Classes and Objects
- Object-Oriented Programming
- Functions and Modules
- Dictionaries and Nested Dictionaries
- JSON Serialization and Deserialization
- File Handling
- CRUD Operations
- Sorting using Lambda Functions
- Exception Handling
- Data Persistence

## Current Limitations

- Each subject has a maximum of 100 marks.
- All subjects have equal weightage.
- Percentage is calculated using the average of entered subjects.
- Data is stored locally in a JSON file.
- No database or authentication system is implemented.

## Learning Outcome

This project helped me understand how to build a student management application using Python, implement CRUD operations, work with JSON files, perform calculations, sort records, and maintain persistent data
====================================================