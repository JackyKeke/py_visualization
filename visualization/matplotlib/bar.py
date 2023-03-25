from visualization.plt_util import get_plt
import pandas as pd
import seaborn as sns


# 条形图
def bar_sample():
    import seaborn as sns
    # 数据准备
    x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
    y = [5, 4, 8, 12, 7]
    # 用 Matplotlib 画条形图 xy调转不正常
    # get_plt().bar(y, x)
    # get_plt().show()
    # 用 Seaborn 画条形图 xy调转才是正常
    # sns.barplot(x=y, y=x)
    sns.barplot(x=x, y=y)
    get_plt().show()




if __name__ == '__main__':
    bar_sample()
