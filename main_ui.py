# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from customnWidget import (BarChartView, CircularProgress, PieChartView)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1001, 616)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(8, 8, 8)")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 80))
        self.topBar.setMaximumSize(QSize(16777215, 80))
        self.topBar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 5px 0px 0px 5px;\n"
"}")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.topBar)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.topBar)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 30))
        self.titleBar.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(1504, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.actionButtonsBar = QFrame(self.titleBar)
        self.actionButtonsBar.setObjectName(u"actionButtonsBar")
        self.actionButtonsBar.setMinimumSize(QSize(100, 0))
        self.actionButtonsBar.setMaximumSize(QSize(100, 16777215))
        self.actionButtonsBar.setStyleSheet(u"")
        self.actionButtonsBar.setFrameShape(QFrame.StyledPanel)
        self.actionButtonsBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.actionButtonsBar)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.min_bt = QPushButton(self.actionButtonsBar)
        self.min_bt.setObjectName(u"min_bt")
        self.min_bt.setMinimumSize(QSize(30, 30))
        self.min_bt.setMaximumSize(QSize(30, 30))
        self.min_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_bt.setIcon(icon)
        self.min_bt.setIconSize(QSize(17, 17))

        self.horizontalLayout_8.addWidget(self.min_bt)

        self.max_bt = QPushButton(self.actionButtonsBar)
        self.max_bt.setObjectName(u"max_bt")
        self.max_bt.setMinimumSize(QSize(30, 30))
        self.max_bt.setMaximumSize(QSize(30, 30))
        self.max_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.max_bt.setIcon(icon1)
        self.max_bt.setIconSize(QSize(17, 17))

        self.horizontalLayout_8.addWidget(self.max_bt)

        self.close_bt = QPushButton(self.actionButtonsBar)
        self.close_bt.setObjectName(u"close_bt")
        self.close_bt.setMinimumSize(QSize(30, 30))
        self.close_bt.setMaximumSize(QSize(30, 30))
        self.close_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 15;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(124, 124, 124);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 0, 0) ;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_bt.setIcon(icon2)
        self.close_bt.setIconSize(QSize(17, 17))

        self.horizontalLayout_8.addWidget(self.close_bt)


        self.horizontalLayout_7.addWidget(self.actionButtonsBar)


        self.verticalLayout_5.addWidget(self.titleBar)

        self.actionBar = QFrame(self.topBar)
        self.actionBar.setObjectName(u"actionBar")
        self.actionBar.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(13, 9, 36);\n"
"}\n"
"\n"
"QSpacer {\n"
"	background-color: rgb(13, 9, 36);\n"
"}")
        self.actionBar.setFrameShape(QFrame.NoFrame)
        self.actionBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.actionBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.actionBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(40, 40))
        self.frame_5.setMaximumSize(QSize(40, 40))
        self.frame_5.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"border-radius: 20;\n"
