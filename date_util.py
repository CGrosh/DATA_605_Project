def time_cleaner(t):
    date, time = t.split()
    hour, minute, second = time.split(':')
    if int(hour) < 8:
        hour = int(hour) + 12
    
    return f'{date} {hour}:{minute}:{second}'
