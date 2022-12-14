import sys
from tabs_with_dialog import *
class Graph_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(Graph_app,self).__init__()
        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.show()
    def init_UI(self):
        self.setWindowTitle("Редактор графа")
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = Graph_app()
    application.show()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
