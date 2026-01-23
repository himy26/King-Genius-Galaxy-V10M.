import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QTabWidget, 
                             QTextEdit, QProgressBar, QFrame, QGroupBox, QGridLayout)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QFont, QIcon, QColor, QPalette

# --- تصميم الألوان (THEME: Dark Royal Blue & Gold) ---
STYLESHEET = """
QMainWindow {
    background-color: #1e1e2e;
}
QGroupBox {
    border: 2px solid #3e3e5e;
    border-radius: 8px;
    margin-top: 10px;
    font-weight: bold;
    color: #ffffff;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #a6accd;
}
QPushButton {
    background-color: #2b2b40;
    color: #ffffff;
    border: 1px solid #3e3e5e;
    border-radius: 5px;
    padding: 10px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #4e4e7e;
    border: 1px solid #6e6e9e;
}
QPushButton:pressed {
    background-color: #1e1e2e;
}
/* زر العمليات الخطيرة بلون مميز */
QPushButton#ActionBtn {
    background-color: #007acc;
    color: white;
}
QPushButton#ActionBtn:hover {
    background-color: #0098ff;
}
QTextEdit {
    background-color: #0f0f15;
    color: #00ff00; /* Hacker Green Text */
    border: 1px solid #3e3e5e;
    font-family: Consolas, Monospace;
    font-size: 12px;
}
QLabel {
    color: #cdd6f4;
    font-size: 14px;
}
QProgressBar {
    border: 1px solid #3e3e5e;
    border-radius: 5px;
    text-align: center;
    color: white;
    background-color: #1e1e2e;
}
QProgressBar::chunk {
    background-color: #007acc;
    width: 10px;
}
"""

class VisionPrinceGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VISION PRINCE TOOL - AI Mobile Utility v2.0")
        self.setGeometry(100, 100, 1100, 700)
        self.setStyleSheet(STYLESHEET)

        # الواجهة الرئيسية
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        
        # التخطيط العام (أفقي: قائمة جانبية + مساحة عمل)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # --- 1. القائمة الجانبية (Tabs) ---
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.West) # التبويبات على اليسار
        self.tabs.setFixedWidth(200)
        
        # إضافة الصفحات
        self.tab_dashboard = QWidget()
        self.tab_samsung = QWidget()
        self.tab_mtk = QWidget()
        
        self.tabs.addTab(self.tab_dashboard, "📱 Dashboard")
        self.tabs.addTab(self.tab_samsung, "🔵 SAMSUNG")
        self.tabs.addTab(self.tab_mtk, "🔴 MTK / BROM")
        
        main_layout.addWidget(self.tabs)

        # --- 2. مساحة العمل (Workspace) ---
        self.workspace_layout = QVBoxLayout()
        
        # منطقة المعلومات العلوية
        self.info_panel = QFrame()
        self.info_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.info_panel_layout = QHBoxLayout()
        
        self.lbl_status = QLabel("🔴 Status: Waiting for Device...")
        self.lbl_status.setStyleSheet("color: #ff5555; font-weight: bold;")
        self.lbl_model = QLabel("Model: N/A")
        self.lbl_port = QLabel("Port: COM --")
        
        self.info_panel_layout.addWidget(self.lbl_status)
        self.info_panel_layout.addStretch()
        self.info_panel_layout.addWidget(self.lbl_model)
        self.info_panel_layout.addWidget(self.lbl_port)
        self.info_panel.setLayout(self.info_panel_layout)
        
        self.workspace_layout.addWidget(self.info_panel)

        # منطقة الأزرار (تتغير حسب التبويب - هنا نضع مثال السامسونج)
        self.group_actions = QGroupBox("AI Quick Actions (Auto-Detect)")
        self.actions_layout = QGridLayout()
        
        # أزرار العمليات
        self.btn_frp = QPushButton("REMOVE FRP (All Samsung)")
        self.btn_frp.setObjectName("ActionBtn")
        self.btn_frp.clicked.connect(lambda: self.log("Starting FRP Bypass Process..."))
        
        self.btn_imei = QPushButton("REPAIR IMEI (Cert Patch)")
        self.btn_imei.clicked.connect(lambda: self.log("Initializing Modem for IMEI Repair..."))
        
        self.btn_factory = QPushButton("FACTORY RESET")
        self.btn_kg = QPushButton("UNLOCK KG / MDM")
        
        self.actions_layout.addWidget(self.btn_frp, 0, 0)
        self.actions_layout.addWidget(self.btn_imei, 0, 1)
        self.actions_layout.addWidget(self.btn_factory, 1, 0)
        self.actions_layout.addWidget(self.btn_kg, 1, 1)
        
        self.group_actions.setLayout(self.actions_layout)
        self.workspace_layout.addWidget(self.group_actions)

        # --- 3. سجل العمليات (Log Console) ---
        self.log_group = QGroupBox("System Log & AI Analysis")
        self.log_layout = QVBoxLayout()
        
        self.console = QTextEdit()
        self.console.setReadOnly(True)
        self.console.setText(" [*] Vision Prince AI System Initialized...\n [*] Waiting for USB Connection...")
        
        self.progress = QProgressBar()
        self.progress.setValue(0)
        
        self.log_layout.addWidget(self.console)
        self.log_layout.addWidget(self.progress)
        self.log_group.setLayout(self.log_layout)
        
        self.workspace_layout.addWidget(self.log_group)
        
        # إضافة الـ Workspace للتخطيط الرئيسي
        container = QWidget()
        container.setLayout(self.workspace_layout)
        main_layout.addWidget(container)

        # مؤقت للمحاكاة (سنربطه بالكود الخلفي لاحقاً)
        self.timer = QTimer()
        self.timer.timeout.connect(self.auto_detect_simulation)
        self.timer.start(3000) # كل 3 ثواني يحاول الكشف

    def log(self, message):
        """ دالة لإضافة نصوص للشاشة السوداء """
        self.console.append(f" > {message}")
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())

    def auto_detect_simulation(self):
        """ محاكاة اكتشاف جهاز ليرى المستخدم كيف ستعمل """
        # في البرنامج الحقيقي هنا نستدعي دالة الكشف من الكود السابق
        pass 
        # self.lbl_status.setText("🟢 Status: Device Connected!")
        # self.lbl_status.setStyleSheet("color: #55ff55; font-weight: bold;")

# تشغيل التطبيق
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # تعيين خط حديث
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = VisionPrinceGUI()
    window.show()
    sys.exit(app.exec())