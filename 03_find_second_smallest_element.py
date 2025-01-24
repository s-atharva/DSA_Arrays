def find_second_smallest_number(arr: list, n: int) -> int:
    if n < 2:
        return -1
    smallest = arr[0]
    s_smallest = float('inf')
    for num in arr:
        if num < smallest:
            s_smallest = smallest
            smallest = num
        if num != smallest and num < s_smallest:
            s_smallest = num
    return s_smallest


if __name__ == "__main__":
    arr = [5]
    n = len(arr)
    print(find_second_smallest_number(arr=arr, n=n))
