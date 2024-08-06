
# Solution 1
# Time - O(n^2); Space - O(1)
def two_number_sum(array, target_sum):
    for idx1 in range(len(array)):
        x = array[idx1]
        for idx2 in range(idx1+1, len(array)):
            y = array[idx2]
            if x + y == target_sum:
                return [x, y]

    return []


# Solution 2
# Time - O(nlog(n)); Space - O(1)
def two_number_sum(array, target_sum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        x = array[left]
        y = array[right]
        if x + y == target_sum:
            return [x, y]
        elif x + y < target_sum:
            left += 1
        elif x + y > target_sum:
            right -= 1

    return []


# Solution 3
# Time - O(n); Space - O(n)
def two_number_sum(array, target_sum):
    table = {}
    for x in array:
        y = target_sum - x
        if y in table:
            return [x, y]
        table[x] = True

    return []
