import tkinter as tk
from PIL import ImageTk, Image

class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Car Rentals")
        self.window.resizable(False, False)

        window_width = 1050
        window_height = 550

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        frame_width = int(window_width * 3 / 5)
        frame_height = window_height
        first_frame = tk.Frame(self.window, bg='red', width=frame_width, height=frame_height)
        first_frame.place(x=0, y=0)

        # Load and resize the image to fit the red frame
        image = Image.open("carLoginPic.jpg")
        image = image.resize((frame_width, frame_height))
        image = ImageTk.PhotoImage(image)

        # Create a label to display the image and expand it to cover the entire frame
        image_label = tk.Label(first_frame, image=image)
        image_label.place(relwidth=1, relheight=1)

        second_frame_width = window_width - frame_width
        second_frame = tk.Frame(self.window, bg='white', width=second_frame_width, height=frame_height)
        second_frame.place(x=frame_width, y=0)

        welcome_back_label = tk.Label(second_frame, text="WELCOME BACK", bg='white')
        welcome_back_label.grid(row=0, column=0, pady=10, padx=10)

        login_label = tk.Label(second_frame, text="Login", bg='white')
        login_label.grid(row=1, column=0, pady=5, padx=10)

        user_label = tk.Label(second_frame, text="Username", bg='white')
        user_label.grid(row=2, column=0, pady=5, padx=10)

        user_input = tk.Entry(second_frame)
        user_input.grid(row=2, column=1, pady=5, padx=10)

        pass_label = tk.Label(second_frame, text="Password", bg='white', font="Sans")
        pass_label.grid(row=3, column=0, pady=5, padx=10)

        pass_input = tk.Entry(second_frame, show="*")
        pass_input.grid(row=3, column=1, pady=5, padx=10)

        self.window.mainloop()

