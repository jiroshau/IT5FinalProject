import tkinter as tk
from PIL import ImageTk, Image
from Database import Database

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

        image = Image.open("carLoginPic.jpg")
        image = image.resize((frame_width, frame_height))
        self.image = ImageTk.PhotoImage(image)

        image_label = tk.Label(first_frame, image=self.image)
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

        self.user_input = tk.Entry(second_frame)
        self.user_input.grid(row=2, column=1, pady=5, padx=10)

        pass_label = tk.Label(second_frame, text="Password", bg='white', font="Sans")
        pass_label.grid(row=3, column=0, pady=5, padx=10)

        self.pass_input = tk.Entry(second_frame, show="*")
        self.pass_input.grid(row=3, column=1, pady=5, padx=10)

        login_button = tk.Button(second_frame, text="Login", font=("Arial", 13), command=self.login)
        login_button.grid(row=10, column=1, columnspan=2, padx=10, pady=17)

        register_label = tk.Label(second_frame, text="Register", fg="blue", cursor="hand2")
        register_label.bind("<Button-1>", self.open_register)
        register_label.grid(row=11, column=0)

        self.window.mainloop()

    def open_register(self, event):
        self.window.destroy()
        import Register
        register_window = Register.Register()
        register_window.window.mainloop()

    def login(self):
        db = Database('localhost', 'root', '', 'final_project')
        user = self.user_input.get()
        password = self.pass_input.get()
        result = db.login(user, password)
        if result:
            print("Login successful")
        else:
            print("Invalid username or password")