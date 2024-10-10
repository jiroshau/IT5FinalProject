from Database import Database
from Login import Login

def main(self):
    db = Database('localhost', 'root', '', 'final_project')
    login_window = Login()
    login_window.window.mainloop()

