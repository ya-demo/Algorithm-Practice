import random
# 原始資料
count = random.randint(1, 10)
nums = [random.randint(1, 50) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Selection Sort Start
def switch(nums, now, target):
    tmp = nums[now]
    nums[now] = nums[target]
    nums[target] = tmp

for start in range(len(nums)):
    minIndex = start
    for index in range(start + 1, len(nums)):
        if nums[index] < nums[minIndex]:
            minIndex = index
    switch(nums, start, minIndex)
    print('處理資料：', nums)
# Selection Sort End

# 輸出結果
print('\n輸出資料：', nums, '\n')
