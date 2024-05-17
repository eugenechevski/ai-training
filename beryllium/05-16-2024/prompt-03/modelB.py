def merge_intervals(meeting_times):
    meeting_times.sort(key=lambda x: x[0])
    merged_intervals = []
    for meeting in meeting_times:
        if not merged_intervals or merged_intervals[-1][1] < meeting[0]:
            merged_intervals.append(list(meeting))
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], meeting[1])
    return merged_intervals

# Example
meeting_times = [(8, 10), (9, 11), (14, 16),(16, 18), (18, 20)]
result = merge_intervals(meeting_times)  
print(result)