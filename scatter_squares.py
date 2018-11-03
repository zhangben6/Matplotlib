'''使用scatter()绘制散点图并设置其样式'''
import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)

#设置图标标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Squares of value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()