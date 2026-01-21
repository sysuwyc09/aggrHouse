# 从main_ui继承Ui_MainWindow类
from main_ui import Ui_MainWindow
from PySide6 import QtCore
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from main_ui import Ui_MainWindow
from fileThread import *
from publicFunc import *
from customnWidget import ErrorInfoForm
import time


class Mainwin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwin, self).__init__()
        #隐藏标题栏
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # 添加鼠标拖动相关变量
        self.drag_pos = QtCore.QPoint()
        self.setupUi(self)  # 调用Ui_MainWindow的setupUi方法


        # 点击关闭按钮，关闭窗口
        self.close_bt.clicked.connect(self.close)
        # 点击最小化按钮，最小化窗口
        self.min_bt.clicked.connect(self.showMinimized)
        # 点击最大化按钮，判断是否为最大，是则最小化，不是则最大化
        self.max_bt.clicked.connect(self.maximize_restore)
        self.module_bt.clicked.connect(self.pageSelect)
        self.home_bt.clicked.connect(self.pageSelect)
        self.kpi_bt.clicked.connect(self.pageSelect)
        self.fileTypeCols = [
            '设备高度', '汇聚机房', '机架位', '设备清单'
        ]
        self.fileCols = [
            ['专业', '设备型号', '设备高度'],
            ['所属区县', '所属站点', '机房名称', '业务级别', '生命周期状态','入网时间'],
            ['所属机房',  '装机位置编号'],
            ['设备名称', '所属机房', '设备型号', '生命周期状态']
        ]
        # 类型页面初始隐藏
        self.type_frame.setVisible(False)
        self.fileType_cb.currentIndexChanged.connect(self.changeColLabel)
        self.fileType_cb.addItems(self.fileTypeCols)
        self.currentCols = []
        self.currentLis = []
        self.select_file_bt.clicked.connect(self.choseFile)
        self.update_db_bt.clicked.connect(self.updateDataBase)
        self.keys_le.returnPressed.connect(self.searchHouse)
        self.search_percent_bt.clicked.connect(self.searchOneHousePercent)
        self.rack_df = pd.DataFrame()
        self.device_df = pd.DataFrame()
        self.table_df = pd.DataFrame()
        self.download_bt.clicked.connect(self.downLoadFile)
        self.setting_bt.clicked.connect(self.pageSelect)
        self.search_table_bt.clicked.connect(self.searchTable)
        self.clear_table_bt.clicked.connect(self.clearDataBaseTable)
        # TopN 页面按钮查询
        self.topN_bt.clicked.connect(self.pageSelect)
        self.search_topN_bt.clicked.connect(self.searchTopNHouse)
        self.search_work_bt.clicked.connect(self.searchWorkHouse)
        # 初始页面为home页面
        self.stackedWidget.setCurrentIndex(0)

        self.area_house_bar.barClicked.connect(self.onBarClicked)
        self.important_pie.pieClicked.connect(self.onAggrHouseDetail)
        self.normal_pie.pieClicked.connect(self.onAggrHouseDetail)
        self.business_pie.pieClicked.connect(self.onAggrHouseDetail)

    def searchWorkHouse(self):
        yellow_num = self.yellow_month_QB.value()
        red_num = self.red_month_QB.value()
        if yellow_num >= red_num:
            QMessageBox.information(self, '提示', '预警阈值应小于超期阈值')
            return;
        self.search_work_thread = queryWorkHouseThread(yellow_num,red_num)
        self.search_work_thread.state_signal.connect(self.showStatus)
        self.search_work_thread.area_signal.connect(self.showAreaCol)
        self.search_work_thread.pie_signal.connect(self.showAllPie)
        self.search_work_thread.dataframe_signal.connect(self.showWorkDataFrame)
        self.search_work_thread.start()

    def showWorkDataFrame(self, area_table,house_df,all_table):
        self.device_df = area_table
        self.rack_df = house_df
        self.table_df = all_table
        if house_df.shape[0] == 0:
            QMessageBox.information(self, '提示', '没有符合条件的机房')
            return;
        self.showWorkTable(house_df)


    def showWorkTable(self, work_df):
        work_df = work_df[['所属区县','机房名称','业务级别','生命周期状态','入网时间','已入网时间(月)','建设情况']].copy().reset_index(drop=True)
        work_df = work_df.astype(str)
        self.topN_tw.setRowCount(work_df.shape[0])
        cols = ['所属区县','机房名称','业务级别','生命周期状态','入网时间','已入网时间(月)','建设情况']
        self.topN_tw.setColumnCount(work_df.shape[1])
        self.topN_tw.setHorizontalHeaderLabels(cols)

        # 机房名称列随内容扩展
        self.topN_tw.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        # 建设情况列隐藏
        self.topN_tw.setColumnHidden(6, True)
        for i in range(work_df.shape[0]):
            # 颜色
            if work_df.iloc[i, 6] == '超期':
                color = 'red'
            elif work_df.iloc[i, 6] == '预警':
                # 橙色
                color = 'orange'
            elif work_df.iloc[i, 6] == '正常':
                color = 'green'
            else:
                # 粉红色
                color = 'pink'
            for j in range(work_df.shape[1]):
                item = QTableWidgetItem(str(work_df.iloc[i, j]))
                item.setForeground(QColor(color))
                self.topN_tw.setItem(i, j, item)


    def onAggrHouseDetail(self, title_name):
        house_type = title_name[:4]
        # print(house_type)
        temp_df = self.rack_df.copy()
        temp_df = temp_df[temp_df['业务级别'] == house_type]
        self.stackedWidget.setCurrentIndex(4)
        if '利用率' in title_name:
            self.showTopNTable(temp_df)
        elif '在建情况' in title_name:
            self.showWorkTable(temp_df)

    def onBarClicked(self, area_name, house_use_status):
        temp_df = self.rack_df.copy()
        temp_df = temp_df[temp_df['所属区县'] == area_name]
        if house_use_status != '全部':
            if self.area_house_bar.title_name == '各区域汇聚机房利用率情况':
                temp_df = temp_df[temp_df['利用率状态'] == house_use_status]
            elif self.area_house_bar.title_name == '各区域汇聚机房在建情况':
                temp_df = temp_df[temp_df['建设情况'] == house_use_status]
        if temp_df.shape[0] == 0:
            return;
        self.stackedWidget.setCurrentIndex(4)
        if self.area_house_bar.title_name == '各区域汇聚机房利用率情况':
            self.showTopNTable(temp_df)
        elif self.area_house_bar.title_name == '各区域汇聚机房在建情况':
            self.showWorkTable(temp_df)

    # TopN 页面查询所有利用率机房
    def searchTopNHouse(self):
        yellow_num = self.yellow_num_QB.value()
        red_num = self.red_num_QB.value()
        if yellow_num >= red_num:
            QMessageBox.information(self, '提示', '预警阈值应小于紧张阈值')
            return;
        self.search_topN_thread = queryAllHouseThread(yellow_num,red_num)
        self.search_topN_thread.state_signal.connect(self.showStatus)
        self.search_topN_thread.area_signal.connect(self.showAreaCol)
        self.search_topN_thread.pie_signal.connect(self.showAllPie)
        self.search_topN_thread.error_signal.connect(self.showError)
        self.search_topN_thread.dataframe_signal.connect(self.showTopNDataFrame)
        self.search_topN_thread.start()        

    def showTopNDataFrame(self, device_df,  rack_df,  table_df):
        self.device_df = device_df
        self.rack_df = rack_df
        self.table_df = table_df
        topN_df = rack_df.copy()
        if topN_df.shape[0] == 0:
            QMessageBox.information(self, '提示', '没有符合条件的机房')
            return;
        self.showTopNTable(topN_df)



    def showTopNTable(self, topN_df):
        topN_df = topN_df[['所属区县','机房名称','业务级别','机架数','可装设施高度','已用设施高度','利用率','利用率状态']]
        self.topN_tw.setRowCount(topN_df.shape[0])
        # 最后一列添加操作列，操作列为按钮，按钮绑定事件点击详情，调用searchOneHousePercent，house_name为对应列机房名称
        self.topN_tw.setColumnCount(topN_df.shape[1]+1)
        cols = ['所属区县','机房名称','业务级别','机架数','可装设施高度','已用设施高度','利用率%','利用率状态','操作']
        self.topN_tw.setHorizontalHeaderLabels(cols)
        # 机房名称列随内容扩展
        self.topN_tw.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        # 利用率状态列隐藏
        self.topN_tw.setColumnHidden(7, True)

        for i in range(topN_df.shape[0]):
            # 颜色
            if topN_df.iloc[i, 7] == '已用完':
                color = 'red'
            elif topN_df.iloc[i, 7] == '紧张':
                # 橙色
                color = 'orange'
            elif topN_df.iloc[i, 7] == '预警':
                color = 'yellow'
            elif topN_df.iloc[i, 7] == '充足':
                color = 'green'
            else:
                # 粉红色
                color = 'pink'
            for j in range(topN_df.shape[1]):
                item = QTableWidgetItem(str(topN_df.iloc[i, j]))
                item.setForeground(QColor(color))
                self.topN_tw.setItem(i, j, item)
            # 操作列添加按钮
            btn = QPushButton('详情')
            btn.setStyleSheet("""
                QPushButton { 
                    border: 1px solid """ + color + """;  
                    background-color: rgb(13, 9, 36); 
                    color: """ + color + """; 
                    border-radius: 6px;
                } 
                
                QPushButton:hover { 
                    background-color: rgb(85, 0, 255); 
                    color: rgb(7, 255, 119); 
                } 
                
                QPushButton:pressed { 
                    background-color: rgb(0, 0, 0); 
                }
            """)
            btn.clicked.connect(lambda checked=False, name=topN_df.iloc[i, 1]: self.searchTopNOneHouseDetail(name))
            self.topN_tw.setCellWidget(i, topN_df.shape[1], btn)        


    def searchTopNOneHouseDetail(self, house_name):
        self.stackedWidget.setCurrentIndex(0)
        self.keys_le.setText(house_name)
        self.house_names_cb.clear()
        self.house_names_cb.addItem(house_name)
        self.house_names_cb.setCurrentIndex(0)
        self.searchOneHousePercent()

    def clearDataBaseTable(self):
        table_name = self.table_names_cb.currentText()
        if len(table_name) == 0:
            QMessageBox.information(self, '提示', '请选择表名')
            return;
        # 弹窗确认
        ret = QMessageBox.question(self, '提示', '确定清除表数据吗？')
        if ret == QMessageBox.No:
            return;
        clearDataBaseTable(table_name)
        self.showStatus('清除成功')


    # 查找数据库结构
    def searchTable(self):
        self.search_table_thread = SearchTableThread()
        self.search_table_thread.state_signal.connect(self.showStatus)
        self.search_table_thread.table_signal.connect(self.setTableComboBox)
        self.search_table_thread.dataframe_signal.connect(self.showTableInfor)
        self.search_table_thread.start()
    
    def setTableComboBox(self, table_names):
        self.table_names_cb.clear()
        self.table_names_cb.addItems(table_names)
    
    def showTableInfor(self,device_high_table,house_table,rack_table,net_table):
        tableWidgets = [self.device_high_tw,self.house_tw,self.rack_tw,self.net_tw]
        dataframes = [device_high_table,house_table,rack_table,net_table]
        for tableWidget,dataframe in zip(tableWidgets,dataframes):
            tableWidget.setRowCount(dataframe.shape[0])
            tableWidget.setColumnCount(dataframe.shape[1])
            tableWidget.setHorizontalHeaderLabels(dataframe.columns)
            for i in range(dataframe.shape[0]):
                for j in range(dataframe.shape[1]):
                    tableWidget.setItem(i, j, QTableWidgetItem(str(dataframe.iloc[i, j])))
            tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    # 饼状图 展示所有利用率机房分布
    def showAllPie(self, important_dict,normal_dict,business_dict,title):
        # print(important_dict,normal_dict,business_dict,title)
        self.important_pie.setData(important_dict,'重要汇聚'+title)
        self.normal_pie.setData(normal_dict,'普通汇聚'+title)
        self.business_pie.setData(business_dict,'业务汇聚'+title)

    # 柱状图显示各区域汇聚机房数
    def showAreaCol(self, area_table,title):
        self.area_house_bar.setData(area_table,title)

    def downLoadFile(self):
        # 生成文件名
        filename = f"机房设备及机架位查询结果_{time.strftime('%Y%m%d%H%M', time.localtime())}.xlsx"
        path = QFileDialog.getSaveFileName(self, '保存文件', f'结果/{filename}', 'Excel文件 (*.xlsx)')[0]
        if len(path) == 0:
            return;
        self.write_xlsx_thread = writeXlsxThread(path,self.device_df,self.rack_df,self.table_df)
        self.write_xlsx_thread.state_signal.connect(self.showStatus)
        self.write_xlsx_thread.start()

    # 查找1个机房的机房利用率
    def searchOneHousePercent(self):
        house_name = self.house_names_cb.currentText()
        if len(house_name) == 0:
            QMessageBox.information(self, '提示', '请选择机房')
            return;
        self.query_one_house_thread = queryOneHouseThread(house_name)
        self.query_one_house_thread.state_signal.connect(self.showStatus)
        self.query_one_house_thread.result_signal.connect(self.showOneHouseReslut)
        self.query_one_house_thread.error_signal.connect(self.showError)
        self.query_one_house_thread.percent_signal.connect(self.setPercent)
        self.query_one_house_thread.start()

    def showOneHouseDataFrame(self, device_df,rack_df,table_df):
        self.device_df = device_df
        self.rack_df = rack_df
        self.table_df = table_df

    def showOneHouseReslut(self, major_count_dict, major_height_dict):
        self.high_num_pie.setData(major_height_dict,'机房已装设备高度分布')
        self.ne_num_pie.setData(major_count_dict,'机房已装设备数量分布')

    def showError(self, error_list):
        self.error_form = ErrorInfoForm(None,error_list)
        self.error_form.show()

    def setPercent(self, percent):
        self.use_percent.setValue(percent)
        self.use_percent.update_animation()

    def setHousePercent(self, cols,values):
        df = pd.DataFrame(values, columns=cols)
        data = df['机房名称'].tolist()
        self.house_names_cb.clear()
        self.house_names_cb.addItems(data)

    def pageSelect(self):
        page_widget = self.stackedWidget.findChild(QWidget, "home_page")
        if self.sender() == self.home_bt:
            page_widget = self.stackedWidget.findChild(QWidget, "home_page")
        elif self.sender() == self.module_bt:
            page_widget = self.stackedWidget.findChild(QWidget, "importFile_page")
        elif self.sender() == self.kpi_bt:
            page_widget = self.stackedWidget.findChild(QWidget, "kpi_page")
        elif self.sender() == self.setting_bt:
            page_widget = self.stackedWidget.findChild(QWidget, "setting_page")
        elif self.sender() == self.topN_bt:
            page_widget = self.stackedWidget.findChild(QWidget, "topN_page")
        
        if page_widget:
            self.stackedWidget.setCurrentWidget(page_widget)
    
    def changeColLabel(self):
        # 初始化
        if self.fileType_cb.currentIndex() == 3:
            self.type_frame.setVisible(True)
        else:
            self.type_frame.setVisible(False)
        self.currentCols = []
        self.currentLis = []
        for col in range(0, 6):
            self.cols_grid.itemAtPosition(0,col).widget().setText("- - - -")
            self.cols_grid.itemAtPosition(1,col).widget().clear()
        cols = self.fileCols[self.fileType_cb.currentIndex()]
        for i in range(len(cols)):
            self.cols_grid.itemAtPosition(0, i).widget().setText(cols[i])

    def choseFile(self):
        self.filePath, _ = QFileDialog.getOpenFileName(
            self, '选择资源表格', '', "Excel表格 (*.xlsx *.xls)")
        self.select_path_le.setText(self.filePath)
        if len(self.filePath) == 0:
            return
        self.readFileTD = FileImportThread(self.filePath)
        self.readFileTD.state_signal.connect(self.showStatus)
        self.readFileTD.result_signal.connect(self.readFileCols)
        self.readFileTD.start()

    # 显示软件运行状态
    def showStatus(self, status):
        self.import_status.setText(status)

    def searchHouse(self):
        keyword = self.keys_le.text().strip()
        if len(keyword) == 0:
            QMessageBox.information(self, '提示', '请输入搜索内容')
            return;
        keys = keyword.split(' ')
        self.search_house_thread = searchDataBaseThread('汇聚机房', '机房名称',keys)
        self.search_house_thread.state_signal.connect(self.showStatus)
        self.search_house_thread.result_signal.connect(self.setHouseCBox)
        self.search_house_thread.start()

    def setHouseCBox(self, cols,values):
        df = pd.DataFrame(values, columns=cols)
        data = df['机房名称'].tolist()
        self.house_names_cb.clear()
        self.house_names_cb.addItems(data)

    # 匹配名称
    def readFileCols(self, cols, data):
        self.currentCols, self.currentLis = cols, data
        cols = self.fileCols[self.fileType_cb.currentIndex()]
        for i in range(len(cols)):
            self.cols_grid.itemAtPosition(1, i).widget().clear()
            self.cols_grid.itemAtPosition(1, i).widget().addItems(self.currentCols)
            tempCol = self.cols_grid.itemAtPosition(0,i).widget().text()
            if tempCol in self.currentCols:
                self.cols_grid.itemAtPosition(1, i).widget().setCurrentIndex(self.currentCols.index(tempCol))
            else:
                tempMark = fuzzy_match(tempCol, self.currentCols)
                self.cols_grid.itemAtPosition(1, i).widget().setCurrentIndex(self.currentCols.index(tempMark))
        self.showStatus('自动匹配对应列如上，请核对，确认无问题后更新缓存按钮！')

    # 写入数据库，更新缓存
    def updateDataBase(self):
        # 根据cols_grid 0行和1行对应修改currentCols
        df = pd.DataFrame(self.currentLis, columns=self.currentCols)
        cols = self.fileCols[self.fileType_cb.currentIndex()]
        for i in range(len(cols)):
            old_col_name = self.cols_grid.itemAtPosition(1, i).widget().currentText()
            df.rename(columns={old_col_name: cols[i]}, inplace=True)
        df = df[cols]
        if self.fileType_cb.currentIndex() == 3:
            # 判断type_frame check的RadioButton哪个
            if self.cs_qb.isChecked():
                df['专业'] = '传输'
            elif self.cy_qb.isChecked():
                df['专业'] = '城域网'
            elif self.wx_qb.isChecked():
                df['专业'] = '无线'
            elif self.odf_qb.isChecked():
                df['专业'] = '光缆'
                df['设备型号'] = 'ODF'
            elif self.iodf_qb.isChecked():
                df['专业'] = 'IODF'
        self.writeDataBaseTD = writeDataBaseThread(self.fileType_cb.currentText(), df)
        self.writeDataBaseTD.state_signal.connect(self.showStatus)
        self.writeDataBaseTD.start()

    # 最大化和最小化
    def maximize_restore(self):
        if self.isMaximized():
            # 恢复原来MainWindow.resize(1001, 616)的大小，位置居中
            self.resize(1001, 616)
            self.move((QApplication.primaryScreen().geometry().width() - self.width()) // 2,
                      (QApplication.primaryScreen().geometry().height() - self.height()) // 2)
        else:
            self.showMaximized()

    def mousePressEvent(self, event):
        """鼠标按下事件"""
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()
            
    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_pos)
            event.accept()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/house.ico"))
    window = Mainwin()
    window.show()
    sys.exit(app.exec())