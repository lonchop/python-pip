import utils
from read_csv import read_csv
import charts
import matplotlib.pyplot as plt


def run():
    data = read_csv('data.csv')

    # data = list(
    #     filter(lambda item: item['Continent'] == 'South America', data))

    # countries = list(map(lambda x: x['Country'], data))
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    # charts.generate_pie_chart(countries, percentages)

    country = input('Type Country => ')

    result = utils.population_by_country(data, country)

    print(result[0])

    # def generate_bar_chart(labels, values):
    #     plt.bar(labels, values)
    #     plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    #     plt.show()

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        labels = list(labels)[::-1]
        values = list(values)[::-1]
        charts.generate_bar_chart(country['Country'], labels, values)


if __name__ == '__main__':
    run()
