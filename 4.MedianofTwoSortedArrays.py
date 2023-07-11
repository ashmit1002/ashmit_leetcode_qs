nums1 = []
nums2 = [2, 3]

nums = nums1 + nums2
nums.sort()
print(nums)

midway = len(nums) // 2
print(midway)

if len(nums) % 2 == 0:
    median = (nums[midway] + nums[midway - 1]) / 2
else:
    median = nums[midway]

print(float(median))