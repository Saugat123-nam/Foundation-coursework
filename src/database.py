"""
Task 3 & 4 — Database Normalization + SQL Operations
Creates a normalized SQLite database (Students, Clubs, Memberships)
and demonstrates INSERT, SELECT, and JOIN queries.
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "db", "college.db")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_schema(conn: sqlite3.Connection):
    conn.executescript("""
        DROP TABLE IF EXISTS Membership;
        DROP TABLE IF EXISTS Student;
        DROP TABLE IF EXISTS Club;

        CREATE TABLE Student (
            StudentID   INTEGER PRIMARY KEY,
            StudentName TEXT    NOT NULL,
            Email       TEXT    NOT NULL UNIQUE
        );

        CREATE TABLE Club (
            ClubID      TEXT PRIMARY KEY,
            ClubName    TEXT NOT NULL,
            ClubRoom    TEXT NOT NULL,
            ClubMentor  TEXT NOT NULL
        );

        CREATE TABLE Membership (
            MembershipID INTEGER PRIMARY KEY AUTOINCREMENT,
            StudentID    INTEGER NOT NULL REFERENCES Student(StudentID),
            ClubID       TEXT    NOT NULL REFERENCES Club(ClubID),
            JoinDate     TEXT    NOT NULL,
            UNIQUE (StudentID, ClubID)
        );
    """)


def seed_data(conn: sqlite3.Connection):
    conn.executemany(
        "INSERT INTO Student VALUES (?, ?, ?)",
        [
            (1, "Asha",   "asha@email.com"),
            (2, "Bikash", "bikash@email.com"),
            (3, "Nisha",  "nisha@email.com"),
            (4, "Rohan",  "rohan@email.com"),
            (5, "Suman",  "suman@email.com"),
            (6, "Pooja",  "pooja@email.com"),
            (7, "Aman",   "aman@email.com"),
        ],
    )
    conn.executemany(
        "INSERT INTO Club VALUES (?, ?, ?, ?)",
        [
            ("C01", "Music Club",  "R101", "Mr. Raman"),
            ("C02", "Sports Club", "R202", "Ms. Sita"),
            ("C03", "Drama Club",  "R303", "Mr. Kiran"),
            ("C04", "Coding Club", "Lab1", "Mr. Anil"),
        ],
    )
    conn.executemany(
        "INSERT INTO Membership (StudentID, ClubID, JoinDate) VALUES (?, ?, ?)",
        [
            (1, "C01", "2024-01-10"),
            (2, "C02", "2024-01-12"),
            (1, "C02", "2024-01-15"),
            (3, "C01", "2024-01-20"),
            (4, "C03", "2024-01-18"),
            (5, "C01", "2024-01-22"),
            (2, "C03", "2024-01-25"),
            (6, "C02", "2024-01-27"),
            (3, "C04", "2024-01-28"),
            (7, "C04", "2024-01-30"),
        ],
    )
    conn.commit()


def insert_student(conn: sqlite3.Connection, student_id: int, name: str, email: str):
    conn.execute(
        "INSERT INTO Student (StudentID, StudentName, Email) VALUES (?, ?, ?)",
        (student_id, name, email),
    )
    conn.commit()


def insert_club(conn: sqlite3.Connection, club_id: str, name: str, room: str, mentor: str):
    conn.execute(
        "INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor) VALUES (?, ?, ?, ?)",
        (club_id, name, room, mentor),
    )
    conn.commit()


def get_all_students(conn: sqlite3.Connection) -> list:
    return conn.execute("SELECT * FROM Student ORDER BY StudentID").fetchall()


def get_all_clubs(conn: sqlite3.Connection) -> list:
    return conn.execute("SELECT * FROM Club ORDER BY ClubID").fetchall()


def get_memberships(conn: sqlite3.Connection) -> list:
    return conn.execute("""
        SELECT s.StudentName, c.ClubName, m.JoinDate
        FROM   Membership m
        JOIN   Student    s ON s.StudentID = m.StudentID
        JOIN   Club       c ON c.ClubID    = m.ClubID
        ORDER  BY s.StudentName, m.JoinDate
    """).fetchall()


def run_demo():
    print("\n" + "=" * 50)
    print("TASK 3 & 4 — DATABASE + SQL OPERATIONS")
    print("=" * 50)

    conn = get_connection()
    create_schema(conn)
    seed_data(conn)

    # Insert new records (Task 4 examples)
    insert_student(conn, 8, "Kripa", "kripa@email.com")
    insert_club(conn, "C05", "Photography Club", "R404", "Ms. Preet")

    print("\nAll Students:")
    for row in get_all_students(conn):
        print(f"  {dict(row)}")

    print("\nAll Clubs:")
    for row in get_all_clubs(conn):
        print(f"  {dict(row)}")

    print("\nMembership Report (JOIN):")
    print(f"  {'Student':<12} {'Club':<18} {'Join Date'}")
    print(f"  {'-'*12} {'-'*18} {'-'*10}")
    for row in get_memberships(conn):
        print(f"  {row['StudentName']:<12} {row['ClubName']:<18} {row['JoinDate']}")

    conn.close()