"image: url(:/icons/icons/building.svg);\n"
"padding: 3px;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.label_4 = QLabel(self.actionBar)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(168, 168, 168);")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(134, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_7 = QFrame(self.actionBar)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(200, 40))
        self.frame_7.setMaximumSize(QSize(250, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.module_bt = QPushButton(self.frame_7)
        self.module_bt.setObjectName(u"module_bt")
        sizePolicy.setHeightForWidth(self.module_bt.sizePolicy().hasHeightForWidth())
        self.module_bt.setSizePolicy(sizePolicy)
        self.module_bt.setMinimumSize(QSize(100, 30))
        self.module_bt.setMaximumSize(QSize(26, 26))
        self.module_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.module_bt.setIcon(icon3)
        self.module_bt.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.module_bt)

        self.setting_bt = QPushButton(self.frame_7)
        self.setting_bt.setObjectName(u"setting_bt")
        sizePolicy.setHeightForWidth(self.setting_bt.sizePolicy().hasHeightForWidth())
        self.setting_bt.setSizePolicy(sizePolicy)
        self.setting_bt.setMinimumSize(QSize(100, 30))
        self.setting_bt.setMaximumSize(QSize(26, 26))
        self.setting_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.setting_bt.setIcon(icon4)
        self.setting_bt.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.setting_bt)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout_5.addWidget(self.actionBar)


        self.verticalLayout.addWidget(self.topBar)

        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"background-color: rgb(8, 8, 8);")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.container)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stackedWidget = QStackedWidget(self.container)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_3 = QVBoxLayout(self.home_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.keys_le = QLineEdit(self.home_page)
        self.keys_le.setObjectName(u"keys_le")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.keys_le.sizePolicy().hasHeightForWidth())
        self.keys_le.setSizePolicy(sizePolicy1)
        self.keys_le.setMinimumSize(QSize(300, 30))
        self.keys_le.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.keys_le)

        self.house_names_cb = QComboBox(self.home_page)
        self.house_names_cb.setObjectName(u"house_names_cb")
        sizePolicy.setHeightForWidth(self.house_names_cb.sizePolicy().hasHeightForWidth())
        self.house_names_cb.setSizePolicy(sizePolicy)
        self.house_names_cb.setMinimumSize(QSize(450, 30))
        self.house_names_cb.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.horizontalLayout_10.addWidget(self.house_names_cb)

        self.search_percent_bt = QPushButton(self.home_page)
        self.search_percent_bt.setObjectName(u"search_percent_bt")
        sizePolicy.setHeightForWidth(self.search_percent_bt.sizePolicy().hasHeightForWidth())
        self.search_percent_bt.setSizePolicy(sizePolicy)
        self.search_percent_bt.setMinimumSize(QSize(100, 30))
        self.search_percent_bt.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_10.addWidget(self.search_percent_bt)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.ne_num_pie = PieChartView(self.home_page)
        self.ne_num_pie.setObjectName(u"ne_num_pie")

        self.horizontalLayout_11.addWidget(self.ne_num_pie)

        self.high_num_pie = PieChartView(self.home_page)
        self.high_num_pie.setObjectName(u"high_num_pie")

        self.horizontalLayout_11.addWidget(self.high_num_pie)

        self.use_percent = CircularProgress(self.home_page)
        self.use_percent.setObjectName(u"use_percent")

        self.horizontalLayout_11.addWidget(self.use_percent)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.home_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.horizontalLayout_15 = QHBoxLayout(self.setting_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_6 = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.table_names_cb = QComboBox(self.setting_page)
        self.table_names_cb.setObjectName(u"table_names_cb")
        sizePolicy.setHeightForWidth(self.table_names_cb.sizePolicy().hasHeightForWidth())
        self.table_names_cb.setSizePolicy(sizePolicy)
        self.table_names_cb.setMinimumSize(QSize(250, 30))
        self.table_names_cb.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.horizontalLayout_14.addWidget(self.table_names_cb)

        self.search_table_bt = QPushButton(self.setting_page)
        self.search_table_bt.setObjectName(u"search_table_bt")
        sizePolicy.setHeightForWidth(self.search_table_bt.sizePolicy().hasHeightForWidth())
        self.search_table_bt.setSizePolicy(sizePolicy)
        self.search_table_bt.setMinimumSize(QSize(100, 30))
        self.search_table_bt.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_14.addWidget(self.search_table_bt)

        self.clear_table_bt = QPushButton(self.setting_page)
        self.clear_table_bt.setObjectName(u"clear_table_bt")
        sizePolicy.setHeightForWidth(self.clear_table_bt.sizePolicy().hasHeightForWidth())
        self.clear_table_bt.setSizePolicy(sizePolicy)
        self.clear_table_bt.setMinimumSize(QSize(100, 30))
        self.clear_table_bt.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_14.addWidget(self.clear_table_bt)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.setting_page)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.setting_page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.setting_page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_5 = QLabel(self.setting_page)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 1)

        self.device_high_tw = QTableWidget(self.setting_page)
        self.device_high_tw.setObjectName(u"device_high_tw")
        self.device_high_tw.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1a1a3a;  /* \u6bd4\u7a97\u4f53\u80cc\u666f\u7a0d\u4eae\uff0c\u5f62\u6210\u5c42\u6b21\u611f */\n"
