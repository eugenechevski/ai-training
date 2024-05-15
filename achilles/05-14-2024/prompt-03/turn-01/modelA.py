def product_except_self(nums):
    # Calculate prefix products
    prefix = [1]
    for num in nums[:-1]:
        prefix.append(prefix[-1] * num)

    # Calculate postfix products
    postfix = [1]
    for num in reversed(nums[1:]):
        postfix.append(postfix[-1] * num)
    postfix = list(reversed(postfix))

    # Calculate the final result
    result = []
    for i in range(len(nums)):
        result.append(prefix[i] * postfix[i])

    return result

print(product_except_self([1, 2, 3, 4]))