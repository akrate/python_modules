# 🌱 Growing Code  
### *Python Fundamentals Through Garden Data*

Welcome to **Growing Code**, an introductory Python project where you will learn essential programming concepts through simple gardening-themed exercises.  
Each task focuses on core Python fundamentals such as input/output, variables, conditions, loops, and functions.

---

## 📁 Project Structure

Your repository should be organized as follows:

ex00/
ft_hello_garden.py

ex01/
ft_plot_area.py

ex02/
ft_harvest_total.py

ex03/
ft_plant_age.py

ex04/
ft_water_reminder.py

ex05/
ft_count_harvest_iterative.py
ft_count_harvest_recursive.py

ex06/
ft_garden_summary.py

ex07/
ft_seed_inventory.py

main.py

README.md



---

## 🧩 General Rules

- Each exercise must be in its **own directory**.
- Each file must contain **only the function requested**, nothing else.
- **Do NOT** write:
  - a main program  
  - `if __name__ == "__main__":`  
  - test calls or additional helpers
- Your functions must:
  - handle input and output directly (unless parameters are specified)
  - follow **Python 3.10+** syntax
  - respect the **flake8** linter
- Type annotations are optional except for Exercise 7.

---

## 📝 Exercises Overview

### **Exercise 0 – Hello Garden**
**File:** `ex0/ft_hello_garden.py`  
Prints a simple welcome message.

### **Exercise 1 – Garden Plot Area**
**File:** `ex1/ft_plot_area.py`  
Asks for length and width, then prints the area.

### **Exercise 2 – Harvest Total**
**File:** `ex2/ft_harvest_total.py`  
Reads 3 harvest weights and computes the total.

### **Exercise 3 – Plant Age Check**
**File:** `ex3/ft_plant_age.py`  
Determines whether a plant is ready to harvest (>60 days).

### **Exercise 4 – Water Reminder**
**File:** `ex4/ft_water_reminder.py`  
Prints whether plants need watering based on the number of days.

### **Exercise 5 – Count to Harvest**
**Files:**  
- `ft_count_harvest_iterative.py` (loop version)  
- `ft_count_harvest_recursive.py` (recursive version)

Both functions print from Day 1 → Day N, then “Harvest time!”.

### **Exercise 6 – Garden Summary**
**File:** `ex6/ft_garden_summary.py`  
Reads garden info and prints a formatted summary.

### **Exercise 7 – Seed Inventory (with Type Hints)**
**File:** `ex7/ft_seed_inventory.py`  
Displays seed information based on seed type, quantity, and unit.

---

## 🧪 Testing With main.py

A helper script `main.py` is provided with the project subject.

To test your exercises:

```bash
python3 main.py
