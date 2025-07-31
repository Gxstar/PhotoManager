from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGridLayout, QPushButton

class InfoPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(320)
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 标题栏
        header = QWidget()
        header.setStyleSheet("background-color: white; border-bottom: 1px solid #e5e7eb; padding: 16px;")
        header_layout = QVBoxLayout(header)

        title_label = QLabel("照片详情")
        title_label.setStyleSheet("font-size: 16px; font-weight: 600; color: #111827;")
        header_layout.addWidget(title_label)

        main_layout.addWidget(header)

        # 内容区域
        content = QWidget()
        content.setStyleSheet("padding: 16px;")
        content_layout = QVBoxLayout(content)
        content_layout.setSpacing(24)

        # 照片预览
        self.add_photo_preview(content_layout)

        # 照片信息
        self.add_photo_info(content_layout)

        # 快速操作
        self.add_quick_actions(content_layout)

        # 添加到相册
        self.add_to_albums(content_layout)

        main_layout.addWidget(content)

    def add_photo_preview(self, layout):
        preview_frame = QFrame()
        preview_frame.setStyleSheet("border: 1px solid #e5e7eb; border-radius: 4px; padding: 8px; background-color: white;")
        preview_layout = QVBoxLayout(preview_frame)

        # 占位图片
        img_label = QLabel()
        pixmap = QPixmap(300, 200)
        pixmap.fill(Qt.lightGray)
        img_label.setPixmap(pixmap)
        img_label.setAlignment(Qt.AlignCenter)
        preview_layout.addWidget(img_label)

        layout.addWidget(preview_frame)

    def add_photo_info(self, layout):
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setSpacing(12)

        # 信息项
        info_items = [
            ("文件名", "sunset_mountains_2023.jpg"),
            ("拍摄时间", "2023 年 7 月 15 日 18:23"),
            ("文件信息", "JPEG · 3.2 MB · 4000 × 3000"),
            ("拍摄地点", "黄山, 中国"),
            ("相机信息", "Canon EOS R5 · f/8 · 1/125s · ISO 100")
        ]

        for label, value in info_items:
            row = QWidget()
            row_layout = QVBoxLayout(row)
            row_layout.setSpacing(4)

            label_widget = QLabel(label)
            label_widget.setStyleSheet("font-size: 12px; color: #6b7280;")
            value_widget = QLabel(value)
            value_widget.setStyleSheet("font-size: 14px;")

            row_layout.addWidget(label_widget)
            row_layout.addWidget(value_widget)
            info_layout.addWidget(row)

        layout.addWidget(info_widget)

    def add_quick_actions(self, layout):
        actions_widget = QWidget()
        actions_layout = QVBoxLayout(actions_widget)
        actions_layout.setSpacing(8)

        # 标题
        title = QLabel("快速操作")
        title.setStyleSheet("font-size: 12px; font-weight: 600; color: #6b7280; margin-bottom: 4px;")
        actions_layout.addWidget(title)

        # 按钮网格
        grid_layout = QGridLayout()
        grid_layout.setSpacing(8)

        # 操作按钮
        action_buttons = [
            ("编辑", "fa-edit"),
            ("分享", "fa-share-alt"),
            ("删除", "fa-trash-alt"),
            ("标签", "fa-tags")
        ]

        for i, (text, icon) in enumerate(action_buttons):
            btn = QPushButton(text)
            btn.setStyleSheet("padding: 8px; border: 1px solid #e5e7eb; border-radius: 4px; background-color: white; text-align: left;")
            grid_layout.addWidget(btn, i//2, i%2)

        actions_layout.addLayout(grid_layout)
        layout.addWidget(actions_widget)

    def add_to_albums(self, layout):
        albums_widget = QWidget()
        albums_layout = QVBoxLayout(albums_widget)
        albums_layout.setSpacing(8)

        # 标题
        title = QLabel("添加到相册")
        title.setStyleSheet("font-size: 12px; font-weight: 600; color: #6b7280; margin-bottom: 4px;")
        albums_layout.addWidget(title)

        # 相册项
        album_items = [
            ("旅行记忆", "fa-mountain"),
            ("美食日记", "fa-utensils"),
            ("新建相册", "fa-plus")
        ]

        for text, icon in album_items:
            btn = QPushButton(text)
            btn.setStyleSheet("padding: 8px; border: 1px solid #e5e7eb; border-radius: 4px; background-color: white; text-align: left;")
            albums_layout.addWidget(btn)

        layout.addWidget(albums_widget)