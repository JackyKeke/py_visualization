import matplotlib.pyplot as plt
import seaborn as sns

from visualization.plt_util import get_plt


def heatmap_sample():
    # 数据准备
    flights = sns.load_dataset("flights")
    data = flights.pivot('year', 'month', 'passengers')
    # 用 Seaborn 画热力图
    sns.heatmap(data)
    get_plt().show()


if __name__ == '__main__':
    heatmap_sample()
