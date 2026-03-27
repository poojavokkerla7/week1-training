def product_except_self(nums):
    result = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)

    return result

print(product_except_self([1,2,3,4]))
