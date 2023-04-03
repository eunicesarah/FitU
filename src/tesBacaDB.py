import sqlite3

con = sqlite3.connect("fitu.db")
cur = con.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS user (
            name text PRIMARY KEY,
            height integer,
            weight integer,
            goal text,
            gender text,
            age integer
            )
            """)
cur.execute("""
            CREATE TABLE IF NOT EXISTS daftar_latihan (
            exercise_id integer PRIMARY KEY,
            title text,
            description text,
            goals text,
            duration text,
            repetition integer,
            gif text
            )
            """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS riwayat_latihan (
            history_id integer PRIMARY KEY AUTOINCREMENT,
            program_id integer,
            name text,
            title_program text,
            calories integer,
            date text,
            tot_duration integer
            )
            """)

cur.execute("""
            INSERT INTO daftar_latihan 
                (exercise_id, title, description, goals, duration, repetition, gif)
            VALUES 
                (201, 'Push Up', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor','Goals', NULL, 10, '../img/push-up.gif'),
                (202, "Sit Up", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (203, "Pull Up", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (204, "Squat Jump", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (205, "Lunges", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (206, "Crunches", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (207, "Burpees", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (208, "Bicycle Crunch", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "../img/"),
                (101, "Jumping Rope", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (102, "Running", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (103, "Jumping Jacks", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (104, "Plank", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (105, "Bridge", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (106, "High Knees", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (107, "Squat", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "../img/"),
                (108, "Russian Twist", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL,"../img/")
            """)

con.commit()
# cur.execute("""
#             INSERT INTO daftar_request
#                 (user_id, trainer_id, umur, jenis_kelamin, berat_badan, tinggi_badan, tujuan, status, title, description)
#             VALUES
#                 (1, 2, 20, 'Laki-laki', 65, 170, 'I want to have a sixpack stomach', True, 'Chest Day', 'This workout plan is made to strengthen your \nabdominal muscles.'),
#                 (1,2,20, 'Laki-laki', 65, 170, 'I want to have a strong leg muscles', True, 'Leg Day', 'This workout plan is made to strengthen your \nleg muscles.')
#             """)
# cur.execute("""
#             INSERT INTO workout
#                 (request_id, olahraga_id, status)
#             VALUES
#                 (1, 2, False),
#                 (1, 3, False),
#                 (1, 6, False),
#                 (2, 4, False),
#                 (2, 7, False)
#             """)


# daftarLatihan = cur.execute("SELECT * FROM daftar_latihan")
# daftarLatihan = daftarLatihan.fetchall()

# for i in daftarLatihan:
#     print(i)