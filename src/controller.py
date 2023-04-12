from PyQt6.QtWidgets import QApplication
import sys
import sqlite3
from register import register
from dashboard import dashboard
from listlatihan2 import listLatihan2
from tesBacaDB import tesBaca
class controller:
    def __init__(self):
        self.conn = sqlite3.connect('fitu.db')
        self.tesBacaDB = tesBaca()
        self.registerWin = register()
        self.registerWin.switch.connect(self.fromRegister)
        self.dashboard = dashboard()
        # self.dashboard.switch.connect(self.fromDashboard)
        # self.listLatihan = listLatihan2()
        # self.listLatihan.switch.connect(self.fromListLatihan)
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

    # def fromDashboard(self, page):
    #     self.registerWin.close()
    #     if (page == "listLatihan"):
    #         self.listLatihan.show()

    # def fromListLatihan(self, page):
    #     self.listLatihan.close()
    #     if (page == "dashboard"):
    #         self.dashboard.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = controller()
    controller.start()
    app.exec()