"    color: #ffffff;             /* \u767d\u8272\u6587\u5b57\u786e\u4fdd\u53ef\u8bfb\u6027 */\n"
"    gridline-color: #2a2a4a;    /* \u6df1\u8272\u7f51\u683c\u7ebf\uff0c\u4e0e\u80cc\u666f\u534f\u8c03 */\n"
"    font-family: \"Microsoft YaHei\", Arial;\n"
"    font-size: 12px;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: #1a1a3a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2a2a4a;\n"
"    padding: 4px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #3a3a5a;  /* \u9009\u4e2d\u9879\u4f7f\u7528\u7a0d\u4eae\u7684\u84dd\u8272 */\n"
"    color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #252545;  /* \u8868\u5934\u80cc\u666f\u6bd4\u8868\u683c\u7a0d\u4eae */\n"
"    color: #ffffff;\n"
"    padding: 6px;\n"
"    border: 1px solid #2a2a4a;\n"
"    font-weight: bold;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color:"
                        " #1a1a3a;\n"
"    width: 10px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4a4a6a;  /* \u6eda\u52a8\u6761\u6ed1\u5757\u989c\u8272 */\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: #1a1a3a;\n"
"    height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #4a4a6a;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}")

        self.gridLayout.addWidget(self.device_high_tw, 1, 0, 1, 1)

        self.house_tw = QTableWidget(self.setting_page)
        self.house_tw.setObjectName(u"house_tw")
        self.house_tw.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1a1a3a;  /* \u6bd4\u7a97\u4f53\u80cc\u666f\u7a0d\u4eae\uff0c\u5f62\u6210\u5c42\u6b21\u611f */\n"
"    color: #ffffff;             /* \u767d\u8272\u6587\u5b57\u786e\u4fdd\u53ef\u8bfb\u6027 */\n"
"    gridline-color: #2a2a4a;    /* \u6df1\u8272\u7f51\u683c\u7ebf\uff0c\u4e0e\u80cc\u666f\u534f\u8c03 */\n"
"    font-family: \"Microsoft YaHei\", Arial;\n"
"    font-size: 12px;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: #1a1a3a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2a2a4a;\n"
"    padding: 4px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #3a3a5a;  /* \u9009\u4e2d\u9879\u4f7f\u7528\u7a0d\u4eae\u7684\u84dd\u8272 */\n"
"    color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #252545;  /* \u8868\u5934\u80cc\u666f\u6bd4\u8868\u683c\u7a0d\u4eae */\n"
"    color: #ffffff;\n"
"    padding: 6px;\n"
"    border: 1px solid #2a2a4a;\n"
"    font-weight: bold;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color:"
                        " #1a1a3a;\n"
"    width: 10px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4a4a6a;  /* \u6eda\u52a8\u6761\u6ed1\u5757\u989c\u8272 */\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: #1a1a3a;\n"
"    height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #4a4a6a;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}")

        self.gridLayout.addWidget(self.house_tw, 1, 1, 1, 1)

        self.rack_tw = QTableWidget(self.setting_page)
        self.rack_tw.setObjectName(u"rack_tw")
        self.rack_tw.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1a1a3a;  /* \u6bd4\u7a97\u4f53\u80cc\u666f\u7a0d\u4eae\uff0c\u5f62\u6210\u5c42\u6b21\u611f */\n"
"    color: #ffffff;             /* \u767d\u8272\u6587\u5b57\u786e\u4fdd\u53ef\u8bfb\u6027 */\n"
"    gridline-color: #2a2a4a;    /* \u6df1\u8272\u7f51\u683c\u7ebf\uff0c\u4e0e\u80cc\u666f\u534f\u8c03 */\n"
"    font-family: \"Microsoft YaHei\", Arial;\n"
"    font-size: 12px;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: #1a1a3a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2a2a4a;\n"
"    padding: 4px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #3a3a5a;  /* \u9009\u4e2d\u9879\u4f7f\u7528\u7a0d\u4eae\u7684\u84dd\u8272 */\n"
"    color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #252545;  /* \u8868\u5934\u80cc\u666f\u6bd4\u8868\u683c\u7a0d\u4eae */\n"
"    color: #ffffff;\n"
"    padding: 6px;\n"
"    border: 1px solid #2a2a4a;\n"
"    font-weight: bold;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color:"
                        " #1a1a3a;\n"
