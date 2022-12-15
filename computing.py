import pandas
from ressource_library import PROCESSORS_NAME
from tasks import TASKS_NAME
from tabels import operational_time_table

performance_table = pandas.DataFrame(
    data=[['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']],
    index=PROCESSORS_NAME,
    columns=TASKS_NAME)

execution_time_table = pandas.DataFrame(
    data=[['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']],
    index=PROCESSORS_NAME,
    columns=TASKS_NAME)

energy_consumption_table = pandas.DataFrame(
    data=[['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']],
    index=PROCESSORS_NAME,
    columns=TASKS_NAME)


def computing_results(graph, task_vertex):
    """
    :param graph: Graph object
    :param task_vertex: a task node which should be done
    """
    for processor in graph.give_nondirected_edges(task_vertex):
        # calculate cycle per instruction for each task
        instruction_count, frequency_rate, cpi_instruction = graph.vertices_functions[task_vertex]
        cpi = frequency_rate * cpi_instruction
        # get frequency rate and clock rate of each processor
        p_frequency_rate, p_clock_rate, p_consume_power = graph.vertices_functions[processor]
        # performance = clock rate/CPI
        performance = round(p_clock_rate / cpi, 3)
        # add data to the table
        performance_table.loc[processor][task_vertex] = performance
        # instruction_count = clock_rate/CPI
        instruction_count = p_clock_rate / cpi
        # execution time = (instruction_count*CPI)/frequency_rate
        execution_time = round((instruction_count * cpi) / p_frequency_rate, 3)
        # add data to the table
        execution_time_table.loc[processor][task_vertex] = execution_time
        # energy consumption = consume power * operational time
        energy_consumption = round(p_consume_power * operational_time_table.loc[processor][task_vertex],2)
        # add data to the table
        energy_consumption_table.loc[processor][task_vertex] = energy_consumption
        # going to next task
    for task in graph.give_directed_edges(task_vertex):
        computing_results(graph, task)
