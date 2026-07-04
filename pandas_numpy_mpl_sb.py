import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import math as m

"""
1. Add Employees
2. Add New Employee
3. Calculate Bonus
4. Calculate Total Salary
5. Salary Details
6. Search Employee
7. Load Data
8. Save Data
9. View All Employees
10. Exit
"""

def add_student():
    try:
        n = int(input("Enter the number of employees: "))
    except ValueError:
        print("Enter only integers.")
        return pd.DataFrame()

    employee = []

    for i in range(n):
        print(f"\nEmployee {i+1}")

        try:
            name = input("Name : ")
            emp_id = int(input("ID : "))
            age = int(input("Age : "))
            number = input("Phone Number : ")
            s1 = int(input("Score 1 : "))
            s2 = int(input("Score 2 : "))
            s3 = int(input("Score 3 : "))
            salary = int(input("Salary : "))
        except ValueError:
            print("Invalid input. Employee skipped.")
            continue

        score = ((s1 + s2 + s3) / 300) * 100

        employee.append({
            "name": name,
            "salary": salary,
            "id's": emp_id,
            "age": age,
            "P_no.": number,
            "s1": s1,
            "s2": s2,
            "s3": s3,
            "score": score
        })

    return pd.DataFrame(employee)


def add(df):

    if "bonus" not in df.columns:
        df["bonus"] = 0

    if "total_salary" not in df.columns:
        df["total_salary"] = 0

    try:
        name = input("Name : ")
        emp_id = int(input("ID : "))
        age = int(input("Age : "))
        number = input("Phone Number : ")
        s1 = int(input("Score 1 : "))
        s2 = int(input("Score 2 : "))
        s3 = int(input("Score 3 : "))
        salary = int(input("Salary : "))
    except ValueError:
        print("Invalid input.")
        return df

    score = ((s1 + s2 + s3) / 300) * 100

    df.loc[len(df)] = {
        "name": name,
        "salary": salary,
        "id's": emp_id,
        "age": age,
        "P_no.": number,
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "score": score,
        "bonus": 0,
        "total_salary": salary
    }

    print("Employee Added Successfully.")
    return df


def bonus(df):

    if df.empty:
        print("No employee data found.")
        return df

    df["bonus"] = 0

    df.loc[(df["salary"] > 0) & (df["salary"] <= 20000), "bonus"] = df["salary"] * 0.10
    df.loc[(df["salary"] > 20000) & (df["salary"] <= 50000), "bonus"] = df["salary"] * 0.20
    df.loc[df["salary"] > 50000, "bonus"] = df["salary"] * 0.25

    print("Bonus Calculated Successfully.")
    return df


def total_salary(df):

    if df.empty:
        print("No employee data found.")
        return df

    if "bonus" not in df.columns:
        print("Please calculate bonus first.")
        return df

    df["total_salary"] = df["salary"] + df["bonus"]

    print(df)
    return df


def detail(df):

    if df.empty:
        print("No employee data.")
        return

    if "total_salary" not in df.columns:
        print("Calculate total salary first.")
        return

    print("\nSalary Details")
    print("-" * 30)

    print("Mean   :", df["total_salary"].mean())
    print("Median :", df["total_salary"].median())
    print("Mode   :")
    print(df["total_salary"].mode())


def save(df):

    if df.empty:
        print("No data to save.")
        return

    df.to_csv("man013.csv", index=False)
    print("File Saved Successfully.")


def Loading():

    try:
        df = pd.read_csv("man013.csv")
        print("File Loaded Successfully.")
        return df

    except FileNotFoundError:
        print("File not found.")
        return pd.DataFrame()


def search(df):

    if df.empty:
        print("No employee data.")
        return df

    try:
        emp_id = int(input("Enter Employee ID : "))
    except ValueError:
        print("Invalid ID.")
        return df

    result = df[df["id's"] == emp_id]

    if len(result) > 0:
        print(result)
    else:
        print("Employee Not Found.")

    return df


def menu():

    df = pd.DataFrame()

    while True:

        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employees")
        print("2. Add New Employee")
        print("3. Calculate Bonus")
        print("4. Calculate Total Salary")
        print("5. Salary Details")
        print("6. Search Employee")
        print("7. Load Data")
        print("8. Save Data")
        print("9. View All Employees")
        print("10. Exit")

        try:
            c = int(input("Enter Your Choice : "))
        except ValueError:
            print("Enter only integers.")
            continue

        if c == 1:
            df = add_student()

        elif c == 2:
            df = add(df)

        elif c == 3:
            df = bonus(df)

        elif c == 4:
            df = total_salary(df)

        elif c == 5:
            detail(df)

        elif c == 6:
            search(df)

        elif c == 7:
            df = Loading()

        elif c == 8:
            save(df)

        elif c == 9:
            if df.empty:
                print("No employee data.")
            else:
                print(df)

        elif c == 10:
            print("Thank You.")
            break

        else:
            print("Invalid Choice.")


menu()