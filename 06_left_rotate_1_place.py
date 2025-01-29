def left_rotate_by_one_place_01(arr: list[int]):
    # check if the list is empty
    if not arr:
        return
    first_element = arr.pop(0)
    arr.append(first_element)
    return arr


def left_rotate_by_one_place_02(arr: list[int]):
    # check is the list is empty
    if not arr:
        return
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    arr[len(arr) - 1] = temp
    return arr


my_arr = [1, 2, 3, 4, 5]
print(left_rotate_by_one_place_02(arr=my_arr))
