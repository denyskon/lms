#!/usr/bin/python3

##LIBRARIES
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
##/LIBRARIES

##QT APPLICATION
app = QApplication(sys.argv)
##/QT APPLICATION

##ICONS
abouticon = QIcon.fromTheme("help-about")
foldericon = QIcon.fromTheme("folder")
helpicon = QIcon.fromTheme("help-contents")
runicon = QIcon.fromTheme("go-next")
app_icon = QIcon.fromTheme("lms")
info_text = "%Y year\n%m month\n%d day\n%H hour\n%M minute\n%S second\nOther text will be detected as text"
##/ICONS

##TRANSLATIONS

##SYNTAX

# elif language == "LOCALE_CODE":
#     openbutt = "TRANSLATION"
#     runbutt = "TRANSLATION"
#     ckboxlang = "TRANSLATION"

##/SYNTAX

##START
language = os.environ["LANG"]

if language == "de_DE.UTF-8":
    metaname = "&Metadaten"
    tabname = "&Steuerung"
    viewname = "&Bild anzeigen"
    openbutt = "&Ordner öffnen"
    runbutt = "&Start"
    ckboxlang = "&Verschieben in den Ordner "
    flnlang = "Neuer Dateiname"
    title = "LXDB MediaSorter Version 2020.2"
    text_open = "Öffnen"
    text_meta = "Metadaten anzeigen"
    format_error = "Format wird nicht unterstützt."
elif language == "ru_RU.UTF-8":
    metaname = "&Мета-данные"
    tabname = "&Управление"
    viewname = "&Просмотр изображения"
    openbutt = "&Открыть папку"
    runbutt = "&Начать"
    ckboxlang = "&Отправить в папку "
    flnlang = "&Новое название файла: "
elif language == "uk_UA.UTF-8":
    metaname = "&Мета-данні"
    tabname = "&Керування"
    viewname = "&Перегляд фотографії"
    openbutt = "&ідкрити папку"
    runbutt = "&Почати"
    ckboxlang = "&Пересунути в папку "
    flnlang = "Нова назва файлу:"
    title = "LXDB MediaSorter"
else:
    metaname = "&Meta data"
    tabname = "&Main tool"
    viewname = "&View image"
    openbutt = "&Open folder"
    runbutt = "&Run"
    ckboxlang = "&Move to folder "
    flnlang = "New file name:"
    title = "LXDB MediaSorter Version 2020.2"
##/END

##/TRANSLATIONS