"    width: 10px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4a4a6a;  /* \u6eda\u52a8\u6761\u6ed1\u5757\u989c\u8272 */\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: #1a1a3a;\n"
"    height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #4a4a6a;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}")

        self.gridLayout.addWidget(self.rack_tw, 1, 2, 1, 1)

        self.net_tw = QTableWidget(self.setting_page)
        self.net_tw.setObjectName(u"net_tw")
        self.net_tw.setStyleSheet(u"QTableWidget {\n"
"    background-color: #1a1a3a;  /* \u6bd4\u7a97\u4f53\u80cc\u666f\u7a0d\u4eae\uff0c\u5f62\u6210\u5c42\u6b21\u611f */\n"
"    color: #ffffff;             /* \u767d\u8272\u6587\u5b57\u786e\u4fdd\u53ef\u8bfb\u6027 */\n"
"    gridline-color: #2a2a4a;    /* \u6df1\u8272\u7f51\u683c\u7ebf\uff0c\u4e0e\u80cc\u666f\u534f\u8c03 */\n"
"    font-family: \"Microsoft YaHei\", Arial;\n"
"    font-size: 12px;\n"
"}\n"
"QTableWidget::item {\n"
"    background-color: #1a1a3a;\n"
"    color: #ffffff;\n"
"    border: 1px solid #2a2a4a;\n"
"    padding: 4px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #3a3a5a;  /* \u9009\u4e2d\u9879\u4f7f\u7528\u7a0d\u4eae\u7684\u84dd\u8272 */\n"
"    color: #ffffff;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #252545;  /* \u8868\u5934\u80cc\u666f\u6bd4\u8868\u683c\u7a0d\u4eae */\n"
"    color: #ffffff;\n"
"    padding: 6px;\n"
"    border: 1px solid #2a2a4a;\n"
"    font-weight: bold;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color:"
                        " #1a1a3a;\n"
"    width: 10px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #4a4a6a;  /* \u6eda\u52a8\u6761\u6ed1\u5757\u989c\u8272 */\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    background-color: #1a1a3a;\n"
"    height: 10px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #4a4a6a;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}")

        self.gridLayout.addWidget(self.net_tw, 1, 3, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)

        self.verticalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_6.addItem(self.verticalSpacer_8)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_8)

        self.stackedWidget.addWidget(self.setting_page)
        self.importFile_page = QWidget()
        self.importFile_page.setObjectName(u"importFile_page")
        self.horizontalLayout_5 = QHBoxLayout(self.importFile_page)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 138, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fileType_cb = QComboBox(self.importFile_page)
        self.fileType_cb.setObjectName(u"fileType_cb")
        sizePolicy.setHeightForWidth(self.fileType_cb.sizePolicy().hasHeightForWidth())
        self.fileType_cb.setSizePolicy(sizePolicy)
        self.fileType_cb.setMinimumSize(QSize(150, 30))
        self.fileType_cb.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.horizontalLayout_4.addWidget(self.fileType_cb)

        self.select_path_le = QLineEdit(self.importFile_page)
        self.select_path_le.setObjectName(u"select_path_le")
        sizePolicy1.setHeightForWidth(self.select_path_le.sizePolicy().hasHeightForWidth())
        self.select_path_le.setSizePolicy(sizePolicy1)
        self.select_path_le.setMinimumSize(QSize(50, 30))
        self.select_path_le.setMaximumSize(QSize(16777215, 30))
        self.select_path_le.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.select_path_le)

        self.select_file_bt = QPushButton(self.importFile_page)
        self.select_file_bt.setObjectName(u"select_file_bt")
        sizePolicy.setHeightForWidth(self.select_file_bt.sizePolicy().hasHeightForWidth())
        self.select_file_bt.setSizePolicy(sizePolicy)
        self.select_file_bt.setMinimumSize(QSize(100, 30))
        self.select_file_bt.setMaximumSize(QSize(16777215, 30))
        self.select_file_bt.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.select_file_bt)

        self.update_db_bt = QPushButton(self.importFile_page)
        self.update_db_bt.setObjectName(u"update_db_bt")
        sizePolicy.setHeightForWidth(self.update_db_bt.sizePolicy().hasHeightForWidth())
        self.update_db_bt.setSizePolicy(sizePolicy)
        self.update_db_bt.setMinimumSize(QSize(100, 30))
        self.update_db_bt.setMaximumSize(QSize(16777215, 30))
        self.update_db_bt.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_4.addWidget(self.update_db_bt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.cols_grid = QGridLayout()
        self.cols_grid.setObjectName(u"cols_grid")
        self.col1_label = QLabel(self.importFile_page)
        self.col1_label.setObjectName(u"col1_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.col1_label.sizePolicy().hasHeightForWidth())
        self.col1_label.setSizePolicy(sizePolicy2)
        self.col1_label.setMaximumSize(QSize(16777215, 30))
        self.col1_label.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.col1_label.setAlignment(Qt.AlignCenter)

        self.cols_grid.addWidget(self.col1_label, 0, 0, 1, 1)

        self.col2_label = QLabel(self.importFile_page)
        self.col2_label.setObjectName(u"col2_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.col2_label.sizePolicy().hasHeightForWidth())
        self.col2_label.setSizePolicy(sizePolicy3)
        self.col2_label.setMinimumSize(QSize(0, 30))
        self.col2_label.setMaximumSize(QSize(16777215, 30))
        self.col2_label.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.col2_label.setAlignment(Qt.AlignCenter)

        self.cols_grid.addWidget(self.col2_label, 0, 1, 1, 1)

        self.col3_label = QLabel(self.importFile_page)
        self.col3_label.setObjectName(u"col3_label")
        sizePolicy3.setHeightForWidth(self.col3_label.sizePolicy().hasHeightForWidth())
        self.col3_label.setSizePolicy(sizePolicy3)
        self.col3_label.setMinimumSize(QSize(0, 30))
        self.col3_label.setMaximumSize(QSize(16777215, 30))
        self.col3_label.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.col3_label.setAlignment(Qt.AlignCenter)

        self.cols_grid.addWidget(self.col3_label, 0, 2, 1, 1)

        self.col3_label_3 = QLabel(self.importFile_page)
        self.col3_label_3.setObjectName(u"col3_label_3")
        sizePolicy3.setHeightForWidth(self.col3_label_3.sizePolicy().hasHeightForWidth())
        self.col3_label_3.setSizePolicy(sizePolicy3)
        self.col3_label_3.setMinimumSize(QSize(0, 30))
        self.col3_label_3.setMaximumSize(QSize(16777215, 30))
        self.col3_label_3.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.col3_label_3.setAlignment(Qt.AlignCenter)

        self.cols_grid.addWidget(self.col3_label_3, 0, 4, 1, 1)

        self.col1_cb = QComboBox(self.importFile_page)
        self.col1_cb.setObjectName(u"col1_cb")
        sizePolicy2.setHeightForWidth(self.col1_cb.sizePolicy().hasHeightForWidth())
        self.col1_cb.setSizePolicy(sizePolicy2)
        self.col1_cb.setMaximumSize(QSize(16777215, 30))
        self.col1_cb.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.cols_grid.addWidget(self.col1_cb, 1, 0, 1, 1)

        self.col2_cb = QComboBox(self.importFile_page)
        self.col2_cb.setObjectName(u"col2_cb")
        sizePolicy2.setHeightForWidth(self.col2_cb.sizePolicy().hasHeightForWidth())
        self.col2_cb.setSizePolicy(sizePolicy2)
        self.col2_cb.setMaximumSize(QSize(16777215, 30))
        self.col2_cb.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.cols_grid.addWidget(self.col2_cb, 1, 1, 1, 1)

        self.col3_cb = QComboBox(self.importFile_page)
        self.col3_cb.setObjectName(u"col3_cb")
        sizePolicy3.setHeightForWidth(self.col3_cb.sizePolicy().hasHeightForWidth())
        self.col3_cb.setSizePolicy(sizePolicy3)
        self.col3_cb.setMinimumSize(QSize(0, 30))
        self.col3_cb.setMaximumSize(QSize(16777215, 30))
        self.col3_cb.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.cols_grid.addWidget(self.col3_cb, 1, 2, 1, 1)

        self.col2_cb_2 = QComboBox(self.importFile_page)
        self.col2_cb_2.setObjectName(u"col2_cb_2")
        sizePolicy3.setHeightForWidth(self.col2_cb_2.sizePolicy().hasHeightForWidth())
        self.col2_cb_2.setSizePolicy(sizePolicy3)
        self.col2_cb_2.setMinimumSize(QSize(0, 30))
        self.col2_cb_2.setMaximumSize(QSize(16777215, 30))
        self.col2_cb_2.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.cols_grid.addWidget(self.col2_cb_2, 1, 3, 1, 1)

        self.col3_label_2 = QLabel(self.importFile_page)
        self.col3_label_2.setObjectName(u"col3_label_2")
        sizePolicy3.setHeightForWidth(self.col3_label_2.sizePolicy().hasHeightForWidth())
        self.col3_label_2.setSizePolicy(sizePolicy3)
        self.col3_label_2.setMinimumSize(QSize(0, 30))
        self.col3_label_2.setMaximumSize(QSize(16777215, 30))
        self.col3_label_2.setStyleSheet(u"QLabel {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}")
        self.col3_label_2.setAlignment(Qt.AlignCenter)

        self.cols_grid.addWidget(self.col3_label_2, 0, 3, 1, 1)

        self.col2_cb_5 = QComboBox(self.importFile_page)
        self.col2_cb_5.setObjectName(u"col2_cb_5")
        sizePolicy3.setHeightForWidth(self.col2_cb_5.sizePolicy().hasHeightForWidth())
        self.col2_cb_5.setSizePolicy(sizePolicy3)
        self.col2_cb_5.setMinimumSize(QSize(0, 30))
        self.col2_cb_5.setMaximumSize(QSize(16777215, 30))
        self.col2_cb_5.setStyleSheet(u"QComboBox{\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"        color: rgb(0, 170, 255);  /* \u4e0b\u62c9\u9879\u6587\u672c\u989c\u8272 */\n"
" }\n"
"QComboBox QAbstractItemView::item:hover {\n"
"        color: rgb(7, 255, 119); \n"
"}")

        self.cols_grid.addWidget(self.col2_cb_5, 1, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.cols_grid)

        self.verticalSpacer_2 = QSpacerItem(20, 200, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_4 = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.stackedWidget.addWidget(self.importFile_page)
        self.kpi_page = QWidget()
        self.kpi_page.setObjectName(u"kpi_page")
        self.verticalLayout_4 = QVBoxLayout(self.kpi_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.query_all_bt = QPushButton(self.kpi_page)
        self.query_all_bt.setObjectName(u"query_all_bt")
        sizePolicy.setHeightForWidth(self.query_all_bt.sizePolicy().hasHeightForWidth())
        self.query_all_bt.setSizePolicy(sizePolicy)
        self.query_all_bt.setMinimumSize(QSize(100, 30))
        self.query_all_bt.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid rgb(85, 170, 255);\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.query_all_bt)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.area_house_bar = BarChartView(self.kpi_page)
        self.area_house_bar.setObjectName(u"area_house_bar")

        self.verticalLayout_4.addWidget(self.area_house_bar)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.important_pie = PieChartView(self.kpi_page)
        self.important_pie.setObjectName(u"important_pie")

        self.horizontalLayout_12.addWidget(self.important_pie)

        self.normal_pie = PieChartView(self.kpi_page)
        self.normal_pie.setObjectName(u"normal_pie")

        self.horizontalLayout_12.addWidget(self.normal_pie)

        self.business_pie = PieChartView(self.kpi_page)
        self.business_pie.setObjectName(u"business_pie")

        self.horizontalLayout_12.addWidget(self.business_pie)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 5)
        self.stackedWidget.addWidget(self.kpi_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.container)

        self.bottomBar = QFrame(self.centralwidget)
        self.bottomBar.setObjectName(u"bottomBar")
        sizePolicy3.setHeightForWidth(self.bottomBar.sizePolicy().hasHeightForWidth())
        self.bottomBar.setSizePolicy(sizePolicy3)
        self.bottomBar.setMinimumSize(QSize(0, 40))
        self.bottomBar.setMaximumSize(QSize(16777215, 40))
        self.bottomBar.setStyleSheet(u"background-color: rgb(13, 9, 36);")
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.import_status = QLabel(self.bottomBar)
        self.import_status.setObjectName(u"import_status")
        self.import_status.setStyleSheet(u"QLabel {\n"
"	color: rgb(0, 170, 255);\n"
"}")

        self.horizontalLayout_9.addWidget(self.import_status)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.home_bt = QPushButton(self.bottomBar)
        self.home_bt.setObjectName(u"home_bt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.home_bt.sizePolicy().hasHeightForWidth())
        self.home_bt.setSizePolicy(sizePolicy4)
        self.home_bt.setMinimumSize(QSize(100, 26))
        self.home_bt.setMaximumSize(QSize(26, 26))
        self.home_bt.setLayoutDirection(Qt.LeftToRight)
        self.home_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.home_bt.setIcon(icon5)
        self.home_bt.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.home_bt)

        self.kpi_bt = QPushButton(self.bottomBar)
        self.kpi_bt.setObjectName(u"kpi_bt")
        self.kpi_bt.setMinimumSize(QSize(100, 26))
        self.kpi_bt.setMaximumSize(QSize(26, 26))
        self.kpi_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.kpi_bt.setIcon(icon6)
        self.kpi_bt.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.kpi_bt)

        self.download_bt = QPushButton(self.bottomBar)
        self.download_bt.setObjectName(u"download_bt")
        sizePolicy.setHeightForWidth(self.download_bt.sizePolicy().hasHeightForWidth())
        self.download_bt.setSizePolicy(sizePolicy)
        self.download_bt.setMinimumSize(QSize(100, 26))
        self.download_bt.setMaximumSize(QSize(26, 26))
        self.download_bt.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(13, 9, 36);\n"
"	border-radius: 13;\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(7, 255, 119);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.download_bt.setIcon(icon7)
        self.download_bt.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.download_bt)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.bottomBar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.min_bt.setText("")
        self.max_bt.setText("")
        self.close_bt.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6c47\u805a\u673a\u623f\u5229\u7528\u7387\u7edf\u8ba1\u5de5\u5177", None))
        self.module_bt.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u66f4\u65b0", None))
        self.setting_bt.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.search_percent_bt.setText(QCoreApplication.translate("MainWindow", u"\u6838\u5bf9", None))
        self.search_table_bt.setText(QCoreApplication.translate("MainWindow", u"\u8868\u67e5\u8be2", None))
        self.clear_table_bt.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u9ad8\u5ea6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6c47\u805a\u673a\u623f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u673a\u67b6\u4f4d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u6e05\u5355", None))
        self.select_file_bt.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.update_db_bt.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u7f13\u5b58", None))
        self.col1_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.col2_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.col3_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.col3_label_3.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.col3_label_2.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.query_all_bt.setText(QCoreApplication.translate("MainWindow", u"\u5168\u91cf\u5206\u6790", None))
        self.import_status.setText("")
        self.home_bt.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.kpi_bt.setText(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1\u62a5\u8868", None))
        self.download_bt.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
    # retranslateUi

