# Geometric Shape Calculator

A simple Python-based Geometric Shape Calculator that calculates areas, volumes, perimeters, surface areas, and other measurements for different geometric shapes.

The program provides a menu of 12 geometric shapes, accepts user input, performs the required calculation, displays the result, and maintains a calculation history during the program run.

## Features

- Supports 12 different geometric shapes

- Calculates areas and volumes

📏 Calculates perimeter, circumference, surface area, and slant height where applicable

🎲 Generates a random shape suggestion

🔢 Generates a random number

🕒 Displays the current date and time

📋 Displays the formula used for the selected shape

- Stores calculation history during the program execution

- Validates that dimensions are greater than zero

- Handles invalid menu choices

## Supported Shapes
No.	Shape	Calculation
1	Circle	Area, Circumference
2	Rectangle	Area, Perimeter
3	Square	Area, Perimeter
4	Triangle	Area
5	Trapezium	Area
6	Parallelogram	Area
7	Cube	Volume, Surface Area
8	Cuboid	Volume, Surface Area
9	Cylinder	Volume, Curved Surface Area
10	Cone	Volume, Slant Height
11	Sphere	Volume, Surface Area
12	Hemisphere	Volume, Curved Surface Area
📐 Formulas Used
1. Circle

Area

π × r²


Circumference

2 × π × r

2. Rectangle

Area

length × breadth


Perimeter

2 × (length + breadth)

3. Square

Area

side²


Perimeter

4 × side

4. Triangle

Area

½ × base × height

5. Trapezium

Area

½ × (a + b) × height

6. Parallelogram

Area

base × height

7. Cube

Volume

side³


Surface Area

6 × side²

8. Cuboid

Volume

length × breadth × height


Surface Area

2 × (lb + bh + hl)

9. Cylinder

Volume

π × r² × h


Curved Surface Area

2 × π × r × h

10. Cone

Volume

(π × r² × h) / 3


Slant Height

√(r² + h²)

11. Sphere

Volume

(4 × π × r³) / 3


Surface Area

4 × π × r²

12. Hemisphere

Volume

(2 × π × r³) / 3


Curved Surface Area

2 × π × r²

🛠️ Technologies Used

Python 3

math module

random module

datetime module

All modules used in the program are part of Python's standard library, so no external packages are required.

📁 Project Structure
Geometric-Shape-Calculator/\
│ \
├── geometric_shape_calculator.py\
└── README.md


Replace geometric_shape_calculator.py with the actual filename if your Python file has a different name.

🚀 How to Run
1. Install Python

Make sure Python 3 is installed on your computer.

You can check your Python installation using:

python --version


or:

python3 --version

2. Clone or Download the Project

Download the project files to your computer.

3. Open the Project Folder

Open a terminal or command prompt in the project directory.

4. Run the Program
python geometric_shape_calculator.py


On some systems, use:

python3 geometric_shape_calculator.py

▶️ Example Usage

When the program starts, it displays the available shapes:

========================================
       GEOMETRIC SHAPE CALCULATOR
========================================
1. Circle
2. Rectangle
3. Square
4. Triangle
5. Trapezium
6. Parallelogram
7. Cube
8. Cuboid
9. Cylinder
10. Cone
11. Sphere
12. Hemisphere
========================================


The program also generates a random shape suggestion:

Random Shape Number: 3
Random Shape Suggestion: Square


The user can then select a shape:

Enter your choice: 1


For a circle, the program asks for the radius:

Enter radius: 5


The output may look like:

Shape = Circle
Area = 78.53981633974483
Circumference = 31.41592653589793


The selected shape and its formula are displayed afterward:

========================================
Selected Shape: Circle
Formula: Area = 3.14 * r * r
========================================

📚 Calculation History

The program stores completed calculations in the history list.

For example:

Calculation History:
[('Circle', 78.53981633974483)]


If the calculation is not completed because of invalid input, the program displays:

No calculation was completed


Note: The history is stored only while the program is running. It is not saved to a file or database.

🎲 Random Features

The program uses Python's random module for two purposes.

Random Shape Suggestion

A number from 1 to 12 is generated:

random_number = random.randint(1, 12)


This number is used to suggest one of the available shapes.

Random Number

At the end of the program, another random number from 1 to 100 is generated:

random_number = random.randint(1, 100)

🕒 Date and Time

The program displays the current date and time using Python's datetime module.

Example:

Date: 2026-09-27
Time: 01:02:30

✅ Input Validation

The program checks that dimensions such as radius, length, breadth, base, height, and side are greater than zero.

For example:

Enter radius: -5
Radius must be greater than 0


This prevents calculations from being performed with invalid negative dimensions.

⚠️ Current Limitations

The program accepts only one calculation per execution.

Calculation history is not permanently saved.

Entering non-numeric input such as abc can cause a ValueError.

The formula dictionary uses 3.14 for display, while calculations use math.pi.

The sphere volume formula displayed in the formulas dictionary should mathematically be interpreted as (4 × π × r³) / 3.

The program does not currently provide an option to repeat calculations without restarting.

The shape_set is used to count the total number of shapes but does not otherwise affect calculations.

🔮 Possible Future Improvements

The project could be improved by adding:

🔄 A loop to perform multiple calculations in one execution

💾 Saving calculation history to a text, CSV, or JSON file

🧾 A dedicated history menu

🛡️ Better handling of non-numeric input using try-except

🎨 A graphical user interface using Tkinter

📊 More geometric shapes

📏 Additional measurements such as total surface area

🔢 Rounded results for easier reading

🧹 Cleaner and more reusable functions for each shape

📖 More detailed formula descriptions

❌ An option to exit the calculator from the menu

🎯 Learning Objectives

This project demonstrates several important Python concepts:

Variables and data types

User input with input()

Conditional statements

if, elif, and else

Tuples

Sets

Dictionaries

Lists

List methods such as append()

Mathematical calculations

Built-in Python modules

Random number generation

Date and time handling

Basic input validation

Functions from the math module

👨‍💻 Project Purpose

The main purpose of this project is to create a beginner-friendly Python application for performing common geometric calculations while practicing fundamental programming concepts.

It can also be used as a school/college Python project or as a beginner programming exercise.

📜 License

This project is free to use, modify, and learn from.

⭐ Acknowledgement

Built using Python and its standard library modules:

random
datetime
math


Thank you for using the Geometric Shape Calculator! 📐🐍
