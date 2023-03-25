from visualization.plt_util import get_plt


def box_plot_sample():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import pandas as pd

    # 数据准备
    # 生成 0-1 之间的 10*4 维度数据
    data = np.random.normal(size=(10, 4))
    lables = ['A', 'B', 'C', 'D']
    # 用 Matplotlib 画箱线图
    get_plt().boxplot(data, labels=lables)
    get_plt().show()
    # 用 Seaborn 画箱线图
    df = pd.DataFrame(data, columns=lables)
    sns.boxplot(data=df)
    get_plt().show()


if __name__ == '__main__':
    box_plot_sample()
