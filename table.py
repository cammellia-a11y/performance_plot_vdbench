#coding=utf-8
from prettytable import PrettyTable  
  
# 初始化表格并设置表头  
table = PrettyTable(["姓名", "年龄", "城市"])  
  
# 设置表头样式和对齐方式  
# table.header_style = "title"  
# table.align["姓名"] = "l"  # 左对齐  
# table.align["年龄"] = "c"  # 居中对齐  
# table.align["城市"] = "r"  # 右对齐  
  
# 添加数据行  
table.add_row(["张三", 28, "北京"])  
table.add_row(["李四", 22, "上海"])  
table.add_row(["王五", 30, "广州"])  
  
# 设置边框和填充字符  
table.border = True  
table.padding_width = 2  
  
# 设置表格标题  
#table.set_title("people_table")  
  
# 打印表格  
print(table)