from random import randint
# 原始資料
location_count = randint(2, 5)
locations = [ location for location in range(location_count) ]
hours = [[ 0 if location == target else randint(1, 50) for target in range(location_count)] for location in range(location_count)]
condition = randint(50, 100)
print('\n位置資料：\n', str(locations))
print('時間成本：\n', str(hours).replace('],' , '],\n '))
print('目標時數：\n', condition, '\n')

# Backtracking Start
move_records = []
total_records = []
def move_next():
    total = 0
    for index in range(len(move_records) - 1):
        total += hours[move_records[index]][move_records[index+1]]
    if total >= condition:
        print('[X]',str(move_records).replace(',', ' ->'), ' = ', total)
        return
    if len(move_records) == len(locations):
        print('[O]',str(move_records).replace(',', ' ->'), ' = ', total)
        total_records.append(total)
        return

    for i in range(len(locations)):
        if locations[i] == -1:
            continue 
        move_records.append(i)
        tmp = locations[i]
        locations[i] = -1
        move_next()
        move_records.remove(i)
        locations[i] = tmp
    
start = 0
locations[start] = -1
move_records.append(start)
move_next()
# Backtracking End

# 輸出結果
print('\n符合條件路徑數：', len(total_records))
print('最佳路徑：', min(total_records) if len(total_records) > 0 else '(無)', '\n')