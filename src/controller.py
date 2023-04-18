from PyQt6.QtWidgets import QApplication
import sys
import sqlite3
from register import register
from dashboard import dashboard
from listlatihan2 import listLatihan2
from customize import customizeWorkout
from plan import plan
from plan2 import plan2
from endOfExercise import endOfExe
import os 
import os.path
class controller:
    def __init__(self):
        self.initDatabase()
        self.conn = sqlite3.connect('fitu.db')
        self.registerWin = register()
        self.registerWin.switch.connect(self.fromRegister)
        self.dashboard = dashboard()
        self.dashboard.switch.connect(self.fromDashboard)
        self.listLatihan = listLatihan2()
        self.listLatihan.switch.connect(self.fromListLatihan)
        self.customize = customizeWorkout(0)
        self.customize.switch.connect(self.fromCustomize)
        self.plan = plan()
        self.plan.switch.connect(self.fromPlan)
        self.plan2 = plan2(1)
        self.plan.switch.connect(self.toPlan2)
        self.endOfExe = endOfExe()
        self.endOfExe.switch.connect(self.toEndOfExe)
        self.endOfExe.switch.connect(self.fromEndOfExe)
        pass

        
    def start(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM user")
        count = c.fetchone()
        if (count != None):
            # print("dashboard")
            self.dashboard.show()        
        else:
            self.registerWin.show()

    def fromRegister(self):
        self.registerWin.close()
        self.dashboard = dashboard()
        self.dashboard.switch.connect(self.fromDashboard)
        self.dashboard.show()

    def fromDashboard(self, page, program_id):
        self.registerWin.close()
        self.dashboard.close()
        if (page == "listLatihan"):
            self.listLatihan.show()
        elif (page == "customize"):
            self.customize.show()
        elif (page == "plan"):
            self.plan.show()


    def fromListLatihan(self, page, program_id):
        self.listLatihan.close()
        if (page == "dashboard"):
            self.dashboard.show()
        elif (page == "customize"):
            self.customize.show()
        elif (page == "plan"):
            self.plan.show()

    def fromPlan(self, page, program_id):
        self.plan.close()
        if (page == "dashboard"):
            self.dashboard.show()
        elif (page == "customize"):
            self.customize = customizeWorkout(program_id)
            self.customize.switch.connect(self.fromCustomize)
            self.customize.show()
        elif (page == "listLatihan"):
            self.listLatihan.show()
        elif (page == "plan2"):
            self.plan2 = plan2(program_id)
            self.plan2.switch.connect(self.toEndOfExe)
            self.plan2.show()

    def fromCustomize(self, page, program_id):
        self.customize.close()
        if (page == "dashboard"):
            self.dashboard.show()
        elif (page == "listLatihan"):
            self.listLatihan.show()
        elif (page == "plan"):
            self.plan = plan()
            self.plan.switch.connect(self.fromPlan)
            self.plan.show()

    def toPlan2(self, page, program_id):
        self.plan.close()
        if (page == "plan2"):
            print("ctrl" + str(program_id))
            self.plan2 = plan2(program_id)
            self.plan2.switch.connect(self.toEndOfExe)
            self.plan2.show()

    def toEndOfExe(self,page):
        self.plan2.close()
        if (page == "endOfExe"):
            self.endOfExe.show()

    def fromEndOfExe(self,page):
        self.endOfExe.close()
        if (page == "dashboard"):
            self.dashboard = dashboard()
            self.dashboard.switch.connect(self.fromDashboard)
            self.dashboard.show()

    def initDatabase(self):
        if not os.path.exists("fitu.db"):
            self.con = sqlite3.connect("fitu.db")
            cur = self.con.cursor()

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
                        duration integer,
                        repetition integer,
                        gif text
                        )
                        """)

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS riwayat_latihan (
                        history_id integer,
                        program_id integer,
                        name text,
                        title_program text,
                        calories integer,
                        date text,
                        tot_duration integer,
                        FOREIGN KEY (program_id) REFERENCES program (program_id)
                        )
                        """)
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS program (
                        program_id integer PRIMARY KEY AUTOINCREMENT,
                        title_program text
                        )
                        """)

            cur.execute("""
                        CREATE TABLE IF NOT EXISTS latihan_program (
                        program_id integer,
                        exercise_id integer,
                        FOREIGN KEY (program_id) REFERENCES program (program_id)
                        )
                        """)

            cur.execute("""
                        INSERT or IGNORE INTO daftar_latihan 
                            (exercise_id, title, description, goals, duration, repetition, gif)
                        VALUES 
                            (101, "Hip Dip", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-hipdip.gif"),
                            (102, "Bear Crawl", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-bearcrawl.gif"),
                            (103, "Jumping Jacks", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-jumpingjack.gif"),
                            (104, "Plank", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-plank.gif"),
                            (105, "Bridge", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-bridges.gif"),
                            (106, "High Knees", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-highknee.gif"),
                            (107, "Mountain Climber", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL, "img/exe-mountain.gif"),
                            (108, "Russian Twist", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', 30, NULL,"img/exe-russian.gif"),
                            (201, 'Push Up', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor','Goals', NULL, 10, 'img/exe-pushup.gif'),
                            (202, "Sit Up", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-situp.gif"),
                            (203, "Toe Tap", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-toetap.gif"),
                            (204, "Shoulder Tap", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-shouldertap.gif"),
                            (205, "Lunges", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-lunges.gif"),
                            (206, "Crunches", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-crunches.gif"),
                            (207, "Burpees", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-burpees.gif"),
                            (208, "Bicycle Crunch", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ac venenatis purus. Nulla a fringilla ante. Aenean id ipsum pellentesque, convallis ex eget, cursus dolor", 'Goals', NULL, 10, "img/exe-bicycle.gif")
                        """)

            cur.execute("""
                        INSERT or IGNORE INTO program
                            (program_id, title_program)
                        VALUES
                            (1, 'Full Body Workout'),
                            (2, 'Upper Body Workout'),
                            (3, 'Lower Body Workout'),
                            (4, 'Core Workout')
                        """)

            cur.execute("""
                        INSERT or IGNORE INTO latihan_program
                            (program_id, exercise_id)
                        VALUES
                            (1, 201),
                            (1, 105),
                            (1, 106),
                            (1, 202),
                            (2, 104),
                            (2, 107),
                            (2, 108),
                            (2, 201),
                            (3, 202),
                            (3, 205),
                            (3, 106)
                        """)
            
            # cur.execute("""
            #         INSERT INTO riwayat_latihan
            #             (program_id, name, title_program, calories, date, tot_duration)
            #         VALUES
            #             (1, 'Push Up', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Sit Up', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Pull Up', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Squat Jump', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Lunges', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Crunches', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Burpees', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Bicycle Crunch', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Jumping Rope', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Running', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Jumping Jacks', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Plank', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Bridge', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'High Knees', 'Chest Day', 100, '2020-12-12', 30),
            #             (1, 'Squat', 'Chest Day', 100, '2020-12-12', 30),
            #             (2, 'Push Up', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Sit Up', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Pull Up', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Squat Jump', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Lunges', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Crunches', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Burpees', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Bicycle Crunch', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Jumping Rope', 'Leg Day', 100, '2020-12-15', 30),
            #             (2, 'Running', 'Leg Day', 100, '2020-12-15', 30)
            #         """)

            self.con.commit()
            self.con.close()
        else:
            print("Database already exists")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = controller()
    controller.start()
    app.exec()
