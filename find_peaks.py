"""
https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

Given a numeric array -- a valid int array, return a dictionary (python) or object (Javascript)
in the format
{pos: [], peaks: []}

where the pos array contains the indices of the peaks, and peaks array contains their values.
Examples:

arr = [0, 1, 2, 5, 1, 0]
{pos: [3], peaks: [5]}


pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3])
{pos: [3, 7], peaks: [6, 3]}

[1, 2, 2, 2, 3]
{pos: [], peaks: []}

pickPeaks([1, 2, 2, 2, 1])
{pos: [1], peaks: [2]}
"""

'''
def pick_peaks(arr):
    # Initialize pos array
    pos = []
    # Initialize peaks array
    peaks = []
    return_dict = dict()
    # Initialize min and max variable
    min = None
    max = None
    max_index = 0
    # Iterate through array.
    for i, num in enumerate(arr):
        if not min: 
            min = num
            print('now min is ', str(min))
        if not max:
            max = num
            max_index = i
            print('now max is ', str(max))

        if num < min:
            min = num
            print('now min is ', str(min))
        elif num > min:
            if num < max:
                print('found a peak')
                pos.append(max_index)
                peaks.append(max)
                max = None
            elif num > max:
                max = num
                max_index = i
                print('now max is ', str(max))
        

    return_dict['pos'] = pos
    return_dict['peaks'] = peaks
    return return_dict
    '''


# print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
# print(pick_peaks([1, 2, 2, 2, 3]))
# print(pick_peaks([1, 2, 2, 2, 1]))

def pick_peaks(arr):
    # Initialize pos array
    pos = []
    # Initialize peaks array
    peaks = []
    return_dict = dict()
    current_peak_value = arr[0]  # None
    peak_index = 0  # None

    for i in range(1, len(arr)-1):
        # print(arr[i])
        if arr[i] > arr[i-1] and arr[i] < arr[i+1]:
            # print('continuing up')
            if not current_peak_value or arr[i+1] > current_peak_value:
                current_peak_value = arr[i+1]
                peak_index = i+1
        elif arr[i] < arr[i-1] and arr[i] > arr[i+1]:
            # print('going down')
        elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            # print('in a valley')
        elif arr[i] == arr[i-1] or arr[i] == arr[i+1]:
            if arr[i] > current_peak_value:
                current_peak_value = arr[i]
                peak_index = i
            # print('on a plateau')
        else:
            # print('at a peak')
            pos.append(peak_index)
            peaks.append(current_peak_value)
            peak_index = None
            current_peak_value = None
    # print('current peak value: ' + str(current_peak_value))
    if arr[-2] > arr[-1] and arr[-2] == current_peak_value:
        print('last check: ' + str(arr[-2]) + ' ' + str(arr[-1]))
        pos.append(arr.index(arr[-2]))
        peaks.append(arr[-2])
    return_dict['pos'] = pos
    return_dict['peaks'] = peaks

    return return_dict


# print(pick_peaks([0, 1, 2, 5, 1, 0]))  # {pos: [3], peaks: [5]}

# {'pos': [3, 7], 'peaks': [6, 3]}
# print(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]))
print(pick_peaks([1, 2, 2, 2, 3]))  # {'pos': [], 'peaks': []}
# print(pick_peaks([1, 2, 2, 2, 1]))  # {pos: [1], peaks: [2]}
