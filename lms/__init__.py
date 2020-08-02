#LXDB MediaSorter - A program to sort media files.
#Copyright (C) 2019-2020 LXDB Team

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#LXDB MediaSorter,  Copyright (C) 2019-2020  LXDB Team
#This program comes with ABSOLUTELY NO WARRANTY
#This is free software, and you are welcome to redistribute it
#under certain conditions.

##LIBRARIES
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import lms.exif
import webbrowser
import locale
##/LIBRARIES

##QT APPLICATION
app = QApplication(sys.argv)
##/QT APPLICATION

##ICONS
abouticon = QIcon.fromTheme("help-about")
foldericon = QIcon.fromTheme("folder")
helpicon = QIcon.fromTheme("help-contents")
runicon = QIcon.fromTheme("go-next")
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
language = locale.getdefaultlocale()

if language[0] == "de_DE":
    metaname = "&Metadaten"
    tabname = "&Steuerung"
    viewname = "&Bild anzeigen"
    openbutt = "&Ordner öffnen"
    runbutt = "&Start"
    ckboxlang = "&Verschieben in den Ordner "
    flnlang = "Neuer Dateiname"
    title = "LXDB MediaSorter Version 2020.07"
    text_open = "Öffnen"
    text_meta = "Metadaten anzeigen"
    format_error = "Format wird nicht unterstützt."
    error_text = "Fehler"
    recursive_text = "Unterordner einbeziehen"
    about_text = "Über LXDB MediaSorter"
    help_text = "Dokumentation"
elif language[0] == "ru_RU":
    metaname = "&Мета-данные"
    tabname = "&Управление"
    viewname = "&Просмотр изображения"
    openbutt = "&Открыть папку"
    runbutt = "&Начать"
    ckboxlang = "&Отправить в папку "
    flnlang = "&Новое название файла: "
    title = "LXDB MediaSorter Версия 2020.07"
    text_open = "Открыть"
    text_meta = "Просмотр метаданных"
    format_error = "Формат не поддерживается."
    error_text = "Ошибка"
    recursive_text = "Включить подпапки"
    about_text = "О LXDB MediaSorter"
    help_text = "Документация"
elif language[0] == "uk_UA":
    metaname = "&Мета-данні"
    tabname = "&Керування"
    viewname = "&Перегляд фотографії"
    openbutt = "&ідкрити папку"
    runbutt = "&Почати"
    ckboxlang = "&Пересунути в папку "
    flnlang = "Нова назва файлу:"
    title = "LXDB MediaSorter версія 2020.07"
    text_open = "Bідкрити"
    text_meta = "Перегляд метаданих"
    format_error = "Формат не підтримується."
    error_text = "Помилка"
    recursive_text = "Включити підпапки"
    about_text = "Про LXDB MediaSorter"
    help_text = "Документація"
else:
    metaname = "&Meta data"
    tabname = "&Main tool"
    viewname = "&View image"
    openbutt = "&Open folder"
    runbutt = "&Run"
    ckboxlang = "&Move to folder "
    flnlang = "New file name:"
    title = "LXDB MediaSorter Version 2020.07"
    text_open = "Open"
    text_meta = "View metadata"
    format_error = "Format not supported."
    error_text = "Error"
    recursive_text = "Include subfolders"
    about_text = "About LXDB MediaSorter"
    help_text = "Documentation"
##/END

##/TRANSLATIONS

