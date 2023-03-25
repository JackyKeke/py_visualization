from visualization.plt_util import get_plt


def pie():
    # 数据准备
    nums = [25, 37, 33, 37, 6]
    labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
    # 用 Matplotlib 画饼图
    get_plt().pie(x=nums, labels=labels)
    get_plt().show()


if __name__ == '__main__':
    pie()
