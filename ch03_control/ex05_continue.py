for k in range(5):
    if(k==2):
        continue
    print(k)


k=0
while True:
    k=k+1
    if(k==2):
        print("continue")
        continue
    if(k>4):
        break
    print(k)
    