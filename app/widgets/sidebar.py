from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QScrollArea
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QLabel, QPushButton, QHBoxLayout

class SidebarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(280)
        self.setup_ui()

    def setup_ui(self):
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        main_layout.addWidget(scroll_area)

        # 滚动内容部件
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)
        content_layout = QVBoxLayout(scroll_content)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # 应用标题
        self.add_header(content_layout)

        # 主导航
        self.add_navigation(content_layout)

        # 本地目录
        self.add_local_directories(content_layout)

        # 我的相册
        self.add_albums(content_layout)

        # 智能分类
        self.add_smart_categories(content_layout)

        # 设置按钮
        self.add_settings_button(content_layout)

    def add_header(self, layout):
        header = QWidget()
        header.setStyleSheet("background-color: white; border-bottom: 1px solid #e5e7eb; padding: 16px;")
        header_layout = QVBoxLayout(header)

        title_label = QLabel("照片管理器")
        title_label.setFont(QFont("Pacifico", 16))
        title_label.setStyleSheet("color: #111827;")
        header_layout.addWidget(title_label)

        layout.addWidget(header)

    def add_navigation(self, layout):
        nav_widget = QWidget()
        nav_widget.setStyleSheet("padding: 8px 0;")
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setContentsMargins(16, 0, 16, 0)
        nav_layout.setSpacing(1)

        # 导航按钮
        nav_items = [
            ("全部照片", "fa-images"),
            ("最近导入", "fa-clock"),
            ("收藏夹", "fa-star")
        ]

        for text, icon in nav_items:
            btn = self.create_nav_button(text, icon)
            nav_layout.addWidget(btn)

        layout.addWidget(nav_widget)

    def add_local_directories(self, layout):
        # 实现本地目录部分
        dir_widget = QWidget()
        dir_layout = QVBoxLayout(dir_widget)
        dir_layout.setContentsMargins(16, 16, 16, 0)

        # 添加标题
        title = self.create_section_title("本地目录")
        dir_layout.addWidget(title)

        # 添加目录项
        dir_items = [
            ("我的图片", True),
            ("相机导入", True)
        ]

        for text, has_subdir in dir_items:
            btn = self.create_dir_button(text, has_subdir)
            dir_layout.addWidget(btn)

        layout.addWidget(dir_widget)

    def add_albums(self, layout):
        # 实现相册部分
        album_widget = QWidget()
        album_layout = QVBoxLayout(album_widget)
        album_layout.setContentsMargins(16, 16, 16, 0)

        # 添加标题
        title = self.create_section_title("我的相册")
        album_layout.addWidget(title)

        # 添加相册项
        album_items = [
            ("旅行记忆", "fa-mountain", 128),
            ("美食日记", "fa-utensils", 56),
            ("生日派对", "fa-birthday-cake", 42)
        ]

        for text, icon, count in album_items:
            btn = self.create_album_button(text, icon, count)
            album_layout.addWidget(btn)

        layout.addWidget(album_widget)

    def add_smart_categories(self, layout):
        # 实现智能分类部分
        smart_widget = QWidget()
        smart_layout = QVBoxLayout(smart_widget)
        smart_layout.setContentsMargins(16, 16, 16, 0)

        # 添加标题
        title = self.create_section_title("智能分类")
        smart_layout.addWidget(title)

        # 添加分类项
        category_items = [
            ("人物", "fa-user"),
            ("地点", "fa-map-marker-alt"),
            ("时间线", "fa-calendar-alt")
        ]

        for text, icon in category_items:
            btn = self.create_nav_button(text, icon)
            smart_layout.addWidget(btn)

        layout.addWidget(smart_widget)

    def add_settings_button(self, layout):
        settings_widget = QWidget()
        settings_widget.setStyleSheet("padding: 8px 0; border-top: 1px solid #e5e7eb;")
        settings_layout = QVBoxLayout(settings_widget)
        settings_layout.setContentsMargins(16, 0, 16, 0)

        btn = self.create_nav_button("设置", "fa-cog")
        settings_layout.addWidget(btn)

        layout.addWidget(settings_widget)

    def create_section_title(self, text):
        title = QLabel(text)
        title.setStyleSheet("color: #6b7280; font-size: 12px; font-weight: 600; margin-bottom: 8px;")
        return title

    def create_nav_button(self, text, icon):
        btn = QPushButton(text)
        # 设置按钮样式和图标（实际项目中需要集成FontAwesome）
        btn.setStyleSheet("""QPushButton { text-align: left; padding: 8px 12px; border-radius: 4px; background-color: transparent; }
QPushButton:hover { background-color: #f3f4f6; }""")
        return btn

    def create_dir_button(self, text, has_subdir):
        btn = QPushButton(text)
        btn.setStyleSheet("""QPushButton { text-align: left; padding: 8px 12px; border-radius: 4px; background-color: transparent; }
QPushButton:hover { background-color: #f3f4f6; }""")
        if has_subdir:
            # 添加下拉箭头（实际项目中需要实现）
            pass
        return btn

    def create_album_button(self, text, icon, count):
        btn = QPushButton(text)
        btn.setStyleSheet("""QPushButton { text-align: left; padding: 8px 12px; border-radius: 4px; background-color: transparent; }
QPushButton:hover { background-color: #f3f4f6; }""")
        # 添加照片数量标签（实际项目中需要实现）
        return btn