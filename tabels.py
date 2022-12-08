import pandas

PROCESSORS_NAME = ['fpga', 'risc', 'cisc']
TASKS_NAME = ['task_1', 'task_2', 'task_3', 'task_4', 'task_5', 'task_6']

# ---------------------------------------------------------------------
#                  clock rate     frequency rate   consume power
# FPGA ( XC 2064)  : 33 MHZ    ,      1.5 GHz         3.0 Mw
# RISC ( IBM 801)  : 15 MHz    ,      2.0 GHz         4.3 Mw
# Cisc ( INTEL X88): 10 MHZ    ,      2.5 GHz         6.3 Mw
ressource_library_table = pandas.DataFrame(data=[[33, 1.5, 3], [15, 2.0, 4.3], [10, 2.5, 6.3]],
                                           index=PROCESSORS_NAME, columns=['clock rate', 'frequency rate',
                                                                           'consume power'])

#     frequency | CPI_instruction
# * |    50             5
# + |    30             3
# - |    25             2
# / |    10             3
operations = pandas.DataFrame(data=[[50, 5], [30, 3], [25, 2], [10, 3]],
                              index=['*', '+', '-', '/'], columns=['frequency', 'CPI_instruction'])

operational_time = pandas.DataFrame(data=[[0.03, 0.015, 0.05, 0.04, 0.03, 0.01], [0.04, 0.025, 0.06, 0.05, 0.04, 0.02],
                                          [0.05, 0.03, 0.07, 0.07, 0.05, 0.02]],
                                    index=PROCESSORS_NAME, columns=TASKS_NAME)
