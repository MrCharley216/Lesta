def merge_sort(arr, n):
    if n <= 1:
        return arr
    left = merge_sort(arr[0: len(arr)//2], n//2)
    right = merge_sort(arr[len(arr)//2: n], n//2)
    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]


if __name__ == '__main__':
    n = 8
    arr = [3, 1, 0, 2, 6, 5, 4, 7]
    result = merge_sort(arr, n)
    print(result)
