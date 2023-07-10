import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./images/{name}.png')
    plt.close()


def generate_pie_chart(labels, values, continent="North_America"):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig(f'./images/chart_pie_2.0.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 80]
    generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)
