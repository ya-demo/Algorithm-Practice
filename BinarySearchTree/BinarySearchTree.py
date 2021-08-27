from hashlib import new
from random import randint

# 原始資料
count = randint(3, 10)
nums = [randint(1, 20) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Binary Search Tree Start
tree = [None] * len(nums)
sort_asc_nums = []
sort_desc_nums = []

# 新增一個節點
def addTreeNode(num, root_idx = 0):
    while root_idx >= len(tree):
        extend_tree()
    if tree[root_idx] == None:
        tree[root_idx] = num
        return

    if num == tree[root_idx]:
        print(f'{num} is exist value!')
        return
    elif num < tree[root_idx]:
        left_idx = (root_idx + 1)*2 - 1
        addTreeNode(num, left_idx)
    else: 
        right_idx = (root_idx + 1)*2
        addTreeNode(num, right_idx)

# 搜尋值的位置
def search_idx(num, root_idx = 0):
    if root_idx >= len(tree): return -1
    if tree[root_idx] == None: return -1

    if num == tree[root_idx]:
        return root_idx
    elif num < tree[root_idx]:
        left_idx = (root_idx+1) * 2 - 1
        return search_idx(num, left_idx)
    else:
        right_idx = (root_idx+1) * 2
        return search_idx(num, right_idx)

# 若陣列太小 擴展這個陣列
def extend_tree():
    new_tree = [None] * (len(tree) * 2)
    for idx in range(len(tree)):
        new_tree[idx] = tree[idx]
    tree[:] = new_tree

# 取得最小值
def get_min(root_idx = 0):
    left_idx = (root_idx+1)*2-1
    if left_idx >= len(tree) or tree[left_idx] is None: 
        return tree[root_idx]
    return get_min(left_idx)
    
# 取得最大值
def get_max(root_idx = 0):
    right_idx = (root_idx+1)*2
    if right_idx >= len(tree) or tree[right_idx] is None: 
        return tree[root_idx]
    return get_max(right_idx)

# 正排序
def tree_sort_asc(root_idx = 0):
    if root_idx >= len(tree): return
    if tree[root_idx] is None: return
    
    tree_sort_asc((root_idx+1)*2-1)
    sort_asc_nums.append(tree[root_idx])
    tree_sort_asc((root_idx+1)*2)

# 倒排序
def tree_sort_desc(root_idx = 0):
    if root_idx >= len(tree): return
    if tree[root_idx] is None: return

    tree_sort_desc((root_idx+1)*2)
    sort_desc_nums.append(tree[root_idx])
    tree_sort_desc((root_idx+1)*2-1)

# 二元搜尋法
def binary_search(num, start_idx, end_idx):
    if start_idx > end_idx: return -1
    center_idx = int((start_idx + end_idx)/2)
    if num == sort_asc_nums[center_idx]:
        return center_idx    
    elif num > sort_asc_nums[center_idx]:
        return binary_search(num, center_idx+1, end_idx)
    elif num < sort_asc_nums[center_idx]:
        return binary_search(num, start_idx, center_idx-1)
    else:
        return -1

for num in nums:
    addTreeNode(num)

tree_sort_asc()
tree_sort_desc()

print('\ntree search index:')
for i in range(count):
    idx = search_idx(nums[i])
    print(f'val: {tree[idx]} -> idx: {idx}')
print('\nbinary search index:')   
for i in range(count):
    sort_idx = binary_search(nums[i], 0, len(sort_asc_nums)-1)
    print(f'val: {sort_asc_nums[sort_idx]} -> idx: {sort_idx}')
# Binary Search Tree End

# 輸出結果
print('\n輸出資料：', tree)
print('最大值：', get_max())
print('最小值：', get_min())
print('正排序：', sort_asc_nums)
print('倒排序：', sort_desc_nums, '\n')
