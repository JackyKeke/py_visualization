import os

import seaborn as sns

from visualization.plt_util import get_plt


def pair_plot_sample():
    # 数据准备
    iris = sns.load_dataset('iris')
    # 用 Seaborn 画成对关系
    sns.pairplot(iris)
    get_plt().show()


if __name__ == '__main__':
    pair_plot_sample()
