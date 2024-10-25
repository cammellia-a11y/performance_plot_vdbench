# coding=UTF-8
from open_total_get_data_to_list import get_data_to_lst
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def total_to_plot(x_argument,x_range,y_argument,y_range,z_argument,argument_string):
    # 创建数据
      # X轴数据
    #z_mb=[[794.8, 845.4, 845.8, 845.4, 845.6, 845.4, 846.8, 846.2], [766.6, 973.4, 1032.2, 1033.8, 1034.2, 1030.0, 1034.2, 1036.4], [750.4, 946.6, 1014.4, 1023.2, 1022.8, 1024.8, 1023.8, 1018.4], [807.2, 846.6, 846.4, 846.4, 846.6, 846.4, 846.6, 846.6]]
    
    z=np.array(z_argument)  # z轴

    #将数值进行反转
    # z_reversed =z[::-1]
    # x_reversed=x_range[::-1]

    # 将xy转化为网格坐标
    x,y = np.indices((len(x_range),len(y_range)))

   
    # 将xy展平
    X_flat = x.ravel()
    Y_flat = y.ravel()
    #z已经是平的，因为它直接来自一个二维数组
    Z_flat =z.ravel()

    #改变柱状图颜色
    def count_elements_in_2d_list(lst):  
        return sum(len(sublist) for sublist in lst) 
    # 使用 'RdYlGn'（红-黄-绿）颜色映射
    #colors = plt.cm.RdYlGn(np.linspace(0, 1, 32))
    colors = plt.cm.hot(np.linspace(0, 1,count_elements_in_2d_list(z_argument)))
    #colors = plt.cm.viridis(np.linspace(0, 1, ))
    #colors = plt.cm.spring(np.linspace(0, 1, 32))
    #colors = plt.cm.autumn(np.linspace(0, 1, 32))
    
    # 宽度和高度（这里我们假设dx和dy都是1，但您可以根据需要调整它们）
    dx = 0.3
    dy = 0.3
    dz = Z_flat  # dz就是z值，它决定了柱子的高度


    # 创建图形和3D子图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # 绘制三维柱状图
    ax.bar3d(X_flat, Y_flat, np.zeros_like(Z_flat), dx, dy, dz, color=colors)

    # 设置坐标轴标签和标题
    ax.set_xlabel('Block Size(KiB)')
    ax.set_ylabel('R/W Mix')
    #设置X轴标签
    if argument_string=='BW':
        ax.set_zlabel('MB/sec')
    elif argument_string=='IOPS':
        ax.set_zlabel('IOPS')
    ax.set_title('rw mix IOPS/BS 3D')

    # 设置x和y轴的刻度标签
    # 选择代表性的刻度位置
    x_ticks = np.arange(len(x_range))
    y_ticks = np.arange(len(y_range))

    # 设置刻度标签
    ax.set_xticks(x_ticks+dx/2)  # 偏移dx/2以将标签置于柱子中心
    ax.set_xticklabels(x_range)
    ax.set_yticks(y_ticks+dy/2)  # 偏移dy/2以将标签置于柱子中心
    ax.set_yticklabels(y_range)
    # 保存图片
    plt.savefig('avg_mb.png')
    # 显示图形
    plt.show()
