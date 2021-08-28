from random import randint

# 原始資料
count = randint(3, 15)
nums = [randint(1, 50) for i in range(count)]
print('\n原始資料：', nums)

# Binary Heap Tree Start

def switch(now, target):
    tmp = nums[now]
    nums[now] = nums[target]
    nums[target] = tmp

def move_node_down(size, node_idx = 0):
    if node_idx >= size: return
    
    left_idx = (node_idx + 1) * 2 - 1
    right_idx = (node_idx + 1) * 2
    
    switch_idx = node_idx
    if left_idx < size and nums[switch_idx] < nums[left_idx]:
        switch_idx = left_idx
    if right_idx < size and nums[switch_idx] < nums[right_idx]:
        switch_idx = right_idx

    if switch_idx != node_idx:
        switch(node_idx, switch_idx)
        move_node_down(size, switch_idx)

def move_node_up(node_idx):
    if node_idx <= 0: return
    parent_idx = int((node_idx + 1) / 2) - 1
    if nums[node_idx] > nums[parent_idx]:
        switch(node_idx, parent_idx)
        move_node_up(parent_idx)
        
def remove():
    switch(len(nums)-1, 0)
    nums.pop()
    move_node_down(len(nums))

def add(num):
    nums.append(num)
    move_node_up(len(nums)-1)
    

def heap_sort():
    for idx in range(len(nums)-1, -1, -1):
        switch(idx, 0)
        move_node_down(idx)

def build_tree():
    for idx in range(len(nums)-1, -1, -1):
        move_node_down(len(nums), idx)

# Binary Heap Tree End

# 輸出結果
print('\n輸出資料：')
build_tree()
print('Binary Heap Tree：', nums)
remove()
print(f'Remove Node：', nums)
remove()
print(f'Remove Node：', nums)
remove()
print(f'Remove Node：', nums)
add_num = randint(1, 50)
add(add_num)
print(f'Add {add_num} Node：', nums)
add_num = randint(1, 50)
add(add_num)
print(f'Add {add_num} Node：', nums)
add_num = randint(1, 50)
add(add_num)
print(f'Add {add_num} Node：', nums)
heap_sort()
print('Heap Sort：', nums)