##MAIN APPLICATION
class App(QWidget):
    def __init__(self):
        super().__init__()
        ##APPLICATION TITLE
        self.title = title
        ##/APPLICATION TITLE

        self.initUI()

        ##CONTEXT
        self.file_system.view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.file_system.view.customContextMenuRequested.connect(self.context_menu)
        ##/CONTEXT

    def initUI(self):

        ##TABVIEW
        self.tab_ui = QTabWidget()
        self.tab_ui.setTabsClosable(True)
        self.tab_ui.tabCloseRequested.connect(self.close_tab)
        ##/TABVIEW

        ##LAYOUTS
        self.main_layout = QVBoxLayout()
        self.main_layout.ui = QVBoxLayout()
        self.main_layout.ui.folder_rename = QHBoxLayout()
        self.main_layout.ui.file_rename = QHBoxLayout()

        ##/LAYOUTS

        self.tab_ui.main_tab = QWidget()

        self.tab_ui.addTab(self.tab_ui.main_tab, tabname)

        ##OPEN_FOLDER
        self.tab_ui.main_tab.folder_path_entry = QLineEdit()

        self.tab_ui.main_tab.button_open_folder=QPushButton(openbutt)
        self.tab_ui.main_tab.button_open_folder.setIcon(QIcon(foldericon))
        self.tab_ui.main_tab.button_open_folder.clicked.connect(self.get_folder)
        ##/OPEN_FOLDER

        ##RENAME_MOVE_OPTIONS
        self.tab_ui.main_tab.checkbox_sort = QCheckBox(ckboxlang)

        self.tab_ui.main_tab.file_new_name_label = QLabel(flnlang)

        self.tab_ui.main_tab.folder_new_name = QLineEdit()
        self.tab_ui.main_tab.folder_new_name.setText("%Y/%Y_%m")

        self.tab_ui.main_tab.folder_new_name.help = QPushButton()
        self.tab_ui.main_tab.folder_new_name.help.setIcon(QIcon(abouticon))
        self.tab_ui.main_tab.folder_new_name.help.setToolTip(info_text)

        self.tab_ui.main_tab.file_new_name = QLineEdit()
        self.tab_ui.main_tab.file_new_name.setText("%Y_%m_%d-%H_%M_%S")

        self.tab_ui.main_tab.file_new_name.help = QPushButton()
        self.tab_ui.main_tab.file_new_name.help.setIcon(QIcon(abouticon))
        self.tab_ui.main_tab.file_new_name.help.setToolTip(info_text)


        ##/RENAME_MOVE_OPTIONS

        ##START_BUTTON
        self.tab_ui.main_tab.button_start = QPushButton(runbutt)
        self.tab_ui.main_tab.button_start.setIcon(QIcon(runicon))
        self.tab_ui.main_tab.button_start.clicked.connect(self.start)
        ##/START_BUTTON

        ##FILESYSTEM_MODEL
        self.user_home = os.environ["HOME"]
        self.file_system = QFileSystemModel()
        self.file_system.setRootPath("/")

        self.file_system.view = QTreeView()
        self.file_system.view.setModel(self.file_system)
        self.file_system.view.setAnimated(True)
        self.file_system.view.setIndentation(20)
        self.file_system.view.setSortingEnabled(True)
        self.file_system.view.setRootIndex(self.file_system.index(self.user_home))
        self.file_system.view.setWindowTitle("Dir View")
        self.file_system.view.resize(700, 480)
        ##/FILESYSTEM_MODEL

        ##MENUBAR
        self.menubar = QMenuBar()

        self.menubar.file_menu = self.menubar.addMenu('&File')

        self.menubar.help_menu = self.menubar.addMenu('&Help')

        self.menubar.file_menu.open_folder_action = QAction(QIcon(foldericon), openbutt, self)
        self.menubar.file_menu.open_folder_action.triggered.connect(self.get_folder)

        self.menubar.help_menu.about_action = QAction(QIcon(abouticon), "&About", self)
        self.menubar.help_menu.about_action.triggered.connect(self.aboutwindow)

        self.menubar.help_menu.help_action = QAction(QIcon(helpicon), "&Help", self)
        self.menubar.help_menu.help_action.triggered.connect(self.helpfunc)

        self.menubar.file_menu.addAction(self.menubar.file_menu.open_folder_action)
        self.menubar.help_menu.addAction(self.menubar.help_menu.about_action)
        self.menubar.help_menu.addAction(self.menubar.help_menu.help_action)
        ##/MENUBAR

        ##ADD_WIDGETS
        self.main_layout.ui.addWidget(self.tab_ui.main_tab.folder_path_entry)
        self.main_layout.ui.addWidget(self.tab_ui.main_tab.button_open_folder)
        self.main_layout.ui.addWidget(self.file_system.view)
        self.main_layout.ui.addLayout(self.main_layout.ui.folder_rename)
        self.main_layout.ui.addLayout(self.main_layout.ui.file_rename)
        self.main_layout.ui.addWidget(self.tab_ui.main_tab.button_start)

        self.main_layout.ui.folder_rename.addWidget(self.tab_ui.main_tab.checkbox_sort)
        self.main_layout.ui.folder_rename.addWidget(self.tab_ui.main_tab.folder_new_name)
        self.main_layout.ui.folder_rename.addWidget(self.tab_ui.main_tab.folder_new_name.help)
        self.main_layout.ui.file_rename.addWidget(self.tab_ui.main_tab.file_new_name_label)
        self.main_layout.ui.file_rename.addWidget(self.tab_ui.main_tab.file_new_name)
        self.main_layout.ui.file_rename.addWidget(self.tab_ui.main_tab.file_new_name.help)
        ##/ADD_WIDGETS

        ##ADD_SET_LAYOUTS
        self.tab_ui.main_tab.setLayout(self.main_layout.ui)
        self.main_layout.addWidget(self.menubar)
        self.main_layout.addWidget(self.tab_ui)
        self.setLayout(self.main_layout)
        ##/ADD_SET_LAYOUTS

        ##WINDOW_OPTIONS
        self.setWindowIcon(QIcon(app_icon))
        self.setWindowTitle(self.title)

        self.show()
        ##/WINDOW_OPTIONS

    def context_menu(self):
        self.menu = QMenu()

        self.menu.open = self.menu.addAction(text_open)
        self.menu.open.triggered.connect(self.open_image)

        self.menu.meta = self.menu.addAction(text_meta)
        self.menu.meta.triggered.connect(self.metaview)

        self.cursor = QCursor()

        self.menu.exec_(self.cursor.pos())

    def open_image(self):
        self.index = self.file_system.view.currentIndex()
        self.file_name = str(self.file_system.filePath(self.index))
        print(self.file_name)
        self.tab_ui.image_tab = QWidget()
        i2 = self.tab_ui.addTab(self.tab_ui.image_tab, viewname)
        self.tab_ui.setCurrentIndex(i2)
        self.image_layout = QHBoxLayout()
        self.tab_ui.image_tab.image = QLabel()



        if self.file_name.endswith((".png", ".jpg", ".xcf", ".bmp", ".svg")) == True:
            self.image_layout.addWidget(self.tab_ui.image_tab.image)
            self.tab_ui.image_tab.image.setPixmap(QPixmap(self.file_name))
        else:
            print(format_error)


        self.tab_ui.image_tab.setLayout(self.image_layout)

    def metaview(self):
        self.index = self.file_system.view.currentIndex()
        self.file_name = str(self.file_system.filePath(self.index))
        self.tab_ui.meta_tab = QWidget()
        i2 = self.tab_ui.addTab(self.tab_ui.meta_tab, metaname)
        self.tab_ui.setCurrentIndex(i2)
        self.meta_layout = QHBoxLayout()
        self.tab_ui.meta_tab.metadata = QPlainTextEdit()

        self.meta_layout.addWidget(self.tab_ui.meta_tab.metadata)

        os.system("echo '" + self.file_name + "' > $HOME/.cache/lms_exif_path")
        os.system("bash /usr/share/lms/scripts/metadata.sh")
        self.cache_path = self.user_home + "/.cache/fmds_mime"
        try:
            with open(self.cache_path, 'r') as f:
                self.text = f.read()


        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.tab_ui.meta_tab.metadata.setPlainText(self.text)

        self.tab_ui.meta_tab.setLayout(self.meta_layout)
        os.system("rm " + self.cache_path)

    def get_folder(self):
        self.set_folder = QFileDialog.getExistingDirectory(self, openbutt, self.user_home, QFileDialog.ShowDirsOnly)
        self.tab_ui.main_tab.folder_path_entry.setText(self.set_folder)
        self.file_system.setRootPath(self.set_folder)
        self.file_system.view.setRootIndex(self.file_system.index(self.set_folder))

    def start(self):
        if self.tab_ui.main_tab.checkbox_sort.isChecked() == True:
            movevar = "move"
            movefld = self.tab_ui.main_tab.folder_new_name.text()
        else:
            movevar = "rename"
            movefld = ""
        filenamer = self.tab_ui.main_tab.file_new_name.text()
        path = self.tab_ui.main_tab.folder_path_entry.text()
        print("nothing")


    def close_tab(self, i2):
        if self.tab_ui.count() < 2:
            return
        self.tab_ui.removeTab(i2)

    def aboutwindow(self):
        print("nothing")

    def helpfunc(self):
        print("nothing")

##/HELP WINDOW

if __name__ == '__main__':
    ex = App()
    sys.exit(app.exec_())
