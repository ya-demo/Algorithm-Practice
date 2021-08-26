from random import randint
from queue import Queue
# 原始資料
count = randint(5, 15)
nums = [randint(1, 100) for i in range(count)]
print('\n原始資料：', nums, '\n')

# Bfs Start
queue = Queue()
result = []
queue.put(0)
while True:
    if queue.empty(): break

    node_idx = queue.get()
    if node_idx >= len(nums):
        continue

    result.append(nums[node_idx])
    left_idx = ((node_idx + 1)*2)-1
    queue.put(left_idx)
    right_idx = (node_idx + 1)*2
    queue.put(right_idx)
# Bfs End

# 輸出結果
print('\n輸出資料：', result, '\n')