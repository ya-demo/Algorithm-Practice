from random import randint
# 原始資料
count = randint(5, 15)
nums = [randint(1, 100) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Dfs Left Start
order = []
def pre_order(nums, idx):
    if idx >= len(nums):
        return
    left = ((idx + 1) * 2) -1  
    right = ((idx + 1 ) * 2 + 1) - 1
    order.append(nums[idx])
    pre_order(nums, left)
    pre_order(nums, right)

def in_order(nums, idx):
    if idx >= len(nums):
        return
    left = ((idx + 1) * 2) -1  
    right = ((idx + 1 ) * 2 + 1) - 1
    in_order(nums, left)
    order.append(nums[idx])
    in_order(nums, right)

def post_order(nums, idx):
    if idx >= len(nums):
        return
    left = ((idx + 1) * 2) -1  
    right = ((idx + 1 ) * 2 + 1) - 1
    post_order(nums, left)
    post_order(nums, right)
    order.append(nums[idx])


order.clear()
pre_order(nums, 0)
print('pre_order：', order)
order.clear()
in_order(nums, 0)
print('in_order：', order)
order.clear()
post_order(nums, 0)
print('post_order', order, '\n')
# Dfs Left End