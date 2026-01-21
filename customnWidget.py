from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QTimer, QTime,QPoint,QPointF,Signal,QRectF
from PySide6.QtGui import *
from PySide6.QtCharts import (QChart, QChartView, QPieSeries,QBarSet, QBarSeries, QChart, QChartView, QBarCategoryAxis,
    QPieSlice,QAbstractBarSeries)
import math
import pandas as pd

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
    pieClicked = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chart = QChart()
        
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        
        # 深色主题配色方案
        # self.slice_colors = [
        #     QColor(65, 105, 225),  # 皇家蓝
        #     QColor(50, 205, 50),   # 酸橙绿
        #     QColor(255, 165, 0),   # 橙色
        #     QColor(138, 43, 226),  # 紫罗兰
        #     QColor(220, 20, 60),   # 猩红
        #     QColor(0, 255, 255),   # 青色
        #     QColor(255, 0, 255)    # 洋红
        # ]
        self.slice_labels = {
            '已用完': QColor(255, 0, 0),
            '超期': QColor(255, 0, 0),
            '紧张': QColor(255, 215, 0),
            '预警': QColor(255, 255, 0),
            '充足': QColor(0, 255, 0),
            '正常': QColor(0, 255, 0),
            '零利用率': QColor(255, 192, 203),
            '传输': QColor(255, 0, 0),
            '无线': QColor(255, 215, 0),
            '城域网': QColor(255, 255, 0),
            '光缆': QColor(0, 255, 0),
            'IODF': QColor(255, 192, 203),
        }
        # 设置深色背景
        self.setDarkTheme()
        self.title_name = ''
        
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
        names = []
        self.title_name = title
        # 先计算数据总和
        total = sum(data_dict.values())
        
        # 添加数据切片并应用颜色
        for i, name in enumerate(self.slice_labels):
            if name not in data_dict:          # 如果某一项没有数据，可跳过或补 0
                continue
            value = data_dict[name]
            names.append(name)
            slice = series.append(name, value)
            # 设置标签格式：显示数值和百分比（使用固定的总和计算）
            percentage = (value / total * 100) if total > 0 else 0
            slice.setLabel(f"{percentage:.1f}%")
            slice.setLabelVisible(True)
            # 设置标签字体大小和颜色
            label_font = QFont()
            label_font.setPixelSize(12)  # 增大字体便于阅读
            label_font.setBold(True)     # 加粗字体
            slice.setLabelFont(label_font)
            slice.setLabelPosition(QPieSlice.LabelOutside)  # 外围显示
            # 设置标签连接线
            slice.setLabelArmLengthFactor(0.2)  # 连接线长度
            # 使用预设颜色
            slice.setBrush(self.slice_labels[name])
            slice.setLabelBrush(QColor(255, 255, 255))  # 白色标签文字
            slice.hovered.connect(self.onHovered)
            
        self.chart.removeAllSeries()
        self.chart.addSeries(series)
        # 设置图表动画
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        legend = self.chart.legend()
        legend.setVisible(True)
        legend.setAlignment(Qt.AlignBottom)
        # 获取所有图例标记并设置为原始name
        markers = legend.markers(series)
        for i, marker in enumerate(markers):
            if i < len(names):
                marker.setLabel(names[i])

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
                f"{int(slice.value())}"
            )
        else:
            QToolTip.hideText()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pieClicked.emit(self.title_name)
        super().mousePressEvent(event)

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

