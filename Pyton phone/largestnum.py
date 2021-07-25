num = [10002, 23, 23, 3466, 45, 6, 5640000]

maxnum = num[0]

for i in num:
    if i > maxnum:
        maxnum = i
    print("current number",i,"maxnum",maxnum)

print("Max is ",maxnum)