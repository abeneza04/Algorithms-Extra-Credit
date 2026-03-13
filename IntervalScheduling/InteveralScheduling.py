"""
Problem: Given a set of intervals (jobs) with start and finish times,
the goal is to select the maximum number of non-overlapping intervals.
Result is in the README
"""
def interval_scheduling(intervals):
    intervals.sort(key=lambda x: x[1]) # Sort intervals by finish time
    
    selected = []
    last_finish = float('-inf')
    
    for interval in intervals:
        start, finish = interval # Unpack the start and finish times of the interval
        if start >= last_finish:
            selected.append(interval)  # Add the interval to the selected list
            last_finish = finish
            
    return selected

intervals = [(1, 3), (2, 5), (4, 6), (6, 8)]
print("Original intervals:", intervals)
optimal_schedule = interval_scheduling(intervals)
print("Selected non-overlapping intervals:", optimal_schedule)