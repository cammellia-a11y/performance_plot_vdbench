# coding=utf-8
from presetting_format import part_format
from python_vdbench_operation import vdbench_operation
from open_total_get_data_to_list import get_data
from open_total_get_data_to_list import get_data_to_lst
from alter_config import into_X_argument
from  alter_config import into_Y_argument
from  alter_config import  alter_argument
from total_data_to_plot import total_to_plot
from prettytable import PrettyTable  
# 可调节变量
#外围变量
x_argument,x_range = into_X_argument()
#内围变量
y_argument,y_range = into_Y_argument()
#请输入要收集的参数
argument_string=input('请输入想要收集的参数:(IOPS/BW)')

#z轴列表--用于收集每次循环后的参数

z_argument =[]
string_lst=[]

#执行运行+收集数据
for n in range(len(x_range)):
    for num in range(len(y_range)):
        # 预置--格式化分区
        part_format()
        # 运行vdbench
        config_path='/root/Data_collection/config_document/vdbench_config.txt'
        print_reasult = vdbench_operation(config_path)
        if print_reasult == "vdbench执行成功":
            # 收集totals数据
            get_data()
            # 对Y参数进行替换
            alter_argument(y_argument,y_range,num,config_path)
    
   
    # 将收集的数据写入列表
    lst,string_line = get_data_to_lst(argument_string)
    z_argument.append(lst)
    string_lst.append(string_line)

    # 以写入模式（'w'）打开文件时，如果文件已存在，其内容会被截断为零长度，即文件内容被清除。如果文件不存在，将创建一个新文件。
    with open('/root/Data_collection/config_document/avg_vdbench.txt', 'w', encoding='utf-8') as f:
        pass
    # 对x参数进行替换
    alter_argument(x_argument, x_range, n,config_path)


#将数据进行保存---形成可视化表格
#创建初始化列表
table=PrettyTable()
#绘制行头
element='blocksize/RW mix--IOPS' #需要新加的元素
tail_list=[]
for i in range(len(y_range)):  #将y_range中的元素转化为字符串
    tail_list.append(str(y_range[i]))
tail_list.insert(0,element) #在第一个元素加开头
#print(tail_list)
table.field_names=tail_list  #构建开头行
#添加行
for i in range(len(string_lst)):
    new_element=x_range[i]
    line_lst=string_lst
    line_lst[i].insert(0,new_element)
    table.add_row(line_lst[i])
#print(line_lst)
#打开文件将收集的数据以列表的形式写入到文件中  
with open('/root/Data_collection/all_data_txt/data_list.txt','w',encoding='utf-8') as f:
    f.write(table.get_string())




# 绘制图表
total_to_plot(x_argument,x_range,y_argument,y_range,z_argument,argument_string)