# 修改为接收Pandas DataFrame
class BarChartView(QChartView):
    # 定义点击信号，参数为：类别名称、分类名称
    barClicked = Signal(str, str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.chart = QChart()
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        # 预定义颜色调色板
        self.color_palette = {
            '已用完': QColor(255, 0, 0),
            '超期': QColor(255, 0, 0),
            '紧张': QColor(255, 215, 0),
            '预警': QColor(255, 255, 0),
            '充足': QColor(0, 255, 0),
            '正常': QColor(0, 255, 0),
            '零利用率': QColor(255, 192, 203),
        }
        # 设置深色主题
        self.setDarkTheme()
        self.df = pd.DataFrame()
        self.title_name = ''
    
    def setDarkTheme(self):
        """应用深色主题设置"""
        self.chart.setBackgroundBrush(QBrush(QColor(13, 9, 36)))
        self.chart.setTitleBrush(QBrush(QColor(255, 255, 255)))
        self.chart.legend().setLabelColor(QColor(200, 200, 200))
    
    def setData(self, df: pd.DataFrame, title):
        """
        接收Pandas DataFrame并绘制柱状图（无枚举依赖，100%无报错）
        功能：显示0值标签 + 所有标签在柱状图上方
        """
        # 清空图表原有内容（系列和坐标轴）
        self.title_name = title
        self.df = df
        self.df['合计'] = self.df.iloc[:, 1:].sum(axis=1)
        self.df['合计'] = self.df['合计'].astype('str')
        self.df['所属区县'] = self.df['所属区县'] + '[' + self.df['合计'] + ']'
        self.df.drop(columns=['合计'], inplace=True)
        self.chart.removeAllSeries()
        for axis in self.chart.axes(Qt.Horizontal):
            self.chart.removeAxis(axis)
        for axis in self.chart.axes(Qt.Vertical):
            self.chart.removeAxis(axis)

        # 1. 获取X轴分类标签（第一列：所属区县/区域）
        category_col = df.columns[0]
        x_labels = df[category_col].tolist()

        # 2. 获取数据列（除第一列外的所有列）
        data_columns = df.columns[1:].tolist()

        # 3. 为每个数据列创建QBarSet并填充数据
        bar_sets = []
        for col in data_columns:
            bar_set = QBarSet(col)
            bar_set.setColor(self.color_palette.get(col, QColor(128, 128, 128)))
            bar_data = df[col].tolist()
            bar_set.append(bar_data)
            bar_sets.append(bar_set)

        # 4. 创建QBarSeries并添加所有QBarSet
        series = QBarSeries()
        for bar_set in bar_sets:
            series.append(bar_set)
        
        # 核心修正：无枚举依赖的标签配置（终极兜底，无任何导入错误）
        series.setLabelsVisible(True)  # 强制显示所有标签（包括0值，关键）
        series.setLabelsFormat("@value")  # 标签显示为纯数值
        series.setLabelsPosition(QAbstractBarSeries.LabelsPosition.LabelsOutsideEnd)
        # 把标签整体抬高 6 像素（负值=向上，可视情况微调）
        series.setLabelsAngle(0)          # 保持水平
        
        self.chart.addSeries(series)
        # for bar_set in bar_sets:                # 对每个 QBarSet 生效
        #     bar_set.setLabelOffset(QPointF(0, -6))

        # 设置X轴
        axisX = QBarCategoryAxis()
        axisX.append(x_labels)
        axisX.setLabelsColor(QColor(255, 255, 255))
        axisX.setLinePenColor(QColor(255, 255, 255))
        self.chart.setAxisX(axisX, series)
        
        # 添加一个X轴标题，显示第二列的值
        axisX = QBarCategoryAxis()
        axisX.append(x_labels)
        axisX.setLabelsColor(QColor(255, 255, 255))
        axisX.setLinePenColor(QColor(255, 255, 255))
        self.chart.setAxisX(axisX, series)

        # 设置图表标题和图例
        self.chart.setTitle(title)
        self.chart.legend().setVisible(True)
        # legend右侧
        self.chart.legend().setAlignment(Qt.AlignRight)

    def mousePressEvent(self, event: QMouseEvent):
        """重写鼠标点击事件，处理坐标匹配逻辑"""
        if event.button() == Qt.LeftButton:
            # 1. 获取鼠标点击的屏幕像素坐标（相对于图表视图）
            screen_pos = event.pos()
            # print(f"\n鼠标点击屏幕坐标：({screen_pos.x()}, {screen_pos.y()})")
            # 2. 屏幕坐标 → 图表数值坐标（核心转换方法）
            value_pos = self.chart.mapToValue(screen_pos)
            chart_x = value_pos.x()  # X轴数值坐标（对应分类索引的浮点型）
            chart_y = value_pos.y()  # Y轴数值坐标（对应数据值的近似值）
            # print(f"转换为图表数值坐标：X={chart_x:.2f}, Y={chart_y:.2f}")
            bar_series = self.chart.series()[0]
            category_axis = self.chart.axes(Qt.Horizontal)[0]
            bar_sets = bar_series.barSets()

            # 3. 匹配 QBarCategoryAxis 的具体分类值
            categories = category_axis.categories()  # 获取所有分类标签
            category_count = len(categories)

            # 计算分类索引：对X轴数值坐标四舍五入取整，同时防止索引越界
            category_index = round(chart_x)
            if 0 <= category_index < category_count:
                target_category = categories[category_index]
                # print(f"匹配到 QBarCategoryAxis 分类值：{target_category}（索引：{category_index}）")
            else:
                # print("点击位置超出分类范围，无对应分类值")
                super().mousePressEvent(event)
                return
            area_name = target_category.split('[')[0]
            if chart_y < 0:
                self.barClicked.emit(area_name, '全部')
                super().mousePressEvent(event)
                return

            # 4. 计算 QBarSet 索引
            step = 0.5/len(bar_sets)
            bar_set_index = int((chart_x - category_index+0.25) / step)
            cols = self.df.columns[1:].tolist()
            if 0 <= bar_set_index < len(cols):
                bar_set_label = cols[bar_set_index]
                # print(f"匹配到 QBarSet[{bar_set_index}]：名称={bar_set_label}")
                self.barClicked.emit(area_name, bar_set_label)
        # 保留父类的鼠标事件行为
        super().mousePressEvent(event)

    
