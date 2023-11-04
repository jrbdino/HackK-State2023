import pandas as pd
from SortedPriorityQueue import SortedPriorityQueue


def prioritize(dataframe: pd.DataFrame) -> pd.DataFrame:
    my_queue = SortedPriorityQueue()
    day_weight = 1
    point_weight = 1
    weight_weight = 0

    priority = day_weight * dataframe['Days Left Till Due'] + point_weight * dataframe['Assignment_Points'] + weight_weight * \
               dataframe['Assignment_Weight']

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
