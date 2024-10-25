# coding=utf-8
from presetting_format import part_format
from python_vdbench_operation import vdbench_operation
from open_total_get_data_to_list import get_data
from open_total_get_data_to_list import get_data_to_lst
from alter_config import into_X_argument
from  alter_config import into_Y_argument
from  alter_config import  alter_argument
from total_data_to_plot import total_to_plot

# 可调节变量
#外围变量
x_argument,x_range = into_X_argument()
#内围变量
y_argument,y_range = into_Y_argument()
#请输入要收集的参数
argument_string=input('请输入想要收集的参数:(IOPS/BW)')

#验证
print(x_argument,x_range)
print(y_argument,y_range)
print(argument_string)


#z轴列表--用于收集每次循环后的参数

z_argument = []


#执行运行+收集数据
for n in range(len(x_range)):
    for num in range(len(y_range)):
        # 预置--格式化分区
        part_format()
        # 运行vdbench
        print_reasult = vdbench_operation()
        if print_reasult == "vdbench执行成功":
            # 收集totals数据
            get_data()
            
            # 对Y参数进行替换
            alter_argument(y_argument,y_range,num)
    
   
    # 将收集的数据写入列表
    lst = get_data_to_lst(argument_string)
    print(lst)
    z_argument.append(lst)
    
    # 以写入模式（'w'）打开文件时，如果文件已存在，其内容会被截断为零长度，即文件内容被清除。如果文件不存在，将创建一个新文件。
    with open('/root/avg_vdbench.txt', 'w', encoding='utf-8') as f:
        pass
    # 对x参数进行替换
    alter_argument(x_argument, x_range, n)




# 绘制图表
total_to_plot(x_argument,x_range,y_argument,y_range,z_argument,argument_string)






