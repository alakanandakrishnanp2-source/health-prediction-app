import sqlite3

def create_table():
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        dob TEXT NOT NULL,
        email TEXT NOT NULL,
        glucose REAL NOT NULL,
        haemoglobin REAL NOT NULL,
        cholesterol REAL NOT NULL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_patient(full_name, dob, email,
                glucose, haemoglobin,
                cholesterol, remarks):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (full_name, dob, email,
     glucose, haemoglobin,
     cholesterol, remarks)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
    ))

    conn.commit()
    conn.close()


def view_patients():

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    records = cursor.fetchall()

    conn.close()

    return records


def update_patient(
    patient_id,
    full_name,
    dob,
    email,
    glucose,
    haemoglobin,
    cholesterol,
    remarks
):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients
    SET
        full_name = ?,
        dob = ?,
        email = ?,
        glucose = ?,
        haemoglobin = ?,
        cholesterol = ?,
        remarks = ?
    WHERE id = ?
    """, (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks,
        patient_id
    ))

    rows_updated = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_updated


def delete_patient(patient_id):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM patients
    WHERE id = ?
    """, (patient_id,))

    rows_deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_deleted


if __name__ == "__main__":
    create_table()
