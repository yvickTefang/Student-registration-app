from tkinter import *
from PIL import ImageTk, Image
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import Frontend.students_view
import Frontend.RegistrationForm
import Frontend.edit_student


class WelcomeScreen:
    def __init__(self, window):
        self.window = window
        self.window.title('Student Registration System')
        self.window.iconbitmap('images\\aa.ico')
        height = 450
        width = 900
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.resizable(0, 0)

        self.library_frame = Image.open('images\\libraryframe.png')
        photo = ImageTk.PhotoImage(self.library_frame)
        self.library_panel = Label(self.window, image=photo)
        self.library_panel.image = photo
        self.library_panel.pack(fill='both', expand='yes')
        self.txt = "WELCOME TO STUDENT REGISTRATION SYSTEM"
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 15, "bold"), bg="#009aa5", fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=250, y=15, width=440, height=30)

        # ============== Buttons ==========================================================
        self.students_btn = Button(self.window, text="Students View  ", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                                   fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',
                                   command=lambda: self.student_view())
        self.students_btn.place(x=37, y=112, width=118, height=45)

        self.exit_btn = Button(self.window, text="Exit       ", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                               fg="white", bg='#9a258f', bd=0, activebackground='#9a258f', command=self.exit_command)
        self.exit_btn.place(x=38, y=380, width=118, height=45)

        self.manage_btn = Button(self.window, text="Manage View  ", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                                 fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',
                                 command=lambda: self.edit_student())
        self.manage_btn.place(x=36, y=222, width=120, height=45)

        self.fees_btn = Button(self.window, text="School Fees    ", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                                      fg="white", bg='#9a258f', bd=0, activebackground='#9a258f')
        self.fees_btn.place(x=37, y=276, width=118, height=45)

        self.books_shop_btn = Button(self.window, text="Book Shop  ", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                                     fg="white", bg='#9a258f', bd=0, activebackground='#9a258f')
        self.books_shop_btn.place(x=37, y=328, width=118, height=45)

        self.add_btn = Button(self.window, text="Add Students  ", cursor='hand2', font=('yu gothic ui', 11, "bold"),
                              fg="white", bg='#9a258f', bd=0, activebackground='#9a258f',
                              command=lambda: self.add_student())
        self.add_btn.place(x=37, y=167, width=118, height=45)

    def student_view(self):
        win1 = Toplevel()
        Frontend.students_view.ManageStudent(win1)

    def add_student(self):
        win2 = Toplevel()
        Frontend.RegistrationForm.StudentRegisterForm(win2)

    def edit_student(self):
        win3 = Toplevel()
        Frontend.edit_student.EditStudent(win3)
        self.window.withdraw()
        win3.deiconify()

    def exit_command(self):
        exit_command = messagebox.askyesno("Edit Teacher Records", "Are you sure you want to exit")
        if exit_command > 0:
            self.window.destroy()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    WelcomeScreen(window)
    window.mainloop()


if __name__ == '__main__':
    win()
