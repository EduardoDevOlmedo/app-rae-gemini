

import google.generativeai as genai
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time

def classify_image():
    genai.configure(api_key="AIzaSyDPoSQDcchtOaPnZzqPvydEgCZId4AR-zo")

    img = Image.open(file_path_var.get())

    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content([
    "Eres un experto en clasificación de residuos y debes decidir si la imagen corresponde a un residuo electrónico o no. "
    "Si corresponde a un residuo electrónico, debes responder con: 'Es una RAEE'. "
    "Si no corresponde a un residuo electrónico, debes responder con: 'No es una RAEE'. "
    "Considera que una computadora, teléfonos, aunque estén en buen estado, pueden ser considerados como residuos electrónicos.",
    "Luego, explica en una linea el motivo de tu respuesta.",
    "Puedes argumentar si es RAEE o no, por su uso actual, estado y composición.",
    img
    ])
    result_label.config(text=response.text, fg="red" if "no es una raee" in response.text.lower() else "green");

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif"), ("All Files", "*.*")]
    )
    if file_path:
        file_path_var.set(file_path)  
        classify_image()


root = tk.Tk()
root.title("IA para clasificar residuos electrónicos (RAEE)")
root.geometry("600x300")

file_path_var = tk.StringVar()

label = tk.Label(root, text="Selecciona una imagen para ver si es un residuo electrónico:")
label.pack(pady=5)

entry = tk.Entry(root, textvariable=file_path_var, width=50)
entry.pack(padx=10)

browse_button = tk.Button(root, text="Seleccionar imagen", command=browse_file)
browse_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=300, justify="left", font=("Arial", 12))
result_label.pack(pady=10, padx=10)

close_button = tk.Button(root, text="Cerrar", command=root.quit)
close_button.pack(pady=10)

root.mainloop()





