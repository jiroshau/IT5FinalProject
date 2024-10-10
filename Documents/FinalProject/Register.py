import tkinter as tk
from PIL import ImageTk, Image
from Login import Login

class Register:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Create Account")
        self.window.resizable(False, False)
        self.window.configure(bg='white')

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

        # Uncomment and use these lines if you want to display an image in the red frame
        # image = Image.open("car.jpg")
        # image = image.resize((frame_width, frame_height))
        # image = ImageTk.PhotoImage(image)
        # image_label = tk.Label(first_frame, image=image)
        # image_label.place(relwidth=1, relheight=1)

        second_frame_width = window_width - frame_width
        second_frame = tk.Frame(self.window, width=second_frame_width, height=frame_height)
        second_frame.place(x=frame_width, y=0)

        create_account_label = tk.Label(second_frame, text="CREATE ACCOUNT", font=("Sans", 18), bg='white')
        create_account_label.grid(row=0, column=1, columnspan=2, pady=15)

        name_label = tk.Label(second_frame, text="Name", font=("Arial", 10), bg='white')
        name_label.grid(row=1, column=0, padx=10, pady=15)

        self.name_input = tk.Entry(second_frame, font=("Arial", 10), width=30)
        self.name_input.grid(row=1, column=1, padx=10, pady=15)

        username_label = tk.Label(second_frame, text="Username", font=("Sans", 10), bg='white')
        username_label.grid(row=2, column=0, padx=10, pady=17)

        self.username_input = tk.Entry(second_frame, font=("Arial", 10), width=30)
        self.username_input.grid(row=2, column=1, padx=10, pady=17)

        email_label = tk.Label(second_frame, text="Email", font=("Sans", 10), bg='white')
        email_label.grid(row=3, column=0, padx=10, pady=17)

        self.email_input = tk.Entry(second_frame, font=("Arial", 10), width=30)
        self.email_input.grid(row=3, column=1, padx=10, pady=17)

        password_label = tk.Label(second_frame, text="Password", font=("Sans", 10), bg='white')
        password_label.grid(row=4, column=0, padx=10, pady=17)

        self.password_input = tk.Entry(second_frame, show="*", font=("Arial", 10), width=30)
        self.password_input.grid(row=4, column=1, padx=10, pady=15)

        confirm_password_label = tk.Label(second_frame, text="Confirm Password", font=("Sans", 10), bg='white')
        confirm_password_label.grid(row=5, column=0, padx=10, pady=17)

        self.confirm_password_input = tk.Entry(second_frame, show="*", font=("Arial", 10), width=30)
        self.confirm_password_input.grid(row=5, column=1, padx=10, pady=15)

        create_account_button = tk.Button(second_frame, text="Create Account", font=("Arial", 13))
        create_account_button.grid(row=6, column=1, columnspan=2, padx=10, pady=17)

        self.window.mainloop()

    def open_login(self, event):
        self.window.destroy
        login_window = Login()
        login_window.window.mainloop()

if __name__ == "__main__":
    Register()