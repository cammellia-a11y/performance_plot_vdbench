# coding=utf-8
from presetting_format import part_format
from python_vdbench_operation import vdbench_operation
from xy_polt_vdbench_data import avg_data_to_plot
from alter_config import into_X_argument
from  alter_config import into_Y_argument
from  alter_config import  alter_argument
from open_summery_get_data_to_list import plot_get_data
from open_summery_get_data_to_list import plot_get_data_to_lst

# 可调节变量
# #外围变量
# xfersize,xfersize_range = into_X_argument()
# # #内围变量
# elapsed,elapsed_range = into_Y_argument()
#请输入要收集的参数
xfersize='xfersize'
xfersize_range=['512K']
elapsed='elapsed'
elapsed_range=[10,50,200,400,600,1200,1800,2400,3000,3600]

argument_string='BW'
#验证
# print(xfersize,xfersize_range)
# print(elapsed,elapsed_range)


# 预置--格式化分区
part_format()


#收集xy轴数据
Y_lst=[]
elapsed_lst=[[10,50,200,400,600,1200,1800,2400,3000,3600]]
#执行运行+收集数据
for n in range(1):
    #空盘读数据
    if n==0:
        #先写数据
            w_path='/root/Data_collection/w_vdbench.txt'
            vdbench_operation(w_path)
    for num in range(len(elapsed_range)):
            #读数据
        r_path='/root/Data_collection/r_vdbench.txt'
        print_reasult = vdbench_operation(r_path)
        if print_reasult == "vdbench执行成功":
            
            # 收集totals数据
            plot_get_data()
            # 对Y参数进行替换
            alter_argument(elapsed,elapsed_range,num,r_path)
    # 将收集的数据写入列表
    y= plot_get_data_to_lst(argument_string)
    #验证
    
    print(y) 
    #将数据写入列表
    Y_lst.append(y)
    
    # 以写入模式（'w'）打开文件时，如果文件已存在，其内容会被截断为零长度，即文件内容被清除。如果文件不存在，将创建一个新文件。
    with open('/root/Data_collection/plot_vdbench.txt', 'w', encoding='utf-8') as f:
        pass
   
   



#定义横纵表头
y_name='μs'
x_name='MB/s'
title_name='BW'
# 绘制图表
avg_data_to_plot(Y_lst,elapsed_lst,x_name,y_name,title_name)







