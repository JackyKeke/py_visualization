from visualization.plt_util import get_plt


def histogram_sample():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # 数据准备
    a = np.random.randn(100)
    s = pd.Series(a)
    # 用 Matplotlib 画直方图
    get_plt().hist(s)
    get_plt().show()

    # 用 Seaborn 画直方图
    sns.distplot(s, kde=False)
    get_plt().show()

    sns.distplot(s, kde=True)
    get_plt().show()


if __name__ == '__main__':
    histogram_sample()
