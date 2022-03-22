# find two integers in array that sum up to the target, return their indexes
def two_sum(nums, target):
    prevMap: {}  # to store every element that comes before the current element
    # The value would be the Key, while the index would be dictionary value

    for i, n in enumerate(nums):
        diff = target - n  # store the difference as we saw in the notes about trees
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
        return


# find two integers in a one based sorted array that sum up to a target
# and return their index in the form (x, y) where (x < y)
def two_sums2(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        curSum = nums[l] + nums[r]

        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l + 1, r + 1]
    return


# Find all the three integers in an array that sum up to zero
# Do not return the same numbers twice.
def three_sum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[1], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
