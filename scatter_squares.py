'''使用scatter()绘制散点图并设置其样式'''
import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values,y_values,s=30)

# #设置图标标题并给坐标轴加上标签
# plt.title("Square Number",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Squares of value",fontsize=14)
# #设置刻度标记的大小
# plt.tick_params(axis="both",which="major",labelsize=14)
# plt.show()



# python绘制1000个点和绘制5个点步骤一样,SO easy!!!
x_values = list(range(1,1001))

y_values = [x**2 for x in x_values]

# 删除黑色的轮廓edgecolor = 'none'
# plt.scatter(x_values,y_values,c = 'red',edgecolor='none',s=60)

# 使用颜色映射
plt.scatter(x_values,y_values,c = y_values,cmap=plt.cm.Blues,edgecolor='none',s=30)

#设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()