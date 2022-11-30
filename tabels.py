import pandas

#         +   -   *   /
# FPGA | 0.1 0.1 0.2 0.2
# RISC | 0.3 0.3 0.4 0.4
# Cisc | 0.2 0.2 0.3 0.3
execution_time_table = pandas.DataFrame(data=[[0.1, 0.1, 0.2, 0.2], [0.3, 0.3, 0.4, 0.4], [0.2, 0.2, 0.3, 0.3]],
                                        index=['fpga', 'risc', 'Cisc'], columns=['+', '-', '*', '/'])

# ----------------------------------------------
# FPGA ( XC 2064)  : 33 MHZ
# RISC ( IBM 801)  : 15 MHz
# Cisc ( INTEL X88): 10 MHZ
clock_rate = pandas.Series(data=[33, 15, 10], index=['fpga', 'risc', 'Cisc'])
