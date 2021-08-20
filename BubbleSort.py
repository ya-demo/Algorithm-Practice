import random
# 原始資料
count = random.randint(1, 10)
nums = [random.randint(1, 50) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Bubble Sort Start
def switch(nums, now, next):
    tmp = nums[now]
    nums[now] = nums[next]
    nums[next] = tmp

for round in range(len(nums)):
    times = len(nums) - round
    for index in range(1, times):
        if nums[index - 1] > nums[index]:
            switch(nums, index-1, index)
    print('處理資料：', nums)
# Bubble Sort End

# 輸出結果
print('\n輸出資料：', nums, '\n')
