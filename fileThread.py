from PySide6.QtCore import QThread, Signal
import pandas as pd
import sqlite3

class FileImportThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    result_signal = Signal(list, list)  # 列名和数据信号
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
    
    def run(self):
        try:
            self.state_signal.emit("正在读取文件..")
            # 读取文件到DataFrame
            df = pd.read_excel(self.file_path)
            # 获取列名和数据
            cols = df.columns.tolist()
            data = df.values.tolist()
            
            # 发送状态信号
            self.state_signal.emit("读取成功")
            # 发送结果信号
            self.result_signal.emit(cols, data)
            
        except Exception as e:
            self.state_signal.emit(f"读取成功: {str(e)}")
            self.result_signal.emit([], [])


class writeDataBaseThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    
    def __init__(self, table_name, df):
        super().__init__()
        self.table_name = table_name
        self.df = df

    def run(self):
        try:
            self.state_signal.emit("正在写入数据库..")
            # 连接数据库
            conn = sqlite3.connect('data/database.db')
            if self.table_name == '汇聚机房' or self.table_name == '机架位':
            # 写入数据库
                self.df.to_sql(self.table_name, conn, if_exists='replace', index=False)
            elif self.table_name == '设备高度':
                # 判断表是否存在，不存在则直接写入
                if self.table_name not in pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)['name'].values:
                    self.df.to_sql(self.table_name, conn, if_exists='replace', index=False)
                else:
                    # 逐行 判断 专业 设备型号 组合是否存在
                    for index, row in self.df.iterrows():
                        # 检查是否存在相同的专业和设备型号组合
                        existing = pd.read_sql(f"SELECT * FROM {self.table_name} WHERE 专业='{row['专业']}' AND 设备型号='{row['设备型号']}';", conn)
                        if existing.empty:
                            # 不存在则插入
                            row.to_frame().T.to_sql(self.table_name, conn, if_exists='append', index=False)
                        else:
                            # 存在则更新
                            # 构建更新语句
                            update_sql = f"UPDATE {self.table_name} SET 设备高度='{row['设备高度']}' WHERE 专业='{row['专业']}' AND 设备型号='{row['设备型号']}';"
                            # 执行更新
                            conn.execute(update_sql)
            elif self.table_name == '设备清单':
                # 判断表是否存在，不存在则直接写入
                if self.table_name not in pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)['name'].values:
                    self.df.to_sql(self.table_name, conn, if_exists='replace', index=False)
                else:
                    # 专业替换更新 设备清单
                    existing_df = pd.read_sql(f"SELECT * FROM {self.table_name}", conn)
                    major = self.df['专业'].tolist()[0]
                    # 筛选出专业匹配的行
                    existing_df = existing_df[existing_df['专业'] != major]
                    self.df = pd.concat([self.df, existing_df], ignore_index=True)
                    self.df.to_sql(self.table_name, conn, if_exists='replace', index=False)
                    
            conn.commit()
            conn.close()
            self.state_signal.emit("写入数据库成功")
        except Exception as e:
            self.state_signal.emit(f"写入数据库失败: {str(e)}")

class searchDataBaseThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    result_signal = Signal(list, list)  # 列名和数据信号
    
    def __init__(self, table_name, col_name, keys):
        super().__init__()
        self.table_name = table_name
        self.keys = keys
        self.col_name = col_name
    
    def run(self):
        try:
            self.state_signal.emit("正在查询数据库..")
            # 连接数据库
            conn = sqlite3.connect('data/database.db')
            # 构建查询语句
            query = f"SELECT * FROM {self.table_name} WHERE "
            for key in self.keys:
                query += f"{self.col_name} LIKE '%{key}%' AND "
            query = query[:-5]  # 移除最后一个AND
            # 执行查询
            df = pd.read_sql(query, conn)
            # 关闭数据库连接
            conn.close()
            # 发送状态信号
            self.state_signal.emit("查询成功")
            # 发送结果信号
            self.result_signal.emit(df.columns.tolist(), df.values.tolist())
        except Exception as e:
            self.state_signal.emit(f"查询失败: {str(e)}")
            self.result_signal.emit([], [])


class queryOneHouseThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    result_signal = Signal(dict, dict)  # 列名和数据信号
    percent_signal = Signal(float)  # 机房利用率信号
    error_signal = Signal(list)  # 错误信号

    def __init__(self, house_name):
        super().__init__()
        self.house_name = house_name
    
    def run(self):
        try:
            self.state_signal.emit("正在查询数据库..")
            # 连接数据库
            conn = sqlite3.connect('data/database.db')
            rack_df = pd.read_sql(f"SELECT * FROM 机架位 WHERE 所属机房='{self.house_name}';", conn)
            total_high_num = rack_df.shape[0] * 45
            if total_high_num == 0:
                self.state_signal.emit("查询失败: 该机房不存在")
                return;
            device_df = pd.read_sql(f"SELECT * FROM 设备清单 WHERE 所属机房='{self.house_name}';", conn)
            device_high_df = pd.read_sql(f"SELECT * FROM 设备高度", conn)
            device_df = device_df.astype('str')
            # 删除生命周期状态包含 已拆除 的行
            device_df = device_df[~device_df['生命周期状态'].str.contains('已拆除')]
            device_df = device_df[device_df['设备型号']!='None']
            device_df = pd.merge(device_df, device_high_df, on=['专业', '设备型号'], how='left')
            # 找出设备为空的行
            empty_device_df = device_df[device_df['设备高度'].isnull()]
            # 如果存在设备为空的行，将这些行的专业和设备型号添加到错误列表中
            if not empty_device_df.empty:
                error_list = empty_device_df[['专业', '设备型号']].drop_duplicates().values.tolist()
                self.error_signal.emit(error_list)
                return;
            major_table = pd.pivot_table(device_df, index='专业', aggfunc={'设备名称':'count','设备高度':'sum'})
            major_table = major_table.reset_index()
            major_count_dict = major_table.set_index('专业')['设备名称'].to_dict()
            major_height_dict = major_table.set_index('专业')['设备高度'].to_dict()
            self.result_signal.emit(major_count_dict, major_height_dict)
            # 计算利用率
            use_high_num = device_df['设备高度'].astype(float).sum()
            use_percent = round(use_high_num / total_high_num * 100, 2)
            self.percent_signal.emit(use_percent)
            
            self.state_signal.emit("查询数据库完成..")
        except Exception as e:
            self.state_signal.emit(f"查询失败: {str(e)}")


