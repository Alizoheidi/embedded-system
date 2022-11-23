import pandas

execution_time_table = pandas.DataFrame(data=[[0.1,0.1,0.2,0.2],[0.3,0.3,0.4,0.4],[0.2,0.2,0.3,0.3]],
                                        index=['fpga','risc','HWM'],columns=['+','-','*','/'])

