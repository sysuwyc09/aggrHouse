from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QTimer, QTime,QPoint
from PySide6.QtGui import *
from PySide6.QtCharts import QChart, QChartView, QPieSeries,QBarSet, QBarSeries, QChart, QChartView, QBarCategoryAxis
import math

class CircularProgress(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.target_value = 0
        self.min_value = 0
        self.max_value = 100
        self.progress_width = 50
        self.text_color = QColor(0, 170, 255)
        self.font_size = 20
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.animation_duration = 100  # 2秒动画
        self.animation_start_time = 0
        self.animation_start_value = 0
        
    def setValue(self, value):
        self.target_value = min(max(value, self.min_value), self.max_value)
        self.animation_start_value = self.value
        self.animation_start_time = QTime.currentTime().msecsSinceStartOfDay()
        self.timer.start(16)  # 约60帧/秒
        
    def update_animation(self):
        current_time = QTime.currentTime().msecsSinceStartOfDay()
        elapsed = current_time - self.animation_start_time
        
        if elapsed >= self.animation_duration:
            self.value = self.target_value
            self.timer.stop()
        else:
            # 使用缓动函数使动画更平滑
            progress = elapsed / self.animation_duration
            self.value = int(self.animation_start_value + 
                           (self.target_value - self.animation_start_value) * 
                           (1 - (1 - progress) ** 3))  # 三次缓动
            
        self.update()
        
    def paintEvent(self, event):
        width = min(self.width(), self.height()) - self.progress_width
        progress = (self.value - self.min_value) / (self.max_value - self.min_value) * 360
        # 修正颜色逻辑
        if self.value >= 90:
            color = QColor(255, 0, 0)  # 红色
        elif self.value >= 70:
            color = QColor(255, 165, 0)  # 橙色
        elif self.value >= 50:
            color = QColor(255, 215, 0)  # 金色
        else:
            color = QColor(0, 255, 0)  # 绿色    
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制背景圆
        pen = QPen()
        pen.setColor(QColor(200, 200, 200))
        pen.setWidth(self.progress_width)
        painter.setPen(pen)
        painter.drawEllipse(self.progress_width//2, self.progress_width//2, 
                           width, width)
        
        # 绘制进度圆
        pen.setColor(color)
        painter.setPen(pen)
        painter.drawArc(self.progress_width//2, self.progress_width//2, 
                       width, width, 90 * 16, -progress * 16)
        
        # 绘制百分比文本
        font = QFont()
        font.setPixelSize(self.font_size)
        painter.setFont(font)
        painter.setPen(QPen(self.text_color))
        painter.drawText(self.rect(), Qt.AlignCenter, f"{self.value}%")


class PieChartView(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chart = QChart()
        
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        
        # 深色主题配色方案
        self.slice_colors = [
            QColor(65, 105, 225),  # 皇家蓝
            QColor(50, 205, 50),   # 酸橙绿
            QColor(255, 165, 0),   # 橙色
            QColor(138, 43, 226),  # 紫罗兰
            QColor(220, 20, 60),   # 猩红
            QColor(0, 255, 255),   # 青色
            QColor(255, 0, 255)    # 洋红
        ]
        
        # 设置深色背景
        self.setDarkTheme()
        
    def setDarkTheme(self):
        """应用深色主题设置"""
        # 背景色
        self.chart.setBackgroundBrush(QBrush(QColor(13, 9, 36)))
        # 标题颜色
        self.chart.setTitleBrush(QBrush(QColor(255, 255, 255)))
        # 图例颜色
        self.chart.legend().setLabelColor(QColor(200, 200, 200))
        
    def setData(self, data_dict,title):
        """设置数据，自动循环使用预设颜色"""
        series = QPieSeries()
        self.chart.setTitle(title)
        
        # 添加数据切片并应用颜色
        for i, (name, value) in enumerate(data_dict.items()):
            slice = series.append(name, value)
            slice.setLabelVisible(False)
            slice.hovered.connect(self.onHovered)
            
            # 循环使用预设颜色
            color_index = i % len(self.slice_colors)
            slice.setBrush(self.slice_colors[color_index])
            
        self.chart.removeAllSeries()
        self.chart.addSeries(series)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignRight)
        
    def onHovered(self, state):
        slice = self.sender()
        if state:
            # 获取饼图中心点
            center = self.chart.plotArea().center()
            # 计算中间角度
            mid_angle = slice.startAngle() + slice.angleSpan() / 2
            radius = self.chart.plotArea().width() / 2 * 0.7
            x = center.x() + radius * math.cos(math.radians(mid_angle))
            y = center.y() - radius * math.sin(math.radians(mid_angle))
            
            QToolTip.showText(
                self.mapToGlobal(QPoint(int(x), int(y))),
                f"{slice.label()}: {slice.value()} ({slice.percentage()*100:.1f}%)"
            )
        else:
            QToolTip.hideText()


# 自定义个窗体显示 错误信息 列名为专业、设备型号，输入list
class ErrorInfoForm(QFrame):
    def __init__(self, parent=None, error_list=[]):
        super().__init__(parent)
        self.error_list = error_list
        self.initUI()

    def initUI(self):
        self.setWindowTitle('高度录入缺少')
        self.setGeometry(100, 100, 300, 200)
        # 设置暗黑风格
        # self.setStyleSheet('background-color: #333; color: #fff;')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        # 用 tableWidget显示
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['专业', '设备型号'])
        # 设置表头样式
        # self.tableWidget.horizontalHeader().setStyleSheet('''
        #     QHeaderView::section {
        #         background-color: #333;
        #         color: #fff;
        #         padding: 5px;
        #         border: none;
        #     }
        # ''')
        # self.tableWidget.verticalHeader().setStyleSheet('''
        #     QHeaderView::section {
        #         background-color: #444;
        #         color: #fff;
        #         padding: 5px;
        #         border: none;
        #     }
        # ''')
        self.tableWidget.setRowCount(len(self.error_list))
        for i in range(0,len(self.error_list)):
            self.tableWidget.setItem(i,0,QTableWidgetItem(self.error_list[i][0]))
            self.tableWidget.setItem(i,1,QTableWidgetItem(self.error_list[i][1]))
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        # 设置列扩展
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        # 设置表格样式
        # self.tableWidget.setStyleSheet('background-color: #333; color: #fff;')

        # 用 按钮 关闭
        self.closeButton = QPushButton('关闭')
        self.layout.addWidget(self.closeButton)

        self.closeButton.clicked.connect(self.close)

