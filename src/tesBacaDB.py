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
            repetition text
            )
            """)

cur.execute("""
            CREATE TABLE IF NOT EXISTS riwayat_latihan (
            history_id integer PRIMARY KEY AUTOINCREMENT,
            program_id integer,
            name text,
            title_program text,
            calories integer,
            date text
            tot_duration integer
            )
            """)

cur.execute("""
            INSERT INTO daftar_latihan 
                (exercise_id, title, description, goals, duration, repetition)
            VALUES 
                (001, 'Push Up', 'Push-ups are exercises to strengthen your arms and \nchest muscles. They are done by lying with your face \ntowards the floor and pushing with your hands to \nraise your body until your arms are straight.', '10 Repetition', '../img/push-up.png', 'https://www.youtube.com/watch?v=bTJIkQRsmaE', NULL),
                ("Sit Up", "Sit-ups are exercises that you do to strengthen your \nstomach muscles. They involve sitting up from a lying \nposition while keeping your legs straight on the floor.", "10 Repetition", "../img/sit-up.png", "https://www.youtube.com/watch?v=6eJVLbgxbBE", NULL),
                ("Pull Up", "A pull-up is an upper-body strength exercise. The \npull-up is a closed-chain movement where the body \nis suspended by the hands and pulls up.", "10 Repetition", "../img/pull-up.png", "https://www.youtube.com/watch?v=eGo4IYlbE5g", NULL),
                ("Jumping Rope", "Jumping rope is jumping over a rope held with \none end in each hand as the rope is repeatedly \nspun over the head and under the feet.", "20 Repetition", "../img/jumping-rope.png", "https://www.youtube.com/watch?v=FJmRQ5iTXKE", NULL),
                ("Weightlifting", "Weight training is a common type of strength training \nfor developing the strength and size of skeletal \nmuscles.", "70Kg", "../img/weightlifting.png", "https://www.youtube.com/watch?v=RP85w6g7jPU", NULL),
                ("Swimming", "The propulsion of the body through water by \ncombined arm and leg motions and the natural \nflotation of the body.", "300 meters", "../img/swimming.png", "https://www.youtube.com/watch?v=gh5mAtmeR3Y", NULL),
                ("Running", "Running is a form of exercise that is usually \ndone to develop the speed and endurance of the body.", "5Km", "../img/running.png", "https://www.youtube.com/watch?v=ZQQ6_XQQxQ4", NULL)
            """)
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

# a = cur.execute("Select * from list_olahraga")

# a = cur.fetchall()

# for i in a:
#     print(i)

