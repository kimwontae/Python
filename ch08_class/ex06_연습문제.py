class Calculator:
    def __init__(self, num):
        self.num=num

    def sum(self):
        self.sum=0
        for i in self.num:
            self.sum+=i
        #print("sum= {0}".format(self.sum))
        return(self.sum)

    def avg(self):
        self.avg=self.sum/len(self.num)
        #print("avg= {0}".format(self.avg))
        return(self.avg)

cal1=Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2=Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())