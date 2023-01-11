from computing import exe_mapping_option, performance_table, energy_consumption_table
from resource_library import PROCESSORS_NAME
from tasks import TASKS_NAME


def asp_resource_library(graph):
    p_name_str = ''
    p_consumePower_str = ''
    performance_str = ''
    energy_consumption_str = ''
    p_clock_rate_str = ''
    p_type_str = ''
    i = 0
    for p in PROCESSORS_NAME:
        p_performance = sum(
            [round(performance, 6) for performance in performance_table.iloc[i].values if performance != '-'])
        p_energy_consumption = sum(
            [round(energy, 6) for energy in energy_consumption_table.iloc[i].values if energy != '-'])
        i += 1
        p_type, cpi, p_frequency, p_consume_power, clock_rate = graph.vertices_functions[p]
        p_clock_rate_str += f'clock rate(r{i},{clock_rate}).\n'
        p_type_str += f'type(r{i},{p_type})\n'
        p_name_str += f'resourceTyp(r{i},{p}).\n'
        p_consumePower_str += f'consumePower(r{i},{p_consume_power}).\n'
        performance_str += f'performance(r{i},{p_performance}).\n'
        energy_consumption_str += f'frequency(r{i},{p_energy_consumption}).\n'

    str_data = p_name_str + p_type_str + p_consumePower_str + energy_consumption_str + performance_str + p_clock_rate_str

    with open('ASP_resource_library.lp', 'w') as f:
        f.truncate(0)
        f.write(str_data)

    return str_data


def asp_taskList(graph):
    instructionCount_str = ''
    sizeOfgraph = ''
    operator_str = "taskOperator(t1,+).\ntaskOperator(t2,-).\ntaskOperator(t3,*)." \
                   "\ntaskOperator(t4,*).\ntaskOperator(t5,+).\ntaskOperator(t6,/).\n"

    sucessors_str = "sucessors(s1,t1,0).\nsucessors(s2,t2,t1).\nsucessors(s3,t3,t2).\n" \
                    "sucessors(s4,t4,0).\nsucessors(s5,t5,t4).\nsucessors(s6,t6,t5).\n"

    task_id = ""

    for task in TASKS_NAME:
        task_id += f"taskId({task},a1).\n"
        instruction_count, frequency_rate = graph.vertices_functions[task]
        instructionCount_str += f"instructionCount({task},{instruction_count}).\n"
        sizeOfgraph += f'nodeDegree({task},{len(graph.give_nondirected_edges(task))}).\n'

    str_data = "application(a1).\n\n" + task_id + operator_str + sizeOfgraph + instructionCount_str + sucessors_str

    with open('ASP_taskList.lp', 'w') as f:
        f.truncate(0)
        f.write(str_data)

    return str_data


def asp_mapping_option():
    mappingOption_str = ''
    executionTime_str = ''
    i = 0
    for m in exe_mapping_option:
        i += 1
        mappingOption_str += f'mappingOption(m{i},{m[0]},{m[1]}).\n'
        executionTime_str += f'executionTime(m{i},{m[2]}).\n'

    str_data = mappingOption_str + '\n' + executionTime_str

    with open('ASP_mapping_option.lp', 'w') as f:
        f.truncate(0)
        f.write(str_data)
    return str_data
