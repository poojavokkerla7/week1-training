def two_sum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in hashmap:
            return [hashmap[diff], i]

        hashmap[nums[i]] = i

    return []

print(two_sum([2, 7, 11, 15], 9))
