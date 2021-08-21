import random
# 原始資料
count = random.randint(1, 10)
nums = [random.randint(1, 50) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Insertion Sort Start
def switch(nums, now, target):
    tmp = nums[now]
    nums[now] = nums[target]
    nums[target] = tmp

for start in range(len(nums)):
    for index in range(start, 0, -1):
        if nums[index] < nums[index - 1]:
            switch(nums, index, index - 1)
        else:
            break
    print('處理資料：', nums)
# Insertion Sort End

# 輸出結果
print('\n輸出資料：', nums, '\n')
