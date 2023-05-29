''' Exercise 1 '''

def asteriskLists(n):
    list = []
    for i in range(1, n+1):
        asterisk = '*' * i
        list.append(asterisk)
    return list

#Testing the funcion
result = asteriskLists(5)
print('\n')
print(result, '\n')





''' Exercise 2 '''

def smallAbsoluteDiff(array):
    array.sort()
    minorDiff = float('inf')
    pairs = [] 

    for i in range(len(array) - 1):
        diff = abs(array[i] - array[i + 1])

        if diff < minorDiff:
            minorDiff = diff
            pairs = [(array[i], array[i + 1])]
        elif diff == minorDiff:
            pairs.append((array[i], array[i + 1]))

    return pairs

#Testing the function
array = [3, 8, 50, 5, 1, 18, 12]
result = smallAbsoluteDiff(array)
print(result, '\n')





''' Exercise 3 '''

def findSubsets(nums):
    subsets = [[]]

    for num in nums:
        newSubsets = []

        for subset in subsets:
            newSubset = subset + [num]
            newSubsets.append(newSubset)

        subsets.extend(newSubsets)
    return subsets

#Testing the function
nums = [1, 2]
result = findSubsets(nums)
print(result, '\n')
