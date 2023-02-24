def study_schedule(permanence_period, target_time):
    n = len(permanence_period)
    counter = 0
    for index in range(0, n):
        start, end = permanence_period[index]
        if (type(start) is not int or type(end) is not int
                or type(target_time) is not int):
            return None
        elif start == '' or end == '':
            return None
        elif start <= target_time <= end:
            counter += 1
    return counter
