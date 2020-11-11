import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel


class GUI:
    def __init__(self, book_service, client_service, rental_service):
        self._book_service = book_service
        self._client_service = client_service
        self._rental_service = rental_service

    def run(self):
        application = QApplication(sys.argv)
        main_menu = MainMenuWindow()
        main_menu.show()
        sys.exit(application.exec_())


class MainMenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Library')
        self.setFixedWidth(800)
        self.setFixedHeight(210)

        self.secondWindow = ManageEntitiesWindow()

        mainLayout = QVBoxLayout()
        self.setStyleSheet("""
            QLineEdit{height: 40px; font-size: 30px}
            QLabel{font-size: 30px}
            QPushButton{font-size: 30px}
        """)

        """self.name = QLineEdit()
        self.age = QLineEdit()
        mainLayout.addWidget(QLabel('Name:'))
        mainLayout.addWidget(self.name)
        mainLayout.addWidget(QLabel('Age:'))
        mainLayout.addWidget(self.age)"""

        self.ManageEntities = QPushButton('Manage Entities')
        self.ManageEntities.clicked.connect(self.open_manage_entities)

        self.ManageRentals = QPushButton('Manage Rentals')
        self.ManageRentals.clicked.connect(self.exit_application)

        self.ListEntities = QPushButton('List Entities')
        self.ListEntities.clicked.connect(self.exit_application)

        self.ExitApplication = QPushButton('Exit Application')
        self.ExitApplication.clicked.connect(self.exit_application)

        mainLayout.addWidget(self.ManageEntities)
        mainLayout.addWidget(self.ManageRentals)
        mainLayout.addWidget(self.ListEntities)
        mainLayout.addWidget(self.ExitApplication)

        self.setLayout(mainLayout)

    @staticmethod
    def exit_application():
        sys.exit()

    def open_manage_entities(self):
        self.secondWindow.displayInfo()
        self.close_main_menu()
        if self.secondWindow.isHidden():
            self.show()

    def close_main_menu(self):
        self.hide()

    def displayInfo(self):
        self.show()


class ManageEntitiesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Library')
        self.setFixedWidth(800)
        self.setFixedHeight(210)
        self.setStyleSheet("""
            QPushButton{
                font-size: 30px
            }
            """)
        mainLayout = QVBoxLayout()

        self.BooksOption = QPushButton('Books')
        mainLayout.addWidget(self.BooksOption)

        self.ClientsOption = QPushButton('Clients')
        mainLayout.addWidget(self.ClientsOption)

        self.closeButton = QPushButton('Back to main menu')
        self.closeButton.clicked.connect(self.back_to_main_menu)
        mainLayout.addWidget(self.closeButton)

        self.setLayout(mainLayout)

    def back_to_main_menu(self):
        self.hide()

    def displayInfo(self):
        self.show()


class SecondWindow2(QWidget):
    def __init__(self):
        super(MainMenuWindow).__init__()
        self.setWindowTitle('Library')
        self.setFixedWidth(800)
        self.setFixedHeight(210)
        self.setStyleSheet("""
            QLineEdit{
                font-size: 30px
            }
            QPushButton{
                font-size: 30px
            }
            """)
        mainLayout = QVBoxLayout()

        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)

        self.closeButton = QPushButton('Close')
        self.closeButton.clicked.connect(self.close)
        mainLayout.addWidget(self.closeButton)

        self.setLayout(mainLayout)

    def displayInfo(self):
        self.show()