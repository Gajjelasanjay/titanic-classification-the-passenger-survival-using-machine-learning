import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk  # Make sure to install the Pillow library

def configure_option(option):
    # Add your configuration logic here based on the selected option
    print(f'Configuration for {option} will be implemented here.')

def show_interface(option, image_path):
    new_window = tk.Toplevel(root)
    new_window.title(f"Configuration Interface - {option}")
    
    # Add widgets and layout for the new interface
    label = tk.Label(new_window, text=f"Configuration Interface for {option}")
    label.pack(padx=50, pady=50)

    # Load and display the image
    img = Image.open(image_path)
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(new_window, image=img)
    image_label.image = img
    image_label.pack(pady=50)
    
    # You can add more widgets and customize the new interface as needed

# Create the main window
root = tk.Tk()
root.title("Titanic Classification Predicting the Passenger Survival ")

# Function to handle button clicks
def button_click(option, image_path):
    configure_option(option)
    show_interface(option, image_path)

# Create buttons with associated images
age_image_path = "c:/Users/Sanjay/Pictures/Screenshots/Screenshot 2023-12-10 115958.png"
fare_image_path = "c:/Users/Sanjay/Pictures/Screenshots/Screenshot 2023-12-10 120020.png"
embarked_image_path = "c:/Users/Sanjay/Pictures/Screenshots/Screenshot 2023-12-10 113938.png"
sex_image_path = "c:/Users/Sanjay/Pictures/Screenshots/Screenshot 2023-12-10 113846.png"

age_button = tk.Button(root, text="PASSENGER AGE VS COUNT", command=lambda: button_click("Age", age_image_path))
fare_button = tk.Button(root, text="PASSENGER FARE VS COUNT", command=lambda: button_click("Fare", fare_image_path))
embarked_button = tk.Button(root, text="PASSENGER EMBARKED VS SURVIVED", command=lambda: button_click("Embarked", embarked_image_path))
sex_button = tk.Button(root, text="PASSENGER SEX VS SURVIVED", command=lambda: button_click("Sex", sex_image_path))

# Pack buttons into the window
age_button.pack(pady=50)
fare_button.pack(pady=50)
embarked_button.pack(pady=50)
sex_button.pack(pady=50)

# Start the GUI event loop
root.mainloop()