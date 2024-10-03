import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Car Rentals")
window.resizable(False, False)

window_width = 1050
window_height = 550

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

frame_width = int(window_width * 3 / 5)
frame_height = window_height
first_frame = tk.Frame(window, bg='red', width=frame_width, height=frame_height)
first_frame.place(x=0, y=0)

image = Image.open("carLoginPic.jpg")
image = image.resize((frame_width, frame_height))
image = ImageTk.PhotoImage(image)

image_label = tk.Label(first_frame, image=image)
image_label.place(relwidth=1, relheight=1)

second_frame_width = window_width - frame_width
second_frame = tk.Frame(window, bg='white', width=second_frame_width, height=frame_height)
second_frame.place(x=frame_width, y=0)

welcome_back_label = tk.Label(second_frame, text="WELCOME BACK")
welcome_back_label.pack(pady=10)

login_label = tk.Label(second_frame, text="Login")
login_label.pack(pady=5)

user_label = tk.Label(second_frame, text="Username")
user_label.pack(pady=5)

user_input = tk.Entry(second_frame)
user_input.pack(pady=5)

pass_label = tk.Label(second_frame, text="Password")
pass_label.pack(pady=5)

pass_input = tk.Entry(second_frame, show="*")
pass_input.pack(pady=5)

window.mainloop()
