import threading  
import time  
from datetime import datetime
from alter_config_run_vdbench_draw import draw_IOPS
from alter_config_run_vdbench_draw import alter_run_vdbench
from presetting_format import part_format

#初始化--format全盘
part_format()
#配置文件路径
config_path='/root/Data_collection/config_document/IOPS_vdbench_config.txt'
# 次函数，每隔60秒执行一次  
def secondary_function():  
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    figure_lst=draw_IOPS(argument_string='IOPS',title_name=f'IOPS_{current_time}_plot',interval=[0,5],x_interval=10)
    return figure_lst 
    # 这里可以添加其他需要定期执行的任务 

#主函数-调用次函数
def main_function(config_path):
    #global number_lst
    try:
        def run_periodically(): 
            time.sleep(50) 
            while True:  
                time.sleep(50)  # 等待60秒  
                figure=secondary_function()
                #number_lst.append(figure)  
        # 启动一个单独的线程来运行定期任务  daemon=True守护线程---主程序结束也结束
        threading.Thread(target=run_periodically, daemon=True).start() 
        #运行主程序
        alter_run_vdbench(config_path,rdpct=[0,100],seekpct=[0,100],xfersize=[0,'4K'],run_time=[0,600],interval=[0,5])
    except KeyboardInterrupt:
        print('程序中断导出最新数据')
  

main_function(config_path)
