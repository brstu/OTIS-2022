
from pyvis.network import Network as net
import networkx as nx
from networkx.algorithms import tournament,euler,is_tree,is_planar,is_connected

from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout,QColorDialog

import pickle

from pop_with_one_input import Ui_Dialog
from pop_with_two_input import Ui_Dialog_two
from pop_with_three_input import Ui_Dialog_three

from test_ui import ui_text_browser
from text_info_editor import text_edi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1346, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, -10, 161, 41))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(630, 20, 162, 138))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_9.setStyleSheet("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_4.addWidget(self.checkBox_9, 0, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_7.setStyleSheet("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_4.addWidget(self.checkBox_7, 4, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_8.setStyleSheet("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_4.addWidget(self.checkBox_8, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 0, 161, 41))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 30, 178, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 290, 1231, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.changing_node_name = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changing_node_name.setObjectName("changing_node_name")
        self.verticalLayout.addWidget(self.changing_node_name)
        self.remove_node = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_node.setObjectName("remove_node")
        self.verticalLayout.addWidget(self.remove_node)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(210, 0, 191, 111))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.remove_edge = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.remove_edge.setObjectName("remove_edge")
        self.verticalLayout_3.addWidget(self.remove_edge)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1040, 30, 181, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(820, 20, 201, 80))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.add_tab = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.add_tab.setObjectName("add_tab")
        self.verticalLayout_6.addWidget(self.add_tab)
        self.remove_tab = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.remove_tab.setObjectName("remove_tab")
        self.verticalLayout_6.addWidget(self.remove_tab)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 130, 250, 151))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_7.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_7.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_7.addWidget(self.pushButton_8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1346, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.alghoritms = QtWidgets.QMenu(self.menubar)
        self.alghoritms.setObjectName("alghoritms")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(MainWindow)
        self.action_12.setObjectName("action_12")
        self.action_13 = QtWidgets.QAction(MainWindow)
        self.action_13.setObjectName("action_13")
        self.action_14 = QtWidgets.QAction(MainWindow)
        self.action_14.setObjectName("action_14")
        self.action_15 = QtWidgets.QAction(MainWindow)
        self.action_15.setObjectName("action_15")
        self.action_16 = QtWidgets.QAction(MainWindow)
        self.action_16.setObjectName("action_16")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtWidgets.QAction(MainWindow)
        self.action_18.setObjectName("action_18")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.alghoritms.addAction(self.action_9)
        self.alghoritms.addAction(self.action_10)
        self.alghoritms.addAction(self.action_11)
        self.alghoritms.addAction(self.action_18)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_12)
        self.menu_2.addAction(self.action_17)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.alghoritms.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.color = "red"
        self.graphs = []
        self.htmls = []
        self.graphs_name=[]
        self.flags = [0]
        self.add_tab.clicked.connect(self.adding_tab)
        self.remove_tab.clicked.connect(self.removing_tab)
        self.checkBox_5.setChecked(True)
        self.checkBox_7.setChecked(True)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.pushButton.clicked.connect(self.create_node_window)
        self.changing_node_name.clicked.connect(self.create_rename_window)
        self.pushButton_2.clicked.connect(self.create_add_edge_window)
        self.pushButton_3.clicked.connect(self.get_color)
        self.remove_node.clicked.connect(self.create_rmnode_window)
        self.remove_edge.clicked.connect(self.create_remove_edge_window)

        self.pushButton_4.clicked.connect(self.print_node_info)
        self.pushButton_5.clicked.connect(self.create_node_info)
        self.pushButton_6.clicked.connect(self.delete_node_info)
        self.pushButton_7.clicked.connect(self.edit_node_info)
        self.pushButton_8.clicked.connect(self.create_searching_window)

        self.action.triggered.connect(self.export_in_interior_format)
        self.action_2.triggered.connect(self.edge_and_node_amount)
        self.action_3.triggered.connect(self.node_degress)
        self.action_4.triggered.connect(self.adj_matrix)
        self.action_5.triggered.connect(self.incidence_matrix)
        self.action_6.triggered.connect(self.create_import_interior_format)
        self.action_7.triggered.connect(self.export_txt)
        self.action_8.triggered.connect(self.create_import_txt_window)
        self.action_9.triggered.connect(self.create_findpath_window)
        self.action_10.triggered.connect(self.create_find_shortestspaths_window)
        self.action_11.triggered.connect(self.create_lenght_path_window)
        self.action_12.triggered.connect(self.graph_radius_diametr_center)
        self.action_17.triggered.connect(self.type_of_graph)
        self.action_18.triggered.connect(self.find_cycles)
        self.retranslateUi(MainWindow)
        # self.lineEdit.setPlaceholderText("Введите вершину для добавления")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_color(self):
        self.Dialog = QColorDialog()
        self.color = self.Dialog.getColor().name()

    def create_oneline_window(self, text, placeholder_text):
        self.Dialog = Ui_Dialog()
        self.Dialog.setupUi(self.Dialog)
        self.Dialog.label.setText(text)
        self.Dialog.lineEdit.setPlaceholderText(placeholder_text)
        self.Dialog.label.adjustSize()

    def create_twoline_window(self, text):
        self.Dialog = Ui_Dialog_two()
        self.Dialog.setupUi(self.Dialog)
        self.Dialog.label.setText(text)
        self.Dialog.label.adjustSize()

    def create_threeline_window(self, text):
        self.Dialog = Ui_Dialog_three()
        self.Dialog.setupUi(self.Dialog)
        self.Dialog.label.setText(text)
        self.Dialog.label.adjustSize()

    def create_info_window(self, text):
        self.Dialog = ui_text_browser()
        self.Dialog.setupUi(self.Dialog)
        self.Dialog.textBrowser.setText(text)
        self.Dialog.show()
        self.Dialog.exec_()

    def create_text_editor(self, text1, text2):
        self.Dialog = text_edi()
        self.Dialog.setupUi(self.Dialog)
        self.Dialog.textEdit.setPlainText(text1)
        self.Dialog.textEdit_2.setPlainText(text2)
        self.Dialog.show()
        self.Dialog.exec_()

    def edge_and_node_amount(self):
        try:
            nodes = self.graphs[self.tabWidget.currentIndex()].nodes
            edges = self.graphs[self.tabWidget.currentIndex()].edges
            res = f"Граф имеет {len(nodes)} вершин(ы) и {len(edges)} ребёр(а)"
            self.print_message("Информация о графе", res)
        except IndexError:
            self.print_error("Сначала создайте граф")
    @staticmethod
    def print_message(name, text):
        message = QMessageBox()
        message.setWindowTitle(name)
        message.setText(text)
        message.exec()

    def node_degress(self):
        try:
            res = ''
            for node, degree in self.graphs[self.tabWidget.currentIndex()].degree:
                res += f"Вершина {node} --- cтепень {degree} \n"
            self.print_message("Степени вершин", res)
        except IndexError:
            self.print_error("Сначала создайте граф")

    def graph_radius_diametr_center(self):
        radius, diametr, centre = 0, 0, 0
        error = 0
        if len(self.graphs[self.tabWidget.currentIndex()].nodes) == 0:
            self.print_error("В графе нет ни одной верщины ")
        else:
            try:
                radius = nx.radius(self.graphs[self.tabWidget.currentIndex()])
            except nx.NetworkXError:
                self.print_error("Радиус графа равен 0 , так как ориентированный граф должен быть сильно связным,")
            except IndexError:
                self.print_error("Сначала создайте граф")
                error += 1
            try:
                diametr = nx.diameter(self.graphs[self.tabWidget.currentIndex()])
                centre = nx.center(self.graphs[self.tabWidget.currentIndex()])
            except IndexError:
                if error != 1:
                    self.print_error("Сначала создайте граф")
            except Exception:
                pass
        res = f"Граф имеет радиус {radius}, диаметр {diametr} и центр в вершине {centre} "
        self.create_info_window(res)

    def create_node_info(self):
        self.create_threeline_window("Введите номер вершины")
        self.Dialog.buttonBox.accepted.connect(self.creating_node_info)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def creating_node_info(self):
        try:
            if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()):
                node = self.Dialog.lineEdit.text()
                self.graphs[self.tabWidget.currentIndex()].nodes[node]['info'] = self.Dialog.lineEdit_2.text()
                self.graphs[self.tabWidget.currentIndex()].nodes[node]['ref'] = self.Dialog.lineEdit_3.text()
            else:
                self.print_error(f"Граф не содержит вершины с номером {self.Dialog.lineEdit.text()}")
        except IndexError:
            self.print_error("Сначала создайте граф")

    def print_node_info(self):
        try:
            result = ""
            for i in self.graphs[self.tabWidget.currentIndex()].nodes.data():
                value = i[1]["info"]
                ref = i[1]["ref"]
                temp = f"Вершина {i[0]} содержит {value} и ссылку {ref}\n"
                result += temp
            self.create_info_window(result)
        except IndexError:
            self.print_error("Сначала создайте граф")

    def delete_node_info(self):
        self.create_oneline_window("Введите вершину для удаления содержимого", "Введите номер вершины")
        self.Dialog.buttonBox.accepted.connect(self.Dialog.close)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()
        try:
            if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()):
                node = self.Dialog.lineEdit.text()
                self.graphs[self.tabWidget.currentIndex()].nodes[node]['info'] = ""
                self.graphs[self.tabWidget.currentIndex()].nodes[node]['ref'] = ""
            else:
                self.print_error(f"Граф не содержит вершины с номером {self.Dialog.lineEdit.text()}")
        except:
            pass

    def edit_node_info(self):
        self.create_oneline_window("Введите вершину для редактирования содержимого", "Введите номер вершины")
        self.Dialog.buttonBox.accepted.connect(self.edit_info)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def edit_info(self):
        try:
            if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()):
                node = self.Dialog.lineEdit.text()
                self.create_text_editor(self.graphs[self.tabWidget.currentIndex()].nodes[node]['info'],
                                        self.graphs[self.tabWidget.currentIndex()].nodes[node]['ref'])
                self.graphs[self.tabWidget.currentIndex()].nodes[node]['info'] = self.Dialog.textEdit.toPlainText()
                self.graphs[self.tabWidget.currentIndex()].nodes[node]['ref'] = self.Dialog.textEdit2.toPlainText()

            else:
                self.print_error(f"Граф не содержит вершины с номером {self.Dialog.lineEdit.text()}")
        except:
            pass

    def adj_matrix(self):
        try:
            res = ''
            for i in nx.to_numpy_matrix(self.graphs[self.tabWidget.currentIndex()]):
                res += str(i)[1:-1:] + "\n"
            self.print_message("Матрица смежности", res)
        except IndexError:
            self.print_error("Сначала создайте граф")

    def incidence_matrix(self):
        try:
            res = str(nx.incidence_matrix(self.graphs[self.tabWidget.currentIndex()], oriented=self.graphs[
                self.tabWidget.currentIndex()].is_directed()).todense())
            self.print_message("Матрица инцидентности", res)
        except IndexError:
            self.print_error("Сначала создайте граф")

    def create_graph(self):
        if self.checkBox_4.isChecked() is True:
            graph = nx.Graph()
            if self.tabWidget.currentIndex() < len(self.flags):
                self.flags[self.tabWidget.currentIndex()] = 0
            else:
                self.flags.append(0)
        elif self.checkBox_5.isChecked() is True:
            graph = nx.DiGraph()
            if self.tabWidget.currentIndex() < len(self.flags):
                self.flags[self.tabWidget.currentIndex()] = 1
            else:
                self.flags.append(1)
        return graph

    def check_shape_box(self):
        shape = "dot"
        if self.checkBox_9.isChecked() is True:
            shape = "dot"
        elif self.checkBox_7.isChecked() is True:
            shape = "triangle"
        elif self.checkBox_8.isChecked() is True:
            shape = "star"
        return shape
    @staticmethod
    def print_error(text):
        error = QMessageBox()
        error.setText(text)
        error.setWindowTitle("Ошибка")
        error.setIcon(QMessageBox.Warning)
        error.exec()

    def updating_graph(self):
        vis = net(directed=self.flags[self.tabWidget.currentIndex() - 1])
        vis.from_nx(self.graphs[self.tabWidget.currentIndex()])
        # self.vis.show_buttons(['physics'])
        if self.tabWidget.currentIndex() < len(self.htmls):
            self.htmls[self.tabWidget.currentIndex()] = vis.generate_html()
        else:
            self.htmls.append(vis.generate_html())
        self.add_web()

    def add_web(self):
        web = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.tabWidget.widget(self.tabWidget.currentIndex()).layout().removeItem(
            self.tabWidget.widget(self.tabWidget.currentIndex()).layout().itemAt(0))
        web.setHtml(self.htmls[self.tabWidget.currentIndex()])
        self.tabWidget.widget(self.tabWidget.currentIndex()).layout().addWidget(web)

    def create_node_window(self):
        self.create_oneline_window(" Введите номер cоздаваемой вершины ", "Введите номер вершины")
        self.Dialog.buttonBox.accepted.connect(self.ad_node)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def ad_node(self):
        try:
            if not self.Dialog.lineEdit.text():
                self.print_error("Не задано значение вершины")
            else:
                if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()) == False:
                    self.graphs[self.tabWidget.currentIndex()].add_node(self.Dialog.lineEdit.text(),
                                                                        color=self.color,
                                                                        shape=self.check_shape_box(), info="", ref="")
                    self.updating_graph()
                else:
                    self.print_error("Такая вершина уже существует")
        except IndexError:
            self.print_error("Сначала создайте граф")

    def create_rmnode_window(self):
        self.create_oneline_window("Введите номер удаляемой вершины", "Введите номер вершины")
        self.Dialog.buttonBox.accepted.connect(self.rm_node)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def rm_node(self):
        try:
            if not self.Dialog.lineEdit.text():
                pass
            else:
                if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()) == True:
                    self.graphs[self.tabWidget.currentIndex()].remove_node(self.Dialog.lineEdit.text())
                    self.updating_graph()
                elif self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()) == False:
                    self.print_error("Такой вершины не существует")
                else:
                    pass
        except IndexError:
            self.print_error("Сначала создайте граф")

    def create_rename_window(self):
        self.create_twoline_window("Введите название вершины")
        self.Dialog.buttonBox.accepted.connect(self.rename_node)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def rename_node(self):
        try:
            if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()):
                mapping = {self.Dialog.lineEdit.text(): self.Dialog.lineEdit_2.text()}
                self.graphs[self.tabWidget.currentIndex()] = nx.relabel_nodes(
                    self.graphs[self.tabWidget.currentIndex()], mapping=mapping)
                self.updating_graph()
            else:
                self.print_error("Вершины с таким именем нет")
        except IndexError:
            self.print_error("Сначала создайте граф")
        self.Dialog.close()

    def create_add_edge_window(self):
        self.create_twoline_window("Введите вершины")
        self.Dialog.buttonBox.accepted.connect(self.ad_edge)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def ad_edge(self):
        try:
            if self.graphs[self.tabWidget.currentIndex()].has_edge(self.Dialog.lineEdit.text(),
                                                                   self.Dialog.lineEdit_2.text()) is False:
                if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()) is True:
                    if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit_2.text()) is True:
                        self.graphs[self.tabWidget.currentIndex()].add_edge(self.Dialog.lineEdit.text(),
                                                                            self.Dialog.lineEdit_2.text(),
                                                                            color=self.color)
                        self.updating_graph()
                    else:

                        self.print_error("Вершины два не существует ")
                else:
                    self.print_error("Вершины один не существует")
            else:
                self.print_error("Такое ребро уже существует")
        except Exception:
            self.print_error("Сначала создайте граф")
        self.Dialog.close()

    def create_remove_edge_window(self):
        self.create_twoline_window("Введите название удаляемой вершины")
        self.Dialog.buttonBox.accepted.connect(self.rm_edge)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def rm_edge(self):
        try:
            if self.graphs[self.tabWidget.currentIndex()].has_edge(self.Dialog.lineEdit.text(),
                                                                   self.Dialog.lineEdit_2.text()) is True:
                if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit.text()) is True:
                    if self.graphs[self.tabWidget.currentIndex()].has_node(self.Dialog.lineEdit_2.text()) is True:
                        self.graphs[self.tabWidget.currentIndex()].remove_edge(self.Dialog.lineEdit.text(),
                                                                               self.Dialog.lineEdit_2.text())
                        self.updating_graph()
                    else:

                        self.print_error("Вершины два не существует ")
                else:
                    self.print_error("Вершины один не существует")
            else:
                self.print_error("Такое ребро не существует")
            self.Dialog.close()
        except IndexError:
            self.print_error("Сначала создайте граф ")

    def adding_tab(self):
        self.create_oneline_window("Имя графа", "Введите имя графа")
        self.Dialog.buttonBox.accepted.connect(self.ad_tab)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def ad_tab(self):
        tab_3 = QtWidgets.QWidget()
        tab_3.setObjectName("tab_3")
        layout = QVBoxLayout()
        tab_3.setLayout(layout)
        graph = self.create_graph()
        self.graphs.append(graph)

        self.tabWidget.addTab(tab_3, self.Dialog.lineEdit.text())
        self.graphs_name.append(self.Dialog.lineEdit.text())

    def removing_tab(self):
        try:
            self.graphs.remove(self.graphs[self.tabWidget.currentIndex()])
            self.htmls.remove(self.htmls[self.tabWidget.currentIndex()])
            self.tabWidget.removeTab(self.tabWidget.currentIndex())
        except Exception:
            self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def create_findpath_window(self):
        self.create_twoline_window("Введите вершины")
        self.Dialog.buttonBox.accepted.connect(self.find_all_paths)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()

    def find_all_paths(self):
        first_node = self.Dialog.lineEdit.text()
        second_node = self.Dialog.lineEdit_2.text()
        paths = ''
        if self.graphs[self.tabWidget.currentIndex()].has_node(first_node) is True:
            if self.graphs[self.tabWidget.currentIndex()].has_node(second_node) is True:
                for i in nx.all_simple_paths(self.graphs[self.tabWidget.currentIndex()], first_node, second_node):
                    paths += str(i) + '\n'
                if len(paths) == 0:
                    self.print_error(f"Не существует пути между вершинами {first_node} и {second_node}")
                else:
                    self.print_message("Пути", paths)
            else:
                self.print_error(f"Вершины {second_node} не существует")
        else:
            self.print_error(f"Вершины {first_node} не существует ")

    def create_find_shortestspaths_window(self):
        self.create_twoline_window("Введите вершины")
        self.Dialog.buttonBox.accepted.connect(self.find_shortest_paths)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()
    def find_shortest_paths(self):
        first_node=self.Dialog.lineEdit.text()
        second_node=self.Dialog.lineEdit_2.text()
        paths=''
        if self.graphs[self.tabWidget.currentIndex()].has_node(first_node) is True:
            if self.graphs[self.tabWidget.currentIndex()].has_node(second_node) is True:
                try:
                    for i in nx.all_shortest_paths(self.graphs[self.tabWidget.currentIndex()], first_node,
                                                         second_node):
                        paths += str(i) + '\n'
                        self.print_message("Кратчайшие пути", paths)
                except nx.NetworkXNoPath:
                    self.print_error(f"Не существует пути между вершинами {first_node} и {second_node}")
            else:
                self.print_error(f"Вершины {second_node} не существует")
        else:
            self.print_error(f"Вершины {first_node} не существует ")


    def create_lenght_path_window(self):
        self.create_twoline_window("Введите вершины")
        self.Dialog.buttonBox.accepted.connect(self.find_length)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()
    def find_length(self):
        first_node=self.Dialog.lineEdit.text()
        second_node=self.Dialog.lineEdit_2.text()
        if self.graphs[self.tabWidget.currentIndex()].has_node(first_node) is True:
            if self.graphs[self.tabWidget.currentIndex()].has_node(second_node) is True:
                try:
                    length = nx.shortest_path_length(self.graphs[self.tabWidget.currentIndex()], first_node,
                                                           second_node)
                    self.print_message("Длина пути", str(length))
                except:
                    self.print_error(f"Не существует пути между вершинами {first_node} и {second_node}")
            else:
                self.print_error(f"Вершины {second_node} не существует")
        else:
            self.print_error(f"Вершины {first_node} не существует ")
    def find_cycles(self):
        if not self.graphs:
            self.print_error("Сначала создайте граф")
        else:
            try:
                hamiltonian_cycle=tournament.hamiltonian_path(self.graphs[self.tabWidget.currentIndex()])
                if not hamiltonian_cycle:
                    hamiltonian_cycle=None
            except:
                hamiltonian_cycle=None
            try:
                euler_cycle=list(euler.eulerian_path(self.graphs[self.tabWidget.currentIndex()]))
                if not euler_cycle:
                    euler_cycle=None
            except:
                euler_cycle=None
            text=f"Гамильтонов цикл {hamiltonian_cycle}\n Элейров цикл {euler_cycle}"
            self.print_message("Циклы",text)
    def type_of_graph(self):
        istree=None
        iscomplete=None
        isconnected=None
        iseulerian=None
        isplanar=None

        def is_complete_graph(G):
            N = len(G) - 1
            return not any(n in nbrdict or len(nbrdict) != N for n, nbrdict in G.adj.items())
        try:
            istree=is_tree(self.graphs[self.tabWidget.currentIndex()])
            iscomplete=is_complete_graph(self.graphs[self.tabWidget.currentIndex()])
            try:
                isconnected=is_connected(self.graphs[self.tabWidget.currentIndex()])
            except :
                isconnected=False
            iseulerian=euler.is_eulerian(self.graphs[self.tabWidget.currentIndex()])
            isplanar=is_planar(self.graphs[self.tabWidget.currentIndex()])
        except IndexError:
            self.print_error("Сначала создайте граф")
        result=f"Граф является деревом {istree}\n Граф является полным {iscomplete}\n Граф является связанным {isconnected}\n" \
               f"Граф является эйлерловым {iseulerian}\n Граф является планарным {isplanar}"
        self.print_message("Тип графа",result)

    def create_searching_window(self):
        self.create_twoline_window("Содержимое")
        self.Dialog.buttonBox.accepted.connect(self.search)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()
    def search(self):
        info_searching = self.Dialog.lineEdit.text()
        ref_searching= self.Dialog.lineEdit_2.text()
        info_node=None
        ref_node=None
        for i in self.graphs:
            for j in range(len(i)):
                if i.nodes[j]['info']==info_searching:
                    info_node=j
                elif i.nodes[j]['ref']==ref_searching:
                    ref_node=j
        result=f"Вершина с найденным текстом {info_node}\n" \
               f"Вершина с найденной ссылкой {ref_node}"
        if not result:
            self.print_error("Вершины с таким содержимым не существует")
        else:
            self.print_message("Поиск по содержимому ",result)

    def create_import_txt_window(self):
        self.create_oneline_window("Введите путь","Путь к файлу")
        self.Dialog.buttonBox.accepted.connect(self.import_txt)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()
    def import_txt(self):
        with open(self.Dialog.lineEdit.text(),"r") as file:
            data=file.read().split(";")
        tab_3 = QtWidgets.QWidget()
        tab_3.setObjectName("tab_3")
        layout = QVBoxLayout()
        tab_3.setLayout(layout)
        graph=None
        directed=False
        if data[0][data[0].find(":")+1::]=="UNORIENT":
            graph=nx.Graph()
        elif data[0][data[0].find(":")+1::]=="ORIENT":
            graph=nx.DiGraph()
            directed=True
        self.graphs.append(graph)
        self.flags.append(directed)
        for i in data[1].split(","):
            graph.add_node(i)
        for i in data[2].split(","):
            graph.add_edge(i[0], i[-1])
        self.tabWidget.addTab(tab_3, self.Dialog.lineEdit.text())
        self.updating_graph()
    def export_txt(self):
        directed=False
        if self.flags[self.tabWidget.currentIndex()]==1:
            directed="ORIENT"
        elif self.flags[self.tabWidget.currentIndex()]==0:
            directed="UNORIENT"
        nodes=[str(i) for i in self.graphs[self.tabWidget.currentIndex()].nodes]
        edges=[f"{str(i[0])}->{str(i[1])}" for i in self.graphs[self.tabWidget.currentIndex()].edges]
        result=f"{self.graphs_name[self.tabWidget.currentIndex()]}:{directed};{','.join(nodes)};{','.join(edges)}"
        with open(f"{self.graphs_name[self.tabWidget.currentIndex()]}.txt","w") as file:
            file.write(result)

    def export_in_interior_format(self):
        with open(f"{self.graphs_name[self.tabWidget.currentIndex()]}.pkl","wb") as file:
            pickle.dump(self.graphs[self.tabWidget.currentIndex()],file)
    def create_import_interior_format(self):
        self.create_oneline_window("Введите путь","Путь к файлу")
        self.Dialog.buttonBox.accepted.connect(self.import_in_interior_format)  # type: ignore
        self.Dialog.buttonBox.rejected.connect(self.Dialog.close)
        self.Dialog.show()
        self.Dialog.exec_()
    def import_in_interior_format(self):
        with open(f"{self.Dialog.lineEdit.text()}","rb") as file:
            graph=pickle.load(file)
        self.graphs.append(graph)
        tab_3 = QtWidgets.QWidget()
        tab_3.setObjectName("tab_3")
        layout = QVBoxLayout()
        tab_3.setLayout(layout)

        self.tabWidget.addTab(tab_3, self.Dialog.lineEdit.text())
        self.updating_graph()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Форма"))
        self.checkBox_9.setText(_translate("MainWindow", "Круг"))
        self.checkBox_7.setText(_translate("MainWindow", "Треугольник"))
        self.checkBox_8.setText(_translate("MainWindow", "Звезда"))
        self.label_3.setText(_translate("MainWindow", "Вид графа"))
        self.checkBox_5.setText(_translate("MainWindow", "Ориентированный"))
        self.checkBox_4.setText(_translate("MainWindow", "Неориентированный"))
        self.pushButton.setText(_translate("MainWindow", "Cоздать вершину"))
        self.changing_node_name.setText(_translate("MainWindow", "Переименовать вершину"))
        self.remove_node.setText(_translate("MainWindow", "Удалить вершину"))
        self.pushButton_2.setText(_translate("MainWindow", "Cоздать ребро"))
        self.remove_edge.setText(_translate("MainWindow", "Удалить ребро"))
        self.pushButton_3.setText(_translate("MainWindow", "Выбрать цвет"))
        self.add_tab.setText(_translate("MainWindow", "Создать граф"))
        self.remove_tab.setText(_translate("MainWindow", "Удалить граф"))
        self.pushButton_5.setText(_translate("MainWindow", "Добавить содержимое узла"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить содержимое узла"))
        self.pushButton_7.setText(_translate("MainWindow", "Редактировать содержимое узла"))
        self.pushButton_4.setText(_translate("MainWindow", "Просмотреть содержимое узла"))
        self.pushButton_8.setText(_translate("MainWindow", "Поиск вершины по содержимому"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.alghoritms.setTitle(_translate("MainWindow", "Алгоритмы"))
        self.menu_2.setTitle(_translate("MainWindow", "Свойства графа"))
        self.action.setText(_translate("MainWindow", "Сохранить граф во внутреннем формате программы"))
        self.action_2.setText(_translate("MainWindow", "Количество всех вершин"))
        self.action_3.setText(_translate("MainWindow", "Количество всех дуг"))
        self.action_4.setText(_translate("MainWindow", "Матрица смежности"))
        self.action_5.setText(_translate("MainWindow", "Матрица инцидентности"))
        self.action_6.setText(_translate("MainWindow", "Загрузить граф из внутрненнего формата программы"))
        self.action_7.setText(_translate("MainWindow", "Сохранить граф в текстовый формат"))
        self.action_8.setText(_translate("MainWindow", "Загрузить граф из текстового формата"))
        self.action_9.setText(_translate("MainWindow", "Поиск всех путей между двумя узлами"))
        self.action_10.setText(_translate("MainWindow", "Поиск кратчайшего пути между двумя узлами"))
        self.action_11.setText(_translate("MainWindow", "Вычисление расстрояния между двумя узлами"))
        self.action_12.setText(_translate("MainWindow", "Радиус , диаметр, центр графа"))
        self.action_13.setText(_translate("MainWindow", "Радиус графа"))
        self.action_14.setText(_translate("MainWindow", "Центра графа"))
        self.action_15.setText(_translate("MainWindow", "Просмотр содержимого вершин"))
        self.action_16.setText(_translate("MainWindow", "деревом, полным, связанным, эйлеровым,планарным"))
        self.action_17.setText(_translate("MainWindow", "Вид графа"))
        self.action_18.setText(_translate("MainWindow", "Нахождение эйлеровых,гамильтоновых циклов"))
