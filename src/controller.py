from PyQt6.QtWidgets import QApplication
import sys
from register import register
from dashboard import dashboard
from listLatihan import listLatihan
from tesBacaDB import tesBacaDB
class controller:
    def __init__(self):
        self.tesBacaDB = tesBacaDB()
        self.registerWin = register()
        self.registerWin.switch.connect(self.fromRegister)
        self.dashboard = dashboard()
        self.dashboard.switch.connect(self.fromDashboard)
        self.listLatihan = listLatihan()
        self.listLatihan.switch.connect(self.fromListLatihan)
        pass

    def start(self):
        # nanti disini kasih validasi dulu, user udah ada apa belum
        self.registerWin.show()

    def fromRegister(self):
        self.registerWin.close()
        self.dashboard.show()

    def fromDashboard(self, page):
        self.registerWin.close()
        if (page == "listLatihan"):
            self.listLatihan.show()

    def fromListLatihan(self, page):
        self.listLatihan.close()
        if (page == "dashboard"):
            self.dashboard.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = controller()
    controller.start()
    app.exec()
