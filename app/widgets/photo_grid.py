from PySide6.QtWidgets import QWidget, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QLineEdit, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListView, QPushButton, QHBoxLayout, QLineEdit

class PhotoGridWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # 主布局
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 添加工具栏
        self.add_toolbar(main_layout)

        # 照片网格视图
        self.photo_view = QListView()
        self.photo_view.setViewMode(QListView.IconMode)
        self.photo_view.setIconSize(QSize(180, 180))
        self.photo_view.setSpacing(16)
        self.photo_view.setResizeMode(QListView.Adjust)
        self.photo_view.setStyleSheet("background-color: #f9fafb; padding: 24px;")

        # 设置模型（临时数据）
        self.setup_model()

        main_layout.addWidget(self.photo_view)

    def add_toolbar(self, layout):
        toolbar = QWidget()
        toolbar.setStyleSheet("background-color: white; border-bottom: 1px solid #e5e7eb; padding: 12px 24px;")
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout.setSpacing(16)

        # 视图切换按钮
        view_layout = QHBoxLayout()
        view_layout.setSpacing(4)

        grid_btn = QPushButton("网格视图")
        grid_btn.setStyleSheet("padding: 4px 12px; border-radius: 4px; background-color: #f3f4f6;")
        list_btn = QPushButton("列表视图")
        list_btn.setStyleSheet("padding: 4px 12px; border-radius: 4px; background-color: transparent;")

        view_layout.addWidget(grid_btn)
        view_layout.addWidget(list_btn)
        toolbar_layout.addLayout(view_layout)

        # 搜索框
        search_layout = QHBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("搜索照片...")
        search_input.setStyleSheet("padding: 6px 12px; border: 1px solid #d1d5db; border-radius: 4px; width: 240px;")
        search_layout.addWidget(search_input)
        toolbar_layout.addLayout(search_layout)

        # 排序和筛选
        sort_layout = QHBoxLayout()
        sort_layout.setSpacing(4)

        sort_btn = QPushButton("按日期")
        sort_btn.setStyleSheet("padding: 4px 12px; border-radius: 4px; background-color: transparent;")
        filter_btn = QPushButton("筛选")
        filter_btn.setStyleSheet("padding: 4px 12px; border-radius: 4px; background-color: transparent;")

        sort_layout.addWidget(sort_btn)
        sort_layout.addWidget(filter_btn)
        toolbar_layout.addLayout(sort_layout)

        # 右对齐
        toolbar_layout.addStretch()

        layout.addWidget(toolbar)

    def setup_model(self):
        # 创建临时模型和数据
        model = QStandardItemModel()
        self.photo_view.setModel(model)

        # 添加示例照片项（实际项目中会从数据库加载）
        for i in range(12):
            item = QStandardItem(f"示例照片 {i+1}")
            # 设置占位符图标（实际项目中会加载缩略图）
            item.setData(QSize(180, 180), Qt.SizeHintRole)
            model.appendRow(item)