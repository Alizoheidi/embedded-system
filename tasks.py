import json

with open('task_list.json') as json_file:
    task_dict = json.load(json_file)
TASKS_NAME = list(task_dict.keys())


def add_task_nodes(graph):
    """
    :param graph: Graph object
    this function will add task nodes to the given graph
    """

    # first Task
    def t1():
        instruction_count = task_dict[TASKS_NAME[0]]["instruction count"]
        frequency_rate = task_dict[TASKS_NAME[0]]["frequency rate"]
        cpi_instruction = task_dict[TASKS_NAME[0]]["CPI instruction"]
        return instruction_count, frequency_rate, cpi_instruction

    graph.add_vertex(TASKS_NAME[0], t1())

    # second Task
    def t2():
        instruction_count = task_dict[TASKS_NAME[1]]["instruction count"]
        frequency_rate = task_dict[TASKS_NAME[1]]["frequency rate"]
        cpi_instruction = task_dict[TASKS_NAME[1]]["CPI instruction"]
        return instruction_count, frequency_rate, cpi_instruction

    graph.add_vertex(TASKS_NAME[1], t2())

    # third Task
    def t3():
        instruction_count = task_dict[TASKS_NAME[2]]["instruction count"]
        frequency_rate = task_dict[TASKS_NAME[2]]["frequency rate"]
        cpi_instruction = task_dict[TASKS_NAME[2]]["CPI instruction"]
        return instruction_count, frequency_rate, cpi_instruction

    graph.add_vertex(TASKS_NAME[2], t3())

    # forth Task
    def t4():
        instruction_count = task_dict[TASKS_NAME[3]]["instruction count"]
        frequency_rate = task_dict[TASKS_NAME[3]]["frequency rate"]
        cpi_instruction = task_dict[TASKS_NAME[3]]["CPI instruction"]
        return instruction_count, frequency_rate, cpi_instruction

    graph.add_vertex(TASKS_NAME[3], t4())

    # fifth Task
    def t5():
        instruction_count = task_dict[TASKS_NAME[4]]["instruction count"]
        frequency_rate = task_dict[TASKS_NAME[4]]["frequency rate"]
        cpi_instruction = task_dict[TASKS_NAME[4]]["CPI instruction"]
        return instruction_count, frequency_rate, cpi_instruction

    graph.add_vertex(TASKS_NAME[4], t5())

    # sixth Task
    def t6():
        instruction_count = task_dict[TASKS_NAME[5]]["instruction count"]
        frequency_rate = task_dict[TASKS_NAME[5]]["frequency rate"]
        cpi_instruction = task_dict[TASKS_NAME[5]]["CPI instruction"]
        return instruction_count, frequency_rate, cpi_instruction

    graph.add_vertex(TASKS_NAME[5], t6())

    initial_nodes = (TASKS_NAME[0], TASKS_NAME[3])

    return initial_nodes
