import sys
from PyQt5.QtWidgets import QMainWindow as main_window
import PyQt5.QtWidgets as Qt
from tabs_with_dialog import Ui_MainWindow
class Graph_app(main_window):
    def __init__(self):
        super(Graph_app,self).__init__()
        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        #self.ui.pushButton.clicked.connect(self.open_other_window)
        self.show()
    def init_UI(self):
        self.setWindowTitle("Редактор графа")
def main():
    app = Qt.QApplication(sys.argv)
    application = Graph_app()
    application.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
