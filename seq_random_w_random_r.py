#coding=UTF-8
from alter_config_run_vdbench_draw import alter_run_vdbench
from alter_config_run_vdbench_draw import table
from alter_config_run_vdbench_draw import draw_IOPS
from presetting_format import part_format
import threading  
import time  
from datetime import datetime


#初始化--format全盘
part_format()

#配置文件路径
config_path='/root/Data_collection/config_document/IOPS_vdbench_config.txt'
#表格列表

number_lst=[]
r_path='/root/Data_collection/all_data_txt/data.log'
w_path='/root/Data_collection/output/summary.html'

#1M顺序写--全盘
#配置参数并运行
alter_run_vdbench(config_path,title_name='1M_seq_W',rdpct=[0,0],seekpct=[0,0],xfersize=[0,'1M'],run_time=[0,600],interval=[0,1])
#收集数据并绘图
figure_lst=draw_IOPS(w_path,argument_string='IOPS',title_name='1M_seq_W',interval=[0,1])
number_lst.append(figure_lst)#收集表格行数据


#4K随机写--全盘
#配置参数并运行
alter_run_vdbench(config_path,title_name='4K_random_w',rdpct=[0,0],seekpct=[0,0],xfersize=[0,'4K'],run_time=[0,600],interval=[0,1])
#收集数据并绘图
figure_lst=draw_IOPS(w_path,argument_string='IOPS',title_name='4K_random_w',interval=[0,1])
number_lst.append(figure_lst)#收集表格行数据





#4K随机读--全盘
#循环函数
def secondary_function(current_time):  
    figure_lst=draw_IOPS(r_path,argument_string='IOPS',title_name=f'IOPS_{current_time}',interval=[0,1])
    return figure_lst 

#利用线程实现同时运行
try:
    def run_periodically(): 
        while True:  
            time.sleep(60)  # 等待60秒  
            current_time=datetime.now().strftime("%Y-%m-%d_%H:%M:%S")  
            figure=secondary_function(current_time) 
            # 启动一个单独的线程来运行定期任务  daemon=True守护线程---主程序结束也结束

    threading.Thread(target=run_periodically, daemon=True).start() 
        #运行主程序
    alter_run_vdbench(config_path,title_name='data',rdpct=[0,100],seekpct=[0,100],xfersize=[0,'4K'],run_time=[0,60000],interval=[0,1])
except KeyboardInterrupt:
    print('程序中断导出最新数据')
  

#导出完整列表
table(number_lst)

