import tkinter as tk
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass
root = tk.Tk()
root.title("To-Do List")
entry_task = tk.Entry(root, width=50)
entry_task.grid(row=0, column=0, padx=5, pady=5)
button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.grid(row=0, column=1, padx=5, pady=5)
listbox_tasks = tk.Listbox(root, height=15, width=50)
listbox_tasks.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
scrollbar_tasks = tk.Scrollbar(root)
scrollbar_tasks.grid(row=1, column=2, padx=5, pady=5, sticky='ns')
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)
button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='we')
root.mainloop()