#coding=utf-8
import survey
from functools import reduce
table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)


# 1. 在 survey.py 和数据文件的目录中创建一个 first.py 文件，然后将下 面的代码输入或复制到文件中:
# import survey
# table = survey.Pregnancies()
# table.ReadRecords()
# print 'Number of pregnancies', len(table.records)
# 结果应该是 13 593 条怀孕记录。
# 2. 编写一个循环遍历表(table)，计算其中活婴的数量。查阅临床结

def alive(table):
    n=0
    for i in table.records:
        if(i.outcome ==1):
            n=n+1
    return n  #9148



# 果(outcome)的文档，确认你的结果跟文档中的总结一致。
# 3. 修改这个循环，将活婴的记录分成两组:一组是第一胎出生;另一 组是其他情况。再看一些出生顺序(birthord)的文档，看看你 的结果跟文档中的结果是否一致。
def getFirstAndOther(table):
    firstB=[]
    notFirstB=[]
    for i in table.records:
        if(i.outcome ==1 and i.birthord==1):
            firstB.append(i)
        elif (i.outcome ==1 and i.birthord!=1):
            notFirstB.append(i)
    return firstB,notFirstB

# 在处理新的数据集时，这种检查对于发现数据中的错误和不一致 性、检查程序中的错误以及检验对字段编码方式的理解是否正确等 都是很有用的。
# 4. 分别计算第一胎婴儿和其他婴儿的平均怀孕周期(单位是周)。两 组之间有差异吗?差异有多大?
#add=lambda x1,x2:x1.prglength+x2.prglength
def MeanPrg(PregnancyArr):
    return reduce(lambda x1,x2: x1 + x2 ,map(lambda x:x.prglength, PregnancyArr) )   /  float(len(PregnancyArr))

#firstBAvg= reduce(lambda x1,x2: x1 + x2 ,map(lambda x:x.prglength, firstB) )   /  float(len(firstB))
#notFirstBAvg= reduce(lambda x1,x2: x1 + x2 ,map(lambda x:x.prglength,notFirstB) )  / float(len(notFirstB))
#print firstBAvg#38.6009517335
#print notFirstBAvg#38.5229144667
