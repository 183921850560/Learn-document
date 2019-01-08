# coding = utf-8
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, Locator


def draw(data, filepath, labels=['SUCCESS', 'FAIL', 'ERROR']):
    width = 1
    index = np.linspace(1, 5, 3)  # 生成数列 开始，结束，个数
    fig = plt.figure(10)
    ax = fig.add_subplot(111)
    rects = ax.bar(index-width/2+0.5, data, width, color=['green', 'orange', 'red'])
    auto_label(rects)
    ax.set_xticks(index)  # X轴数组
    ax.set_xticklabels(labels)   # 设置X轴坐标文本
    ml = MultipleLocator(1)
    if data[0] > 200:
        ml = MultipleLocator(50)
    elif data[0] > 100:
        ml = MultipleLocator(20)
    elif data[0] > 20:
        ml = MultipleLocator(10)
    Locator.MAXTICKS = 2000
    ax.yaxis.set_major_locator(ml)  # 设置Y轴主坐标间隔
    ax.yaxis.set_minor_locator(MultipleLocator(1))  # 设置Y轴次坐标间隔
    ax.set_ylabel('Numbers')
    ax.set_title('Statistical Chart Of Test Result')  # 设置图表标题
    # plt.show()
    plt.savefig(filepath+'/chart.png')
    plt.close()


# 显示设置柱状条上数值
def auto_label(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2, 1.01*height, '%s' % int(height))


if __name__ == '__main__':
    draw([1481, 490, 8], '.')