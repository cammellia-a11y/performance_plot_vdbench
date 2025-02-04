import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 原始数据点inter
y = np.array([0.042, 0.41, 0.386, 0.376, 0.371, 0.368, 0.357, 0.353, 0.346, 0.346, 0.334, 0.324, 0.299, 0.29, 0.284, 0.284, 0.284, 0.285, 0.285, 0.285]
)
x = np.array([50008.27, 79987.1, 110049.73, 140026.58, 170078.98, 199911.61, 229914.02, 259929.71, 290033.9, 309975.8, 339956.0, 370089.17, 399934.54, 429796.15, 446900.2, 445804.24, 446685.53, 446270.25, 445993.39, 445305.37]
)
#原始数据
y1 = np.array([0.092, 0.157, 0.228, 0.246, 0.241, 0.246, 0.255, 0.274, 0.301, 0.301, 0.297, 0.3, 0.336, 0.336, 0.337, 0.336,
      0.336, 0.337, 0.336, 0.336])
x1= np.array([50025.41, 79971.86, 109961.36, 139961.27, 169899.73, 199864.98, 229981.71, 259987.92, 289902.17, 309921.39,
      340001.86, 369974.81, 378862.59, 378695.88, 378359.25, 379034.93, 378611.0, 378426.58, 378991.85, 378711.27])
#our
# y2=[]
# x2=[]
#[50000, 80000, 110000, 140000, 170000, 200000, 230000, 260000, 290000, 310000, 340000, 370000, 400000, 430000, 460000, 490000, 510000, 540000, 570000, 600000]

# 插值，这里使用线性插值，也可以尝试'cubic'等
f = interp1d(x, y, kind='cubic')
# 创建一个更平滑的x轴用于绘图
xnew = np.linspace(x.min(), x.max(), 300)
ynew = f(xnew)



# 插值，这里使用线性插值，也可以尝试'cubic'等
f1 = interp1d(x1, y1, kind='cubic')
# 创建一个更平滑的x轴用于绘图
x1new = np.linspace(x1.min(), x1.max(), 300)
y1new = f1(x1new)


# 绘图
plt.plot(xnew, ynew,label='lain')
plt.plot(x1new, y1new,label='cubic')
#plt.scatter(x1, y1, color='red')  # 显示原始数据点
#plt.scatter(x, y, color='green')
plt.show()