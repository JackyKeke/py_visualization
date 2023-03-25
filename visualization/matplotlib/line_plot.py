
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

from visualization.plt_util import get_plt


def external_data_line_plot_sample(x, y):
    # 使用 Seaborn 画折线图
    df = pd.DataFrame({'x': x, 'y': y})
    sns.lineplot(x="x", y="y", data=df)

    # 获取图的坐标信息# 控制x轴显示的日期个数（如10个） start
    # ax = plt.gca()
    # # 设置日期的显示格式 (即“月-日”)
    # date_format = mpl.dates.DateFormatter("%m-%d")
    # ax.xaxis.set_major_formatter(date_format)  # 控制x轴显示的日期个数（如10个）
    # xlocator = mpl.ticker.LinearLocator(10)
    # ax.xaxis.set_major_locator(xlocator)
    # 获取图的坐标信息# 控制x轴显示的日期个数（如10个） end

    # 设置刻度标签之间的固定间隔，如7天或两周 start
    ax = plt.gca()
    xlocator = mpl.ticker.MultipleLocator(5)
    ax.xaxis.set_major_locator(xlocator)
    # 设置刻度标签之间的固定间隔，如7天或两周 end
    plt.xticks(rotation=45)
    plt.show()


# 折线图
def line_plot_sample():
    # 数据准备
    x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
    # 使用 Matplotlib 画折线图
    get_plt().plot(x, y)
    get_plt().show()

    # 使用 Seaborn 画折线图
    df = pd.DataFrame({'x': x, 'y': y})
    sns.lineplot(x="x", y="y", data=df)
    get_plt().show()


if __name__ == '__main__':
    line_plot_sample()
