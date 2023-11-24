def divideString(string):
    list=[]
    for i in range(0,len(string),5):
        list.append(string[i:i+5])
    print(list)
        
divideString("Aaronn")