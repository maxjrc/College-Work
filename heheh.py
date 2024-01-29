import requests
class StudentManagementSystem:
    def __init__(self):
        self.logged_in = False
        self.students = {"1": {"name": "John", "contact": "12345678"}, "2": {"name": "Jane", "contact": "87654321"}}
 
    def login(self):
        print("Welcome to the Student Management System!")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
 
        # Simple authentication; replace with secure authentication method
        if username == "admin" and password == "password":
            self.logged_in = True
            print("Login successful.")
        else:
            print("Invalid credentials. Please try again.")
 
    def logout(self):
        self.logged_in = False
        print("Logged out. Goodbye!")
 
    def display_menu(self):
        print("\nMENU:")
        print("1. Manage Student Details")
        print("2. Retrieve Student Details")
        print("3. Generate Report")
        print("4. Logout")
 
    def manage_student_details(self):
        if not self.logged_in:
            print("Please log in first.")
            return
 
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        contact = input("Enter contact information: ")
 
        # Add or update student details
        self.students[student_id] = {"name": name, "contact": contact}
        print("Student details updated successfully.")
 
    def retrieve_student_details(self):
        if not self.logged_in:
            print("Please log in first.")
            return
 
        student_id = input("Enter student ID to retrieve details: ")
 
        # Retrieve and display student details
        if student_id in self.students:
            details = self.students[student_id]
            name = details["name"]
            print(f"\nStudent Details for ID {student_id}:")
            print(f"Name: {details['name']}")
            print(f"Contact: {details['contact']}")
            print("About:" + findout(name))
        else:
            print(f"No student found with ID {student_id}.")
 
    def generate_report(self):
        if not self.logged_in:
            print("Please log in first.")
            return
 
        print("\nReport for Form Group:")
        for student_id, details in self.students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Contact: {details['contact']}")
 
    def run(self):
        while True:
            if not self.logged_in:
                self.login()
 
            self.display_menu()
            choice = input("Enter your choice (1-4): ")
 
            if choice == "1":
                self.manage_student_details()
            elif choice == "2":
                self.retrieve_student_details()
            elif choice == "3":
                self.generate_report()
            elif choice == "4":
                self.logout()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
 
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()

def findout(name):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    headers = {
	"X-RapidAPI-Key": "47c1ba099cmsh8f1a4063990aa11p1b58a0jsn203cd995d18b",
	"X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }
    querystring = {"term":name}
    response = requests.get(url, headers=headers, params=querystring)
    json_object = response.json()
    return json_object['list'][0]['definition']