from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image
from ttkthemes import themed_tk as tk
import sqlite3
from tkinter import messagebox
import Frontend.students_view


class StudentRegisterForm:
    def __init__(self, wind):
        self.window = wind
        self.window.title("Student Registration Form")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        # self.window.state('zoomed')
        self.window.configure(background='#108cff')
        self.reg_frame = Frame(self.window, bg="#ffffff", width=1300, height=680)
        self.reg_frame.place(x=30, y=30)

        self.txt = "Student Registration Form"
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.reg_frame, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=10, y=0, width=600)

        style = ttk.Style()
        style.theme_use("clam")

        self.cred_frame = LabelFrame(self.reg_frame, text="Personal Details", bg="white", fg="#4f4e4d", height=140,
                                     width=810, borderwidth=2.4,
                                     font=("yu gothic ui", 13, "bold"))
        self.cred_frame.config(highlightbackground="red")
        self.cred_frame.place(x=100, y=100)

        def Exit():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.window)
            if sure == True:
                self.window.quit()

        self.window.protocol("WM_DELETE_WINDOW", Exit)

        # ========================================================================
        # ============================ Variables ==================================
        # ========================================================================
        self.StudentID = StringVar()
        self.FirstName = StringVar()
        self.Surname = StringVar()
        self.OtherName = StringVar()
        self.StudentClass = StringVar()
        self.DateOfBirth = StringVar()
        self.Gender = StringVar()
        self.Address = StringVar()
        self.Nationality = StringVar()
        self.AdmissionDate = StringVar()
        self.MotherName = StringVar()
        self.FatherName = StringVar()
        self.MotherStatus = StringVar()
        self.FatherStatus = StringVar()
        self.BothParentStatus = StringVar()
        self.PreviousSchool = StringVar()
        self.StudentSponsor = StringVar()
        self.SponsorName = StringVar()
        self.SponsorPhone = StringVar()
        self.SponsorOccupation = StringVar()
        self.StudentMedicalInformation = StringVar()

        # ========================================================================
        # ============================First name==================================
        # ========================================================================
        self.f_name_label = Label(self.cred_frame, text="First Name: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.f_name_label.place(x=10, y=10)

        self.f_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), textvariable=self.FirstName)
        self.f_name_entry.place(x=234, y=167, width=260)  # trebuchet ms

        self.f_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.f_name_line.place(x=234, y=189)

        # ========================================================================
        # ============================middle Name====================================
        # ========================================================================

        self.m_name_label = Label(self.cred_frame, text="Other Name: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.m_name_label.place(x=10, y=50)

        self.m_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), textvariable=self.OtherName)
        self.m_name_entry.place(x=252, y=207, width=260)  # trebuchet ms

        self.m_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.m_name_line.place(x=252, y=230)

        # ========================================================================
        # ============================Surname=======================================
        # ========================================================================

        self.l_name_label = Label(self.cred_frame, text="Surname: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.l_name_label.place(x=370, y=10)

        self.l_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), textvariable=self.Surname)
        self.l_name_entry.place(x=576, y=167, width=350)  # trebuchet ms

        self.l_name_line = Canvas(self.window, width=350, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.l_name_line.place(x=576, y=189)

        # ========================================================================
        # ============================DOB=========================================
        # ========================================================================

        self.dob_label = Label(self.cred_frame, text="Date Of Birth: ", bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.dob_label.place(x=380, y=50)

        self.dob_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12), textvariable=self.DateOfBirth)
        self.dob_entry.insert(0, "dd/mm/yyyy")
        self.dob_entry.place(x=650, y=207, width=255)  # trebuchet ms
        self.dob_entry.bind("<1>", self.pick_date)

        self.dob_line = Canvas(self.window, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.dob_line.place(x=622, y=230)

        # =======================================================================
        # ========================frame for personal credentials ================
        # =======================================================================

        self.personal_frame = LabelFrame(self.reg_frame, text="Account Details", bg="white", fg="#4f4e4d", height=180,
                                         width=810, borderwidth=2.4,
                                         font=("yu gothic ui", 13, "bold"))
        self.personal_frame.config(highlightbackground="red")
        self.personal_frame.place(x=100, y=260)

        # ========================================================================
        # ============================Nationality==================================
        # ========================================================================
        self.country_label = Label(self.personal_frame, text="Nationality: ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.country_label.place(x=10, y=10)

        self.country_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12), textvariable=self.Nationality)
        self.country_entry.place(x=235, y=327, width=260)  # trebuchet ms

        self.country_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.country_line.place(x=235, y=349)

        # ========================================================================
        # ===========================Gender=======================================
        # ========================================================================
        style = ttk.Style()

        # style.map('TCombobox', selectbackground=[('readonly', 'grey')])
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.gender_label = Label(self.personal_frame, text="Gender ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.gender_label.place(x=375, y=10)

        self.gender_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=35, textvariable=self.Gender)

        gender_list = ['Male', 'Female']
        self.gender_combo['values'] = gender_list
        self.gender_combo.place(x=580, y=327)

        # ========================================================================
        # ============================Student ID==================================
        # ========================================================================
        self.student_ID_label = Label(self.personal_frame, text="Student ID: ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.student_ID_label.place(x=10, y=50)

        self.student_ID_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.StudentID)
        self.student_ID_entry.place(x=231, y=367, width=260)  # trebuchet ms

        self.student_ID_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.student_ID_line.place(x=231, y=389)

        # ========================================================================
        # ============================Student Class====================================
        # ========================================================================

        self.student_class_label = Label(self.personal_frame, text="Student Class: ", bg="white", fg="#4f4e4d",
                                         font=("yu gothic ui", 13, "bold"))
        self.student_class_label.place(x=370, y=50)

        self.student_class_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                         font=("yu gothic ui semibold", 12), textvariable=self.StudentClass)
        self.student_class_entry.place(x=612, y=367, width=305)  # trebuchet ms

        self.student_class_line = Canvas(self.window, width=305, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.student_class_line.place(x=612, y=389)

        # ========================================================================
        # ============================Address====================================
        # ========================================================================

        self.address_label = Label(self.personal_frame, text="Address: ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.address_label.place(x=10, y=90)

        self.address_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12), textvariable=self.Address)
        self.address_entry.place(x=213, y=404, width=280)  # trebuchet ms

        self.address_line = Canvas(self.window, width=280, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.address_line.place(x=213, y=427)

        # ========================================================================
        # ============================Admission date====================================
        # ========================================================================

        self.admission_label = Label(self.personal_frame, text="Admission Date: ", bg="white", fg="#4f4e4d",
                                     font=("yu gothic ui", 13, "bold"))
        self.admission_label.place(x=370, y=90)
        self.admission_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                     font=("yu gothic ui semibold", 12), textvariable=self.AdmissionDate)
        self.admission_entry.insert(0, "dd/mm/yyyy")
        self.admission_entry.place(x=650, y=406, width=255)  # trebuchet ms
        self.admission_entry.bind("<1>", self.pick_date2)

        self.admission_line = Canvas(self.window, width=286, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.admission_line.place(x=630, y=429)

        # =======================================================================
        # ========================frame for parent details ================
        # =======================================================================

        self.parent_frame = LabelFrame(self.reg_frame, text="Parent Details", bg="white", fg="#4f4e4d", height=180,
                                       width=810, borderwidth=2.4,
                                       font=("yu gothic ui", 13, "bold"))
        self.parent_frame.config(highlightbackground="red")
        self.parent_frame.place(x=100, y=460)

        # ========================================================================
        # ============================Mother's Name====================================
        # ========================================================================

        self.mother_name_label = Label(self.parent_frame, text="Mother's Name: ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        self.mother_name_label.place(x=10, y=10)

        self.mother_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12), textvariable=self.MotherName)
        self.mother_name_entry.place(x=269, y=528, width=260)  # trebuchet ms

        self.mother_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.mother_name_line.place(x=269, y=550)

        # ========================================================================
        # ============================Mother details =======================================
        # ========================================================================
        self.mother_ad_label = Label(self.parent_frame, text="Mother:      (please choose where necessary)", bg="white",
                                     fg="#4f4e4d", font=("yu gothic ui", 11, "bold"))
        self.mother_ad_label.place(x=450, y=0)

        self.mother_ad_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=35, textvariable=self.MotherStatus)

        mother_list = ['Alive', 'Deceased', 'Unknown']
        self.mother_ad_combo['values'] = mother_list
        self.mother_ad_combo.place(x=570, y=538)

        # ========================================================================
        # ============================Father Details=======================================
        # ========================================================================
        self.father_ad_label = Label(self.parent_frame, text="Father:     (please choose where necessary)", bg="white",
                                     fg="#4f4e4d", font=("yu gothic ui", 11, "bold"))
        self.father_ad_label.place(x=450, y=55)

        self.father_ad_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=35, textvariable=self.FatherStatus)

        father_list = ['Alive', 'Deceased', 'Unknown']
        self.father_ad_combo['values'] = father_list
        self.father_ad_combo.place(x=570, y=595)

        # ========================================================================
        # ============================Father/Mother Details=======================================
        # ========================================================================
        self.father_mother_label = Label(self.parent_frame, text="Both Parents are:   (please choose where necessary)",
                                         bg="white", fg="#4f4e4d", font=("yu gothic ui", 11, "bold"))
        self.father_mother_label.place(x=40, y=120)

        self.father_mother_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                                width=35, textvariable=self.BothParentStatus)

        father_mother_list = ['Living together', 'Separated', 'Divorced']
        self.father_mother_combo['values'] = father_mother_list
        self.father_mother_combo.place(x=570, y=635)

        # ========================================================================
        # ============================father's Name====================================
        # ========================================================================

        self.father_name_label = Label(self.parent_frame, text="Father's Name: ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        self.father_name_label.place(x=10, y=70)

        self.father_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12), textvariable=self.FatherName)
        self.father_name_entry.place(x=269, y=588, width=260)  # trebuchet ms

        self.father_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.father_name_line.place(x=269, y=610)

        # =======================================================================
        # ========================frame for information==========================
        # =======================================================================

        self.info_frame = LabelFrame(self.reg_frame,
                                                          "",
                                     bg="white", fg="#4f4e4d", height=359,
                                     width=340, borderwidth=2.4,
                                     font=("yu gothic ui", 13, "bold"))
        self.info_frame.config(highlightbackground="red")
        self.info_frame.place(x=930, y=80)

        # ========================================================================
        # ===========================Sponsor=======================================
        # ========================================================================
        style = ttk.Style()
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.sponsor_label = Label(self.info_frame, text="Who is Sponsoring the Student? ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.sponsor_label.place(x=40, y=0)

        self.sponsor_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                          width=28, textvariable=self.StudentSponsor)

        sponsor_list = ['Parent', 'Sibling', 'Guardian']
        self.sponsor_combo['values'] = sponsor_list
        # self.gender_combo.current(0)
        self.sponsor_combo.place(x=990, y=140)

        # ========================================================================
        # ===========================Sponsor's Name=======================================
        # ========================================================================
        self.sponsor_na_label = Label(self.info_frame, text="Sponsor's Full Name?", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.sponsor_na_label.place(x=40, y=55)
        self.sponsor_na_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.SponsorName)
        self.sponsor_na_entry.place(x=993, y=190, width=260)  # trebuchet ms

        self.sponsor_na_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.sponsor_na_line.place(x=993, y=212)

        # ========================================================================
        # ===========================Sponsor's Number=======================================
        # ========================================================================
        self.sponsor_no_label = Label(self.info_frame, text="Sponsor's Phone Number?", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.sponsor_no_label.place(x=40, y=105)
        self.sponsor_no_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.SponsorPhone)
        self.sponsor_no_entry.place(x=993, y=240, width=260)  # trebuchet ms

        self.sponsor_no_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.sponsor_no_line.place(x=993, y=265)

        # ========================================================================
        # ===========================Sponsor's Occupation=======================================
        # ========================================================================
        self.sponsor_work_label = Label(self.info_frame, text="Sponsor's Occupation?", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.sponsor_work_label.place(x=40, y=160)
        self.sponsor_work_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.SponsorOccupation)
        self.sponsor_work_entry.place(x=993, y=300, width=260)  # trebuchet ms

        self.sponsor_work_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.sponsor_work_line.place(x=993, y=325)

        # ========================================================================
        # ===========================Health Issues=======================================
        # ========================================================================
        style = ttk.Style()
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.health_label = Label(self.info_frame, text="Student's Medical Information ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.health_label.place(x=40, y=218)

        self.health_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=28, textvariable=self.StudentMedicalInformation)

        health_list = ['Normal health', 'Asthma', 'Eyesight', 'Hearing problem', 'Allergies', 'Other']
        self.health_combo['values'] = health_list
        # self.gender_combo.current(0)
        self.health_combo.place(x=993, y=360)

        # ========================================================================
        # ===========================Previous school=======================================
        # ========================================================================
        self.old_school_label = Label(self.info_frame, text="Student's Previous School", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.old_school_label.place(x=40, y=278)
        self.old_school_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.PreviousSchool)
        self.old_school_entry.place(x=993, y=420, width=260)  # trebuchet ms

        self.old_school_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.old_school_line.place(x=993, y=443)

        # =======================================================================
        # ========================frame for Buttons==========================
        # =======================================================================

        self.buttons_frame = LabelFrame(self.reg_frame,
                                        "",
                                        bg="white", fg="#4f4e4d", height=167,
                                        width=340, borderwidth=2.4,
                                        font=("yu gothic ui", 13, "bold"))
        self.buttons_frame.config(highlightbackground="red")
        self.buttons_frame.place(x=930, y=473)

        # =======================================================================
        # ========================BUTTON IMAGES================================
        # =======================================================================

        submit_button0 = Image.open('images\\submit.png')
        photo = ImageTk.PhotoImage(submit_button0)
        submit_button_lg = Button(self.buttons_frame, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                  cursor="hand2", highlightthickness="0", command=self.add_new_student)
        submit_button_lg.image = photo
        submit_button_lg.place(x=30, y=25)

        # ===================== Exit==================================================
        exit_button0 = Image.open('images\\exit.png')
        photo = ImageTk.PhotoImage(exit_button0)
        exit_button_rg = Button(self.buttons_frame, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                cursor="hand2", highlightthickness="0", command=lambda: self.exit())
        exit_button_rg.image = photo
        exit_button_rg.place(x=120, y=95)
        # ===================== Clear==================================================
        clear_button0 = Image.open('images\\clear.png')
        photo = ImageTk.PhotoImage(clear_button0)
        clear_button_lg = Button(self.buttons_frame, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                 cursor="hand2", highlightthickness="0", command=self.click_clear_button)
        clear_button_lg.image = photo
        clear_button_lg.place(x=180, y=25)

    def click_clear_button(self):
        self.StudentID.set("")
        self.FirstName.set("")
        self.Surname.set("")
        self.OtherName.set("")
        self.StudentClass.set("")
        self.DateOfBirth.set("dd/mm/yyyy")
        self.Gender.set("")
        self.Address.set("")
        self.Nationality.set("")
        self.AdmissionDate.set("dd/mm/yyyy")
        self.MotherName.set("")
        self.FatherName.set("")
        self.MotherStatus.set("")
        self.FatherStatus.set("")
        self.BothParentStatus.set("")
        self.PreviousSchool.set("")
        self.StudentSponsor.set("")
        self.SponsorName.set("")
        self.SponsorPhone.set("")
        self.SponsorOccupation.set("")
        self.StudentMedicalInformation.set("")


    def click_back_button(self):
        win = Toplevel()
        Frontend.manage_student.ManageStudent(win)
        self.window.withdraw()
        win.deiconify()

    def pick_date(self, event):
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('Choose Date of Birth')
        self.date_win.geometry('250x220+590+370')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="mm/dd/y")
        self.cal.place(x=0, y=0)

        self.okay_btn = ttk.Button(self.date_win, text="Okay", command=self.grab_date)
        self.okay_btn.place(x=80, y=180)

    def grab_date(self):
        self.dob_entry.delete(0, END)
        self.dob_entry.config(fg="#6b6a69")
        self.dob_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def pick_date2(self, event):
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('Choose Admission Date')
        self.date_win.geometry('250x220+500+370')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="dd/mm/y")
        self.cal.place(x=0, y=0)

        self.okay_btn = ttk.Button(self.date_win, text="Submit", command=self.grab_date2)
        self.okay_btn.place(x=80, y=180)

    def grab_date2(self):
        self.admission_entry.delete(0, END)
        self.admission_entry.config(fg="#6b6a69")
        self.admission_entry.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def add_new_student(self):

        conn = sqlite3.connect("../Database/student_records.db")

        cur = conn.cursor()
        cur.execute("INSERT INTO student_records values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (self.StudentID.get(), self.FirstName.get(), self.Surname.get(), self.OtherName.get(),
                     self.StudentClass.get(), self.DateOfBirth.get(), self.Gender.get(), self.Address.get(),
                     self.Nationality.get(), self.AdmissionDate.get(), self.MotherName.get(), self.FatherName.get(),
                     self.MotherStatus.get(), self.FatherStatus.get(), self.BothParentStatus.get(),
                     self.PreviousSchool.get(), self.StudentSponsor.get(), self.SponsorName.get(),
                     self.SponsorPhone.get(), self.SponsorOccupation.get(), self.StudentMedicalInformation.get()))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "New Student Record Added Successfully")

    def exit(self):
        exit_command = messagebox.askyesno("Edit Teacher Records", "Are you sure you want to exit")
        if exit_command > 0:
            self.window.destroy()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    StudentRegisterForm(window)
    window.mainloop()


if __name__ == '__main__':
    win()
