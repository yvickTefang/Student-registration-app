from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import sqlite3
import Frontend.RegistrationForm
import Frontend.edit_student


class ManageStudent:
    def __init__(self, window):
        self.window = window
        window.geometry("1366x768")
        window.resizable(0, 0)
        self.window.state('zoomed')
        window.title("Student Information Section")
        self.emp = Label(self.window)
        self.emp.place(relx=0, rely=0, width=1366, height=768)
        self.img = PhotoImage(file="./images/inventory.png")
        self.emp.configure(image=self.img)
        self.txt = "Students View"
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.emp, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=90, y=40, width=600)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="black",
                        background="#108cff")

        # ========================Tree View=============================
        self.scrollbarx = Scrollbar(self.emp, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.emp, orient=VERTICAL)
        self.tree = ttk.Treeview(self.emp)
        self.tree.place(relx=0.03, rely=0.203, width=1260, height=550)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.tree.tag_configure('oddrow', background="white")
        self.tree.tag_configure('evenrow', background="lightblue")

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=549)
        self.scrollbarx.place(relx=0.03, rely=0.927, width=1260, height=22)

        self.tree.configure(
            columns=(
                "StudentID",
                "FirstName",
                "Surname",
                "OtherName",
                "StudentClass",
                "DateOfBirth",
                "Gender",
                "Address",
                "Nationality",
                "AdmissionDate",
                "MotherName",
                "FatherName",
                "MotherStatus",
                "FatherStatus",
                "BothParentStatus",
                "PreviousSchool",
                "StudentSponsor",
                "SponsorName",
                "SponsorPhone",
                "SponsorOccupation",
                "StudentMedicalInformation"
            )
        )

        self.tree.heading("StudentID", text="Student ID", anchor=W)
        self.tree.heading("FirstName", text="First Name", anchor=W)
        self.tree.heading("Surname", text="Surname", anchor=W)
        self.tree.heading("OtherName", text="Other Name", anchor=W)
        self.tree.heading("StudentClass", text="Student Class", anchor=W)
        self.tree.heading("DateOfBirth", text="Date Of Birth", anchor=W)
        self.tree.heading("Gender", text="Gender", anchor=W)
        self.tree.heading("Address", text="Address", anchor=W)
        self.tree.heading("Nationality", text="Nationality", anchor=W)
        self.tree.heading("AdmissionDate", text="Admission Date", anchor=W)
        self.tree.heading("MotherName", text="Mother's Name", anchor=W)
        self.tree.heading("FatherName", text="Father's Name", anchor=W)
        self.tree.heading("MotherStatus", text="Mother's Status", anchor=W)
        self.tree.heading("FatherStatus", text="Father's Status", anchor=W)
        self.tree.heading("BothParentStatus", text="Both Parent status", anchor=W)
        self.tree.heading("PreviousSchool", text="Previous School", anchor=W)
        self.tree.heading("StudentSponsor", text="Student's Sponsor", anchor=W)
        self.tree.heading("SponsorName", text="Sponsor's Name", anchor=W)
        self.tree.heading("SponsorPhone", text="Sponsor's Phone Number", anchor=W)
        self.tree.heading("SponsorOccupation", text="Sponsor's Occupation", anchor=W)
        self.tree.heading("StudentMedicalInformation", text="Student Medical Information", anchor=W)

        self.tree.column("#0", stretch=NO, minwidth=0, width=0)
        self.tree.column("#1", stretch=NO, minwidth=0, width=100)
        self.tree.column("#2", stretch=NO, minwidth=0, width=140)
        self.tree.column("#3", stretch=NO, minwidth=0, width=160)
        self.tree.column("#4", stretch=NO, minwidth=0, width=140)
        self.tree.column("#5", stretch=NO, minwidth=0, width=120)
        self.tree.column("#6", stretch=NO, minwidth=0, width=120)
        self.tree.column("#7", stretch=NO, minwidth=0, width=110)
        self.tree.column("#8", stretch=NO, minwidth=0, width=260)
        self.tree.column("#9", stretch=NO, minwidth=0, width=110)
        self.tree.column("#10", stretch=NO, minwidth=0, width=120)
        self.tree.column("#11", stretch=NO, minwidth=0, width=260)
        self.tree.column("#12", stretch=NO, minwidth=0, width=260)
        self.tree.column("#13", stretch=NO, minwidth=0, width=140)
        self.tree.column("#14", stretch=NO, minwidth=0, width=140)
        self.tree.column("#15", stretch=NO, minwidth=0, width=250)
        self.tree.column("#16", stretch=NO, minwidth=0, width=260)
        self.tree.column("#17", stretch=NO, minwidth=0, width=150)
        self.tree.column("#18", stretch=NO, minwidth=0, width=260)
        self.tree.column("#19", stretch=NO, minwidth=0, width=200)
        self.tree.column("#20", stretch=NO, minwidth=0, width=150)
        self.tree.column("#21", stretch=NO, minwidth=0, width=260)
        self.show_all()

        # ===================== update student==================================================
        edit_r_button = Image.open('images\\Editstudentdetails.png')
        photo = ImageTk.PhotoImage(edit_r_button)
        edit_r_button_l = Button(self.emp, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                 cursor="hand2", highlightthickness="0", command=lambda: self.manage_student())
        edit_r_button_l.image = photo
        edit_r_button_l.place(x=640, y=60)

        # ===================== back ==================================================
        back_r_button = Image.open('images\\exit2.png')
        photo = ImageTk.PhotoImage(back_r_button)
        back_r_button_l = Button(self.emp, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                 cursor="hand2", highlightthickness="0", command=lambda: self.exit())
        back_r_button_l.image = photo
        back_r_button_l.place(x=980, y=60)

    def manage_student(self):
        update_window = Toplevel()
        Frontend.edit_student.EditStudent(update_window)
        self.window.withdraw()
        update_window.deiconify()

    def show_all(self):
        conn = sqlite3.connect("../Database/student_records.db")
        cur = conn.cursor()
        cur.execute("select * from student_records")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('', END, values=row)
            conn.commit()
        conn.close()

    def exit(self):
        exit_command = messagebox.askyesno("Edit Teacher Records", "Are you sure you want to exit")
        if exit_command > 0:
            self.window.destroy()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    ManageStudent(window)
    window.mainloop()


if __name__ == '__main__':
    win()
