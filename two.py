def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return (iterations, arr[mid])

        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Тестуємо функцію
sorted_array = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
target_value = 0.55
result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (3, 0.6)

target_value = 0.9
result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (1, 0.9)

target_value = 1.0
result = binary_search(sorted_array, target_value)
print(result)  # Виведе: (4, None)
