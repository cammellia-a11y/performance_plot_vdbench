#coding=UTF-8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
def avg_data_to_plot(y_lst,x_lst,x_name,y_name,title_name):
# 假设有两组数据
    # x_lst= [[1, 2, 3, 4, 5], [1, 7, 8, 9, 10]]
    # y_lst = [[1, 4, 9, 16, 25],  [2, 10, 5, 7, 11]] # 第一条线的Y轴数据
    #绘制线条
    print(x_lst)
    print(y_lst)
    # 创建图表  
    plt.figure(figsize=(12, 10))  # 设置图表大小  


    # x=np.array(x_lst)
    # y=np.array(y_lst)

    # #绘制曲线图
    # f = interp1d(x, y, kind='cubic')
    # # 创建一个更平滑的x轴用于绘图
    # xnew = np.linspace(x.min(), x.max(), 300)
    # ynew = f(xnew)


    #标注不同状态下的曲线
    plt.plot(x_lst,y_lst,label='W_SSD')
    # 添加图例
    plt.legend()
    # 显示网格线  
    plt.grid(True)  

    # 确保x轴和y轴的0点在同一位置  
    plt.ylim(0, max(y_lst) + 1)  # 确保Y轴从0开始
    plt.xlim(0, max(x_lst) + 1)  # 确保X轴从0开始

    #刻度
    tick_positions=[]
    #lable_lst=[]
    n=0
    x_interval=len(x_lst)//10

    for i in range(1,11):
        n+=x_interval
        tick_positions.append(x_lst[n-1])
   
    plt.xticks(tick_positions)

    #显示变量图标
    plt.xlabel(f'{x_name}')
    plt.ylabel(f'{y_name}')
    plt.title(f'{title_name}')
        
        
    #保存文件
    plt.savefig(f'/root/Data_collection/all_data_txt/{title_name}')
    #显示图表
    plt.show()


       
            


