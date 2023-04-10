# Function that returns a tuple of the average 
# grade and time of a given level.
def get_average(query_set, difficulty, classroom = 'General'):
    avergae_grade = [0, 0, 0]
    average_time = [0, 0, 0]
    total_logs = [0, 0, 0]

    for log in query_set:
        avergae_grade[log.level - 1] += log.grade
        average_time[log.level - 1] += log.time
        total_logs[log.level - 1] += 1

    for i in range(len(total_logs)):
        if(total_logs[i] != 0): 
            avergae_grade[i] /= total_logs[i]
            average_time[i] /= total_logs[i]

    return {'data':{'1':{'grade': avergae_grade[0], 'time': average_time[0]},
            '2':{'grade': avergae_grade[1], 'time': average_time[1]},
            '3':{'grade': avergae_grade[2], 'time': average_time[2]}}, 
            'difficulty': difficulty, 'classroom': classroom}