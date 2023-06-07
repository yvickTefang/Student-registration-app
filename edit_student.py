from tkinter import *
from tkinter import ttk
from tkcalendar import *
from PIL import ImageTk, Image, ImageDraw
from ttkthemes import themed_tk as tk
import sqlite3
from tkinter import messagebox
import os
import Frontend.students_view


class EditStudent:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1366x768")
        self.window.title("Edit Student Records")
        self.window.resizable(False, False)
        self.window.config(background='#98a65d')
        self.window.iconbitmap('images\\aa.ico')
        self.edit_page_frame =Image.open('images\\inventory.png')
        photo = ImageTk.PhotoImage(self.edit_page_frame)
        self.image_panel = Label(self.window, image=photo, width=400, height=428, bg='#98a65d')
        self.image_panel.image = photo
        self.image_panel.pack(fill='both', expand='yes')
        self.txt = "Manage Student Records"
        self.heading = Label(self.window, text=self.txt, font=('yu gothic ui', 30, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=430, y=25, width=600)

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

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=('yu gothic ui', 10, "bold"), foreground="black",
                        background="#108cff")

        # ========================Tree View=============================
        self.scrollbarx = Scrollbar(self.window, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(self.window, orient=VERTICAL)
        self.tree = ttk.Treeview(self.window)
        self.tree.place(relx=0.307, rely=0.203, width=880, height=510)
        self.tree.configure(
            yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set
        )
        self.tree.configure(selectmode="extended")

        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbarx.configure(command=self.tree.xview)

        self.scrollbary.place(relx=0.954, rely=0.203, width=22, height=509)
        self.scrollbarx.place(relx=0.307, rely=0.892, width=884, height=22)

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
        self.show_data()
        self.tree.bind("<ButtonRelease-1>", self.student_info)

        # ========================================================================
        # ============================First name==================================
        # ========================================================================
        self.f_name_label = Label(self.window, text="First Name: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.f_name_label.place(x=22, y=40, height=25)

        self.f_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), textvariable=self.FirstName)
        self.f_name_entry.place(x=114, y=40, width=285)  # trebuchet ms

        self.f_name_line = Canvas(self.window, width=285, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.f_name_line.place(x=114, y=63)
        # ========================================================================
        # ============================middle Name====================================
        # ========================================================================

        self.m_name_label = Label(self.window, text="Other Name: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.m_name_label.place(x=22, y=66, height=25)

        self.m_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), textvariable=self.OtherName)
        self.m_name_entry.place(x=125, y=66, width=274)  # trebuchet ms

        self.m_name_line = Canvas(self.window, width=274, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.m_name_line.place(x=125, y=89)
        # ========================================================================
        # ============================Surname=======================================
        # ========================================================================

        self.l_name_label = Label(self.window, text="Surname: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.l_name_label.place(x=22, y=92, height=25)

        self.l_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), textvariable=self.Surname)
        self.l_name_entry.place(x=98, y=92, width=301)  # trebuchet ms

        self.l_name_line = Canvas(self.window, width=301, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.l_name_line.place(x=98, y=115)
        # ========================================================================
        # ============================DOB=========================================
        # ========================================================================

        self.dob_label = Label(self.window, text="Date Of Birth: ", bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        self.dob_label.place(x=22, y=118, height=25)

        self.dob_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12), textvariable=self.DateOfBirth)
        self.dob_entry.insert(0, "dd/mm/yyyy")
        self.dob_entry.place(x=131, y=118, width=268)  # trebuchet ms
        self.dob_entry.bind("<1>", self.pick_date)

        self.dob_line = Canvas(self.window, width=268, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.dob_line.place(x=131, y=141)
        # ========================================================================
        # ============================Nationality==================================
        # ========================================================================
        self.country_label = Label(self.window, text="Nationality: ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.country_label.place(x=22, y=144, height=25)

        self.country_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12), textvariable=self.Nationality)
        self.country_entry.place(x=115, y=144, width=284)  # trebuchet ms

        self.country_line = Canvas(self.window, width=284, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.country_line.place(x=115, y=167)
        # ========================================================================
        # ===========================Gender=======================================
        # ========================================================================
        style = ttk.Style()

        # style.map('TCombobox', selectbackground=[('readonly', 'grey')])
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.gender_label = Label(self.window, text="Gender ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.gender_label.place(x=22, y=174, height=25)

        self.gender_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=33, textvariable=self.Gender)

        gender_list = ['Male', 'Female']
        self.gender_combo['values'] = gender_list
        self.gender_combo.place(x=84, y=174)
        # ========================================================================
        # ============================Student ID==================================
        # ========================================================================
        self.student_ID_label = Label(self.window, text="Student ID: ", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.student_ID_label.place(x=22, y=202, height=25)

        self.student_ID_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.StudentID)
        self.student_ID_entry.place(x=115, y=202, width=285)  # trebuchet ms

        self.student_ID_line = Canvas(self.window, width=285, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.student_ID_line.place(x=115, y=225)
        # ========================================================================
        # ============================Student Class====================================
        # ========================================================================

        self.student_class_label = Label(self.window, text="Student Class: ", bg="white", fg="#4f4e4d",
                                         font=("yu gothic ui", 13, "bold"))
        self.student_class_label.place(x=22, y=228, height=25)

        self.student_class_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                         font=("yu gothic ui semibold", 12), textvariable=self.StudentClass)
        self.student_class_entry.place(x=134, y=228, width=266)  # trebuchet ms

        self.student_class_line = Canvas(self.window, width=266, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.student_class_line.place(x=134, y=251)
        # ========================================================================
        # ============================Address====================================
        # ========================================================================

        self.address_label = Label(self.window, text="Address: ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.address_label.place(x=22, y=254, height=25)

        self.address_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12), textvariable=self.Address)
        self.address_entry.place(x=90, y=254, width=310)  # trebuchet ms

        self.address_line = Canvas(self.window, width=310, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.address_line.place(x=90, y=277)
        # ========================================================================
        # ============================Admission date====================================
        # ========================================================================

        self.admission_label = Label(self.window, text="Admission Date: ", bg="white", fg="#4f4e4d",
                                     font=("yu gothic ui", 13, "bold"))
        self.admission_label.place(x=22, y=280, height=25)
        self.admission_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                     font=("yu gothic ui semibold", 12), textvariable=self.AdmissionDate)
        self.admission_entry.insert(0, "dd/mm/yyyy")
        self.admission_entry.place(x=150, y=280, width=250)  # trebuchet ms
        self.admission_entry.bind("<1>", self.pick_date2)

        self.admission_line = Canvas(self.window, width=250, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.admission_line.place(x=150, y=303)
        # ========================================================================
        # ============================Mother's Name====================================
        # ========================================================================

        self.mother_name_label = Label(self.window, text="Mother's Name: ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        self.mother_name_label.place(x=22, y=306, height=25)

        self.mother_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12), textvariable=self.MotherName)
        self.mother_name_entry.place(x=149, y=306, width=251)  # trebuchet ms

        self.mother_name_line = Canvas(self.window, width=251, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.mother_name_line.place(x=149, y=329)
        # ========================================================================
        # ============================Mother details =======================================
        # ========================================================================
        self.mother_ad_label = Label(self.window, text="Mother ", bg="white",
                                     fg="#4f4e4d", font=("yu gothic ui", 12, "bold"))
        self.mother_ad_label.place(x=22, y=393, height=25)

        self.mother_ad_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=33, textvariable=self.MotherStatus)

        mother_list = ['Alive', 'Deceased', 'Unknown']
        self.mother_ad_combo['values'] = mother_list
        self.mother_ad_combo.place(x=83, y=392)
        # ========================================================================
        # ============================Father Details=======================================
        # ========================================================================
        self.father_ad_label = Label(self.window, text="Father", bg="white",
                                     fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.father_ad_label.place(x=22, y=360, height=25)

        self.father_ad_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=33, textvariable=self.FatherStatus)

        father_list = ['Alive', 'Deceased', 'Unknown']
        self.father_ad_combo['values'] = father_list
        self.father_ad_combo.place(x=83, y=360)
        # ========================================================================
        # ============================Father/Mother Details=======================================
        # ========================================================================
        self.father_mother_label = Label(self.window, text="Father and Mother",
                                         bg="white", fg="#4f4e4d", font=("yu gothic ui", 11, "bold"))
        self.father_mother_label.place(x=22, y=426, height=25)

        self.father_mother_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'),
                                                state='readonly',
                                                width=25, textvariable=self.BothParentStatus)

        father_mother_list = ['Living together', 'Separated', 'Divorced']
        self.father_mother_combo['values'] = father_mother_list
        self.father_mother_combo.place(x=157, y=424)
        # ========================================================================
        # ============================father's Name====================================
        # ========================================================================
        self.father_name_label = Label(self.window, text="Father's Name: ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        self.father_name_label.place(x=22, y=332, height=25)

        self.father_name_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12), textvariable=self.FatherName)
        self.father_name_entry.place(x=140, y=332, width=260)  # trebuchet ms

        self.father_name_line = Canvas(self.window, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.father_name_line.place(x=140, y=355)
        # ========================================================================
        # ===========================Sponsor=======================================
        # ========================================================================
        style = ttk.Style()
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.sponsor_label = Label(self.window, text="Sponsor", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.sponsor_label.place(x=22, y=457, height=25)

        self.sponsor_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                          width=32, textvariable=self.StudentSponsor)

        sponsor_list = ['Parent', 'Sibling', 'Guardian']
        self.sponsor_combo['values'] = sponsor_list
        # self.gender_combo.current(0)
        self.sponsor_combo.place(x=93, y=457)
        # ========================================================================
        # ===========================Sponsor's Name=======================================
        # ========================================================================
        self.sponsor_na_label = Label(self.window, text="Sponsor's Name:", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.sponsor_na_label.place(x=22, y=488, height=25)
        self.sponsor_na_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.SponsorName)
        self.sponsor_na_entry.place(x=155, y=486, width=247)  # trebuchet ms

        self.sponsor_na_line = Canvas(self.window, width=247, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.sponsor_na_line.place(x=155, y=510)
        # ========================================================================
        # ===========================Sponsor's Number=======================================
        # ========================================================================
        self.sponsor_no_label = Label(self.window, text="Sponsor's Phone No. :", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.sponsor_no_label.place(x=22, y=514, height=25)
        self.sponsor_no_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.SponsorPhone)
        self.sponsor_no_entry.place(x=194, y=514, width=208)  # trebuchet ms

        self.sponsor_no_line = Canvas(self.window, width=208, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.sponsor_no_line.place(x=194, y=537)
        # ========================================================================
        # ===========================Sponsor's Occupation=======================================
        # ========================================================================
        self.sponsor_work_label = Label(self.window, text="Sponsor's Occupation:", bg="white", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
        self.sponsor_work_label.place(x=22, y=540, height=25)
        self.sponsor_work_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                        font=("yu gothic ui semibold", 12), textvariable=self.SponsorOccupation)
        self.sponsor_work_entry.place(x=195, y=540, width=207)  # trebuchet ms

        self.sponsor_work_line = Canvas(self.window, width=207, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.sponsor_work_line.place(x=195, y=563)
        # ========================================================================
        # ===========================Previous school=======================================
        # ========================================================================
        self.old_school_label = Label(self.window, text="Previous School:", bg="white", fg="#4f4e4d",
                                      font=("yu gothic ui", 13, "bold"))
        self.old_school_label.place(x=22, y=570, height=25)
        self.old_school_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                      font=("yu gothic ui semibold", 12), textvariable=self.PreviousSchool)
        self.old_school_entry.place(x=151, y=568, width=252)  # trebuchet ms

        self.old_school_line = Canvas(self.window, width=252, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.old_school_line.place(x=151, y=592)
        # ========================================================================
        # ===========================Health Issues=======================================
        # ========================================================================
        style = ttk.Style()
        self.window.option_add("*TCombobox*Listbox*Foreground", '#f29844')

        self.health_label = Label(self.window, text="Medical Information ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        self.health_label.place(x=22, y=602, height=25)

        self.health_combo = ttk.Combobox(self.window, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=22, textvariable=self.StudentMedicalInformation)

        health_list = ['Normal health', 'Asthma', 'Eyesight', 'Hearing problem', 'Allergies', 'Other']
        self.health_combo['values'] = health_list
        # self.gender_combo.current(0)
        self.health_combo.place(x=185, y=600)

        # =======================================================================
        # ========================BUTTON IMAGES================================
        # =======================================================================

        submit_button4 = Image.open('images\\update.png')
        photo = ImageTk.PhotoImage(submit_button4)
        submit_button_edt = Button(self.window, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                   cursor="hand2", highlightthickness="0", command=lambda: self.update())
        submit_button_edt.image = photo
        submit_button_edt.place(x=279, y=645)

        # =================Delete==============================
        dlt_button = Image.open('images\\delete.png')
        photo = ImageTk.PhotoImage(dlt_button)
        dlt_button_edt = Button(self.window, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                cursor="hand2", highlightthickness="0", command=lambda: self.delete_records())
        dlt_button_edt.image = photo
        dlt_button_edt.place(x=20, y=645)
        # =================Add New==============================
        adn_button = Image.open('images\\addnew.png')
        photo = ImageTk.PhotoImage(adn_button)
        adn_button_edt = Button(self.window, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                cursor="hand2", highlightthickness="0", command=lambda: self.add_student())
        adn_button_edt.image = photo
        adn_button_edt.place(x=150, y=645)

        # =================Exit==============================
        bck_button = Image.open('images\\back.png')
        photo = ImageTk.PhotoImage(bck_button)
        bck_button_edt = Button(self.window, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                cursor="hand2", highlightthickness="0", command=lambda: self.go_to_back())
        bck_button_edt.image = photo
        bck_button_edt.place(x=279, y=690)

        # =================Clear==============================
        clr_button = Image.open('images\\clear.png')
        photo = ImageTk.PhotoImage(clr_button)
        clr_button_edt = Button(self.window, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                cursor="hand2", highlightthickness="0", command=lambda: self.Reset())
        clr_button_edt.image = photo
        clr_button_edt.place(x=150, y=690)

        # =================Exit==============================
        ext_button = Image.open('images\\exit.png')
        photo = ImageTk.PhotoImage(ext_button)
        ext_button_edt = Button(self.window, image=photo, relief=FLAT, borderwidth=0, activebackground="white",
                                cursor="hand2", highlightthickness="0", command=lambda: self.exit())
        ext_button_edt.image = photo
        ext_button_edt.place(x=20, y=690)

        # ========================================================================
        # ===========================Health Issues=======================================
        # ========================================================================
    def Reset(self):
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

        # ======== Fetch =========
    def student_info(self, ev):
        viewInfo = self.tree.focus()
        learner_data = self.tree.item(viewInfo)
        row = learner_data['values']
        self.StudentID.set(row[0])
        self.FirstName.set(row[1])
        self.Surname.set(row[2])
        self.OtherName.set(row[3])
        self.StudentClass.set(row[4])
        self.DateOfBirth.set(row[5])
        self.Gender.set(row[6])
        self.Address.set(row[7])
        self.Nationality.set(row[8])
        self.AdmissionDate.set(row[9])
        self.MotherName.set(row[10])
        self.FatherName.set(row[11])
        self.MotherStatus.set(row[12])
        self.FatherStatus.set(row[13])
        self.BothParentStatus.set(row[14])
        self.PreviousSchool.set(row[15])
        self.StudentSponsor.set(row[16])
        self.SponsorName.set(row[17])
        self.SponsorPhone.set(row[18])
        self.SponsorOccupation.set(row[19])
        self.StudentMedicalInformation.set(row[20])

        # ================== Pick Date Window =========================
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

    def go_to_back(self):
        wind = Toplevel()
        Frontend.students_view.ManageStudent(wind)
        self.window.withdraw()
        wind.deiconify()

    def add_student(self):
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
        self.show_data()
        self.Reset()
        messagebox.showinfo("", "New Student Record Added Successfully")

    def show_data(self):
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

    def delete_records(self):
        try:
            tree_view_content = self.tree.focus()
            tree_view_items = self.tree.item(tree_view_content)
            tree_view_values = tree_view_items['values'][1]
            ask = messagebox.askyesno("Warning",
                                      f"Are you sure you want to delete records of {tree_view_values}")
            if ask is True:
                conn = sqlite3.connect("../Database/student_records.db")
                cur = conn.cursor()
                cur.execute("DELETE FROM student_records where StudentID=?", [self.StudentID.get()])
                conn.commit()
                self.show_data()
                conn.close()
                self.Reset()
                messagebox.showinfo("Success", f" {tree_view_values} records has been deleted Successfully")
            else:
                pass

        except BaseException as msg:
            print(msg)
            messagebox.showerror("Error",
                                 "There is some error deleting the data\n Make sure you have Selected the data")

    def update(self):
        conn = sqlite3.connect("../Database/student_records.db")
        cur = conn.cursor()
        cur.execute("UPDATE student_records set FirstName=?,Surname=?,OtherName=?,StudentClass=?,DateOfBirth=?,Gender=?,"
                    "Address=?,Nationality=?,AdmissionDate=?,MotherName=?,FatherName=?,MotherStatus=?,FatherStatus=?,"
                    "BothParentStatus=?,PreviousSchool=?,StudentSponsor=?,SponsorName=?,SponsorPhone=?,"
                    "SponsorOccupation=?,StudentMedicalInformation=? where StudentID=?",
                    ([self.FirstName.get(), self.Surname.get(), self.OtherName.get(),
                     self.StudentClass.get(), self.DateOfBirth.get(), self.Gender.get(), self.Address.get(),
                     self.Nationality.get(), self.AdmissionDate.get(), self.MotherName.get(), self.FatherName.get(),
                     self.MotherStatus.get(), self.FatherStatus.get(), self.BothParentStatus.get(),
                     self.PreviousSchool.get(), self.StudentSponsor.get(), self.SponsorName.get(),
                     self.SponsorPhone.get(), self.SponsorOccupation.get(), self.StudentMedicalInformation.get(),
                     self.StudentID.get()]))
        conn.commit()
        self.show_data()
        conn.close()
        self.Reset()
        messagebox.showinfo("Success", "Student Record updated Successfully")

    def exit(self):
        exit_command = messagebox.askyesno("Edit Teacher Records", "Are you sure you want to exit")
        if exit_command > 0:
            self.window.destroy()


def win():
    window = tk.ThemedTk()
    window.get_themes()
    window.set_theme("arc")
    EditStudent(window)
    window.mainloop()


if __name__ == '__main__':
    win()
