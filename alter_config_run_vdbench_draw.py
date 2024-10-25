# coding=utf-8
from presetting_format import part_format
from python_vdbench_operation import vdbench_operation
from xy_polt_vdbench_data import avg_data_to_plot
from open_summery_get_data_to_list import dot_get_data
from open_summery_get_data_to_list import IOPS_BW_data
from alter_config import alter_argument
from prettytable import PrettyTable  


#收集数据并绘图
def draw_IOPS(input_file,argument_string,title_name,interval):  #需要获取的参数-数据文件以及图片命名-运行时间-打点时间 
   #收集y轴数据
   Y_lst=[]
   X_lst=[]
   num=0
   figure_lst=[]
   # 将收集的数据写入列表
   dot_get_data(title_name,input_file)   #将数据写入文件
   Y_lst= IOPS_BW_data(argument_string,title_name)  #将文件写入列表并筛选出所需要的数据
   #验证  
   print(Y_lst) 
   #定义x轴列表
   for i in range(len(Y_lst)):
      num+=interval[1]
      X_lst.append(num)
   print(X_lst)
   #定义横纵表头
   if argument_string=='IOPS':
      y_name='IOPS'
      x_name='time/s'#time(seconds)
   elif argument_string=='BW':
      y_name='BW'
      x_name='time/s'#time(seconds)
   #收集最大最小值---添加到列表中
   figure_lst=avg_max_min(title_name,Y_lst)
   # 绘制图表
   avg_data_to_plot(Y_lst,X_lst,x_name,y_name,title_name)
   #返回最大最小值给表格
   return figure_lst
# r_path='/root/Data_collection/all_data_txt/data.log'
# figure_lst=draw_IOPS(r_path,argument_string='IOPS',title_name=f'IOPS_11',interval=[0,5])
# print(figure_lst)

#替换数据并运行脚本
def alter_run_vdbench(config_path,title_name,rdpct,seekpct,xfersize,run_time,interval):
   
   try:
      print("程序正在运行中......")
      alter_argument('rdpct',rdpct,0,config_path)
      alter_argument('seekpct',seekpct,0,config_path)
      alter_argument('xfersize',xfersize,0,config_path)
      alter_argument('elapsed',run_time,0,config_path)
      alter_argument('interval',interval,0,config_path)
      #运行vdbench
      print_reasult=vdbench_operation(title_name)
      if print_reasult == "vdbench执行成功":            
         print('Execution successful')
   except KeyboardInterrupt :
      print("检测到中断，正在处理中.....")
   finally:
      #初始化为最初版本
      alter_argument('rdpct',rdpct,1,config_path)
      alter_argument('seekpct',seekpct,1,config_path)
      alter_argument('xfersize',xfersize,1,config_path)
      alter_argument('elapsed',run_time,1,config_path)
      alter_argument('interval',interval,1,config_path)
  



#计算最大最小值以及平均数
def avg_max_min(title_name,Y_lst):
    #计算最大值最小值
    max_value=max(Y_lst)
    min_value=min(Y_lst)
    #计算平均数
    sum_value=sum(Y_lst)
    count=len(Y_lst)
    avg_value=sum_value//count
    #导入列表中
    num_lst=[]
    num_lst.append(max_value)
    num_lst.append(min_value)
    num_lst.append(avg_value)
    #添加表头
    num_lst.insert(0,title_name)
    return num_lst




#绘制表格
def table(number_lst):
    #创建初始化列表
    table=PrettyTable(['rw_type/degree','max_value','min_value','avg_vale'])  #单位是次
    #添加数据行
    for item in number_lst:
        table.add_row(item) 
    #打开文件将收集的数据以列表的形式写入到文件中  
    with open('/root/Data_collection/all_data_txt/max_min_avg.txt','w',encoding='utf-8') as f:
        f.write(table.get_string())




























