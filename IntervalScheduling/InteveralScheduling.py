def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1])
    
    selected = []
    last_finish = float('-inf')
    
    for interval in intervals:
        start, finish = interval
        if start >= last_finish:
            selected.append(interval)
            last_finish = finish
            
    return selected

intervals = [(1, 3), (2, 5), (4, 6), (6, 8)]
print(interval_scheduling(intervals))