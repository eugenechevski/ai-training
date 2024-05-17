from datetime import datetime


def merge_intervals(meeting_times):
    # If the input list is empty, return an empty list
    if not meeting_times:
        return []

    # Sort the meetings by their start time
    meeting_times = sorted(meeting_times)
    merged_intervals = [list(meeting_times[0])]

    for start_time, end_time in meeting_times[1:]:
        # Get the last sublist of the merged interval
        last_start, last_end = merged_intervals[-1]

        if start_time <= last_end:
            # If the current start time is less than or equal to the last end time, merge it.
            # Update the last sublist's end time to the maximum of end times
            last_end = max(last_end, end_time)
            merged_intervals[-1][1] = last_end
        else:
            # If there is no overlap, add the current meeting as a new interval.
            merged_intervals.append([start_time, end_time])

    result = []
    # Convert the merged intervals back to tuples
    for interval in merged_intervals:
        result.append(tuple(interval))

    return result

# Example
meeting_times = [(8, 10), (9, 11), (14, 16),(16, 18), (18, 20)]
result = merge_intervals(meeting_times)  
print(result)