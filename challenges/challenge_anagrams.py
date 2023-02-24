def is_anagram(first_string, second_string):
    string_one = merge_sort(list(first_string.lower()))
    string_two = merge_sort(list(second_string.lower()))

    if first_string == '' or second_string == '' or string_one != string_two:
        return ("".join(string_one), "".join(string_two), False)
    else:
        return ("".join(string_one), "".join(string_two), True)


def merge_sort(each_string, start=0, end=None):
    if end is None:
        end = len(each_string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(each_string, start, mid)
        merge_sort(each_string, mid, end)
        merge(each_string, start, mid, end)
    return each_string


def merge(each_string, start, mid, end):
    left = each_string[start:mid]
    right = each_string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            each_string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            each_string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            each_string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            each_string[general_index] = right[right_index]
            right_index = right_index + 1

    return each_string