# 现网在用状态下的所有机房
class queryAllHouseThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    area_signal = Signal(pd.DataFrame,str)  # 区域机房数结果信号
    error_signal = Signal(list)  # 错误信号
    pie_signal = Signal(dict,dict,dict,str)  # 利用率结果信号
    dataframe_signal = Signal(pd.DataFrame,pd.DataFrame,pd.DataFrame)

    def __init__(self,yellow_num=60,red_num=80):
        super().__init__()
        self.yellow_num = yellow_num
        self.red_num = red_num
    def run(self):
        try:
            self.state_signal.emit("正在查询数据库..")
            # 连接数据库
            conn = sqlite3.connect('data/database.db')
            # 执行查询
            # 统计机房数
            house_df = pd.read_sql("SELECT * FROM 汇聚机房", conn)
            house_df = house_df[house_df['生命周期状态']=='现网在用']
            # area_table = pd.pivot_table(house_df, index=['所属区县','业务级别'], aggfunc={'机房名称':'count'})
            # area_table = area_table.reset_index()
            # area_grped = area_table.groupby('所属区县')
            # area_dict = {}
            # for name, group in area_grped:
            #     area_dict[name] = group.set_index('业务级别')['机房名称'].to_dict()
            # self.area_signal.emit(area_dict)

            # 统计设备数
            device_df = pd.read_sql("SELECT * FROM 设备清单", conn)
            device_df = device_df.rename(columns={'所属机房':'机房名称'})
            device_df = device_df.merge(house_df[['机房名称']], on='机房名称')
            device_df = device_df.astype('str')

            # 垃圾数据清理
            device_df = device_df[device_df['设备型号']!='None']

            device_df = device_df[~device_df['生命周期状态'].str.contains('已拆除')]
            device_height_df = pd.read_sql("SELECT * FROM 设备高度", conn)
            device_df = device_df.merge(device_height_df, on=['专业', '设备型号'], how='left')

            empty_device_df = device_df[device_df['设备高度'].isnull()]
            # 识别是否有未录入高度设施
            if not empty_device_df.empty:
                error_list = empty_device_df[['专业', '设备型号']].drop_duplicates().values.tolist()
                self.error_signal.emit(error_list)
                return;
            use_table = pd.pivot_table(device_df, index='机房名称', aggfunc={'设备高度':'sum'})
            use_table = use_table.reset_index()
            use_table = use_table.rename(columns={'设备高度':'已用设施高度'})


            rack_df = pd.read_sql("SELECT * FROM 机架位", conn)
            rack_table = pd.pivot_table(rack_df, index='所属机房', aggfunc={'装机位置编号':'count'})
            rack_table = rack_table.reset_index()
            rack_table = rack_table.rename(columns={'装机位置编号':'机架数','所属机房':'机房名称'})
            house_df = house_df.merge(rack_table, on='机房名称',how='left')
            house_df['机架数'] = house_df['机架数'].fillna(1)
            house_df['可装设施高度'] = house_df['机架数'] * 45

            house_df = house_df.merge(use_table, on='机房名称',how='left')
            house_df['已用设施高度'] = house_df['已用设施高度'].fillna(0)
            house_df['利用率'] = round(house_df['已用设施高度'] / house_df['可装设施高度'] * 100, 2)
            house_df['利用率状态'] = house_df['利用率'].apply(self.isUse)
            house_df = house_df.sort_values(by='利用率', ascending=False)

            # 重要汇聚
            important_house_df = house_df[house_df['业务级别']=='重要汇聚'].copy()
            important_table = pd.pivot_table(important_house_df, index='利用率状态', aggfunc={'机房名称':'count'})
            important_table = important_table.reset_index()
            important_dict = important_table.set_index('利用率状态')['机房名称'].to_dict()

            # 普通汇聚
            normal_house_df = house_df[house_df['业务级别']=='普通汇聚'].copy()
            normal_table = pd.pivot_table(normal_house_df, index='利用率状态', aggfunc={'机房名称':'count'})
            normal_table = normal_table.reset_index()
            normal_dict = normal_table.set_index('利用率状态')['机房名称'].to_dict()
            
            # 业务汇聚
            business_house_df = house_df[house_df['业务级别']=='业务汇聚'].copy()
            business_table = pd.pivot_table(business_house_df, index='利用率状态', aggfunc={'机房名称':'count'})
            business_table = business_table.reset_index()
            business_dict = business_table.set_index('利用率状态')['机房名称'].to_dict()

            self.pie_signal.emit(important_dict,normal_dict,business_dict,'利用率状态分布')

            all_table = pd.pivot_table(house_df, index=['业务级别','利用率状态'], aggfunc={'机房名称':'count'})
            all_table = all_table.reset_index()
            all_table = all_table.rename(columns={'机房名称':'数量'})

            # 按区域统计机房数量
            area_table = pd.pivot_table(house_df,index='所属区县',columns='利用率状态',aggfunc={'机房名称':'count'},fill_value=0)
            area_table.columns = area_table.columns.droplevel(0)

            area_sort_cols = ['赤坎区','麻章区','霞山区','坡头区','开发区','雷州市','廉江市','吴川市','遂溪县','徐闻县']
            # area_table 按所属区县列 按area_sort_cols排序
            area_table = area_table.loc[area_sort_cols].reset_index()
            cols = ['所属区县','已用完','紧张','预警','充足','零利用率']
            for col in cols:
                if col not in area_table.columns:
                    area_table[col] = 0
            area_table = area_table[cols]
            self.area_signal.emit(area_table,'各区域汇聚机房利用率情况')

            self.dataframe_signal.emit(device_df,house_df,all_table)


            # 关闭数据库连接
            conn.close()
            # 发送状态信号
            self.state_signal.emit("查询成功")
            # 发送结果信号

        except Exception as e:
            self.state_signal.emit(f"查询失败: {str(e)}")

    def isUse(self,use_percent):
        if use_percent >= 100:
            return '已用完'
        elif use_percent >= self.red_num:
            return '紧张'
        elif use_percent >= self.yellow_num:
            return '预警'
        elif use_percent > 0:
            return '充足'
        else:
            return '零利用率'

