from random import randint
# 原始資料
stack1 = [2, 1]
stack2 = []
stack3 = []
print('\n初始狀態')
print('塔一資料：', stack1)
print('塔二資料：', stack2)
print('塔三資料：', stack3, '\n')
print('------------------')

count = 0
# Divide & Conquer Start
def move(layer, move_from, move_tmp, move_to, count):
    if layer == 0:
        return count
    count = move(layer -1, move_from, move_to, move_tmp, count)    
    num = move_from.pop()
    move_to.append(num)
    # 移動過程
    count += 1
    print('第', count, '步')
    print('塔一資料：', stack1)
    print('塔二資料：', stack2)
    print('塔三資料：', stack3)
    print('------------------')
    count = move(layer -1, move_tmp, move_from, move_to, count)
    return count


count = move(len(stack1), stack1, stack2, stack3, count)

# Divide & Conquer End

# 輸出結果
print('\n最終結果:', count, '次')
print('塔一資料：', stack1)
print('塔二資料：', stack2)
print('塔三資料：', stack3, '\n')
