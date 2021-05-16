import random
try:
    filepath="monster_list.txt"
    count = len(open(filepath,encoding="utf-8").readlines())
    a=random.randint(0,count)
    f = open(filepath,"r",encoding="utf-8")# 返回一個檔案物件 
    line = f.readline()# 呼叫檔案的 readline()方法 
    for i in range(a):                
        line = f.readline()
    print(line)
    f.close() 
except:
    print("請放入monster_list.txt")
