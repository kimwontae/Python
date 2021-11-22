file_name='./ch09_str/coffeeShopSales.txt'

f=open(file_name)
for line in f:
    print(line, end='')
f.close()

f=open(file_name)
header=f.readline()
f.close()
print(header)

f=open(file_name)
header=f.readline()
header_list=header.split()
for line in f:
    data_list=line.split()
    print(data_list)

f.close()


f=open(file_name)
header = f.readline()
header_list = header.split()

espresso=[]
americano=[]
cafelatte=[]
cappucino=[]

for line in f:
    datalist = line.split()

    espresso.append(int(datalist[1]))
    americano.append(int(datalist[2]))
    cafelatte.append(int(datalist[3]))
    cappucino.append(int(datalist[4]))

f.close()

print("{0}: {1}".format(header_list[1], espresso))
print("{0}: {1}".format(header_list[2], americano))
print("{0}: {1}".format(header_list[3], cafelatte))
print("{0}: {1}".format(header_list[4], cappucino))

total_sum=[sum(espresso), sum(americano), sum(cafelatte), sum(cappucino)]
total_mean=[sum(espresso)/len(espresso), sum(americano)/len(americano), 
            sum(cafelatte)/len(cafelatte), sum(cappucino)/len(cappucino)]

for k in range(len(total_sum)):
    print('[{0}] 판매량'.format(header_list[k+1]))
    print('- 4일 판매량: {0}, 하루 평균: {1}'.format(total_sum[k], total_mean[k]))

