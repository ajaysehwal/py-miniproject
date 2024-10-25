import uuid
from enum import Enum

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Status(Enum):
    PENDING = 1
    INPROGRESS = 2
    COMPLETED = 3

class Task:
    def __init__(self, title:str, description:str, priority:Priority=Priority.LOW, due_date=None, assignee=None, status:Status=Status.PENDING):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.assignee = assignee
        self.status = status
        self.id = str(uuid.uuid4()) 

class TODO:
    def __init__(self):
        self.tasks = []

    def add(self, title:str, description:str, priority:Priority=Priority.LOW, due_date=None, assignee=None, status=Status.PENDING):
        task = Task(title, description, priority, due_date, assignee, status)
        self.tasks.append(task)
        return task.id

    def remove(self, taskId):
        self.tasks = [task for task in self.tasks if task.id != taskId]

    def list_tasks(self):
        for task in self.tasks:
            print(f"Task ID: {task.id}, Title: {task.title}, Priority: {task.priority.name}, Due Date: {task.due_date}, Assignee: {task.assignee}")

    def update_task(self, taskId, title=None, description=None, priority=None, due_date=None, assignee=None):
        for task in self.tasks:
            if task.id == taskId:
                if title: task.title = title
                if description: task.description = description
                if priority: task.priority = priority
                if due_date: task.due_date = due_date
                if assignee: task.assignee = assignee
                break

    def update_status(self, taskId, status:Status):
        for task in self.tasks:
            if task.id == taskId:
                task.status = status
                break

class Employee:
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.id = str(uuid.uuid4()) 
        self.designation = designation
        self.tasks = []

    def add_task(self, title, description, priority=Priority.LOW, due_date=None, assignee=None, status=Status.PENDING):
        task = Task(title, description, priority, due_date, assignee, status) 
        self.tasks.append(task)  
        print(f"Assigned task {title} to {self.name}")

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.todo = TODO()

    def add_employee(self, name, age, designation):
        employee = Employee(name, age, designation)
        self.employees.append(employee)
        print(f"Added employee {name}")
        return employee.id

    def remove_employee(self, name):
        self.employees = [employee for employee in self.employees if employee.name != name]
        print(f"Removed employee {name}")

    def assign_task(self, employeeId, taskId):
        for employee in self.employees:
            if employee.id == employeeId:
                for task in self.todo.tasks:
                    if task.id == taskId:
                        employee.add_task(task.title, task.description, task.priority, task.due_date, employeeId, task.status)
                        break
                break

company = Company("ABC Corp")
employee_id = company.add_employee("John Doe", 30, "Software Engineer")
task_id = company.todo.add("Testing", "Testing application", Priority.LOW, "any", employee_id, Status.PENDING)
company.assign_task(employee_id, task_id)
