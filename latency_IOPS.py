# coding=utf-8
from presetting_format import part_format
from python_vdbench_operation import vdbench_operation
from xy_polt_vdbench_data import avg_data_to_plot
from alter_config import into_X_argument
from  alter_config import into_Y_argument
from  alter_config import  alter_argument
from open_total_get_data_to_list import get_data
from open_total_get_data_to_list import get_data_to_lst

# 可调节变量
# #外围变量
# xfersize,xfersize_range = into_X_argument()
# #内围变量
# iorate,iorate_range = into_Y_argument()



#验证
# print(xfersize,xfersize_range)
# print(iorate,iorate_range)

xfersize='xfersize'
xfersize_range=['4K']
iorate='iorate'
iorate_range=[50000, 80000, 110000, 140000, 170000, 200000, 230000, 260000, 290000, 310000, 340000, 370000, 400000, 430000, 460000, 490000, 510000, 540000, 570000, 600000]

argument_string='IOPS_latency'



# 预置--格式化分区
part_format()
#收集xy轴数据
latency_lst=[]
IOPS_lst=[]
#执行运行+收集数据
for n in range(1):
    if n==0:
        #写数据
        w_path='/root/Data_collection/IOPS_w_vdbench.txt'
        vdbench_operation(w_path)
    for num in range(len(iorate_range)):
        #读数据
        r_path='/root/Data_collection/IOPS_r_vdbench.txt'
        print_reasult = vdbench_operation(r_path)
        if print_reasult == "vdbench执行成功":  
            # 收集totals数据
            get_data()
            # 对Y参数进行替换
            alter_argument(iorate,iorate_range,num,r_path)
    # 将收集的数据写入列表
    lst,iops= get_data_to_lst(argument_string)
    #验证
    print(lst)
    print(iops)
    latency_lst.append(lst)
    IOPS_lst.append(iops)
    
    #avg_data_to_plot(latency_lst,IOPS_lst)

    # 以写入模式（'w'）打开文件时，如果文件已存在，其内容会被截断为零长度，即文件内容被清除。如果文件不存在，将创建一个新文件。
    with open('/root/Data_collection/avg_vdbench.txt', 'w', encoding='utf-8') as f:
        pass
   


#定义横纵表头
x_name='IOPS'
y_name='latency'
title_name='IOPS/lantency'
# 绘制图表
avg_data_to_plot(latency_lst,IOPS_lst,x_name,y_name,title_name)







