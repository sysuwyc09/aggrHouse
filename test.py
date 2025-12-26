import sqlite3

# 删除数据库 表
conn = sqlite3.connect('data/database.db')
# 删除表 设备清单
conn.execute("DROP TABLE IF EXISTS 设备清单")
conn.commit()
conn.close()