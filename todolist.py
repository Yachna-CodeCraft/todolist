import tkinter as tk 
from tkinter import messagebox
def add_task():
    task=task_entry.get()
    if task:
        tasks.append(tasks)
        tasks_listbox.insert(tk.END, task) 
    else:
        messagebox.showwarning("Warning", "You must enter a task.")
    
def remove_task():  
    try: 
        selected_task_index = tasks_listbox.curselection()[0] 
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a row of task to remove.")
tasks=[]
root=tk.Tk()
root.title("To-do list")
entry_bg_color = "#d3d3d3"
entry_fg_color = "#000000" 
button_bg_color = "#87CEEB" 
button_fg_color = "#000000" 
listbox_bg_color = "#d3d3d3"  
listbox_fg_color = "#000000"
task_entry_label = tk.Label(root, text="Enter the task:")
task_entry_label.pack(pady=5)
task_entry = tk.Entry(root, width=30,bg=entry_bg_color, fg=entry_fg_color)
task_entry.pack(pady=8)
add_task_button = tk.Button(root, text="Add Task", command=add_task,bg=button_bg_color, fg=button_fg_color) 
add_task_button.pack(pady=8)
tasks_listbox = tk.Listbox(root, width=50, height=10,bg=listbox_bg_color, fg=listbox_fg_color) 
tasks_listbox.pack(pady=8)
remove_task_button = tk.Button(root, text="Remove Task", command=remove_task,bg=button_bg_color, fg=button_fg_color) 
remove_task_button.pack(pady=8)
root.mainloop()