import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random

numbers = [8, 17, 75, 1.093, 89]
strings = ["georgia", "tree", "swamp", "river", "mountain"]

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250))  
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
        
        random_number = random.choice(numbers)
        random_string = random.choice(strings)
        text_label.config(text=f"{random_number}\n{random_string}")



root = tk.Tk()
root.title("Image Loader")
root.geometry("400x450")
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack()

image_label = tk.Label(root)
image_label.pack()
text_label = tk.Label(root, text="", font=("Arial", 14))
text_label.pack()

root.mainloop()






