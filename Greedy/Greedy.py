from random import randint
from heapq import heapify, heappop, heappush
from Node import Node

# 原始資料
row = randint(2, 5)
col = randint(2, 5)
maze = [[randint(1, 10) for c in range(col)] for r in range(row)]
print('\n原始資料：\n', str(maze).replace('],' , '],\n '), '\n')

# Greedy Start
heap = []
maze_result = [[None for c in range(col)] for r in range(row)]

start = Node(0, 0)
target = Node(row - 1, col - 1)
    
start.cost = maze[start.row][start.col]
heap.append(start)
heapify(heap)

while True:
   if len(heap) <= 0:
        break

   now = heappop(heap)
   if maze_result[now.row][now.col] != None:
        continue
   maze_result[now.row][now.col] = now.cost

   # up
   if now.row - 1 >= 0:
        node = Node(now.row - 1, now.col)
        node.cost = now.cost + maze[now.row - 1][now.col]
        heappush(heap, node)
   # down
   if now.row + 1 < row:
        node = Node(now.row + 1, now.col)
        node.cost = now.cost + maze[now.row + 1][now.col]
        heappush(heap, node)
   # left
   if now.col - 1 >= 0:
        node = Node(now.row, now.col - 1)
        node.cost = now.cost + maze[now.row][now.col - 1]
        heappush(heap, node)
   # right
   if now.col + 1 < col:
        node = Node(now.row, now.col + 1)
        node.cost = now.cost + maze[now.row][now.col + 1]
        heappush(heap, node)
   print('移動過程：\n', str(maze_result).replace('],' , '],\n '))
# Greedy End

# 輸出結果
print('\n目標最短路徑：\n', maze_result[target.row][target.col], '\n')
