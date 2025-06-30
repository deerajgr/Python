import os

FILE_NAME = 'employee_data.txt'

# Load data from txt file
def load_data():
    employees = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            for line in f:
                if line.strip() == "":
                    continue
                name, age, designation, salary = line.strip().split(',')
                employees.append({
                    'name': name,
                    'age': int(age),
                    'designation': designation,
                    'salary': int(salary)
                })
    return employees

# Save data to txt file
def save_data(employees):
    with open(FILE_NAME, 'w') as f:
        for emp in employees:
            f.write(f"{emp['name']},{emp['age']},{emp['designation']},{emp['salary']}\n")

def main():
    employees = load_data()

    while True:
        print("\n1) Create\n2) Display\n3) Raise Salary\n4) Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                try:
                    name = input("Enter employee name: ")
                    age = int(input("Enter employee age: "))
                    if not (18 <= age <= 60):
                        raise ValueError("Age must be between 18 and 60.")

                    designation = input("Enter designation (programmer/manager/tester): ").lower()
                    if designation not in ['programmer', 'manager', 'tester']:
                        raise ValueError("Invalid designation. Must be 'programmer', 'manager', or 'tester'.")

                    salary_map = {
                        'programmer': 25000,
                        'manager': 30000,
                        'tester': 20000
                    }
                    salary = salary_map[designation]

                    employees.append({
                        'name': name,
                        'age': age,
                        'designation': designation,
                        'salary': salary
                    })

                    save_data(employees)
                    print("Employee added successfully.")

                except ValueError as e:
                    print(f"Error: {e}")

                cont = input("Do you want to add another employee? (yes/no): ").strip().lower()
                if cont != 'yes':
                    break

        elif choice == '2':
            if not employees:
                print("No employee records found.")
            else:
                for emp in employees:
                    print(f"Name: {emp['name']}, Age: {emp['age']}, Designation: {emp['designation'].capitalize()}, Salary: {emp['salary']}")

        elif choice == '3':
            name = input("Enter employee name to raise salary: ").strip()
            found = False

            for emp in employees:
                if emp['name'].lower() == name.lower():
                    found = True
                    try:
                        hike_percent = float(input("Enter hike percentage (max 30%): "))
                        if hike_percent > 30:
                            raise ValueError("Hike cannot exceed 30%.")
                        hike_amount = emp['salary'] * (hike_percent / 100)
                        emp['salary'] += int(hike_amount)
                        save_data(employees)
                        print(f"Salary updated successfully. New salary: {emp['salary']}")
                    except ValueError as e:
                        print(f"Error: {e}")
                    break

            if not found:
                print("Employee not found.")

        elif choice == '4':
            print("Thank you for using the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
