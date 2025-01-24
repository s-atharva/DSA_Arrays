def find_second_largest_elem(my_arr: list, length: int) -> int:
    if length < 2:
        return -1
    largest = arr[0]
    for num in my_arr:  # O(N)
        if num > largest:
            largest = num

    second_largest = float('-inf')
    for num in my_arr:  # O(N)
        if num > second_largest and num < largest:
            second_largest = num

    if largest == second_largest:
        return -1
    else:
        return second_largest


def find_second_largest_elem_best(my_arr: list, length: int) -> int:
    largest = my_arr[0]
    s_largest = -1
    for num in my_arr:
        if num > largest:
            s_largest = largest
            largest = num
        elif num < largest and num > s_largest:
            s_largest = num

    return s_largest


if __name__ == "__main__":
    arr = [1, 3, 3]
    n = len(arr)
    # print(find_second_largest_elem(my_arr=arr, length=n))  # O(2N)
    print(find_second_largest_elem_best(my_arr=arr, length=n))
