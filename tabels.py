import pandas
from ressource_library import PROCESSORS_NAME
#        t1  t2  t3
# FPGA | 0.1 0.1 0.2
# RISC | 0.3 0.3 0.4
# Cisc | 0.2 0.2 0.3
cycle_per_instruction_table = pandas.DataFrame(data=[[1.5, 0.9, 1.8], [2, 1.3, 2.4], [2.2, 1.5, 2.7]],
                                               index=PROCESSORS_NAME, columns=['task_1','task_2','task_3'])

# ----------------------------------------------
# clock rate
# FPGA ( XC 2064)  : 33 MHZ
# RISC ( IBM 801)  : 15 MHz
# Cisc ( INTEL X88): 10 MHZ
clock_rate = pandas.Series(data=[33, 15, 10], index=PROCESSORS_NAME)
