import pandas as pd
import numpy as np
import os


class Employee:
    def __init__(self, emp_id, name, age, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def to_dict(self):
        return {
            "ID": self.emp_id,
            "Name": self.name,
            "Age": self.age,
            "Department": self.department,
            "Salary": self.salary
        }


class EmployeeManagementSystem:

    def __init__(self):
        self.file_name = "employees.csv"

        if os.path.exists(self.file_name):
            self.df = pd.read_csv(self.file_name)
        else:
            self.df = pd.DataFrame(columns=[
                "ID",
                "Name",
                "Age",
                "Department",
                "Salary"
            ])
            self.save_data()

    def save_data(self):
        self.df.to_csv(self.file_name, index=False)

    def add_employee(self):

        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(
            emp_id,
            name,
            age,
            department,
            salary
        )

        self.df = pd.concat(
            [
                self.df,
                pd.DataFrame([employee.to_dict()])
            ],
            ignore_index=True
        )

        self.save_data()
        print("Employee Added Successfully")

    def view_employees(self):

        if len(self.df) == 0:
            print("No Employee Found")
            return

        print("\nEmployee Records")
        print(self.df)

    def search_employee(self):

        emp_id = int(input("Enter Employee ID: "))

        result = self.df[self.df["ID"] == emp_id]

        if len(result) == 0:
            print("Employee Not Found")
        else:
            print(result)

    def delete_employee(self):

        emp_id = int(input("Enter Employee ID: "))

        self.df = self.df[self.df["ID"] != emp_id]

        self.save_data()

        print("Employee Deleted")

    def update_salary(self):

        emp_id = int(input("Enter Employee ID: "))
        new_salary = float(input("Enter New Salary: "))

        self.df.loc[
            self.df["ID"] == emp_id,
            "Salary"
        ] = new_salary

        self.save_data()

        print("Salary Updated")

    def analytics(self):

        if len(self.df) == 0:
            print("No Data Available")
            return

        salary = self.df["Salary"].to_numpy()

        print("\n----- Analytics -----")

        print(
            "Average Salary:",
            np.mean(salary)
        )

        print(
            "Highest Salary:",
            np.max(salary)
        )

        print(
            "Lowest Salary:",
            np.min(salary)
        )

        print(
            "Median Salary:",
            np.median(salary)
        )

        print(
            "Standard Deviation:",
            np.std(salary)
        )

        print(
            "90 Percentile:",
            np.percentile(
                salary,
                90
            )
        )

    def department_report(self):

        if len(self.df) == 0:
            print("No Data Available")
            return

        report = self.df.groupby(
            "Department"
        )["Salary"].agg(
            [
                "count",
                "mean",
                "max",
                "min"
            ]
        )

        print("\nDepartment Report")
        print(report)

    def top_earners(self):

        if len(self.df) == 0:
            print("No Data Available")
            return

        top = self.df.sort_values(
            by="Salary",
            ascending=False
        ).head(5)

        print("\nTop 5 Earners")
        print(top)

    def age_salary_correlation(self):

        if len(self.df) < 2:
            print("Not Enough Data")
            return

        age = self.df["Age"].to_numpy()
        salary = self.df["Salary"].to_numpy()

        correlation = np.corrcoef(
            age,
            salary
        )

        print("\nAge-Salary Correlation Matrix")
        print(correlation)

    def menu(self):

        while True:

            print("\n")
            print("=" * 40)
            print("EMPLOYEE MANAGEMENT SYSTEM")
            print("=" * 40)

            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Delete Employee")
            print("5. Update Salary")
            print("6. Analytics")
            print("7. Department Report")
            print("8. Top Earners")
            print("9. Correlation Analysis")
            print("10. Exit")

            choice = input("\nEnter Choice: ")

            if choice == "1":
                self.add_employee()

            elif choice == "2":
                self.view_employees()

            elif choice == "3":
                self.search_employee()

            elif choice == "4":
                self.delete_employee()

            elif choice == "5":
                self.update_salary()

            elif choice == "6":
                self.analytics()

            elif choice == "7":
                self.department_report()

            elif choice == "8":
                self.top_earners()

            elif choice == "9":
                self.age_salary_correlation()

            elif choice == "10":
                print("Thank You")
                break

            else:
                print("Invalid Choice")


if __name__ == "__main__":

    system = EmployeeManagementSystem()

    system.menu()