# 工程在建状态的所有机房
class queryWorkHouseThread(QThread):
    # 定义信号
    state_signal = Signal(str)  # 状态信号
    area_signal = Signal(pd.DataFrame,str)  # 区域机房数结果信号
    error_signal = Signal(list)  # 错误信号
    pie_signal = Signal(dict,dict,dict,str)  # 利用率结果信号
    dataframe_signal = Signal(pd.DataFrame,pd.DataFrame,pd.DataFrame)

    def __init__(self,yellow_num=12,red_num=24):
        super().__init__()
        self.yellow_num = yellow_num
        self.red_num = red_num
    
    def run(self):
        try:
            self.state_signal.emit("正在查询工程在建状态的所有机房..")
            # 连接数据库 data/database.db
            conn = sqlite3.connect('data/database.db')
            # 执行查询
            # 统计机房数
            house_df = pd.read_sql("SELECT * FROM 汇聚机房", conn)
            house_df = house_df[(house_df['生命周期状态']=='在建') | (house_df['生命周期状态']=='基础交维')]
            conn.close()
            self.state_signal.emit(f"共查询到{len(house_df)}个工程在建状态的机房")

            # 统计已入网时间
            house_df['入网时间'] = pd.to_datetime(house_df['入网时间'])
            now = pd.Timestamp.now()
            house_df['已入网时间(月)'] = round((now - house_df['入网时间']).dt.total_seconds() / (86400 * 30),2)
            house_df['建设情况'] = house_df['已入网时间(月)'].apply(self.workStatus)
            house_df = house_df.sort_values(by='已入网时间(月)', ascending=False)

            # 重要汇聚
            important_house_df = house_df[house_df['业务级别']=='重要汇聚'].copy()
            important_table = pd.pivot_table(important_house_df, index='建设情况', aggfunc={'机房名称':'count'})
            important_table = important_table.reset_index()
            important_dict = important_table.set_index('建设情况')['机房名称'].to_dict()

            # 普通汇聚
            normal_house_df = house_df[house_df['业务级别']=='普通汇聚'].copy()
            normal_table = pd.pivot_table(normal_house_df, index='建设情况', aggfunc={'机房名称':'count'})
            normal_table = normal_table.reset_index()
            normal_dict = normal_table.set_index('建设情况')['机房名称'].to_dict()
            
            # 业务汇聚
            business_house_df = house_df[house_df['业务级别']=='业务汇聚'].copy()
            business_table = pd.pivot_table(business_house_df, index='建设情况', aggfunc={'机房名称':'count'})
            business_table = business_table.reset_index()
            business_dict = business_table.set_index('建设情况')['机房名称'].to_dict()

            self.pie_signal.emit(important_dict,normal_dict,business_dict,'在建情况分布')

            all_table = pd.pivot_table(house_df, index=['业务级别','建设情况'], aggfunc={'机房名称':'count'})
            all_table = all_table.reset_index()
            all_table = all_table.rename(columns={'机房名称':'数量'})

            # 按区域统计机房数量
            area_table = pd.pivot_table(house_df,index='所属区县',columns='建设情况',aggfunc={'机房名称':'count'},fill_value=0)
            area_table.columns = area_table.columns.droplevel(0)

            area_sort_cols = ['赤坎区','麻章区','霞山区','坡头区','开发区','雷州市','廉江市','吴川市','遂溪县','徐闻县']
            # area_table 按所属区县列 按area_sort_cols排序
            area_table = area_table.loc[area_sort_cols].reset_index()
            cols = ['所属区县','超期','预警','正常']
            for col in cols:
                if col not in area_table.columns:
                    area_table[col] = 0
            area_table = area_table[cols]
            self.area_signal.emit(area_table,'各区域汇聚机房在建情况')


            self.dataframe_signal.emit(area_table,house_df,all_table)

            # 发送状态信号
            self.state_signal.emit("查询成功")
        # 发送结果信号
        except Exception as e:
            self.state_signal.emit(f"查询工程在建状态的所有机房失败: {str(e)}")


    def workStatus(self,month):
        if month >= self.red_num:
            return '超期'
        elif month >= self.yellow_num:
            return '预警'
        else:
            return '正常'



        
class writeXlsxThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    def __init__(self,path, device_df,rack_df,table_df,sheet1_name,sheet2_name,sheet3_name):
        super().__init__()
        self.path = path
        self.device_df = device_df
        self.rack_df = rack_df
        self.table_df = table_df
        self.sheet1_name = sheet1_name
        self.sheet2_name = sheet2_name
        self.sheet3_name = sheet3_name
    def run(self):
        try:
            self.state_signal.emit("正在写入结果文件Excel..")
            # 写入Excel
            with pd.ExcelWriter(self.path) as writer:
                self.table_df.to_excel(writer, sheet_name=self.sheet1_name, index=False)
                self.device_df.to_excel(writer, sheet_name=self.sheet2_name, index=False)
                self.rack_df.to_excel(writer, sheet_name=self.sheet3_name, index=False)
            self.state_signal.emit("写入Excel成功")
        except Exception as e:
            self.state_signal.emit(f"写入Excel失败: {str(e)}")

# 查找数据库结构类，返回数据库表名列表，各表数据行数
class SearchTableThread(QThread):
    # 定义两个信号
    state_signal = Signal(str)  # 状态信号
    table_signal = Signal(list)  # 表名信号
    dataframe_signal = Signal(pd.DataFrame,pd.DataFrame,pd.DataFrame,pd.DataFrame)  # 区域机房数结果信号    
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        # try:
        self.state_signal.emit("正在查询数据库结构..")
        # 连接数据库 data/database.db
        conn = sqlite3.connect('data/database.db')
        cursor = conn.cursor()
        # 查询数据库表名
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        table_names = [table[0] for table in tables]
        # 发送表名信号
        self.table_signal.emit(table_names)
        if '设备高度' in table_names:
            # 查询设备高度表数据
            device_high_df = pd.read_sql("SELECT * FROM 设备高度", conn)
            device_high_table = pd.pivot_table(device_high_df, index='专业', aggfunc={'设备型号':'count'})
            device_high_table = device_high_table.reset_index()
            device_high_table = device_high_table.rename(columns={'设备型号':'设备型号数'})
        else:
            device_high_table = pd.DataFrame(columns=['专业', '设备型号数'])
        if '汇聚机房' in table_names:
            # 查询汇聚机房表数据
            house_df = pd.read_sql("SELECT * FROM 汇聚机房", conn)
            house_table = pd.pivot_table(house_df, index=['业务级别','生命周期状态'], aggfunc={'机房名称':'count'})
            house_table = house_table.reset_index()
            house_table = house_table.rename(columns={'机房名称':'机房数'})
        else:
            house_table = pd.DataFrame(columns=['业务级别','生命周期状态', '机房数'])
        if '设备清单' in table_names:
            # 查询设备清单表数据
            net_df = pd.read_sql("SELECT * FROM 设备清单", conn)
            net_table = pd.pivot_table(net_df, index=['专业','设备型号'], aggfunc={'设备名称':'count'})
            net_table = net_table.reset_index()
            net_table = net_table.rename(columns={'设备名称':'设备数'})
        else:
            net_table = pd.DataFrame(columns=['专业','设备型号', '设备数'])
        if '机架位' in table_names:
            # 查询机架位表数据
            rack_df = pd.read_sql("SELECT * FROM 机架位", conn)
            rack_table = pd.pivot_table(rack_df, index=['所属机房'], aggfunc={'装机位置编号':'count'})
            rack_table = rack_table.reset_index()
            rack_table = rack_table.rename(columns={'所属机房':'机房名称','装机位置编号':'机架位数'})
        else:
            rack_table = pd.DataFrame(columns=['机房名称','机架位数'])
        self.dataframe_signal.emit(device_high_table,house_table,rack_table,net_table)

        # 关闭数据库连接
        conn.close()
        # 发送状态信号
        self.state_signal.emit("查询数据库结构成功")
        # except Exception as e:
        #     self.state_signal.emit(f"查询数据库结构失败: {str(e)}")

