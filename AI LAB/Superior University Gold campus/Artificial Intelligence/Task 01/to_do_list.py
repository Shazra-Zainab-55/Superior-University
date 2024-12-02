class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("To-Do List:")
            for i in range(len(self.tasks)):
                print(f"{i + 1}. {self.tasks[i]}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def delete_task(self, delete_task):
        self.delete_task=int(input("Enter the task number:"))
        if 0 <  self.delete_task <= len(self.tasks):
            print(f"Task '{self.tasks.pop( self.delete_task - 1)}' deleted!")
        else:
            print("Invalid task number!")

    def menu(self):
        while True:
            choice = input("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit\nChoose: ")
            if choice == '1':
                self.show_tasks()
            elif choice == '2': 
                self.add_task(input("Enter task: "))
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                break
            else: print("Invalid option!")

if __name__ == "__main__":
    ToDoList().menu()
