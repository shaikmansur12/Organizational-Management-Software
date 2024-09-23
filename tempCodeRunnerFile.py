import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from final_dbms_dbfile import create_database
create_database()

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee and Department Management System")
        self.root.geometry("800x600")

        self.style = ttk.Style()
        self.style.configure("TButton", foreground="black", background="lightgreen", padding=(10, 5))
        self.style.configure("TNotebook", background="pink", tabposition="n")
        self.style.configure("Treeview", background="lavender", fieldbackground="lavender")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand='yes')

        self.employee_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.employee_tab, text="Employee")

        self.department_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.department_tab, text="Department")

        self.project_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.project_tab, text="Project")

        self.create_employee_widgets()
        self.create_department_widgets()
        self.create_project_widgets()

        self.display_employees()
        self.display_departments()
        self.display_projects()

    def create_employee_widgets(self):
        self.employee_tv = ttk.Treeview(self.employee_tab, columns=("Emp_ID", "Name", "Age", "DOJ", "Email", "Gender", "Contact", "Address", "Department Id"))
        self.employee_tv.heading("#1", text="Emp_ID")
        self.employee_tv.heading("#2", text="Name")
        self.employee_tv.heading("#3", text="Age")
        self.employee_tv.heading("#4", text="DOJ")
        self.employee_tv.heading("#5", text="Email")
        self.employee_tv.heading("#6", text="Gender")
        self.employee_tv.heading("#7", text="Contact")
        self.employee_tv.heading("#8", text="Address")
        self.employee_tv.heading("#9", text="Dept Id")
        self.employee_tv.pack()

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.doj_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.address_var = tk.StringVar()
        self.department_var = tk.StringVar()

        labels = ["Name", "Age", "Date of Joining", "Email", "Gender", "Contact", "Address", "Department Id"]
        entries = [self.name_var, self.age_var, self.doj_var, self.email_var, self.gender_var, self.contact_var, self.address_var, self.department_var]

        for label, entry_var in zip(labels, entries):
            label_widget = tk.Label(self.employee_tab, text=label)
            label_widget.pack()
            entry_widget = tk.Entry(self.employee_tab, textvariable=entry_var)
            entry_widget.pack()

        self.search_employee_var = tk.StringVar()
        search_employee_label = tk.Label(self.employee_tab, text="Search Employee")
        search_employee_label.pack()
        search_employee_entry = tk.Entry(self.employee_tab, textvariable=self.search_employee_var)
        search_employee_entry.pack()

        search_employee_button = ttk.Button(self.employee_tab, text="Search Employee", command=self.search_employee, style="TButton")
        search_employee_button.pack()

        employee_buttons_frame = tk.Frame(self.employee_tab)
        employee_buttons_frame.pack()

        employee_add_button = ttk.Button(employee_buttons_frame, text="Add Employee", command=self.add_employee, style="TButton")
        employee_add_button.pack()

        employee_update_button = ttk.Button(employee_buttons_frame, text="Update Employee", command=self.update_employee, style="TButton")
        employee_update_button.pack()

        employee_delete_button = ttk.Button(employee_buttons_frame, text="Delete Employee", command=self.delete_employee, style="TButton")
        employee_delete_button.pack()

    def create_department_widgets(self):
        self.department_tv = ttk.Treeview(self.department_tab, columns=("Dept_ID","Name", "Location", "Manager", "Department Name", "Emp_ID"))
        self.department_tv.heading("#1", text="Dept_ID")
        self.department_tv.heading("#2", text="Name")
        self.department_tv.heading("#3", text="Location")
        self.department_tv.heading("#4", text="Manager")
        self.department_tv.heading("#5", text="Dept Name")
        self.department_tv.heading("#6", text="Emp_ID")
        self.department_tv.pack()

        self.department_dept_id_var = tk.StringVar()
        self.department_Emp_id_var = tk.StringVar()
        self.department_name_var = tk.StringVar()
        self.department_location_var = tk.StringVar()
        self.department_manager_var = tk.StringVar()
        self.department_dept_name_var = tk.StringVar()

        labels = ["Dept_Id","Emp_ID", "Name", "Location", "Manager", "Department Name"]
        entries = [self.department_dept_id_var, self.department_Emp_id_var, self.department_name_var, self.department_location_var, self.department_manager_var, self.department_dept_name_var]

        for label, entry_var in zip(labels, entries):
            label_widget = tk.Label(self.department_tab, text=label)
            label_widget.pack()
            entry_widget = tk.Entry(self.department_tab, textvariable=entry_var)
            entry_widget.pack()

        self.search_department_var = tk.StringVar()
        search_department_label = tk.Label(self.department_tab, text="Search Department")
        search_department_label.pack()
        search_department_entry = tk.Entry(self.department_tab, textvariable=self.search_department_var)
        search_department_entry.pack()

        search_department_button = ttk.Button(self.department_tab, text="Search Department", command=self.search_department, style="TButton")
        search_department_button.pack()

        department_buttons_frame = tk.Frame(self.department_tab)
        department_buttons_frame.pack()

        department_add_button = ttk.Button(department_buttons_frame, text="Add Department", command=self.add_department, style="TButton")
        department_add_button.pack()

        department_update_button = ttk.Button(department_buttons_frame, text="Update Department", command=self.update_department, style="TButton")
        department_update_button.pack()

        department_delete_button = ttk.Button(department_buttons_frame, text="Delete Department", command=self.delete_department, style="TButton")
        department_delete_button.pack()

    def create_project_widgets(self):
        self.project_tv = ttk.Treeview(self.project_tab, columns=("P_ID", "Name", "Start Date", "End Date", "Employee ID", "Department Id"))
        self.project_tv.heading("#1", text="P_ID")
        self.project_tv.heading("#2", text="Name")
        self.project_tv.heading("#3", text="Start Date")
        self.project_tv.heading("#4", text="End Date")
        self.project_tv.heading("#5", text="Employee ID")
        self.project_tv.heading("#6", text="Department Id")
        self.project_tv.pack()

        self.project_name_var = tk.StringVar()
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()
        self.employee_id_var = tk.StringVar()
        self.department_id_var = tk.StringVar()

        labels = ["Project Name", "Start Date", "End Date", "Employee ID", "Department Id"]
        entries = [self.project_name_var, self.start_date_var, self.end_date_var, self.employee_id_var, self.department_id_var]

        for label, entry_var in zip(labels, entries):
            label_widget = tk.Label(self.project_tab, text=label)
            label_widget.pack()
            entry_widget = tk.Entry(self.project_tab, textvariable=entry_var)
            entry_widget.pack()

        self.search_project_var = tk.StringVar()
        search_project_label = tk.Label(self.project_tab, text="Search Project")
        search_project_label.pack()
        search_project_entry = tk.Entry(self.project_tab, textvariable=self.search_project_var)
        search_project_entry.pack()

        search_project_button = ttk.Button(self.project_tab, text="Search Project", command=self.search_project, style="TButton")
        search_project_button.pack()

        project_buttons_frame = tk.Frame(self.project_tab)
        project_buttons_frame.pack()

        project_add_button = ttk.Button(project_buttons_frame, text="Add Project", command=self.add_project, style="TButton")
        project_add_button.pack()

        project_update_button = ttk.Button(project_buttons_frame, text="Update Project", command=self.update_project, style="TButton")
        project_update_button.pack()

        project_delete_button = ttk.Button(project_buttons_frame, text="Delete Project", command=self.delete_project, style="TButton")
        project_delete_button.pack()

    def add_employee(self):
        name = self.name_var.get()
        age = self.age_var.get()
        doj = self.doj_var.get()
        email = self.email_var.get()
        gender = self.gender_var.get()
        contact = self.contact_var.get()
        address = self.address_var.get()
        department_id = self.department_var.get()

        if name and age and doj and email and gender and contact and address:
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Employee (name, age, doj, email, gender, contact, address, department_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (name, age, doj, email, gender, contact, address, department_id))
            conn.commit()
            conn.close()
            self.clear_employee()
            self.display_employees()
            messagebox.showinfo("Success", "Employee Record Inserted")
        else:
            messagebox.showerror("Error in Input", "Please Fill All the Details")

    def update_employee(self):
        selected_item = self.employee_tv.selection()
        if selected_item:
            name = self.name_var.get()
            age = self.age_var.get()
            doj = self.doj_var.get()
            email = self.email_var.get()
            gender = self.gender_var.get()
            contact = self.contact_var.get()
            address = self.address_var.get()
            department_id = self.department_var.get()
            selected_id = self.employee_tv.item(selected_item, "values")[0]
            if name and age and doj and email and gender and contact and address and department_id:
                conn = sqlite3.connect("Employee_DataBase1.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE Employee SET name=?, age=?, doj=?, email=?, gender=?, contact=?, address=?, department_id=? WHERE Emp_id=?",
                               (name, age, doj, email, gender, contact, address, department_id, selected_id))
                conn.commit()
                conn.close()
                self.clear_employee()
                self.display_employees()
                messagebox.showinfo("Success", "Employee Record Updated")
            else:
                messagebox.showerror("Error in Input", "Please Fill All the Details")
        else:
            messagebox.showerror("Error", "Please select an employee to update.")

    def search_employee(self):
        search_value = self.search_employee_var.get()
        if search_value:
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()

            # Check if the search value is a numeric ID or contact number
            if search_value.isdigit():
                cursor.execute("SELECT * FROM Employee WHERE Emp_id=? OR contact=?", (search_value, search_value))
            else:
                cursor.execute("SELECT * FROM Employee WHERE contact=?", (search_value,))

            records = cursor.fetchall()
            self.employee_tv.delete(*self.employee_tv.get_children())

            if records:
                for record in records:
                    self.employee_tv.insert("", "end", values=record)
            else:
                messagebox.showwarning("Warning", "No matching records found.")

            conn.close()
        else:
            messagebox.showwarning("Warning", "Please enter a Emp ID or Contact Number of Employee.")
            self.display_employees()

    def delete_employee(self):
        selected_item = self.employee_tv.selection()
        if selected_item:
            selected_id = self.employee_tv.item(selected_item, "values")[0]
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Employee WHERE Emp_id=?", (selected_id,))
            conn.commit()
            conn.close()
            self.clear_employee()
            self.display_employees()
            messagebox.showinfo("Success", "Employee Record Deleted")
        else:
            messagebox.showerror("Error", "Please select an employee to delete.")

    def clear_employee(self):
        self.name_var.set("")
        self.age_var.set("")
        self.doj_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.address_var.set("")
        self.department_var.set("")

    def display_employees(self):
        conn = sqlite3.connect("Employee_DataBase1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        records = cursor.fetchall()
        self.employee_tv.delete(*self.employee_tv.get_children())
        for record in records:
            self.employee_tv.insert("", "end", values=record)
        conn.close()
    
    def add_department(self):
        department_Dept_id = self.department_dept_id_var.get()
        department_Emp_id = self.department_Emp_id_var.get()
        department_name = self.department_name_var.get()
        department_location = self.department_location_var.get()
        department_manager = self.department_manager_var.get()
        department_dept_name = self.department_dept_name_var.get()

        if department_name and department_location:
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Department (Dept_id, name, location, manager, dept_name, emp_id) VALUES (?,?, ?, ?, ?, ?)",
                           ( department_Dept_id, department_name, department_location, department_manager, department_dept_name, department_Emp_id))
            conn.commit()
            conn.close()
            self.clear_department()
            self.display_departments()
            messagebox.showinfo("Success", "Department Record Inserted")
        else:
            messagebox.showerror("Error in Input", "Please Fill All the Details")

    def update_department(self):
        selected_item = self.department_tv.selection()
        if selected_item:
            department_Dept_id = self.department_dept_id_var.get()
            department_Emp_id = self.department_Emp_id_var.get()
            department_name = self.department_name_var.get()
            department_location = self.department_location_var.get()
            department_manager = self.department_manager_var.get()
            department_dept_name = self.department_dept_name_var.get()
            selected_id = self.department_tv.item(selected_item, "values")[0]
            if department_name and department_location:
                conn = sqlite3.connect("Employee_DataBase1.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE Department SET dept_id=?, emp_id=?, name=?, location=?, manager=?, dept_name=? WHERE Dept_id=?",
                               (department_Dept_id, department_Emp_id, department_name, department_location, department_manager, department_dept_name, selected_id))
                conn.commit()
                conn.close()
                self.clear_department()
                self.display_departments()
                messagebox.showinfo("Success", "Department Record Updated")
            else:
                messagebox.showerror("Error in Input", "Please Fill All the Details")
        else:
            messagebox.showerror("Error", "Please select a department to update.")

    def search_department(self):
        search_value = self.search_department_var.get()
        if search_value.isdigit():
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            #Searching on emp_id
            cursor.execute("SELECT * FROM Department WHERE emp_id=?", (search_value,))
            records = cursor.fetchall()
            #searching on dept_id
            #cursor.execute("SELECT * FROM Department WHERE Dept_id=?", (search_value,))
            #records = cursor.fetchall()

            self.department_tv.delete(*self.department_tv.get_children())

            if records:
                for record in records:
                    self.department_tv.insert("", "end", values=record)
            else:
                messagebox.showwarning("Warning", "No matching records found.")

            conn.close()
        else:
            messagebox.showwarning("Warning", "Please enter a valid numeric employee ID for Department.")
            self.display_departments()


    def delete_department(self):
        selected_item = self.department_tv.selection()
        if selected_item:
            selected_id = self.department_tv.item(selected_item, "values")[0]
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Department WHERE Dept_id=?", (selected_id,))
            conn.commit()
            conn.close()
            self.clear_department()
            self.display_departments()
            messagebox.showinfo("Success", "Department Record Deleted")
        else:
            messagebox.showerror("Error", "Please select a department to delete.")

    def clear_department(self):
        self.department_dept_id_var.set("")
        self.department_Emp_id_var.set("")
        self.department_name_var.set("")
        self.department_location_var.set("")
        self.department_manager_var.set("")
        self.department_dept_name_var.set("")

    def display_departments(self):
        conn = sqlite3.connect("Employee_DataBase1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Department")
        records = cursor.fetchall()
        self.department_tv.delete(*self.department_tv.get_children())
        for record in records:
            self.department_tv.insert("", "end", values=record)
        conn.close()

    # Functions for Project

    def add_project(self):
        project_name = self.project_name_var.get()
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()
        employee_id = self.employee_id_var.get()
        department_id = self.department_id_var.get()

        if project_name and start_date and end_date and employee_id and department_id:
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Project (name, start_date, end_date, employee_id, department_id) VALUES (?, ?, ?, ?, ?)",
                           (project_name, start_date, end_date, employee_id, department_id))
            conn.commit()
            conn.close()
            self.clear_project()
            self.display_projects()
            messagebox.showinfo("Success", "Project Record Inserted")
        else:
            messagebox.showerror("Error in Input", "Please Fill All the Details")

    def update_project(self):
        selected_item = self.project_tv.selection()
        if selected_item:
            project_name = self.project_name_var.get()
            start_date = self.start_date_var.get()
            end_date = self.end_date_var.get()
            employee_id = self.employee_id_var.get()
            department_id = self.department_id_var.get()
            selected_id = self.project_tv.item(selected_item, "values")[0]
            if project_name and start_date and end_date and employee_id:
                conn = sqlite3.connect("Employee_DataBase1.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE Project SET name=?, start_date=?, end_date=?, employee_id=?, department_id=? WHERE P_id=?",
                               (project_name, start_date, end_date, employee_id, department_id, selected_id))
                conn.commit()
                conn.close()
                self.clear_project()
                self.display_projects()
                messagebox.showinfo("Success", "Project Record Updated")
            else:
                messagebox.showerror("Error in Input", "Please Fill All the Details")
        else:
            messagebox.showerror("Error", "Please select a project to update.")

    def search_project(self):
        search_value = self.search_project_var.get()
        if search_value.isdigit():
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Project WHERE employee_id=?", (search_value,))
            records = cursor.fetchall()

            self.project_tv.delete(*self.project_tv.get_children())

            if records:
                for record in records:
                    self.project_tv.insert("", "end", values=record)
            else:
                messagebox.showwarning("Warning", "No matching records found.")

            conn.close()
        else:
            messagebox.showwarning("Warning", "Please enter a valid numeric employee ID for Project.")
            self.display_projects()


    def delete_project(self):
        selected_item = self.project_tv.selection()
        if selected_item:
            selected_id = self.project_tv.item(selected_item, "values")[0]
            conn = sqlite3.connect("Employee_DataBase1.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Project WHERE P_id=?", (selected_id,))
            conn.commit()
            conn.close()
            self.clear_project()
            self.display_projects()
            messagebox.showinfo("Success", "Project Record Deleted")
        else:
            messagebox.showerror("Error", "Please select a project to delete.")

    def clear_project(self):
        self.project_name_var.set("")
        self.start_date_var.set("")
        self.end_date_var.set("")
        self.employee_id_var.set("")
        self.department_id_var.set("")

    def display_projects(self):
        conn = sqlite3.connect("Employee_DataBase1.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Project")
        records = cursor.fetchall()
        self.project_tv.delete(*self.project_tv.get_children())
        for record in records:
            self.project_tv.insert("", "end", values=record)
        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
