from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("照片管理器")
        self.setGeometry(100, 100, 1200, 800)

        # 创建中央部件和主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QHBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # 创建三栏式布局占位符
        self.create_sidebar()
        self.create_content_area()
        self.create_info_panel()

    def create_sidebar(self):
        from app.widgets.sidebar import SidebarWidget
        self.sidebar = SidebarWidget()
        self.main_layout.addWidget(self.sidebar, 1)

    def create_content_area(self):
        from app.widgets.photo_grid import PhotoGridWidget
        self.content_area = PhotoGridWidget()
        self.main_layout.addWidget(self.content_area, 3)

    def create_info_panel(self):
        from app.widgets.info_panel import InfoPanelWidget
        self.info_panel = InfoPanelWidget()
        self.main_layout.addWidget(self.info_panel, 1)