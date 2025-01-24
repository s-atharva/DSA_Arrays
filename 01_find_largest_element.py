def find_largest_elem(my_arr: list) -> int:
    largest = my_arr[0]
    for i in range(len(my_arr)):
        if my_arr[i] > largest:
            largest = my_arr[i]
    return largest


if __name__ == '__main__':
    arr = [3, 2, 1, 5, 2]
    print(find_largest_elem(my_arr=arr))
