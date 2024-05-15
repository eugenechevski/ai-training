def product_except_self(nums):
    # Create an array to store the products
    products = [1] * len(nums)
    
    # Calculate the product of all numbers to the left of each number
    left_product = 1
    for i in range(len(nums)):
        products[i] *= left_product
        left_product *= nums[i]
    
    # Calculate the product of all numbers to the right of each number
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        products[i] *= right_product
        right_product *= nums[i]
    
    return products

print(product_except_self([1, 2, 3, 4]))