import pandas
from ressource_library import PROCESSORS_NAME
from tasks import TASKS_NAME

operational_time_table = pandas.DataFrame(
        data=[[0.03, 0.015, 0.05, 0.04, 0.03, 0.01], [0.04, 0.025, 0.06, 0.05, 0.04, 0.02],
              [0.05, 0.03, 0.07, 0.07, 0.05, 0.02]],
        index=PROCESSORS_NAME, columns=TASKS_NAME)
