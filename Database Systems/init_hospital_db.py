from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "hospital.db"

# Order: EMPLOYEE, PATIENT, then TEST / TREATMENT (foreign keys).
SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EmployeeID           INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName            TEXT NOT NULL,
    LastName             TEXT NOT NULL,
    JobTitle             TEXT,
    Salary               REAL,
    DepartmentName       TEXT,
    DepartmentLocation   TEXT,
    DepartmentPhone      TEXT
);

CREATE TABLE IF NOT EXISTS PATIENT (
    PatientID     INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName     TEXT NOT NULL,
    LastName      TEXT NOT NULL,
    DateOfBirth   TEXT,
    PhoneNumber   TEXT,
    BedID         TEXT,
    RoomNumber    TEXT,
    BedType       TEXT,
    BedStatus     TEXT
);

CREATE TABLE IF NOT EXISTS TEST (
    TestID      INTEGER PRIMARY KEY AUTOINCREMENT,
    TestName    TEXT NOT NULL,
    TestDate    TEXT,
    Result      TEXT,
    PatientID   INTEGER NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES PATIENT (PatientID)
);

CREATE TABLE IF NOT EXISTS TREATMENT (
    TreatmentID    INTEGER PRIMARY KEY AUTOINCREMENT,
    TreatmentName  TEXT NOT NULL,
    Cost           REAL,
    Description    TEXT,
    PatientID      INTEGER NOT NULL,
    EmployeeID     INTEGER NOT NULL,
    FOREIGN KEY (PatientID) REFERENCES PATIENT (PatientID),
    FOREIGN KEY (EmployeeID) REFERENCES EMPLOYEE (EmployeeID)
);
"""

SEED_SQL = """
INSERT OR IGNORE INTO EMPLOYEE (
    EmployeeID, FirstName, LastName, JobTitle, Salary,
    DepartmentName, DepartmentLocation, DepartmentPhone
) VALUES
  (1, 'Maria', 'Garcia', 'Registered Nurse', 78000,
   'Cardiology', 'Building A, Floor 2', '555-2001'),
  (2, 'James', 'Okonkwo', 'Physician', 185000,
   'Emergency', 'Building B, Floor 1', '555-2002'),
  (3, 'Priya', 'Sharma', 'Lab Technician', 62000,
   'Laboratory', 'Building C', '555-2003'),
  (4, 'Elena', 'Volkov', 'Respiratory Therapist', 71000,
   'Pulmonary', 'Building A, Floor 3', '555-2004'),
  (5, 'David', 'Brown', 'Pharmacist', 125000,
   'Pharmacy', 'Building B, Basement', '555-2005');

INSERT OR IGNORE INTO PATIENT (
    PatientID, FirstName, LastName, DateOfBirth, PhoneNumber,
    BedID, RoomNumber, BedType, BedStatus
) VALUES
  (1, 'Casey', 'Rivera', '1990-04-12', '555-0101',
   'B101', '101', 'Standard', 'Occupied'),
  (2, 'Morgan', 'Singh', '2008-09-03', '555-0102',
   'B102', '102', 'Standard', 'Occupied'),
  (3, 'Riley', 'Chen', '1975-11-21', '555-0103',
   NULL, NULL, NULL, NULL),
  (4, 'Avery', 'Kim', '2001-01-30', '555-0104',
   'B201', '201', 'ICU', 'Occupied'),
  (5, 'Jordan', 'Patel', '1962-08-14', '555-0105',
   'B202', '202', 'Standard', 'Available');

INSERT OR IGNORE INTO TEST (
    TestID, TestName, TestDate, Result, PatientID
) VALUES
  (1, 'Complete Blood Count', '2026-04-05', 'Within normal limits', 1),
  (2, 'Chest X-Ray', '2026-04-06', 'No acute findings', 1),
  (3, 'Urinalysis', '2026-04-07', 'Pending', 2),
  (4, 'Blood Glucose', '2026-04-07', '98 mg/dL', 3),
  (5, 'EKG', '2026-04-08', 'Normal sinus rhythm', 4);

INSERT OR IGNORE INTO TREATMENT (
    TreatmentID, TreatmentName, Cost, Description, PatientID, EmployeeID
) VALUES
  (1, 'IV Fluids', 450.00,
   '500mL saline infusion', 1, 1),
  (2, 'Wound Dressing', 120.50,
   'Sterile redressing of laceration', 2, 1),
  (3, 'ECG', 275.00,
   '12-lead electrocardiogram', 1, 2),
  (4, 'Nebulizer Therapy', 195.00,
   'Albuterol breathing treatment', 4, 4),
  (5, 'Medication Counseling', 85.00,
   'Discharge medication review', 5, 5);
"""


def init_db(reset: bool, seed: bool) -> None:
    if reset and DB_PATH.exists():
        DB_PATH.unlink()

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    try:
        conn.executescript(SCHEMA)
        if seed:
            conn.executescript(SEED_SQL)
        conn.commit()
    finally:
        conn.close()

    print(f"Initialized database: {DB_PATH}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize hospital.db (Lab ER schema).")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Delete existing hospital.db before creating tables.",
    )
    parser.add_argument(
        "--no-seed",
        action="store_true",
        help="Skip inserting sample rows.",
    )
    args = parser.parse_args()
    init_db(reset=args.reset, seed=not args.no_seed)


if __name__ == "__main__":
    main()
