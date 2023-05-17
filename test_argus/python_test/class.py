
class Student():
    def __init__(self, name):
        self.name = name
        self.score = {'數學':0 ,'英文':0 ,'物理':0}

    # 可以利用self取得自己這個類別裡面的變數
    def readMyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')

    def printscore(self):
        print('數學 > ' + str(self.score['數學']) + '，英文 > ' + str(self.score['英文']) + '，物理 > ' + str(self.score['物理']))

    def compare(self,B):
        A_total = self.score['數學'] + self.score['英文'] + self.score['物理']
        B_total = B.score['數學'] + B.score['英文'] + B.score['物理']

        if A_total > B_total:
          print(self.name + '贏了！')
        elif A_total < B_total:
          print('可...可惡，難道，這就是' + B.name + '真正的實力嗎？')
        else:
          print('什麼？竟然平手？！')

ming = Student('阿明')
mei = Student('小美')
print(ming.name)
print(mei.name)
ming.readMyName()
mei.readMyName()

ming.score['數學']=55
ming.score['英文']=70
ming.score['物理']=55
mei.score['數學']=90
mei.score['英文']=88
mei.score['物理']=100
ming.printscore()
mei.printscore()

how = Student('HowHow')
how.score['數學']=80
how.score['英文']=60
how.score['物理']=40
print(how.name)
how.readMyName()
how.printscore()

ming.compare(mei)

"""ans"""

"""
class Student():
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def readMyName(self):
        print('聽清楚了，我的名字是' + self.name + '!!!')

    def compare(self, b):
        diff = sum(self.score.values()) - sum(b.score.values())
        # 有冒號的式子如果底下程式碼只有一行，也可以選擇直接和判斷式寫成同一行
        if diff > 0: print(self.name + '贏了！')
        elif diff == 0: print('什麼？竟然平手？！')
        else: print('可...可惡，難道，這就是' + b.name + '真正的實力嗎？')


ming = Student('阿明', {'數學':55, '英文':70, '物理':55})
mei = Student('小美', {'數學':90, '英文':88, '物理':100})
howhow = Student('HowHow', {'數學':80, '英文':60, '物理':40})
print(ming.name)
print(mei.name)
print(how.name)
print('\n阿明 vs HowHow')
ming.compare(how)
print('\n阿明 vs 小美')
ming.compare(mei)
print('\n小美 vs HowHow')
mei.compare(how)

"""
