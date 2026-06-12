# Student Management System

## Overview

A Student Management System developed using Python, MySQL, and Pandas to manage student records efficiently. The system supports CRUD operations and handles a dataset containing 1,000,000 student records.

## Features

* View Students
* Search Student by ID
* Add New Student
* Update Student Grade
* Delete Student
* MySQL Database Integration
* Large Dataset Handling (1 Million Records)

## Technologies Used

* Python
* MySQL
* Pandas
* SQL

## Dataset

* Dataset Size: 1,000,000 Records
* Source: Kaggle
* Dataset Download: https://drive.google.com/file/d/1JFjuy6h_zMFs7XNlVJy4NxhTFOt4jgFY/view?usp=sharing

## Installation

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Create Database

```sql
CREATE DATABASE student_management;
```

### Run Project

```bash
python import_data.py
python main.py
```

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── database.py
├── import_data.py
├── README.md
├── requirements.txt
```

## Sample Features

1. View Student Records
2. Search Student by ID
3. Add New Student
4. Update Student Grade
5. Delete Student Record

## Author

Naresh Tarigonda

## Future Enhancements

* GUI using Tkinter
* Student Performance Dashboard
* Export Reports to Excel/PDF
* Login Authentication System
