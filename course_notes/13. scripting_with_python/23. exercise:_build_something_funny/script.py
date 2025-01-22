# ==== exercise: build something funny ====
import tkinter as tk
import pyjokes

# Print a random joke
# print(pyjokes.get_joke())


root = tk.Tk()

root.title('Joke teller')
root.geometry('400x300')


label = tk.Label(
    root,
    text='Click the button to get a programming joke',
    wraplength=350,
    justify='left')
label.pack(pady=20)


def on_button_click():
    joke = pyjokes.get_joke()
    label.config(text=joke)
    root.update_idletasks()


button = tk.Button(
    root,
    text='Click Me',
    command=on_button_click)
button.pack(pady=10)

root.mainloop()
