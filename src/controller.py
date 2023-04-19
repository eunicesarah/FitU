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
        self.plan2.switch.connect(self.fromPlan2)
        # self.plan2.switch.connect(self.toDashboard)
        self.endOfExe = endOfExe()
        # self.endOfExe.switch.connect(self.toEndOfExe)
        self.endOfExe.switch.connect(self.fromEndOfExe)
        pass

        
    def start(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM user")
        count = c.fetchone()
        if (count != None):
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
            self.plan2.switch.connect(self.fromPlan2)
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


    def fromPlan2(self,page):
        self.plan2.close()
        if (page == "endOfExe"):
            self.endOfExe.show()
        elif (page == "plan"):
            self.plan.show()

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
                            (101, "Hip Dip", "The hip dip exercise is performed by placing your forearms on the ground with your elbows bent at a 90-degree angle, and then raising your hips off the ground, keeping your feet and forearms on the ground. This exercise targets the oblique muscles and helps to tone and strengthen them.", 'Thin, Fit', 30, NULL, "img/exe-hipdip.gif"),
                            (102, "Bear Crawl", "The bear crawl exercise is performed by getting into a push-up position and then crawling forward on your hands and feet, keeping your back flat and your core engaged. This exercise targets multiple muscle groups including the shoulders, chest, triceps, and core.", 'Thin, Fit', 30, NULL, "img/exe-bearcrawl.gif"),
                            (103, "Jumping Jacks", "Jumping jacks are a simple and effective exercise that involves jumping with your feet spread apart and your arms raised above your head, then returning to a standing position with your arms at your sides. This exercise is a great way to get your heart rate up and work on your cardiovascular fitness.", 'Thin, Fit', 30, NULL, "img/exe-jumpingjack.gif"),
                            (104, "Plank", "The plank is an isometric exercise that involves holding a push-up position for an extended period of time. This exercise targets the core and helps to improve stability and overall strength.", 'Thin, Fit', 30, NULL, "img/exe-plank.gif"),
                            (105, "Bridge", "The bridge exercise is performed by lying on your back with your knees bent and your feet flat on the ground. Then, you lift your hips up towards the ceiling, squeezing your glutes at the top of the movement. This exercise targets the glutes and helps to tone and strengthen them.", 'Thin, Fit', 30, NULL, "img/exe-bridges.gif"),
                            (106, "High Knees", "High knees are performed by running in place while lifting your knees up towards your chest as high as possible. This exercise targets the hip flexors and helps to improve speed, agility, and coordination.", 'Thin, Fit', 30, NULL, "img/exe-highknee.gif"),
                            (107, "Mt. Climber", "The mountain climber exercise is performed by getting into a push-up position and then bringing one knee up towards your chest, alternating legs in a running motion. This exercise targets the core and helps to improve cardiovascular fitness.", 'Thin, Fit', 30, NULL, "img/exe-mountain.gif"),
                            (108, "Russian Twist", "The Russian twist exercise is performed by sitting on the ground with your knees bent and your feet flat on the ground. Then, you lean back slightly and twist your torso from side to side, touching the ground with your hands on each side. This exercise targets the oblique muscles and helps to improve core strength.", 'Thin, Fit', 30, NULL,"img/exe-russian.gif"),
                            (201, 'Push Up', 'The push-up is a classic exercise that involves getting into a plank position with your hands placed slightly wider than shoulder-width apart. Then, you lower your body down towards the ground by bending your elbows and push back up to the starting position. This exercise targets multiple muscle groups including the chest, triceps, and shoulders.','Thin, Fit', NULL, 10, 'img/exe-pushup.gif'),
                            (202, "Sit Up", "The sit-up is performed by lying on your back with your knees bent and your feet flat on the ground. Then, you lift your upper body up towards your knees by contracting your abs. This exercise targets the abdominal muscles and helps to improve core strength.", 'Thin, Fit', NULL, 10, "img/exe-situp.gif"),
                            (203, "Toe Tap", "The toe tap exercise is performed by lying on your back with your legs extended towards the ceiling. Then, you lower one leg down towards the ground and tap your toe on the floor before raising it back up to the starting position. This exercise targets the lower abdominal muscles and helps to improve core strength.", 'Thin, Fit', NULL, 10, "img/exe-toetap.gif"),
                            (204, "Shoulder Tap", "The shoulder tap exercise is performed by getting into a push-up position and then tapping one hand to the opposite shoulder, alternating hands. This exercise targets the core and helps to improve stability and overall strength.", 'Thin, Fit', NULL, 10, "img/exe-shouldertap.gif"),
                            (205, "Lunges", "Lunges are performed by stepping forward with one foot and bending both knees, lowering your body towards the ground before returning to the starting position. This exercise targets the legs and helps to improve lower body strength.", 'Thin, Fit', NULL, 10, "img/exe-lunges.gif"),
                            (206, "Crunches", "Crunches are a classic abdominal exercise that target the rectus abdominis muscle (the six-pack muscles) and the obliques. To perform a crunch, lie on your back with your knees bent and feet flat on the ground. Place your hands behind your head or across your chest, and engage your core to lift your shoulders and upper back off the ground. Exhale as you crunch up, and inhale as you lower back down.", 'Thin, Fit', NULL, 10, "img/exe-crunches.gif"),
                            (207, "Burpees", "Burpees are a full-body exercise that incorporate cardio and strength training. To perform a burpee, start in a standing position, then drop down into a squat and place your hands on the ground. Jump or step your feet back into a plank position, then perform a push-up. Jump or step your feet back up to your hands, then explode up into a jump, reaching your arms overhead. That's one rep", 'Thin, Fit', NULL, 10, "img/exe-burpees.gif"),
                            (208, "Bicycle Crunch", "The bicycle crunch is a core exercise that targets the rectus abdominis and the obliques. To perform a bicycle crunch, lie on your back with your hands behind your head and your knees bent. Lift your shoulders off the ground and bring your right elbow towards your left knee, while straightening your right leg. Then, switch sides, bringing your left elbow towards your right knee, while straightening your left leg. Continue alternating sides in a pedaling motion.", 'Thin, Fit', NULL, 10, "img/exe-bicycle.gif")
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
            
            cur.execute("""
            CREATE TABLE IF NOT EXISTS quotes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT
            )""")

            cur.execute("""
            INSERT OR IGNORE INTO quotes 
                (quote)
            VALUES
                ('“Strength does not come from\nphysical capacity. It comes from\nan indomitable will.”\n-Mahatma Gandhi'),
                ('“Push harder than yesterday if you\nwant a different tomorrow.”\n- Unknown'),
                ('“Motivation is what gets you\nstarted. Habit is what keeps\nyou going.”\n-Jim Ryun'),
                ('“There are two types of pain in this\nworld: pain that hurts you, and pain\nthat changes you.”\n- Unknown'),
                ('“When you hit failure, your\nworkout has just begun.”\n-Ronnie Coleman'),
                ('“It never gets easier, you just\nget better.”\n-Unknown'),
                ('“Don’t limit your challenges.\nChallenge your limits.”\n-Jerry Dunn')


                """)

            self.con.commit()
            self.con.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = controller()
    controller.start()
    app.exec()
