from ressource_library import PROCESSORS_NAME
import matplotlib.pyplot as plt
import numpy as np


def energy_consumption_pie_chart(energy_consumption_table):
    sum_energy = []
    for p in PROCESSORS_NAME:
        p_energy_consumption = sum(
            [round(energy, 6) for energy in energy_consumption_table.loc[p].values if energy != '-'])
        sum_energy.append(p_energy_consumption)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = PROCESSORS_NAME
    sizes = np.array(sum_energy)/100

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


def time_bar_graph(execution_time_table):
    time_list = []
    for p in PROCESSORS_NAME:
        p_execution_time = sum(
            [round(energy, 6) for energy in execution_time_table.loc[p].values if energy != '-'])
        time_list.append(p_execution_time)
    # plot like column
    plt.figure()
    plt.bar(PROCESSORS_NAME, time_list, color=['blue', 'green', 'orange'], label='')
    plt.show()

