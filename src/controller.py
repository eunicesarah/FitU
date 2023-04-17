from PyQt6.QtWidgets import QApplication
import sys
import sqlite3
from register import register
from dashboard import dashboard
from listlatihan2 import listLatihan2
from tesBacaDB import tesBaca
from customize import customizeWorkout
from plan import plan
class controller:
    def __init__(self):
        self.conn = sqlite3.connect('fitu.db')
        self.tesBacaDB = tesBaca()
        self.registerWin = register()
        self.registerWin.switch.connect(self.fromRegister)
        self.dashboard = dashboard()
        self.dashboard.switch.connect(self.fromDashboard)
        self.listLatihan = listLatihan2()
        self.listLatihan.switch.connect(self.fromListLatihan)
        self.customize = customizeWorkout()
        self.customize.switch.connect(self.fromCustomize)
        self.plan = plan()
        # self.plan.switch.connect(self.fromPlan)
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
        self.dashboard.show()

    def fromDashboard(self, page):
        self.registerWin.close()
        self.dashboard.close()
        if (page == "listLatihan"):
            self.listLatihan.show()
        elif (page == "customize"):
            self.customize.show()
        elif (page == "plan"):
            self.plan.show()


    def fromListLatihan(self, page):
        self.listLatihan.close()
        if (page == "dashboard"):
            self.dashboard.show()
        elif (page == "customize"):
            self.customize.show()
        elif (page == "plan"):
            self.plan.show()

    def fromPlan(self, page):
        self.plan.close()
        if (page == "dashboard"):
            self.dashboard.show()
        elif (page == "customize"):
            self.customize.show()
        elif (page == "listLatihan"):
            self.listLatihan.show()

    def fromCustomize(self, page):
        self.customize.close()
        if (page == "dashboard"):
            self.dashboard.show()
        elif (page == "listLatihan"):
            self.listLatihan.show()
        elif (page == "plan"):
            self.plan.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = controller()
    controller.start()
    app.exec()
