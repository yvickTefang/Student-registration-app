import sqlite3

conn = sqlite3.connect("student_records.db")
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS student_records (StudentID INTEGER PRIMARY KEY, FirstName TEXT, Surname TEXT, "
    "OtherName TEXT, StudentClass TEXT, DateOfBirth TEXT, Gender TEXT, Address TEXT, Nationality TEXT, "
    "AdmissionDate TEXT, MotherName TEXT, FatherName TEXT, MotherStatus TEXT, FatherStatus TEXT,  "
    "BothParentStatus TEXT, PreviousSchool TEXT, StudentSponsor TEXT, SponsorName TEXT, SponsorPhone INTEGER, "
    "SponsorOccupation TEXT, StudentMedicalInformation TEXT)")
conn.commit()
conn.close()
