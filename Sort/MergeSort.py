from random import randint
# 原始資料
count = randint(1, 10)
nums = [randint(1, 100) for i in range(count)]
print('\n原始資料：', nums, '\n')


# Merge Sort Start
def merge_sort(nums, start_idx, end_idx):
    if start_idx >= end_idx: return
    
    center = int((end_idx + start_idx) / 2)
    print('target:', nums[start_idx: end_idx+1])
    print('left:', nums[start_idx: center+1])
    print('right:', nums[center+1: end_idx+1])
    print('--------')
    merge_sort(nums, start_idx, center)
    merge_sort(nums, center+1, end_idx)
    print('now:', nums)
    sort(nums, start_idx, center, center+1, end_idx)
    print('sort:', nums)
    print('--------')


def sort(nums, left_start_idx, left_end_idx, right_start_idx, right_end_idx):
    left_current_idx = left_start_idx
    right_current_idx = right_start_idx
    new_nums = []

    while True:
        if left_current_idx > left_end_idx and right_current_idx > right_end_idx: break
        if left_current_idx > left_end_idx:
            new_nums.extend(nums[right_current_idx:right_end_idx+1])
            break
        if right_current_idx > right_end_idx:
            new_nums.extend(nums[left_current_idx:left_end_idx+1])
            break

        left_num = nums[left_current_idx]
        right_num = nums[right_current_idx]
        if left_num < right_num:
            new_nums.append(left_num)
            left_current_idx += 1
        else:
            new_nums.append(right_num)
            right_current_idx += 1
            
    print(f'idx: {left_start_idx}-{right_end_idx}')
    print(f'old:{nums[left_start_idx:right_end_idx+1]}')
    for idx in range(left_start_idx, right_end_idx+1):
        nums[idx] = new_nums[idx-left_start_idx]
    print(f'new:{nums[left_start_idx:right_end_idx+1]}')
    
merge_sort(nums, 0, len(nums)-1)
# Merge Sort End

# 輸出結果
print('\n輸出資料：', nums, '\n')
