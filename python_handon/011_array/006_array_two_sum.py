# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution
# Example:
#     Given nums = [2, 7, 11, 15], target = 26,
#     Because nums[2] + nums[3] = 11 + 15 = 26,
#     return [2, 3].


def solution(numbers, target):
    length = len(numbers)
    for i in range(length):
        for j in range(i, length):
            if numbers[i] + numbers[j] == target:
                return [i, j]


def main():
    numbers = [2, 7, 11, 15]
    target = 26
    solution_indices = solution(numbers, target)
    print(
        f'Given numbers = {numbers}, target = {target},\n'
        f'Because numbers[{solution_indices[0]}] + numbers[{solution_indices[1]}]'
        f' = {numbers[solution_indices[0]]} + {numbers[solution_indices[1]]}'
        f' = {numbers[solution_indices[0]] + numbers[solution_indices[1]]},\n'
        f'return {solution_indices}'
    )


if __name__ == '__main__':
    main()
