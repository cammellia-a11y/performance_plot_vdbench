#coding=UTF-8
import matplotlib.pyplot as plt
def avg_data_to_plot(latecy_lst,IOPS_lst):
# 假设有两组数据
#     x_lst= [[1, 2, 3, 4, 5], [1, 7, 8, 9, 10]]
#     y_lst = [[1, 4, 9, 16, 25],  [2, 10, 5, 7, 11]] # 第一条线的Y轴数据
    #绘制线条
   
    for i in  range(len(IOPS_lst)):
        plt.plot(IOPS_lst[i],latecy_lst[i])
       
            


    #保存文件
    plt.savefig('plot.png')

# 显示图表
    plt.show()
#summery_data_to_plot()