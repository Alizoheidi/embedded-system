from computing import exe_mapping_option, performance_table, energy_consumption_table
from ressource_library import PROCESSORS_NAME
from tasks import TASKS_NAME


def asp_resource_library(graph):
    p_name_str = ''
    p_consumePower_str = ''
    performance_str = ''
    energy_consumption_str = ''
    i = 0
    for p in PROCESSORS_NAME:
        p_performance = sum([round(performace, 6) for performace in performance_table.iloc[i].values if performace != '-'])
        p_energy_consumption = sum([round(energy, 6) for energy in energy_consumption_table.iloc[i].values if energy != '-'])
        i += 1
        cpi, p_frequency, p_consume_power = graph.vertices_functions[p]
        p_name_str += f'resourceTyp(r{i},{p}).\n'
        p_consumePower_str += f'consumePower(r{i},{p_consume_power}).\n'
        performance_str += f'p_performance(r{i},{p_performance}).\n'
        energy_consumption_str += f'frequency(r{i},{p_energy_consumption}).\n'

    str_data = "######  resources library\n\n" + p_name_str + p_consumePower_str + energy_consumption_str+ performance_str

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
    for t in TASKS_NAME:
        task_id += f"taskId({t},a1).\n"
        instruction_count, frequency_rate, cpi_instruction = graph.vertices_functions[t]
        instructionCount_str += f"instructionCount({t},{instruction_count}).\n"
        sizeOfgraph += f'sizeOfgraph({t},{len(graph.give_nondirected_edges(t))})\n'

    str_data = "####### task list\n\napplication(a1).\n\n" + task_id + operator_str + sizeOfgraph + instructionCount_str + sucessors_str

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

    str_data = '#######  mapping_option\n\n' + mappingOption_str + '\n' + \
               '##### dynamic_charactristic\n\n' + executionTime_str

    with open('ASP_mapping_option.lp', 'w') as f:
        f.truncate(0)
        f.write(str_data)
    return str_data
