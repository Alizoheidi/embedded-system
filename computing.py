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

exe_mapping_option = []


def computing_results(graph, task_vertex):
    """
    :param graph: Graph object
    :param task_vertex: a task node which should be done
    """
    for processor in graph.give_nondirected_edges(task_vertex):
        # get properties of each task
        instruction_count, frequency_rate, cpi_instruction = graph.vertices_functions[task_vertex]
        # get frequency ,cpi and clock rate of each processor
        cpi, p_frequency, p_consume_power = graph.vertices_functions[processor]
        # cycle time = 1/frequency
        cycle_time = 1 / p_frequency
        # execution time = instruction_count * CPI * cycle time
        execution_time = round(instruction_count * cpi * cycle_time, 3)
        # add data to the table
        execution_time_table.loc[processor][task_vertex] = execution_time
        # performance = 1/execution time
        performance = 1 / execution_time
        # add data to the table
        performance_table.loc[processor][task_vertex] = performance
        # energy consumption = consume power * operational time
        energy_consumption = round(p_consume_power * operational_time_table.loc[processor][task_vertex], 2)
        # add data to the table
        energy_consumption_table.loc[processor][task_vertex] = energy_consumption

        # ----create mapping options for .lp file----------------------------------
        exe_mapping_option.append((task_vertex, processor, execution_time))

        # going to next task
    for task in graph.give_directed_edges(task_vertex):
        computing_results(graph, task)
