nums = [2,7,11,15]
target = 9

result = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        sum = nums[i] + nums[j]
        if sum == target:
            result.append(i)
            result.append(j)
            print(result)
            quit()