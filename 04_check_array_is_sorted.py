def is_sorted(arr):
    flag = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            pass
        else:
            flag = False
    return flag


if __name__ == "__main__":
    my_arr = [1, 2, 30, 4, 5]
    print(is_sorted(arr=my_arr))
