import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo_list = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.done_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.todo_list.append({"task": task, "done": False})
        self.task_listbox.insert(tk.END, f"{task} - Not Done")
        self.task_entry.delete(0, tk.END)

    def update_task(self):
        task_num = int(self.task_listbox.curselection()[0])
        new_task = self.task_entry.get()
        self.todo_list[task_num]["task"] = new_task
        self.task_listbox.delete(task_num)
        self.task_listbox.insert(task_num, f"{new_task} - {'Done' if self.todo_list[task_num]['done'] else 'Not Done'}")
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        task_num = int(self.task_listbox.curselection()[0])
        del self.todo_list[task_num]
        self.task_listbox.delete(task_num)

    def mark_done(self):
        task_num = int(self.task_listbox.curselection()[0])
        self.todo_list[task_num]["done"] = True
        self.task_listbox.delete(task_num)
        self.task_listbox.insert(task_num, f"{self.todo_list[task_num]['task']} - Done")

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()