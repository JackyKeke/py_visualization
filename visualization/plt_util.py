import matplotlib.pyplot as plt


def get_plt():
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # 解决中文乱码
    return plt