class BarChartView(QChartView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chart = QChart()
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        # 预定义16种颜色（可根据需要扩展）
        self.color_palette = [
            QColor(65, 105, 225),   # 皇家蓝
            QColor(220, 20, 60),    # 猩红
            QColor(50, 205, 50),    # 酸橙绿
            QColor(255, 165, 0),    # 橙色
            QColor(138, 43, 226),   # 紫罗兰
            QColor(0, 255, 255),    # 青色
            QColor(255, 0, 255),    # 洋红
            QColor(255, 215, 0),    # 金色
            QColor(0, 139, 139),    # 深青色
            QColor(148, 0, 211),    # 深紫罗兰
            QColor(255, 99, 71),    # 番茄色
            QColor(60, 179, 113),   # 海洋绿
            QColor(238, 130, 238),  # 紫罗兰
            QColor(255, 140, 0),    # 深橙色
            QColor(70, 130, 180),   # 钢蓝色
            QColor(205, 92, 92)     # 印度红
        ]
        # 设置深色主题
        self.setDarkTheme()
    def setDarkTheme(self):
        """应用深色主题设置"""
        self.chart.setBackgroundBrush(QBrush(QColor(13, 9, 36)))
        self.chart.setTitleBrush(QBrush(QColor(255, 255, 255)))
        self.chart.legend().setLabelColor(QColor(200, 200, 200))
    
    def setData(self, data_dict, title):
        self.chart.removeAllSeries()  
        # 获取所有分类
        categories = {category for class_data in data_dict.values() 
                           for category in class_data.keys()}
        # 为每个分类创建QBarSet并分配颜色
        bar_sets = {}
        for i, category in enumerate(categories):
            bar_set = QBarSet(category)
            bar_sets[category] = bar_set
            
            # 循环使用颜色调色板
            color_index = i % len(self.color_palette)
            bar_set.setColor(self.color_palette[color_index])
        
        # 填充数据
        class_names = []
        for class_name, class_data in data_dict.items():
            class_names.append(class_name)
            for category in categories:
                value = class_data.get(category, 0)
                bar_sets[category].append(value)
        
        # 创建柱状图系列并添加数据
        series = QBarSeries()
        for bar_set in bar_sets.values():
            series.append(bar_set)
            
        # 启用标签显示并设置格式
        series.setLabelsVisible(True)
        series.setLabelsFormat("@value")
        
        self.chart.addSeries(series)
        
        # 设置X轴
        axisX = QBarCategoryAxis()
        axisX.append(class_names)
        axisX.setLabelsColor(QColor(255, 255, 255))
        axisX.setLinePenColor(QColor(255, 255, 255))
        self.chart.setAxisX(axisX, series)
        
        # 设置图表标题和图例
        self.chart.setTitle(title)
        self.chart.legend().setVisible(True)
        # legend右侧
        self.chart.legend().setAlignment(Qt.AlignRight)
