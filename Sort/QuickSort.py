from random import randint
# 原始資料
count = randint(1, 10)
nums = [randint(1, 100) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Quick Sort Start
def switch(nums, index, target):
    tmp = nums[index]
    nums[index] = nums[target]
    nums[target] = tmp

def quick_sort(nums, root, left_idx, right_idx):
    if len(nums) == 1: return
    if left_idx > right_idx: return
    root = sort(nums, root, left_idx, right_idx)
    print('\nnow：',nums[left_idx-1:right_idx+1])
    print('root: ',nums[root])
    print('left: ',nums[left_idx-1:root])
    print('right: ',nums[root+1:right_idx+1])
    quick_sort(nums, left_idx-1, left_idx, root-1)
    quick_sort(nums, root+1, root+2, right_idx)
    
def sort(nums, root, left_idx, right_idx) -> int:
    while True:
        if nums[left_idx] > nums[root] or left_idx >= right_idx: break
        left_idx += 1
    while True:
        if nums[right_idx] < nums[root] or right_idx <= left_idx: break
        right_idx -= 1
    if left_idx == right_idx:  
        if nums[root] >= nums[right_idx]:
            switch(nums, root, left_idx)
            root = left_idx
        else:
            switch(nums, root, left_idx -1)
            root = left_idx -1
        return root
    switch(nums, left_idx, right_idx)
    return sort(nums, root, left_idx, right_idx)

root = 0
quick_sort(nums, root, root+1, len(nums)-1)
# Quick Sort End

# 輸出結果
print('\n輸出資料：', nums, '\n')
