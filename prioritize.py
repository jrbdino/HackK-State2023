import datetime

import pandas as pd
from SortedPriorityQueue import SortedPriorityQueue


def prioritize(dataframe: pd.DataFrame, priority_type: int) -> pd.DataFrame:
    my_queue = SortedPriorityQueue()

    # 1=grade, 2=day, 3=difficulty
    if priority_type == 1:
        grade_weight = 1
        day_weight = 0.2
        difficulty_weight = 0.2

    elif priority_type == 2:
        grade_weight = 0.2
        day_weight = 1
        difficulty_weight = 0.2

    elif priority_type == 3:
        grade_weight = 0.2
        day_weight = 0.2
        difficulty_weight = 1

    today_date = pd.Timestamp(datetime.datetime.today())
    dataframe['Due Date'] = pd.to_datetime(dataframe['Due Date'])

    dataframe['Days Left'] = (dataframe['Due Date'] - today_date).dt.days

    priority = 1 / ((day_weight * dataframe.iloc[:, 5]) + (grade_weight * dataframe.iloc[:, 3]) + (difficulty_weight *
                    dataframe.iloc[:, 4]))

    dataframe['Priority'] = priority

    for index in range(len(dataframe)):
        my_queue.add(dataframe.iloc[index, 5], dataframe.iloc[index, 0])

    prioritized_dict = {'Assignment_Name': [], 'Priority': []}
    for index in range(len(my_queue)):
        key, value = my_queue.remove_min()
        prioritized_dict['Assignment_Name'].append(value)
        prioritized_dict['Priority'].append(key)

    priority_frame = pd.DataFrame(prioritized_dict)
    priority_frame['Priority'] = range(1, len(priority_frame) + 1)
    return priority_frame
