import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values,rw.y_values,s=5)
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break

# 终端显示:
# D:\Github_zack\Requests>python d:/Github_zack/Matplotlib/rw_visual.py
# Make another walk?(y/n)y
# Make another walk?(y/n)y
# Make another walk?(y/n)y
# Make another walk?(y/n)n