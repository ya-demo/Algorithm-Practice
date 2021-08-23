from random import randint
from heapq import heapify, heappop, heappush
from Location import Location
# 原始資料
location_count = randint(2, 5)
locations = [ location for location in range(location_count) ]
costs = [[ 0 if location == target else randint(1, 50) for target in range(location_count)] for location in range(location_count)]
print('\n位置資料：\n', str(locations))
print('花費成本：\n', str(costs).replace('],' , '],\n '), '\n')

# Branch & Bound Start
move_records = []
best = None
def move_next(root, best):
    total = 0
    for index in range(len(move_records) - 1):
        total += costs[move_records[index]][move_records[index+1]]
    if (best != None) and (total >= best):
        print('[bound]',str(move_records).replace(',', ' ->'), ' = ', total)
        return best
    if len(move_records) == len(locations):
        print('[update]',str(move_records).replace(',', ' ->'), ' = ', total)
        return total if best == None or total < best else best
    tmp_locations = [Location(location, costs[root][location]) for location in locations if location > -1]
    heapify(tmp_locations)
    while True:
        if len(tmp_locations) <= 0:
            return best
        next_location = heappop(tmp_locations)
        move_records.append(next_location.target)
        tmp = locations[next_location.target]
        locations[next_location.target] = -1
        best = move_next(next_location.target, best)
        move_records.remove(next_location.target)
        locations[next_location.target] = tmp
    
start = 0
locations[start] = -1
move_records.append(start)
best = move_next(start, best)
# Branch & Bound End

# 輸出結果
print('\n最佳路徑：', best, '\n')