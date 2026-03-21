# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FormatStrFormatter
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        MainWindow.setMinimumSize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.tabWidget)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pB_Gwyddion = QtWidgets.QPushButton(self.tab_3)
        self.pB_Gwyddion.setGeometry(QtCore.QRect(30, 50, 109, 41))
        self.pB_Gwyddion.setObjectName("pB_Gwyddion")
        self.pB_Labelstudio = QtWidgets.QPushButton(self.tab_3)
        self.pB_Labelstudio.setGeometry(QtCore.QRect(120, 200, 109, 41))
        self.pB_Labelstudio.setObjectName("pB_Labelstudio")
        self.pB_Composedset = QtWidgets.QPushButton(self.tab_3)
        self.pB_Composedset.setGeometry(QtCore.QRect(120, 250, 109, 31))
        self.pB_Composedset.setObjectName("pB_Composedset")
        self.pB_Opentopo = QtWidgets.QPushButton(self.tab_3)
        self.pB_Opentopo.setGeometry(QtCore.QRect(30, 95, 80, 30))
        self.pB_Opentopo.setObjectName("pB_Opentopo")
        self.lB_Toponame = QtWidgets.QLabel(self.tab_3)
        self.lB_Toponame.setGeometry(QtCore.QRect(32, 125, 121, 20))
        self.lB_Toponame.setObjectName("lB_Toponame")
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setGeometry(QtCore.QRect(30, 20, 250, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(30, 180, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.line_4 = QtWidgets.QFrame(self.tab_3)
        self.line_4.setGeometry(QtCore.QRect(10, 160, 621, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.tBR_Dataset = QtWidgets.QTextBrowser(self.tab_3)
        self.tBR_Dataset.setGeometry(QtCore.QRect(240, 200, 381, 261))
        self.tBR_Dataset.setObjectName("tBR_Dataset")
        self.tBR_Dataset.setText("")
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(20, 290, 56, 12))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_3)
        self.label_34.setGeometry(QtCore.QRect(90, 290, 81, 16))
        self.label_34.setObjectName("label_34")
        self.lE_TrainR = QtWidgets.QLineEdit(self.tab_3)
        self.lE_TrainR.setGeometry(QtCore.QRect(20, 310, 61, 20))
        self.lE_TrainR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lE_TrainR.setObjectName("lE_TrainR")
        self.lE_ValidR = QtWidgets.QLineEdit(self.tab_3)
        self.lE_ValidR.setGeometry(QtCore.QRect(100, 310, 61, 20))
        self.lE_ValidR.setObjectName("lE_ValidR")
        self.lE_ValidR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.label_35 = QtWidgets.QLabel(self.tab_3)
        self.label_35.setGeometry(QtCore.QRect(180, 290, 51, 16))
        self.label_35.setObjectName("label_35")
        self.lE_TestR = QtWidgets.QLineEdit(self.tab_3)
        self.lE_TestR.setGeometry(QtCore.QRect(170, 310, 61, 20))
        self.lE_TestR.setObjectName("lE_TestR")
        self.lE_TestR.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)


        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(474, 15, 147, 36))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/newPrefix/j3spm-AI36.png"))
        self.label_21.setObjectName("label_21")
        self.pB_Editclass = QtWidgets.QPushButton(self.tab_3)
        self.pB_Editclass.setGeometry(QtCore.QRect(20, 200, 91, 31))
        self.pB_Editclass.setObjectName("pB_Editclass")

        self.tBR_Imageinfo = QtWidgets.QTextBrowser(self.tab_3)
        self.tBR_Imageinfo.setGeometry(QtCore.QRect(260, 10, 201, 141))
        self.tBR_Imageinfo.setObjectName("tBR_Imageinfo")
        self.tBR_Imageinfo.setText("")
        self.pB_Labelme = QtWidgets.QPushButton(self.tab_3)
        self.pB_Labelme.setGeometry(QtCore.QRect(20, 350, 109, 41))
        self.pB_Labelme.setObjectName("pB_Labelme")
        self.pB_Labelme2yolo = QtWidgets.QPushButton(self.tab_3)
        self.pB_Labelme2yolo.setGeometry(QtCore.QRect(20, 400, 109, 31))
        self.pB_Labelme2yolo.setObjectName("pB_Labelme2yolo")
        self.pB_VideoToImages = QtWidgets.QPushButton(self.tab_3)
        self.pB_VideoToImages.setGeometry(QtCore.QRect(20, 450, 109, 31))
        self.pB_VideoToImages.setObjectName("pB_VideoToImages")

        # --- Responsive layout for 'Preparation' tab (tab_3) ---
        # 목표(사용자 요청 반영):
        #  - SPM IMG: Post-processing: [View Image | Gwyddion] (1행 2열)
        #  - AI Pre-processing 내부에 3개 묶음:
        #      * LabelImg: [Edit Classes | LabelImg] (1행 2열)
        #      * Label me: [Label me | Convert to yolov5] (1행 2열)
        #      * Compose dataset: 버튼 1줄 + Train/Validation/Test 1줄(한 줄에 모두)
        #  - 우측 정보창은 Image info(위) / Dataset info(아래)로 유지

        # Root layout on tab_3
        self._tab3_root_v = QtWidgets.QVBoxLayout(self.tab_3)
        self._tab3_root_v.setContentsMargins(10, 10, 10, 10)
        self._tab3_root_v.setSpacing(8)

        # Hide legacy absolute-position headings/lines (we use group boxes instead)
        for _w in (self.label_31, self.label_32, self.line_4):
            _w.setVisible(False)

        # Top row: logo aligned to the right
        self._tab3_logo_row = QtWidgets.QHBoxLayout()
        self._tab3_logo_row.setContentsMargins(0, 0, 0, 0)
        self._tab3_logo_row.addStretch(1)
        self.label_21.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self._tab3_logo_row.addWidget(self.label_21, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self._tab3_root_v.addLayout(self._tab3_logo_row)

        # Main horizontal splitter (left controls / right info)
        self._tab3_hsplit = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self.tab_3)
        self._tab3_hsplit.setChildrenCollapsible(False)
        self._tab3_root_v.addWidget(self._tab3_hsplit, 1)

        # ----------------------
        # Left: controls (grouped)
        # ----------------------
        self._tab3_left = QtWidgets.QWidget(self.tab_3)
        self._tab3_left_v = QtWidgets.QVBoxLayout(self._tab3_left)
        self._tab3_left_v.setContentsMargins(0, 0, 0, 0)
        self._tab3_left_v.setSpacing(10)

        # Group 1: Post-processing
        self.gb_post = QtWidgets.QGroupBox("SPM IMG: Post-processing", self._tab3_left)
        self._tab3_title_font_bold = QtGui.QFont()
        self._tab3_title_font_bold.setBold(True)
        self._tab3_title_font_normal = QtGui.QFont()
        self._tab3_title_font_normal.setBold(False)
        self.gb_post.setFont(self._tab3_title_font_bold)
        self.gb_post_v = QtWidgets.QVBoxLayout(self.gb_post)
        self.gb_post_v.setContentsMargins(10, 10, 10, 10)
        self.gb_post_v.setSpacing(6)

        self.gb_post_grid = QtWidgets.QGridLayout()
        self.gb_post_grid.setHorizontalSpacing(8)
        self.gb_post_grid.setVerticalSpacing(6)
        self.gb_post_grid.addWidget(self.pB_Opentopo, 0, 0)
        self.gb_post_grid.addWidget(self.pB_Gwyddion, 0, 1)
        self.pB_Opentopo.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.pB_Gwyddion.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.gb_post_v.addLayout(self.gb_post_grid)

        # Topography file name (keep as info line under buttons)
        self.lB_Toponame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.gb_post_v.addWidget(self.lB_Toponame)
        self.pB_Opentopo.setFont(self._tab3_title_font_normal)
        self.pB_Gwyddion.setFont(self._tab3_title_font_normal)
        self.lB_Toponame.setFont(self._tab3_title_font_normal)

        self._tab3_left_v.addWidget(self.gb_post)

        # Group 2: AI Pre-processing (contains 3 sub-groups)
        self.gb_ai = QtWidgets.QGroupBox("AI Pre-processing", self._tab3_left)
        self.gb_ai.setFont(self._tab3_title_font_bold)
        self.gb_ai_v = QtWidgets.QVBoxLayout(self.gb_ai)
        self.gb_ai_v.setContentsMargins(10, 10, 10, 10)
        self.gb_ai_v.setSpacing(10)

        # Sub-group: LabelImg
        self.gb_labelimg = QtWidgets.QGroupBox("LabelImg", self.gb_ai)
        self.gb_labelimg_grid = QtWidgets.QGridLayout(self.gb_labelimg)
        self.gb_labelimg_grid.setContentsMargins(10, 10, 10, 10)
        self.gb_labelimg_grid.setHorizontalSpacing(8)
        self.gb_labelimg_grid.setVerticalSpacing(6)
        self.gb_labelimg_grid.addWidget(self.pB_Editclass, 0, 0)
        self.gb_labelimg_grid.addWidget(self.pB_Labelstudio, 0, 1)
        self.pB_Editclass.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.pB_Labelstudio.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.gb_ai_v.addWidget(self.gb_labelimg)

        # Sub-group: Label me
        self.gb_labelme = QtWidgets.QGroupBox("Label me", self.gb_ai)
        self.gb_labelme_grid = QtWidgets.QGridLayout(self.gb_labelme)
        self.gb_labelme_grid.setContentsMargins(10, 10, 10, 10)
        self.gb_labelme_grid.setHorizontalSpacing(8)
        self.gb_labelme_grid.setVerticalSpacing(6)
        self.gb_labelme_grid.addWidget(self.pB_Labelme, 0, 0)
        self.gb_labelme_grid.addWidget(self.pB_Labelme2yolo, 0, 1)
        self.pB_Labelme.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.pB_Labelme2yolo.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.gb_ai_v.addWidget(self.gb_labelme)

        # Sub-group: Compose dataset
        self.gb_compose = QtWidgets.QGroupBox("Compose dataset", self.gb_ai)
        self.gb_compose_v = QtWidgets.QVBoxLayout(self.gb_compose)
        self.gb_compose_v.setContentsMargins(10, 10, 10, 10)
        self.gb_compose_v.setSpacing(8)

        self.pB_Composedset.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.gb_compose_v.addWidget(self.pB_Composedset)

        # Train/Validation/Test in a single row
        self._rates_row = QtWidgets.QHBoxLayout()
        self._rates_row.setSpacing(8)

        # Reuse existing labels so retranslateUi texts are kept
        for _lab in (self.label_33, self.label_34, self.label_35):
            _lab.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        for _le in (self.lE_TrainR, self.lE_ValidR, self.lE_TestR):
            _le.setFixedWidth(50)

        self._rates_row.addWidget(self.label_33)
        self._rates_row.addWidget(self.lE_TrainR)
        self._rates_row.addSpacing(8)
        self._rates_row.addWidget(self.label_34)
        self._rates_row.addWidget(self.lE_ValidR)
        self._rates_row.addSpacing(8)
        self._rates_row.addWidget(self.label_35)
        self._rates_row.addWidget(self.lE_TestR)
        self._rates_row.addStretch(1)

        self.gb_compose_v.addLayout(self._rates_row)
        self.gb_ai_v.addWidget(self.gb_compose)
        self.gb_labelimg.setFont(self._tab3_title_font_normal)
        self.gb_labelme.setFont(self._tab3_title_font_normal)
        self.gb_compose.setFont(self._tab3_title_font_normal)
        for _w in (self.pB_Editclass, self.pB_Labelstudio, self.pB_Labelme, self.pB_Labelme2yolo,
                   self.pB_Composedset, self.label_33, self.label_34, self.label_35,
                   self.lE_TrainR, self.lE_ValidR, self.lE_TestR):
            _w.setFont(self._tab3_title_font_normal)

        self._tab3_left_v.addWidget(self.gb_ai)

        # Group 3: Video Pre-processing
        self.gb_video = QtWidgets.QGroupBox("Video Pre-processing", self._tab3_left)
        self.gb_video.setFont(self._tab3_title_font_bold)
        self.gb_video_v = QtWidgets.QVBoxLayout(self.gb_video)
        self.gb_video_v.setContentsMargins(10, 10, 10, 10)
        self.gb_video_v.setSpacing(6)

        self.gb_video_grid = QtWidgets.QGridLayout()
        self.gb_video_grid.setHorizontalSpacing(8)
        self.gb_video_grid.setVerticalSpacing(6)
        self.gb_video_grid.setColumnStretch(0, 1)
        self.gb_video_grid.setColumnStretch(1, 1)
        self.gb_video_grid.addWidget(self.pB_VideoToImages, 0, 0)
        self.pB_VideoToImages.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.pB_VideoToImages.setMinimumHeight(self.pB_Opentopo.minimumSizeHint().height())
        self.gb_video_v.addLayout(self.gb_video_grid)

        # Add some vertical gap before the Video Pre-processing section
        self._tab3_video_spacer = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self._tab3_left_v.addItem(self._tab3_video_spacer)
        self.pB_VideoToImages.setFont(self._tab3_title_font_normal)
        self._tab3_left_v.addWidget(self.gb_video)


        # Push everything up
        self._tab3_left_v.addStretch(1)

        self._tab3_hsplit.addWidget(self._tab3_left)

        # ----------------------
        # Right: info split (Image / Dataset)
        # ----------------------
        self._tab3_right = QtWidgets.QWidget(self.tab_3)
        self._tab3_right_v = QtWidgets.QVBoxLayout(self._tab3_right)
        self._tab3_right_v.setContentsMargins(0, 0, 0, 0)
        self._tab3_right_v.setSpacing(8)

        self.gb_imginfo = QtWidgets.QGroupBox("Scanned Image information", self._tab3_right)
        self.gb_imginfo_v = QtWidgets.QVBoxLayout(self.gb_imginfo)
        self.gb_imginfo_v.setContentsMargins(8, 8, 8, 8)
        self.gb_imginfo_v.addWidget(self.tBR_Imageinfo)

        self.gb_datasetinfo = QtWidgets.QGroupBox("Dataset information", self._tab3_right)
        self.gb_datasetinfo_v = QtWidgets.QVBoxLayout(self.gb_datasetinfo)
        self.gb_datasetinfo_v.setContentsMargins(8, 8, 8, 8)
        self.gb_datasetinfo_v.addWidget(self.tBR_Dataset)

        self._tab3_vsplit = QtWidgets.QSplitter(QtCore.Qt.Vertical, self._tab3_right)
        self._tab3_vsplit.setChildrenCollapsible(False)
        self._tab3_vsplit.addWidget(self.gb_imginfo)
        self._tab3_vsplit.addWidget(self.gb_datasetinfo)
        self._tab3_vsplit.setStretchFactor(0, 1)
        self._tab3_vsplit.setStretchFactor(1, 2)

        self._tab3_right_v.addWidget(self._tab3_vsplit, 1)

        self._tab3_hsplit.addWidget(self._tab3_right)

        # Initial left/right ratio
        self._tab3_hsplit.setStretchFactor(0, 0)
        self._tab3_hsplit.setStretchFactor(1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        
        
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 30, 318, 138))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lE_Project = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lE_Project.setObjectName("lE_Project")
        self.gridLayout_6.addWidget(self.lE_Project, 5, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 2, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout_6.addWidget(self.label_25, 2, 0, 1, 2)
        self.lE_Model = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lE_Model.setObjectName("lE_Model")
        self.gridLayout_6.addWidget(self.lE_Model, 5, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 0, 3, 1, 1)
        # Hyper parameter path display: same behavior as Data path row
        self.lB_Hyper = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lB_Hyper.setObjectName("lB_Hyper")
        self.lB_Hyper.setReadOnly(True)
        self.lB_Hyper.setStyleSheet("background-color: white; border: 1px solid #B0B0B0; padding: 2px 6px;")
        self.lB_Hyper.setMinimumHeight(24)
        self.lB_Hyper.setMinimumWidth(180)
        self.lB_Hyper.setMaximumWidth(520)
        self.lB_Hyper.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.lB_Hyper.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lB_Hyper.setCursorPosition(0)
        # Data path display: user-resizable width with a maximum limit
        self.lB_DYaml = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lB_DYaml.setObjectName("lB_DYaml")
        self.lB_DYaml.setReadOnly(True)
        self.lB_DYaml.setStyleSheet("background-color: white; border: 1px solid #B0B0B0; padding: 2px 6px;")
        self.lB_DYaml.setMinimumHeight(24)
        self.lB_DYaml.setMinimumWidth(180)
        self.lB_DYaml.setMaximumWidth(520)
        self.lB_DYaml.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self.lB_DYaml.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lB_DYaml.setCursorPosition(0)
        self.cB_Cache = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.cB_Cache.setObjectName("cB_Cache")
        self.cB_Cache.setChecked(True)
        self.gridLayout_6.addWidget(self.cB_Cache, 2, 3, 1, 1)

        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 4, 3, 1, 1)
        self.sB_Batch = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sB_Batch.setObjectName("sB_Batch")
        self.sB_Batch.setMinimum(-1) 
        self.sB_Batch.setMaximum(500)
        self.sB_Batch.setValue(-1)
        self.gridLayout_6.addWidget(self.sB_Batch, 1, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 4, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout_6.addWidget(self.label_23, 0, 2, 1, 1)
        self.sB_Epochs = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sB_Epochs.setObjectName("sB_Epochs")
        self.sB_Epochs.setMaximum(1000)
        self.sB_Epochs.setValue(3)
        self.gridLayout_6.addWidget(self.sB_Epochs, 1, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.gridLayout_6.addWidget(self.comboBox, 3, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 4, 2, 1, 1)
        self.sB_IPixes = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.sB_IPixes.setObjectName("sB_IPixes")
        self.sB_IPixes.setMaximum(1024)
        self.sB_IPixes.setValue(640)
        self.gridLayout_6.addWidget(self.sB_IPixes, 1, 0, 1, 1)
        self.pB_DYaml = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB_DYaml.setObjectName("pB_DYaml")
        self.pB_DYaml.setMinimumWidth(70)
        self.pB_DYaml.setMaximumWidth(90)

        # Splitter for the Data row: the user can drag the divider,
        # and the path editor itself will never grow beyond its maximum width.
        self.dataYamlRow = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self.gridLayoutWidget)
        self.dataYamlRow.setObjectName("dataYamlRow")
        self.dataYamlRow.setChildrenCollapsible(False)
        self.dataYamlRow.setHandleWidth(6)
        self.dataYamlRow.setMinimumWidth(260)
        self.dataYamlRow.setMaximumWidth(620)
        self.dataYamlRow.addWidget(self.lB_DYaml)
        self.dataYamlRow.addWidget(self.pB_DYaml)
        self.dataYamlRow.setStretchFactor(0, 1)
        self.dataYamlRow.setStretchFactor(1, 0)
        self.dataYamlRow.setSizes([480, 80])
        self.gridLayout_6.addWidget(self.dataYamlRow, 3, 0, 1, 2)

        self.pB_Hyper = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pB_Hyper.setObjectName("pB_Hpyer")
        self.pB_Hyper.setMinimumWidth(70)
        self.pB_Hyper.setMaximumWidth(90)

        # Splitter for the Hyper parameter row: same layout as the Data row.
        self.hyperRow = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self.gridLayoutWidget)
        self.hyperRow.setObjectName("hyperRow")
        self.hyperRow.setChildrenCollapsible(False)
        self.hyperRow.setHandleWidth(6)
        self.hyperRow.setMinimumWidth(260)
        self.hyperRow.setMaximumWidth(620)
        self.hyperRow.addWidget(self.lB_Hyper)
        self.hyperRow.addWidget(self.pB_Hyper)
        self.hyperRow.setStretchFactor(0, 1)
        self.hyperRow.setStretchFactor(1, 0)
        self.hyperRow.setSizes([480, 80])
        self.gridLayout_6.addWidget(self.hyperRow, 5, 0, 1, 2)
        self.pB_Train = QtWidgets.QPushButton(self.tab_4)
        self.pB_Train.setGeometry(QtCore.QRect(10, 30, 109, 41))
        self.pB_Train.setObjectName("pB_Train")

        # Google Colab button (responsive: placed in action bar layout)
        self.pB_coLab = QtWidgets.QPushButton(self.tab_4)
        self.pB_coLab.setObjectName("pB_coLab")
        self.tBR_Train = QtWidgets.QTextBrowser(self.tab_4)
        self.tBR_Train.setGeometry(QtCore.QRect(10, 190, 625, 265))
        self.tBR_Train.setObjectName("tBR_Train")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 104, 80, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")

        self.label_37 = QtWidgets.QLabel(self.tab_4)
        self.label_37.setGeometry(QtCore.QRect(100, 74, 71, 23))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab_4)
        self.label_38.setGeometry(QtCore.QRect(10, 130, 111, 23))
        self.label_38.setObjectName("label_38")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 158, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_39 = QtWidgets.QLabel(self.tab_4)
        self.label_39.setGeometry(QtCore.QRect(10, 74, 71, 23))
        self.label_39.setObjectName("label_39")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 104, 80, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        # --- Clean GroupBox layout for 'Training' tab (tab_4) ---
        # Root layout
        self._tab4_root_v = QtWidgets.QVBoxLayout(self.tab_4)
        self._tab4_root_v.setContentsMargins(10, 10, 10, 10)
        self._tab4_root_v.setSpacing(8)

        # Action bar: Train button (left)
        self._tab4_actions = QtWidgets.QHBoxLayout()
        self._tab4_actions.setSpacing(6)
        self._tab4_actions.addWidget(self.pB_Train)
        self._tab4_actions.addStretch(1)
        self._tab4_actions.addWidget(self.pB_coLab)
        self._tab4_root_v.addLayout(self._tab4_actions)

        # Splitter: (top controls) / (log)
        self._tab4_split_v = QtWidgets.QSplitter(QtCore.Qt.Vertical, self.tab_4)
        self._tab4_root_v.addWidget(self._tab4_split_v)

        # --- Top controls area ---
        self._tab4_top = QtWidgets.QWidget(self.tab_4)
        self._tab4_top_h = QtWidgets.QHBoxLayout(self._tab4_top)
        self._tab4_top_h.setContentsMargins(0, 0, 0, 0)
        self._tab4_top_h.setSpacing(10)

        # Left: quick options
        self._tab4_gb_quick = QtWidgets.QGroupBox(self._tab4_top)
        self._tab4_gb_quick.setTitle("Quick Options")
        self._tab4_gb_quick_v = QtWidgets.QVBoxLayout(self._tab4_gb_quick)
        self._tab4_gb_quick_v.setContentsMargins(10, 10, 10, 10)
        self._tab4_gb_quick_v.setSpacing(8)

        self._tab4_quick_grid = QtWidgets.QGridLayout()
        self._tab4_quick_grid.setHorizontalSpacing(8)
        self._tab4_quick_grid.setVerticalSpacing(6)

        # Row 0/1: Action + Configure (use existing labels/combos)
        self._tab4_quick_grid.addWidget(self.label_39, 0, 0)
        self._tab4_quick_grid.addWidget(self.label_37, 0, 1)
        self._tab4_quick_grid.addWidget(self.comboBox_3, 1, 0)
        self._tab4_quick_grid.addWidget(self.comboBox_2, 1, 1)

        # Row 2/3: Additional options
        self._tab4_quick_grid.addWidget(self.label_38, 2, 0, 1, 2)
        # Additional options: use a wrapping editor for display/input, while keeping lineEdit_3 for compatibility
        self.lineEdit_3.setVisible(False)

        self._tab4_addopts = QtWidgets.QPlainTextEdit(self._tab4_gb_quick)
        self._tab4_addopts.setObjectName("_tab4_addopts")
        self._tab4_addopts.setTabChangesFocus(True)
        self._tab4_addopts.setPlaceholderText("")
        self._tab4_addopts.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)
        self._tab4_addopts.setMinimumHeight(55)
        self._tab4_addopts.setMaximumHeight(75)
        self._tab4_addopts.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self._tab4_addopts.setStyleSheet("background-color: white; border: 1px solid #B0B0B0; padding: 4px;")

        # Put the wrapping editor into the grid
        self._tab4_quick_grid.addWidget(self._tab4_addopts, 3, 0, 1, 2)
        self._tab4_quick_grid.setRowStretch(3, 0)

        # Sync: keep the underlying command as a single line in lineEdit_3
        def _tab4_sync_addopts_to_lineedit():
            txt = self._tab4_addopts.toPlainText().replace("\n", " ")
            if self.lineEdit_3.text() != txt:
                self.lineEdit_3.blockSignals(True)
                self.lineEdit_3.setText(txt)
                self.lineEdit_3.blockSignals(False)

        def _tab4_sync_lineedit_to_addopts(txt):
            if self._tab4_addopts.toPlainText() != txt:
                self._tab4_addopts.blockSignals(True)
                self._tab4_addopts.setPlainText(txt)
                self._tab4_addopts.blockSignals(False)

        self._tab4_addopts.textChanged.connect(_tab4_sync_addopts_to_lineedit)
        self.lineEdit_3.textChanged.connect(_tab4_sync_lineedit_to_addopts)

        # Initialize display from existing value
        _tab4_sync_lineedit_to_addopts(self.lineEdit_3.text())


        self._tab4_gb_quick_v.addLayout(self._tab4_quick_grid)
        self._tab4_gb_quick_v.addStretch(1)

        # Right: full training setup grid (existing gridLayoutWidget)
        self._tab4_gb_setup = QtWidgets.QGroupBox(self._tab4_top)
        self._tab4_gb_setup.setTitle("Training Setup")
        self._tab4_gb_setup_v = QtWidgets.QVBoxLayout(self._tab4_gb_setup)
        self._tab4_gb_setup_v.setContentsMargins(10, 10, 10, 10)
        self._tab4_gb_setup_v.setSpacing(6)

        # Reuse existing gridLayoutWidget content
        self.gridLayoutWidget.setParent(self._tab4_gb_setup)
        self.gridLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self._tab4_gb_setup_v.addWidget(self.gridLayoutWidget)

        # Keep the Training Setup area responsive, but prevent the Data path row
        # from making the whole panel excessively wide.
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 0)
        self.gridLayout_6.setColumnStretch(2, 0)
        self.gridLayout_6.setColumnStretch(3, 0)

        # Assemble top area
        self._tab4_top_h.addWidget(self._tab4_gb_quick, 0)
        self._tab4_top_h.addWidget(self._tab4_gb_setup, 1)

        # --- Log area ---
        self._tab4_gb_log = QtWidgets.QGroupBox(self.tab_4)
        self._tab4_gb_log.setTitle("Log")
        self._tab4_gb_log_v = QtWidgets.QVBoxLayout(self._tab4_gb_log)
        self._tab4_gb_log_v.setContentsMargins(10, 10, 10, 10)
        self._tab4_gb_log_v.setSpacing(6)

        self.tBR_Train.setParent(self._tab4_gb_log)
        self.tBR_Train.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        # Ensure non-transparent editor look
        self.tBR_Train.setStyleSheet("QTextBrowser { background-color: white; border: 1px solid #B0B0B0; }")
        self._tab4_gb_log_v.addWidget(self.tBR_Train)

        # Put into splitter
        self._tab4_split_v.addWidget(self._tab4_top)
        self._tab4_split_v.addWidget(self._tab4_gb_log)
        self._tab4_split_v.setStretchFactor(0, 0)
        self._tab4_split_v.setStretchFactor(1, 1)
        # ---------------------------------------------------------



        self.tabWidget.addTab(self.tab_4, "")
        
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.pB_Openimage = QtWidgets.QPushButton(self.tab_5)
        self.pB_Openimage.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.pB_Openimage.setObjectName("pB_Openimage")
        self.pB_Mode_select = QtWidgets.QPushButton(self.tab_5)
        self.pB_Mode_select.setGeometry(QtCore.QRect(10, 60, 91, 41))
        self.pB_Mode_select.setObjectName("pB_Mode_select")
        self.pB_Inference = QtWidgets.QPushButton(self.tab_5)
        self.pB_Inference.setGeometry(QtCore.QRect(10, 109, 61, 41))
        self.pB_Inference.setObjectName("pB_Inference")
        self.tBR_Result1 = QtWidgets.QTextBrowser(self.tab_5)
        self.tBR_Result1.setGeometry(QtCore.QRect(230, 10, 401, 91))
        self.tBR_Result1.setObjectName("tBR_Result1")
        self.tBR_Result2 = QtWidgets.QTextBrowser(self.tab_5)
        self.tBR_Result2.setGeometry(QtCore.QRect(262, 110, 369, 210))
        self.tBR_Result2.setObjectName("tBR_Result2")
        self.lB_imagname = QtWidgets.QLabel(self.tab_5)
        self.lB_imagname.setGeometry(QtCore.QRect(130, 20, 81, 16))
        self.lB_imagname.setObjectName("lB_imagname")
        self.lB_modelname = QtWidgets.QLabel(self.tab_5)
        self.lB_modelname.setGeometry(QtCore.QRect(130, 70, 91, 20))
        self.lB_modelname.setObjectName("lB_modelname")
        self.pB_Search = QtWidgets.QPushButton(self.tab_5)
        self.pB_Search.setGeometry(QtCore.QRect(10, 170, 91, 41))
        self.pB_Search.setObjectName("pB_Search")
        self.pB_Zoomscan = QtWidgets.QPushButton(self.tab_5)
        self.pB_Zoomscan.setGeometry(QtCore.QRect(10, 210, 91, 41))
        self.pB_Zoomscan.setObjectName("pB_Zoomscan")
        self.lE_Class = QtWidgets.QLineEdit(self.tab_5)
        self.lE_Class.setGeometry(QtCore.QRect(103, 189, 81, 20))
        self.lE_Class.setObjectName("lE_Class")
        self.lE_Class.setText('person')
        self.lE_Confi = QtWidgets.QLineEdit(self.tab_5)
        self.lE_Confi.setGeometry(QtCore.QRect(190, 189, 61, 20))
        self.lE_Confi.setObjectName("lE_Confi")
        self.lE_Confi.setText('25')
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_4.setGeometry(QtCore.QRect(72, 110, 70, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_61 = QtWidgets.QLabel(self.tab_5)
        self.label_61.setGeometry(QtCore.QRect(110, 170, 41, 16))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.tab_5)
        self.label_62.setGeometry(QtCore.QRect(110, 253, 41, 16))
        self.label_62.setObjectName("label_62")

        self.label_63 = QtWidgets.QLabel(self.tab_5)
        self.label_63.setGeometry(QtCore.QRect(130, 422, 41, 16))
        self.label_63.setObjectName("label_63")
        self.lB_Currentob = QtWidgets.QLabel(self.tab_5)
        self.lB_Currentob.setGeometry(QtCore.QRect(170, 422, 31, 16))
        self.lB_Currentob.setObjectName("lB_Currentob")
        self.lB_ClassQu = QtWidgets.QLabel(self.tab_5)
        self.lB_ClassQu.setGeometry(QtCore.QRect(110, 270, 41, 16))
        self.lB_ClassQu.setObjectName("lB_ClassQu")

        self.verticalLayoutWidget_15 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(260, 170, 371, 272))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")

        self.label_64 = QtWidgets.QLabel(self.tab_5)
        self.label_64.setGeometry(QtCore.QRect(20, 310, 91, 16))
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.tab_5)
        self.label_65.setGeometry(QtCore.QRect(100, 360, 91, 16))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.tab_5)
        self.label_66.setGeometry(QtCore.QRect(190, 170, 61, 16))
        self.label_66.setObjectName("label_66")
        self.pBA_ProgFS = QtWidgets.QProgressBar(self.tab_5)
        self.pBA_ProgFS.setGeometry(QtCore.QRect(20, 420, 111, 23))
        self.pBA_ProgFS.setProperty("value", 0)
        self.pBA_ProgFS.setObjectName("pBA_ProgFS")

        self.sB_ReXZ = QtWidgets.QSpinBox(self.tab_5)
        self.sB_ReXZ.setGeometry(QtCore.QRect(20, 330, 71, 22))
        self.sB_ReXZ.setObjectName("sB_ReXZ")
        self.sB_ReXZ.setMaximum(1000)
        self.sB_ReXZ.setValue(256)
        self.label_68 = QtWidgets.QLabel(self.tab_5)
        self.label_68.setGeometry(QtCore.QRect(110, 209, 56, 20))
        self.label_68.setObjectName("label_68")
        self.sB_indexZ = QtWidgets.QSpinBox(self.tab_5)
        self.sB_indexZ.setGeometry(QtCore.QRect(110, 228, 51, 22))
        self.sB_indexZ.setObjectName("sB_indexZ")
        self.sB_indexZ.setMaximum(1000)
        self.cB_Allobj = QtWidgets.QCheckBox(self.tab_5)
        self.cB_Allobj.setGeometry(QtCore.QRect(190, 222, 51, 16))
        self.cB_Allobj.setObjectName("cB_Allobj")
        self.pB_Zscanel = QtWidgets.QPushButton(self.tab_5)
        self.pB_Zscanel.setGeometry(QtCore.QRect(10, 250, 91, 41))
        self.pB_Zscanel.setObjectName("pB_Zscanel")
        self.cB_Sim = QtWidgets.QCheckBox(self.tab_5)
        self.cB_Sim.setGeometry(QtCore.QRect(190, 240, 61, 16))
        self.cB_Sim.setObjectName("cB_Sim")
        self.cB_Sim.setChecked(True)
        self.pB_Saveres = QtWidgets.QPushButton(self.tab_5)
        self.pB_Saveres.setGeometry(QtCore.QRect(147, 109, 56, 41))
        self.pB_Saveres.setObjectName("pB_Saveres")
        self.pB_Loadres = QtWidgets.QPushButton(self.tab_5)
        self.pB_Loadres.setGeometry(QtCore.QRect(205, 109, 56, 41))
        self.pB_Loadres.setObjectName("pB_Loadres")
        self.label_69 = QtWidgets.QLabel(self.tab_5)
        self.label_69.setGeometry(QtCore.QRect(100, 310, 81, 16))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.tab_5)
        self.label_70.setGeometry(QtCore.QRect(20, 360, 51, 16))
        self.label_70.setObjectName("label_70")
        self.dSB_Xlength = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.dSB_Xlength.setGeometry(QtCore.QRect(98, 330, 71, 22))
        self.dSB_Xlength.setObjectName("dSB_Xlength")
        self.dSB_Xlength.setValue(10)
        self.dSB_Xlength.setMaximum(1000)
        self.dSB_L2volt = QtWidgets.QDoubleSpinBox(self.tab_5)
        self.dSB_L2volt.setGeometry(QtCore.QRect(20, 380, 71, 22))
        self.dSB_L2volt.setObjectName("dSB_L2volt")
        self.dSB_L2volt.setValue(1)
        self.sB_LinesZ = QtWidgets.QSpinBox(self.tab_5)
        self.sB_LinesZ.setGeometry(QtCore.QRect(100, 380, 61, 22))
        self.sB_LinesZ.setObjectName("sB_LinesZ")
        self.sB_LinesZ.setMaximum(1000)

        self.sB_LinesZ.setValue(3)

        self.portCombo = QtWidgets.QComboBox(self.tab_5)
        self.portCombo.setGeometry(QtCore.QRect(335, 359, 151, 22))
        self.portCombo.setObjectName("comboBox")
        self.portCombo.setEnabled(False)
        self.pB_SerConect = QtWidgets.QPushButton(self.tab_5)
        self.pB_SerConect.setGeometry(QtCore.QRect(490, 351, 71, 31))
        self.pB_SerConect.setObjectName("pB_SerConect")
        self.pB_SerConect.setEnabled(False)

        self.cB_Serialout = QtWidgets.QCheckBox(self.tab_5)
        self.cB_Serialout.setGeometry(QtCore.QRect(260, 360, 81, 16))
        self.cB_Serialout.setObjectName("cB_Serialout")

        self.tBR_Serialput = QtWidgets.QTextBrowser(self.tab_5)
        self.tBR_Serialput.setGeometry(QtCore.QRect(260, 390, 371, 61))
        self.tBR_Serialput.setObjectName("tBR_Serialput")
        self.cB_Ethernet = QtWidgets.QCheckBox(self.tab_5)
        self.cB_Ethernet.setGeometry(QtCore.QRect(260, 330, 81, 16))
        self.cB_Ethernet.setObjectName("cB_Ethernet")
        self.cB_Ethernet.setChecked(True)
        self.lE_Port = QtWidgets.QLineEdit(self.tab_5)
        self.lE_Port.setGeometry(QtCore.QRect(570, 330, 61, 20))
        self.lE_Port.setObjectName("lE_Port")
        self.lE_Port.setText("8089")
        self.label_71 = QtWidgets.QLabel(self.tab_5)
        self.label_71.setGeometry(QtCore.QRect(540, 329, 41, 20))
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.tab_5)
        self.label_72.setGeometry(QtCore.QRect(331, 329, 56, 20))
        self.label_72.setObjectName("label_72")
        self.lE_Host = QtWidgets.QLineEdit(self.tab_5)
        self.lE_Host.setGeometry(QtCore.QRect(360, 329, 171, 20))
        self.lE_Host.setObjectName("lE_Host")
        self.lE_Host.setText("localhost")


        self.pB_SerDiscon = QtWidgets.QPushButton(self.tab_5)
        self.pB_SerDiscon.setGeometry(QtCore.QRect(560, 351, 71, 31))
        self.pB_SerDiscon.setObjectName("pB_SerDiscon")
        self.pB_SerDiscon.setEnabled(False)

        
                # --- Responsive/compact layout for 'Inference' tab (tab_5) ---
        # 목표(요청하신 스타일):
        #   1) 좌측 컨트롤을 3개의 GroupBox로 구분
        #      - Data/Model/Inference, Search, Zoom/Scan/Connection
        #   2) 우측 결과창은 Vertical splitter로 배치하고 Result1 높이를 조금 더 키움
        #   3) 창 크기 변경 시 우측 결과 영역이 주로 확장되도록 설정

        # Root (tab_5)
        self._tab5_root_h = QtWidgets.QHBoxLayout(self.tab_5)
        self._tab5_root_h.setContentsMargins(10, 10, 10, 10)
        self._tab5_root_h.setSpacing(10)

        self._tab5_split_h = QtWidgets.QSplitter(QtCore.Qt.Horizontal, self.tab_5)
        self._tab5_root_h.addWidget(self._tab5_split_h)

        # ---------------- Left: grouped control panel ----------------
        self._tab5_left = QtWidgets.QWidget(self.tab_5)
        self._tab5_left.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        self._tab5_left_v = QtWidgets.QVBoxLayout(self._tab5_left)
        self._tab5_left_v.setContentsMargins(0, 0, 0, 0)
        self._tab5_left_v.setSpacing(8)

        # --- Group 1: Data/Model/Inference ---
        self._tab5_gb_actions = QtWidgets.QGroupBox("Data / Model / Inference", self._tab5_left)
        self._tab5_gb_actions.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self._tab5_actions_grid = QtWidgets.QGridLayout(self._tab5_gb_actions)
        self._tab5_actions_grid.setContentsMargins(8, 10, 8, 8)
        self._tab5_actions_grid.setHorizontalSpacing(8)
        self._tab5_actions_grid.setVerticalSpacing(6)
        self._tab5_actions_grid.setColumnStretch(0, 0)
        self._tab5_actions_grid.setColumnStretch(1, 0)
        self._tab5_actions_grid.setColumnStretch(2, 1)
        self._tab5_actions_grid.setColumnStretch(3, 0)
        self._tab5_actions_grid.setColumnStretch(4, 0)

        # Row 0: Open data + selected image
        self._tab5_actions_grid.addWidget(self.pB_Openimage, 0, 0, 1, 1)
        self._tab5_actions_grid.addWidget(self.lB_imagname, 0, 1, 1, 4)

        # Row 1: Model select + selected model
        self._tab5_actions_grid.addWidget(self.pB_Mode_select, 1, 0, 1, 1)
        self._tab5_actions_grid.addWidget(self.lB_modelname, 1, 1, 1, 4)

        # Row 2: Inference + mode + save/load
        self._tab5_actions_grid.addWidget(self.pB_Inference, 2, 0, 1, 1)
        self._tab5_actions_grid.addWidget(self.comboBox_4, 2, 1, 1, 1)
        self._tab5_actions_grid.addWidget(self.pB_Saveres, 2, 2, 1, 1)
        self._tab5_actions_grid.addWidget(self.pB_Loadres, 2, 3, 1, 1)

        self._tab5_left_v.addWidget(self._tab5_gb_actions)

        # --- Group 2: Search ---
        self._tab5_gb_search = QtWidgets.QGroupBox("Search", self._tab5_left)
        self._tab5_gb_search.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        self._tab5_search_grid = QtWidgets.QGridLayout(self._tab5_gb_search)
        self._tab5_search_grid.setContentsMargins(8, 10, 8, 8)
        self._tab5_search_grid.setHorizontalSpacing(8)
        self._tab5_search_grid.setVerticalSpacing(6)

        self._tab5_search_grid.setColumnStretch(0, 0)
        self._tab5_search_grid.setColumnStretch(1, 0)
        self._tab5_search_grid.setColumnStretch(2, 1)
        self._tab5_search_grid.setColumnStretch(3, 0)
        self._tab5_search_grid.setColumnStretch(4, 0)

        self._tab5_search_grid.addWidget(self.pB_Search, 0, 0, 1, 1)
        self._tab5_search_grid.addWidget(self.label_61, 0, 1, 1, 1)
        self._tab5_search_grid.addWidget(self.lE_Class, 0, 2, 1, 1)
        self._tab5_search_grid.addWidget(self.label_66, 0, 3, 1, 1)
        self._tab5_search_grid.addWidget(self.lE_Confi, 0, 4, 1, 1)

        self._tab5_left_v.addWidget(self._tab5_gb_search)

        # --- Group 3: Zoom/Scan & Connection ---
        self._tab5_gb_scan = QtWidgets.QGroupBox("Zoom / Scan / Connection", self._tab5_left)
        self._tab5_gb_scan.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        self._tab5_scan_grid = QtWidgets.QGridLayout(self._tab5_gb_scan)
        self._tab5_scan_grid.setContentsMargins(8, 10, 8, 8)
        self._tab5_scan_grid.setHorizontalSpacing(8)
        self._tab5_scan_grid.setVerticalSpacing(6)

        # Columns: 0(btn/label) | 1(label) | 2(field) | 3(label) | 4(field/checkbox)
        self._tab5_scan_grid.setColumnStretch(0, 0)
        self._tab5_scan_grid.setColumnStretch(1, 0)
        self._tab5_scan_grid.setColumnStretch(2, 1)
        self._tab5_scan_grid.setColumnStretch(3, 0)
        self._tab5_scan_grid.setColumnStretch(4, 0)

        # Row 0: Zoom scan + Index + All/Simul.
        self._tab5_scan_grid.addWidget(self.pB_Zoomscan, 0, 0, 1, 1)
        self._tab5_scan_grid.addWidget(self.label_68, 0, 1, 1, 1)
        self._tab5_scan_grid.addWidget(self.sB_indexZ, 0, 2, 1, 1)
        self._tab5_scan_grid.addWidget(self.cB_Allobj, 0, 3, 1, 1)
        self._tab5_scan_grid.addWidget(self.cB_Sim, 0, 4, 1, 1)

        # Row 1: Cancel scan + Found + Img.#
        self._tab5_scan_grid.addWidget(self.pB_Zscanel, 1, 0, 1, 1)
        self._tab5_scan_grid.addWidget(self.label_62, 1, 1, 1, 1)
        self._tab5_scan_grid.addWidget(self.lB_ClassQu, 1, 2, 1, 1)
        self._tab5_scan_grid.addWidget(self.label_63, 1, 3, 1, 1)
        self._tab5_scan_grid.addWidget(self.lB_Currentob, 1, 4, 1, 1)

        # Row 2-5: Zoom scan parameters (2x2)
        self._tab5_zoom_grid = QtWidgets.QGridLayout()
        self._tab5_zoom_grid.setHorizontalSpacing(8)
        self._tab5_zoom_grid.setVerticalSpacing(6)
        self._tab5_zoom_grid.addWidget(self.label_64, 0, 0)
        self._tab5_zoom_grid.addWidget(self.label_69, 0, 1)
        self._tab5_zoom_grid.addWidget(self.sB_ReXZ, 1, 0)
        self._tab5_zoom_grid.addWidget(self.dSB_Xlength, 1, 1)
        self._tab5_zoom_grid.addWidget(self.label_70, 2, 0)
        self._tab5_zoom_grid.addWidget(self.label_65, 2, 1)
        self._tab5_zoom_grid.addWidget(self.dSB_L2volt, 3, 0)
        self._tab5_zoom_grid.addWidget(self.sB_LinesZ, 3, 1)

        self._tab5_scan_grid.addLayout(self._tab5_zoom_grid, 2, 0, 4, 5)

        # Spacer + Progress + Connection (moved progress above Ethernet)
        self._tab5_scan_grid.addItem(
            QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed),
            6, 0, 1, 5
        )

        # Progress bar (above Ethernet)
        self._tab5_scan_grid.addWidget(self.pBA_ProgFS, 7, 0, 1, 5)

        # Row 8-9: Connection settings
        self._tab5_conn_grid = QtWidgets.QGridLayout()
        self._tab5_conn_grid.setHorizontalSpacing(8)
        self._tab5_conn_grid.setVerticalSpacing(6)

        # Ethernet row
        self._tab5_conn_grid.addWidget(self.cB_Ethernet, 0, 0)
        self._tab5_conn_grid.addWidget(self.label_72, 0, 1)
        self._tab5_conn_grid.addWidget(self.lE_Host, 0, 2)
        self._tab5_conn_grid.addWidget(self.label_71, 0, 3)
        self._tab5_conn_grid.addWidget(self.lE_Port, 0, 4)

        # Serial row
        self._tab5_conn_grid.addWidget(self.cB_Serialout, 1, 0)
        self._tab5_conn_grid.addWidget(self.portCombo, 1, 2)
        self._tab5_conn_grid.addWidget(self.pB_SerConect, 1, 3)
        self._tab5_conn_grid.addWidget(self.pB_SerDiscon, 1, 4)

        self._tab5_scan_grid.addLayout(self._tab5_conn_grid, 8, 0, 2, 5)

        # Stretch below
        self._tab5_scan_grid.setRowStretch(10, 1)

        self._tab5_left_v.addWidget(self._tab5_gb_scan)
        self._tab5_left_v.addStretch(1)

        # ---------------- Right: output panes ----------------
        self._tab5_right = QtWidgets.QWidget(self.tab_5)
        self._tab5_right_v = QtWidgets.QVBoxLayout(self._tab5_right)
        self._tab5_right_v.setContentsMargins(0, 0, 0, 0)
        self._tab5_right_v.setSpacing(0)

        self._tab5_split_v = QtWidgets.QSplitter(QtCore.Qt.Vertical, self._tab5_right)
        self._tab5_right_v.addWidget(self._tab5_split_v)

        # Height tuning
        self.tBR_Result1.setMinimumHeight(160)
        self.tBR_Result2.setMinimumHeight(220)
        self.tBR_Serialput.setMinimumHeight(90)

        self.tBR_Result1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tBR_Result2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.tBR_Serialput.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self._tab5_split_v.addWidget(self.tBR_Result1)
        self._tab5_split_v.addWidget(self.tBR_Result2)
        self._tab5_split_v.addWidget(self.tBR_Serialput)

        # Default ratios (user can drag splitter)
        self._tab5_split_v.setStretchFactor(0, 2)
        self._tab5_split_v.setStretchFactor(1, 6)
        self._tab5_split_v.setStretchFactor(2, 1)

        # Put panels into main splitter
        self._tab5_split_h.addWidget(self._tab5_left)
        self._tab5_split_h.addWidget(self._tab5_right)
        self._tab5_split_h.setStretchFactor(0, 0)
        self._tab5_split_h.setStretchFactor(1, 1)
        # ---------------------------------------------------------
        self.tabWidget.addTab(self.tab_5, "")


        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.cB_viewImg = QtWidgets.QCheckBox(self.tab_6)
        self.cB_viewImg.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.cB_viewImg.setObjectName("cB_viewImg")
        self.cB_viewImg.setChecked(True)
        self.cB_saveTxt = QtWidgets.QCheckBox(self.tab_6)
        self.cB_saveTxt.setGeometry(QtCore.QRect(140, 60, 81, 16))
        self.cB_saveTxt.setObjectName("cB_saveTxt")
        self.cB_saveTxt.setChecked(True)
        self.cB_saveCsv = QtWidgets.QCheckBox(self.tab_6)
        self.cB_saveCsv.setGeometry(QtCore.QRect(230, 60, 81, 16))
        self.cB_saveCsv.setObjectName("cB_saveCsv")
        self.cB_saveCrop = QtWidgets.QCheckBox(self.tab_6)
        self.cB_saveCrop.setGeometry(QtCore.QRect(320, 60, 81, 16))
        self.cB_saveCrop.setObjectName("cB_saveCrop")
        self.cB_noSave = QtWidgets.QCheckBox(self.tab_6)
        self.cB_noSave.setGeometry(QtCore.QRect(410, 60, 81, 16))
        self.cB_noSave.setObjectName("cB_noSave")
        self.cB_agnoNms = QtWidgets.QCheckBox(self.tab_6)
        self.cB_agnoNms.setGeometry(QtCore.QRect(30, 90, 101, 16))
        self.cB_agnoNms.setObjectName("cB_agnoNms")
        self.cB_augment = QtWidgets.QCheckBox(self.tab_6)
        self.cB_augment.setGeometry(QtCore.QRect(140, 90, 81, 16))
        self.cB_augment.setObjectName("cB_augment")
        self.cB_visualize = QtWidgets.QCheckBox(self.tab_6)
        self.cB_visualize.setGeometry(QtCore.QRect(230, 90, 81, 16))
        self.cB_visualize.setObjectName("cB_visualize")
        self.cB_update = QtWidgets.QCheckBox(self.tab_6)
        self.cB_update.setGeometry(QtCore.QRect(320, 90, 81, 16))
        self.cB_update.setObjectName("cB_update")
        self.cB_existOk = QtWidgets.QCheckBox(self.tab_6)
        self.cB_existOk.setGeometry(QtCore.QRect(410, 90, 81, 16))
        self.cB_existOk.setObjectName("cB_existOk")
        self.cB_hideLab = QtWidgets.QCheckBox(self.tab_6)
        self.cB_hideLab.setGeometry(QtCore.QRect(30, 120, 81, 16))
        self.cB_hideLab.setObjectName("cB_hideLab")
        self.cB_hideConf = QtWidgets.QCheckBox(self.tab_6)
        self.cB_hideConf.setGeometry(QtCore.QRect(140, 120, 81, 16))
        self.cB_hideConf.setObjectName("cB_hideConf")
        self.cB_half = QtWidgets.QCheckBox(self.tab_6)
        self.cB_half.setGeometry(QtCore.QRect(230, 120, 61, 16))
        self.cB_half.setObjectName("cB_half")
        self.cB_dnn = QtWidgets.QCheckBox(self.tab_6)
        self.cB_dnn.setGeometry(QtCore.QRect(320, 120, 61, 16))
        self.cB_dnn.setObjectName("cB_dnn")
        self.cB_retina = QtWidgets.QCheckBox(self.tab_6)
        self.cB_retina.setGeometry(QtCore.QRect(410, 120, 91, 16))
        self.cB_retina.setObjectName("cB_retina")
        self.lE_prjname = QtWidgets.QLineEdit(self.tab_6)
        self.lE_prjname.setGeometry(QtCore.QRect(180, 240, 81, 20))
        self.lE_prjname.setObjectName("lE_prjname")
        self.lE_prjname.setText('proj')
        self.label_40 = QtWidgets.QLabel(self.tab_6)
        self.label_40.setGeometry(QtCore.QRect(190, 220, 56, 12))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab_6)
        self.label_41.setGeometry(QtCore.QRect(30, 160, 81, 16))
        self.label_41.setObjectName("label_41")
        self.dB_confThres = QtWidgets.QDoubleSpinBox(self.tab_6)
        self.dB_confThres.setGeometry(QtCore.QRect(30, 180, 71, 22))
        self.dB_confThres.setObjectName("dB_confThres")
        self.dB_confThres.setValue(0.25)
        self.label_42 = QtWidgets.QLabel(self.tab_6)
        self.label_42.setGeometry(QtCore.QRect(120, 160, 81, 16))
        self.label_42.setObjectName("label_42")
        self.dB_ioufThres = QtWidgets.QDoubleSpinBox(self.tab_6)
        self.dB_ioufThres.setGeometry(QtCore.QRect(120, 180, 71, 22))
        self.dB_ioufThres.setObjectName("dB_ioufThres")
        self.dB_ioufThres.setValue(0.35)
        self.label_43 = QtWidgets.QLabel(self.tab_6)
        self.label_43.setGeometry(QtCore.QRect(280, 220, 56, 12))
        self.label_43.setObjectName("label_43")
        self.lE_prjname_2 = QtWidgets.QLineEdit(self.tab_6)
        self.lE_prjname_2.setGeometry(QtCore.QRect(280, 240, 81, 20))
        self.lE_prjname_2.setObjectName("lE_prjname_2")
        self.lE_prjname_2.setText('inf')
        self.label_44 = QtWidgets.QLabel(self.tab_6)
        self.label_44.setGeometry(QtCore.QRect(210, 160, 81, 16))
        self.label_44.setObjectName("label_44")
        self.sB_maxDet = QtWidgets.QSpinBox(self.tab_6)
        self.sB_maxDet.setGeometry(QtCore.QRect(210, 180, 61, 22))
        self.sB_maxDet.setObjectName("sB_maxDet")
        self.sB_maxDet.setMaximum(3000)
        self.sB_maxDet.setValue(1000)
        self.label_45 = QtWidgets.QLabel(self.tab_6)
        self.label_45.setGeometry(QtCore.QRect(310, 160, 91, 16))
        self.label_45.setObjectName("label_45")
        self.sB_lineThick = QtWidgets.QSpinBox(self.tab_6)
        self.sB_lineThick.setGeometry(QtCore.QRect(310, 180, 61, 22))
        self.sB_lineThick.setObjectName("sB_lineThick")
        self.sB_lineThick.setValue(1)
        self.label_46 = QtWidgets.QLabel(self.tab_6)
        self.label_46.setGeometry(QtCore.QRect(410, 160, 91, 16))
        self.label_46.setObjectName("label_46")
        self.sB_vidStride = QtWidgets.QSpinBox(self.tab_6)
        self.sB_vidStride.setGeometry(QtCore.QRect(410, 180, 61, 22))
        self.sB_vidStride.setObjectName("sB_vidStride")
        self.sB_vidStride.setValue(1)
        self.label_47 = QtWidgets.QLabel(self.tab_6)
        self.label_47.setGeometry(QtCore.QRect(380, 220, 56, 12))
        self.label_47.setObjectName("label_47")
        self.lE_device = QtWidgets.QLineEdit(self.tab_6)
        self.lE_device.setGeometry(QtCore.QRect(380, 240, 81, 20))
        self.lE_device.setObjectName("lE_device")
        self.label_48 = QtWidgets.QLabel(self.tab_6)
        self.label_48.setGeometry(QtCore.QRect(30, 20, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.tab_6)
        self.label_49.setGeometry(QtCore.QRect(30, 220, 56, 12))
        self.label_49.setObjectName("label_49")
        self.lE_classes = QtWidgets.QLineEdit(self.tab_6)
        self.lE_classes.setGeometry(QtCore.QRect(30, 240, 121, 20))
        self.lE_classes.setObjectName("lE_classes")
        self.cB_saveConf = QtWidgets.QCheckBox(self.tab_6)
        self.cB_saveConf.setGeometry(QtCore.QRect(500, 60, 81, 16))
        self.cB_saveConf.setObjectName("cB_saveConf")

        # --- Responsive layout for 'Settings' tab (tab_6) ---
        self._tab6_root_v = QtWidgets.QVBoxLayout(self.tab_6)
        self._tab6_root_v.setContentsMargins(10, 10, 10, 10)
        self._tab6_root_v.setSpacing(10)

        self._tab6_root_v.addWidget(self.label_48)

        # Save options
        self._tab6_save_box = QtWidgets.QGroupBox(self.tab_6)
        self._tab6_save_box.setTitle("Save / Output")
        self._tab6_save_grid = QtWidgets.QGridLayout(self._tab6_save_box)
        self._tab6_save_grid.addWidget(self.cB_viewImg, 0, 0)
        self._tab6_save_grid.addWidget(self.cB_saveTxt, 0, 1)
        self._tab6_save_grid.addWidget(self.cB_saveCsv, 0, 2)
        self._tab6_save_grid.addWidget(self.cB_saveCrop, 0, 3)
        self._tab6_save_grid.addWidget(self.cB_saveConf, 0, 4)
        self._tab6_save_grid.addWidget(self.cB_noSave, 0, 5)
        self._tab6_root_v.addWidget(self._tab6_save_box)

        # Inference flags
        self._tab6_flag_box = QtWidgets.QGroupBox(self.tab_6)
        self._tab6_flag_box.setTitle("Inference Options")
        self._tab6_flag_grid = QtWidgets.QGridLayout(self._tab6_flag_box)
        self._tab6_flag_grid.addWidget(self.cB_agnoNms, 0, 0)
        self._tab6_flag_grid.addWidget(self.cB_augment, 0, 1)
        self._tab6_flag_grid.addWidget(self.cB_visualize, 0, 2)
        self._tab6_flag_grid.addWidget(self.cB_update, 0, 3)
        self._tab6_flag_grid.addWidget(self.cB_existOk, 0, 4)
        self._tab6_flag_grid.addWidget(self.cB_hideLab, 1, 0)
        self._tab6_flag_grid.addWidget(self.cB_hideConf, 1, 1)
        self._tab6_flag_grid.addWidget(self.cB_half, 1, 2)
        self._tab6_flag_grid.addWidget(self.cB_dnn, 1, 3)
        self._tab6_flag_grid.addWidget(self.cB_retina, 1, 4)
        self._tab6_root_v.addWidget(self._tab6_flag_box)

        # Thresholds / numeric settings
        self._tab6_num_box = QtWidgets.QGroupBox(self.tab_6)
        self._tab6_num_box.setTitle("Thresholds / Limits")
        self._tab6_num_grid = QtWidgets.QGridLayout(self._tab6_num_box)
        self._tab6_num_grid.addWidget(self.label_41, 0, 0)
        self._tab6_num_grid.addWidget(self.dB_confThres, 1, 0)
        self._tab6_num_grid.addWidget(self.label_42, 0, 1)
        self._tab6_num_grid.addWidget(self.dB_ioufThres, 1, 1)
        self._tab6_num_grid.addWidget(self.label_44, 0, 2)
        self._tab6_num_grid.addWidget(self.sB_maxDet, 1, 2)
        self._tab6_num_grid.addWidget(self.label_45, 0, 3)
        self._tab6_num_grid.addWidget(self.sB_lineThick, 1, 3)
        self._tab6_num_grid.addWidget(self.label_46, 0, 4)
        self._tab6_num_grid.addWidget(self.sB_vidStride, 1, 4)
        self._tab6_root_v.addWidget(self._tab6_num_box)

        # Project / class / device
        self._tab6_misc_box = QtWidgets.QGroupBox(self.tab_6)
        self._tab6_misc_box.setTitle("Names / Device")
        self._tab6_misc_grid = QtWidgets.QGridLayout(self._tab6_misc_box)
        self._tab6_misc_grid.addWidget(self.label_49, 0, 0)
        self._tab6_misc_grid.addWidget(self.lE_classes, 1, 0, 1, 2)
        self._tab6_misc_grid.addWidget(self.label_40, 0, 2)
        self._tab6_misc_grid.addWidget(self.lE_prjname, 1, 2)
        self._tab6_misc_grid.addWidget(self.label_43, 0, 3)
        self._tab6_misc_grid.addWidget(self.lE_prjname_2, 1, 3)
        self._tab6_misc_grid.addWidget(self.label_47, 0, 4)
        self._tab6_misc_grid.addWidget(self.lE_device, 1, 4)
        self._tab6_root_v.addWidget(self._tab6_misc_box)

        self._tab6_root_v.addStretch(1)
        # ---------------------------------------------------------

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_h = QtWidgets.QWidget()
        self.tab_h.setObjectName("tab_h")

        self.tabWidget.addTab(self.tab_h, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        self.pB_Gwyddion.clicked.connect(MainWindow.do_gwyddion) # type: ignore
        self.pB_Labelstudio.clicked.connect(MainWindow.do_labelstudio) # type: ignore
        self.pB_Openimage.clicked.connect(MainWindow.do_openimg) # type: ignore
        self.pB_Mode_select.clicked.connect(MainWindow.do_modelselect) # type: ignore
        self.pB_Inference.clicked.connect(MainWindow.do_inference) # type: ignore
        self.pB_Train.clicked.connect(MainWindow.do_training) # type: ignore
        self.pB_DYaml.clicked.connect(MainWindow.do_dataload) # type: ignore
        self.pB_Hyper.clicked.connect(MainWindow.do_hyperload) # type: ignore
        self.pB_Search.clicked.connect(MainWindow.do_search) # type: ignore
        self.pB_Zoomscan.clicked.connect(MainWindow.do_zscan) # type: ignore
        self.pB_Zscanel.clicked.connect(MainWindow.do_zscancancel) # type: ignore
        self.pB_Saveres.clicked.connect(MainWindow.do_saveres) # type: ignore
        self.pB_Loadres.clicked.connect(MainWindow.do_loadres) # type: ignore
        self.pB_Composedset.clicked.connect(MainWindow.do_composedset) # type: ignore
        self.pB_Opentopo.clicked.connect(MainWindow.do_opentopo)
        self.pB_SerConect.clicked.connect(MainWindow.do_Sercon) # type: ignore
        self.comboBox.currentIndexChanged.connect(MainWindow.do_combobox)
        self.comboBox_2.currentIndexChanged.connect(MainWindow.do_combobox_2)
        self.cB_Serialout.stateChanged.connect(MainWindow.do_Serset)
        self.cB_Ethernet.stateChanged.connect(MainWindow.do_Tcpip)
        self.pB_Editclass.clicked.connect(MainWindow.do_Editclass) # type: ignore
        self.pB_SerDiscon.clicked.connect(MainWindow.do_Serdis) # type: ignore
        self.pB_Labelme.clicked.connect(MainWindow.do_labelme) # type: ignore
        self.pB_Labelme2yolo.clicked.connect(MainWindow.do_labelme2yolo) # type: ignore
        self.pB_VideoToImages.clicked.connect(MainWindow.do_video2img)


        self.comboBox_3.currentIndexChanged.connect(MainWindow.do_combobox_3)
        self.comboBox_4.currentIndexChanged.connect(MainWindow.do_combobox_4)
        self.pB_coLab.clicked.connect(MainWindow.do_coLab)



        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "J3SPM_AIMODULE V1.0.0"))
      
        self.pB_Gwyddion.setText(_translate("MainWindow", "Gwyddion"))
        self.pB_Labelstudio.setText(_translate("MainWindow", "Labelimg"))
        self.pB_Composedset.setText(_translate("MainWindow", "Compose dataset"))
        self.pB_Opentopo.setText(_translate("MainWindow", "View Image"))
        self.lB_Toponame.setText(_translate("MainWindow", ""))
        self.label_31.setText(_translate("MainWindow", "SPM IMG: Post-processing"))
        self.label_32.setText(_translate("MainWindow", "AI Pre-processing"))
        self.label_33.setText(_translate("MainWindow", "Train(%)"))
        self.label_34.setText(_translate("MainWindow", "Validation(%)"))
        self.lE_TrainR.setText(_translate("MainWindow", "80"))
        self.lE_ValidR.setText(_translate("MainWindow", "10"))
        self.label_35.setText(_translate("MainWindow", "Test(%)"))
        self.lE_TestR.setText(_translate("MainWindow", "10"))
        self.pB_Editclass.setText(_translate("MainWindow", "Edit Classes"))
        self.pB_Labelme.setText(_translate("MainWindow", "Label me"))
        self.pB_Labelme2yolo.setText(_translate("MainWindow", "Convert to yolov5"))
        self.pB_VideoToImages.setText(_translate("MainWindow", "Video to images"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Preparation"))
        self.label_26.setText(_translate("MainWindow", "Weights"))
        self.label_25.setText(_translate("MainWindow", "Data"))
        self.label_22.setText(_translate("MainWindow", "Img Pixels"))
        self.label_24.setText(_translate("MainWindow", "Epochs"))
        self.lB_Hyper.setText(_translate("MainWindow", "default"))
        self.lB_DYaml.setText(_translate("MainWindow", "None"))
        self.cB_Cache.setText(_translate("MainWindow", "Cache On"))
        self.label_30.setText(_translate("MainWindow", "Model"))
        self.label_28.setText(_translate("MainWindow", "Hyper parameter"))
        self.label_23.setText(_translate("MainWindow", "Batch"))
        self.comboBox.setItemText(0, _translate("MainWindow", "YOLOv5s"))
        self.comboBox.setItemText(1, _translate("MainWindow", "YOLOv5m"))
        self.comboBox.setItemText(2, _translate("MainWindow", "YOLOv5l"))
        self.comboBox.setItemText(3, _translate("MainWindow", "YOLOv5x"))
        self.comboBox.setItemText(4, _translate("MainWindow", "YOLOv5n"))
        self.comboBox.setItemText(5, _translate("MainWindow", ""))

        self.label_29.setText(_translate("MainWindow", "Project"))
        self.pB_DYaml.setText(_translate("MainWindow", "Select"))
        self.pB_Hyper.setText(_translate("MainWindow", "Select"))
        self.pB_Train.setText(_translate("MainWindow", "Train"))
        self.label_37.setText(_translate("MainWindow", "Configure"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "YOLOv5s"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "YOLOv5m"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "YOLOv5l"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "YOLOv5x"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "YOLOv5n"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", ""))

        self.label_38.setText(_translate("MainWindow", "Additonal options"))
        self.label_39.setText(_translate("MainWindow", "Action"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Detection"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Segmenation"))
        self.pB_coLab.setText(_translate("MainWindow", "Google colab."))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Training"))
        self.pB_Openimage.setText(_translate("MainWindow", "Open Data"))
        self.pB_Mode_select.setText(_translate("MainWindow", "Model select"))
        self.pB_Inference.setText(_translate("MainWindow", "Inference"))
        self.lB_imagname.setText(_translate("MainWindow", "Img file"))
        self.lB_modelname.setText(_translate("MainWindow", "Model file"))

        self.lB_imagname.setText(_translate("MainWindow", "select image"))
        self.lB_modelname.setText(_translate("MainWindow", "select model"))
        
        self.pB_Search.setText(_translate("MainWindow", "Search"))
        self.pB_Zoomscan.setText(_translate("MainWindow", "Zoom Scan"))
        self.label_61.setText(_translate("MainWindow", "Class"))
        self.label_62.setText(_translate("MainWindow", "Found"))
        self.label_63.setText(_translate("MainWindow", "Img.#:"))
        self.lB_Currentob.setText(_translate("MainWindow", "0"))
        self.lB_ClassQu.setText(_translate("MainWindow", "0"))
        self.label_64.setText(_translate("MainWindow", "ResX"))
        self.label_65.setText(_translate("MainWindow", "Line scans"))
        self.label_66.setText(_translate("MainWindow", "Conf.(%)"))

        self.label_68.setText(_translate("MainWindow", "Index"))
        self.cB_Allobj.setText(_translate("MainWindow", "All"))
        self.pB_Zscanel.setText(_translate("MainWindow", "Cancel Scan"))
        self.cB_Sim.setText(_translate("MainWindow", "Simul."))
        self.pB_Saveres.setText(_translate("MainWindow", "Save"))
        self.pB_Saveres.setEnabled(False)
        self.pB_Loadres.setText(_translate("MainWindow", "Load"))
        self.pB_Loadres.setEnabled(False)
        self.label_69.setText(_translate("MainWindow", "X leng(um)"))
        self.label_70.setText(_translate("MainWindow", "len/volt"))
        self.pB_SerConect.setText(_translate("MainWindow", "Connect"))
        self.cB_Serialout.setText(_translate("MainWindow", "Enable"))
        self.cB_Ethernet.setText(_translate("MainWindow", "Ethernet"))
        self.label_71.setText(_translate("MainWindow", "port:"))
        self.label_72.setText(_translate("MainWindow", "Host:"))
        self.pB_SerDiscon.setText(_translate("MainWindow", "Discon"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Detect"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Segment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Inference/Send"))
        
        self.cB_viewImg.setText(_translate("MainWindow", "view img"))
        self.cB_saveTxt.setText(_translate("MainWindow", "save txt"))
        self.cB_saveCsv.setText(_translate("MainWindow", "save csv"))
        self.cB_saveCrop.setText(_translate("MainWindow", "save crop"))
        self.cB_noSave.setText(_translate("MainWindow", "no save"))
        self.cB_agnoNms.setText(_translate("MainWindow", "agnostic nms"))
        self.cB_augment.setText(_translate("MainWindow", "augment"))
        self.cB_visualize.setText(_translate("MainWindow", "visualize"))
        self.cB_update.setText(_translate("MainWindow", "update"))
        self.cB_existOk.setText(_translate("MainWindow", "exist ok"))
        self.cB_hideLab.setText(_translate("MainWindow", "hide labels"))
        self.cB_hideConf.setText(_translate("MainWindow", "hide conf"))
        self.cB_half.setText(_translate("MainWindow", "half"))
        self.cB_dnn.setText(_translate("MainWindow", "dnn"))
        self.cB_retina.setText(_translate("MainWindow", "retina masks"))
        self.label_40.setText(_translate("MainWindow", "Project"))
        self.label_41.setText(_translate("MainWindow", "Conf. Thres."))
        self.label_42.setText(_translate("MainWindow", "IOU. Thres."))
        self.label_43.setText(_translate("MainWindow", "Name"))
        self.label_44.setText(_translate("MainWindow", "Max detection"))
        self.label_45.setText(_translate("MainWindow", "Line Thickness"))
        self.label_46.setText(_translate("MainWindow", "Video stride"))
        self.label_47.setText(_translate("MainWindow", "Device"))
        self.label_48.setText(_translate("MainWindow", "Inference options"))
        self.label_49.setText(_translate("MainWindow", "Classes"))
        self.cB_saveConf.setText(_translate("MainWindow", "save conf"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Settings"))

import resource_rc

