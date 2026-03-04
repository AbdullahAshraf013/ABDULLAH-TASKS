# import tkinter as tk
#
# window = tk.Tk()
#
# label = tk.Label(window, text=Hello, Tkinter!, fg=blue", bg="yellow", padx=10,
# pady=5)
# label.pack()
#
# button = tk.Button(window, text="Click Me", width=15, command=lambda:
# print("Button clicked!"))
# button.pack()
#
# window.mainloop()






# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(window, text="Initial Text", bg="Tomato")
# label.pack()
# label2 = tk.Label(window, text="Initial Text", bg="Red")
# label2.pack()
# current_text = label.cget("text") # Using cget()
# print(f"Current text: {current_text}")
# current_bg = label.config()["bg"][-1] # Using config() and dictionary access
# print(f"Current background: {current_bg}")
# window.mainloop()


# import tkinter as tk
# window = tk.Tk()
# label = tk.Label(window, text="Initial Text")
#
# label.pack()
# label.config(text="Updated Text", fg="red", font=("Arial", 16)) # Setting multiple
# label["bg"] ="pink" # Using dictionary-like access to set a single property
# window.mainloop()



import tkinter as tk

window = tk.Tk()
window.title("Color Config App")
window.geometry("400x300")
window.config(bg="red")

def change_color():
    if window.cget("bg") == "red":
        window.config(bg="green")
        btn.config(bg="green", text="Click to change to RED")
    else:
        window.config(bg="red")
        btn.config(bg="red", text="Click to change to GREEN")

btn = tk.Button(
    window,
    text="Click to change to GREEN",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="red",
    padx=20,
    pady=10,
    cursor="hand2",
    command=change_color
)
btn.place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()