##MAIN APPLICATION
class App(QMainWindow):
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
        self.main_layout.folder_rename = QHBoxLayout()
        self.main_layout.file_rename = QHBoxLayout()

        ##/LAYOUTS

        self.tab_ui.main_tab = QWidget()

        self.tab_ui.addTab(self.tab_ui.main_tab, tabname)

        ##OPEN_FOLDER
        self.tab_ui.main_tab.folder_path_entry = QLineEdit()

        self.tab_ui.main_tab.button_open_folder=QPushButton(openbutt)
        self.tab_ui.main_tab.button_open_folder.setIcon(self.style().standardIcon(QStyle.SP_DirOpenIcon))
        self.tab_ui.main_tab.button_open_folder.clicked.connect(self.get_folder)
        ##/OPEN_FOLDER

        ##RENAME_MOVE_OPTIONS
        self.tab_ui.main_tab.checkbox_sort = QCheckBox(ckboxlang)

        self.tab_ui.main_tab.checkbox_recursive = QCheckBox(recursive_text)

        self.tab_ui.main_tab.file_new_name_label = QLabel(flnlang)

        self.tab_ui.main_tab.folder_new_name = QLineEdit()
        self.tab_ui.main_tab.folder_new_name.setText("%Y/%Y_%m")

        self.tab_ui.main_tab.folder_new_name.help = QPushButton()
        self.tab_ui.main_tab.folder_new_name.help.setIcon(self.style().standardIcon(QStyle.SP_DialogHelpButton))
        self.tab_ui.main_tab.folder_new_name.help.setToolTip(info_text)

        self.tab_ui.main_tab.file_new_name = QLineEdit()
        self.tab_ui.main_tab.file_new_name.setText("%Y_%m_%d-%H_%M_%S")

        self.tab_ui.main_tab.file_new_name.help = QPushButton()
        self.tab_ui.main_tab.file_new_name.help.setIcon(self.style().standardIcon(QStyle.SP_DialogHelpButton))
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
        ##/FILESYSTEM_MODEL

        ##MENUBAR
        self.menubar = self.menuBar()

        self.menubar.file_menu = self.menubar.addMenu('&File')

        self.menubar.help_menu = self.menubar.addMenu('&Help')

        self.menubar.file_menu.open_folder_action = QAction(self.style().standardIcon(QStyle.SP_DirOpenIcon), openbutt, self)
        self.menubar.file_menu.open_folder_action.triggered.connect(self.get_folder)

        self.menubar.file_menu.quit_action = QAction(QIcon.fromTheme("application-exit"), "&Exit", self)
        self.menubar.file_menu.quit_action.triggered.connect(self.quit)

        self.menubar.help_menu.about_action = QAction(self.style().standardIcon(QStyle.SP_MessageBoxInformation), "&" + about_text, self)
        self.menubar.help_menu.about_action.triggered.connect(self.aboutwindow)

        self.menubar.help_menu.about_qt_action = QAction(self.style().standardIcon(QStyle.SP_MessageBoxInformation), "Qt", self)
        self.menubar.help_menu.about_qt_action.triggered.connect(self.about_qt)

        self.menubar.help_menu.help_action = QAction(self.style().standardIcon(QStyle.SP_DialogHelpButton), "&" + help_text, self)
        self.menubar.help_menu.help_action.triggered.connect(self.helpfunc)

        self.menubar.file_menu.addAction(self.menubar.file_menu.open_folder_action)
        self.menubar.file_menu.addAction(self.menubar.file_menu.quit_action)
        self.menubar.help_menu.addAction(self.menubar.help_menu.about_action)
        self.menubar.help_menu.addAction(self.menubar.help_menu.about_qt_action)
        self.menubar.help_menu.addAction(self.menubar.help_menu.help_action)
        ##/MENUBAR

        #ADD_WIDGETS
        self.main_layout.addWidget(self.tab_ui.main_tab.folder_path_entry)
        self.main_layout.addWidget(self.tab_ui.main_tab.button_open_folder)
        self.main_layout.addWidget(self.file_system.view)
        self.main_layout.addWidget(self.tab_ui.main_tab.checkbox_recursive)
        self.main_layout.addLayout(self.main_layout.folder_rename)
        self.main_layout.addLayout(self.main_layout.file_rename)
        self.main_layout.addWidget(self.tab_ui.main_tab.button_start)


        self.main_layout.folder_rename.addWidget(self.tab_ui.main_tab.checkbox_sort)
        self.main_layout.folder_rename.addWidget(self.tab_ui.main_tab.folder_new_name)
        self.main_layout.folder_rename.addWidget(self.tab_ui.main_tab.folder_new_name.help)
        self.main_layout.file_rename.addWidget(self.tab_ui.main_tab.file_new_name_label)
        self.main_layout.file_rename.addWidget(self.tab_ui.main_tab.file_new_name)
        self.main_layout.file_rename.addWidget(self.tab_ui.main_tab.file_new_name.help)
        ##/ADD_WIDGETS

        ##ADD_SET_LAYOUTS
        self.tab_ui.main_tab.setLayout(self.main_layout)
        self.setCentralWidget(self.tab_ui)
        ##/ADD_SET_LAYOUTS

        ##WINDOW_OPTIONS
        app.setWindowIcon(QIcon.fromTheme("de.lxdb.lms"))
        self.setWindowTitle(title)
        app.setApplicationName("LXDB MediaSorter")
        app.setApplicationVersion("2020.05")

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

    def quit(self):
        app.quit()

    def open_image(self):
        self.index = self.file_system.view.currentIndex()
        self.file_name = str(self.file_system.filePath(self.index))
        print(self.file_name)
        video_formats = [".mkv", ".mp4", ".avi", ".webm", ".flv", ".vob", ".ogg",
                        ".ogv", ".drc", ".MTS", ".M2TS", ".TS", ".mov", ".qt",
                        ".wmv", ".yuv", ".rm", ".rmvb", ".asf", ".amv", ".m4p",
                        ".m4v", ".mpg", ".mp2", ".mpeg", ".m2v", ".svi", ".3gp",
                        ".3g2", ".mxf", ".roq", ".nsv", ".f4v", ".f4p", ".f42",
                        ".f4b"]

        if self.file_name.endswith((".png", ".jpg", ".xcf", ".bmp", ".svg", ".jpeg")):
            print("True")
            self.tab_ui.image_tab = QWidget()
            self.scaleFactor = 0.0
            self.scrollArea = QScrollArea()
            self.scrollArea.setBackgroundRole(QPalette.Dark)
            self.tab_ui.image_tab.image = QLabel()
            self.tab_ui.image_tab.image.setBackgroundRole(QPalette.Base)
            self.tab_ui.image_tab.image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            self.tab_ui.image_tab.image.setScaledContents(True)
            self.tab_ui.image_tab.image.setPixmap(QPixmap.fromImage(QImage(self.file_name)))
            self.button_smaller = QPushButton()
            self.button_bigger = QPushButton()
            self.button_bigger.setIcon(QIcon.fromTheme("zoom-in"))
            self.button_smaller.setIcon(QIcon.fromTheme("zoom-out"))
            self.button_reset = QPushButton()
            self.button_reset.setIcon(QIcon.fromTheme("back"))
            self.button_reset.clicked.connect(self.reset_size)
            self.button_bigger.clicked.connect(lambda: self.scaleImage(1.25))
            self.button_smaller.clicked.connect(lambda: self.scaleImage(0.8))
            self.scrollArea.setWidget(self.tab_ui.image_tab.image)
            self.button_area = QHBoxLayout()
            self.button_area.addWidget(self.button_bigger)
            self.button_area.addWidget(self.button_smaller)
            self.button_area.addWidget(self.button_reset)
            self.image_layout = QVBoxLayout()
            self.image_layout.addLayout(self.button_area)
            self.image_layout.addWidget(self.scrollArea)
            self.scaleFactor = 1.0
            self.tab_ui.image_tab.image.adjustSize()
            self.tab_ui.image_tab.setLayout(self.image_layout)
            i2 = self.tab_ui.addTab(self.tab_ui.image_tab, self.file_name)
            self.tab_ui.setCurrentIndex(i2)
        elif self.file_name.endswith((tuple(video_formats))):
            self.tab_ui.VideoTab = QWidget()
            self.tab_ui.VideoTab.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
            self.tab_ui.VideoTab.playButton = QPushButton()
            self.tab_ui.VideoTab.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            self.tab_ui.VideoTab.playButton.clicked.connect(self.play)
            self.tab_ui.VideoTab.videoWidget = QVideoWidget()
            self.tab_ui.VideoTab.positionSlider = QSlider(Qt.Horizontal)
            self.tab_ui.VideoTab.positionSlider.setRange(0, 0)
            self.tab_ui.VideoTab.positionSlider.sliderMoved.connect(self.tab_ui.VideoTab.player.setPosition)
            controlLayout = QHBoxLayout()
            controlLayout.setContentsMargins(0, 0, 0, 0)
            controlLayout.addWidget(self.tab_ui.VideoTab.playButton)
            controlLayout.addWidget(self.tab_ui.VideoTab.positionSlider)
            layout = QVBoxLayout()
            layout.addWidget(self.tab_ui.VideoTab.videoWidget)
            layout.addLayout(controlLayout)
            self.tab_ui.VideoTab.setLayout(layout)
            self.tab_ui.VideoTab.player.setVideoOutput(self.tab_ui.VideoTab.videoWidget)
            self.tab_ui.VideoTab.player.positionChanged.connect(self.tab_ui.VideoTab.positionSlider.setValue)
            self.tab_ui.VideoTab.player.durationChanged.connect(self.durationChanged)
            self.tab_ui.VideoTab.player.setMedia(
                    QMediaContent(QUrl.fromLocalFile(self.file_name)))
            self.play()
            i2 = self.tab_ui.addTab(self.tab_ui.VideoTab, self.file_name)
            self.tab_ui.setCurrentIndex(i2)

        else:
            print("False")
            error = QMessageBox()
            error.setIcon(QMessageBox.Critical)
            error.setText(error_text)
            error.setInformativeText(format_error)
            error.setWindowTitle(error_text)
            error.exec_()

    def scaleImage(self, factor):
        self.scaleFactor *= factor
        self.tab_ui.image_tab.image.resize(self.scaleFactor * self.tab_ui.image_tab.image.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

        self.button_bigger.setEnabled(self.scaleFactor < 3.0)
        self.button_smaller.setEnabled(self.scaleFactor > 0.333)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value()
                                + ((factor - 1) * scrollBar.pageStep()/2)))

    def reset_size(self):
        self.tab_ui.image_tab.image.adjustSize()
        self.scaleFactor = 1.0
        self.scaleImage(1.0)

    def play(self):
        if self.tab_ui.VideoTab.player.state() == QMediaPlayer.PlayingState:
            self.tab_ui.VideoTab.player.pause()
        else:
            self.tab_ui.VideoTab.player.play()

    def durationChanged(self, duration):
        self.tab_ui.VideoTab.positionSlider.setRange(0, duration)


    def metaview(self):
        self.index = self.file_system.view.currentIndex()
        self.file_name = str(self.file_system.filePath(self.index))
        self.tab_ui.meta_tab = QWidget()
        i2 = self.tab_ui.addTab(self.tab_ui.meta_tab, metaname)
        self.tab_ui.setCurrentIndex(i2)
        self.meta_layout = QHBoxLayout()
        self.tab_ui.meta_tab.metadata = QPlainTextEdit()

        self.meta_layout.addWidget(self.tab_ui.meta_tab.metadata)

        metadata = exif.GetMetadata(self.file_name)

        self.tab_ui.meta_tab.metadata.setPlainText(metadata)

        self.tab_ui.meta_tab.metadata.setReadOnly(True)

        self.tab_ui.meta_tab.setLayout(self.meta_layout)

    def get_folder(self):
        self.source_folder = QFileDialog.getExistingDirectory(self, openbutt[1:], self.user_home, QFileDialog.ShowDirsOnly)
        self.tab_ui.main_tab.folder_path_entry.setText(self.source_folder)
        self.file_system.setRootPath(self.source_folder)
        self.file_system.view.setRootIndex(self.file_system.index(self.source_folder))

    def start(self):
        if self.tab_ui.main_tab.checkbox_recursive.isChecked():
            rc=True
        else:
            rc=False
        filename_new = self.tab_ui.main_tab.file_new_name.text()
        foldername_new = self.tab_ui.main_tab.folder_new_name.text()
        source = self.tab_ui.main_tab.folder_path_entry.text()
        if self.tab_ui.main_tab.checkbox_sort.isChecked() == True:
            exif.RMove(foldername_new, filename_new, source, rc)
        elif self.tab_ui.main_tab.checkbox_sort.isChecked() == False:
            exif.Rename(filename_new, source, rc)

    def close_tab(self, i2):
        if self.tab_ui.count() < 2:
            return
        print(i2)
        self.tab_ui.removeTab(i2)

    def aboutwindow(self):
        QMessageBox.about(self,
            "About LXDB MediaSorter",
            """<b>LXDB MediaSorter version 2020.07</b>
            <br>Get your files in order !
            <p>Copyright &copy; 2019-2020 LXDB Team
            <br>Licensed under the terms of the <a href="https://www.gnu.org/licenses/">GNU GPLv3.0 License</a>.
            <p>Created, developed and maintained by LXDB Team.
            <p><a href="https://lxdb.de/lms">MediaSorter at LXDB.de</a></p>""")

    def about_qt(self):
        QMessageBox.aboutQt(self)


    def helpfunc(self):
        webbrowser.open_new("https://wiki.lxdb.de/lms")

##/HELP WINDOW
