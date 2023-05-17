# from random import random as rd
import random

print("Python Test")

#
# lt1=[]
# for i in range(1,11):
#     if i % 2 == 0:
#         for j in range(1,11):
#             if j % 2 == 0:
#                 lt1.append(i*j)

# print("lt1 >> " , lt1)
# print("lt2 >> " , [i*j for i in range(2,11,2) for j in range(2,11,2)])


# -------------------- fff -------------------- #
# 猜數字
# value=0
# max=99
# min=0

"""全部"""
# Num=random.randint(0,100)

"""猜數字-去除指定數字"""
# avoid_lt = [4, 14, 44, 94]
# ans=[i for i in range(1,100) if i not in avoid_lt]
# Num=random.choice(ans)

# while  Num != value:
#     value=int(input("請輸入數字:"))
#     if Num > value:
#       min = value + 1
#       print("數字介於" + str(min) + "與" + str(max) + "之間")
#     elif Num < value:
#       max = value - 1
#       print("數字介於"+ str(min)+"與" + str(max) + "之間")
# else:
#     print("correct!")

# -------------------- XAXB -------------------- #
answer = random.sample(range(1, 10), 4)
# print(answer)
a = b = n = 0                            # 設定 a、b、n 三個變數，預設值 0
while a!=4:                              # 使用 while 迴圈，直到 a 等於 4 才停止
    a = b = n = 0                        # 每次重複時將 a、b、n 三個變數再次設定為 0
    user = list(input('輸入四個數字：'))    # 讓使用者輸入數字，並透過 list 轉換成串列
    for i in user:                       # 使用 for 迴圈，將使用者輸入的數字一一取出
        if int(user[n]) == answer[n]:    # 因為使用者輸入的是「字串」，透過 int 轉換成數字，和答案串列互相比較
            a += 1                       # 如果位置和內容都相同，就將 a 增加 1
        else:
            if int(i) in answer:         # 如果位置不同，但答案裡有包含使用者輸入的數字
                b += 1                   # 就將 b 增加 1
        n += 1                           # 因為輸入的每個數字都要判斷，將 n 增加 1
    output = ','.join(user).replace(',','')    # 四個數字都判斷後，使用 join 將串列合併成字串
    print(f'{output}: {a}A{b}B')
print('答對了！')
