import datetime

import pandas
import pandas as pd
from SortedPriorityQueue import SortedPriorityQueue


def prioritize(dataframe: pd.DataFrame) -> pd.DataFrame:
    my_queue = SortedPriorityQueue()
    day_weight = 1
    point_weight = 1
    weight_weight = 0

    today_date = pd.Timestamp(datetime.datetime.today())
    dataframe['Due Date'] = pd.to_datetime(dataframe['Due Date'])
    print(dataframe)

    # dataframe['Days Left'] = today_date
    # print(dataframe)
    # dataframe['Days Left'] = dataframe['Due Date'] - dataframe['Days Left']
    # print(dataframe)
    dataframe['Days Left'] = (dataframe['Due Date'] - today_date).dt.days
    print(dataframe)

    priority = day_weight * dataframe.iloc[:, 3] + point_weight * dataframe.iloc[:, 1] + weight_weight * \
               dataframe.iloc[:, 2]

    dataframe['Priority'] = priority
    print(dataframe)

    for index in range(len(dataframe)):
        my_queue.add(dataframe.iloc[index, 5], dataframe.iloc[index, 0])

    prioritized_dict = {'Assignment_Name': [], 'Priority': []}
    for index in range(len(my_queue)):
        key, value = my_queue.remove_min()
        prioritized_dict['Assignment_Name'].append(value)
        prioritized_dict['Priority'].append(key)
    return pd.DataFrame(prioritized_dict)
