filename = open("PracticeInput.txt")
output = open("output.txt","w")
a = filename.readline()
n = a.strip().split(":")
rm_empty = n[1]
n = int(n[0])
onc = 0
ncd =0
esc = 0
begin_p = False
begin_n = False
counter = 0
node = 0
result = []
for a0 in filename:
    counter += 1
    if begin_p == False and a0.strip() == "[":
        begin_p = True
        continue
    elif begin_p==True and begin_n == False and a0 == "]":
        begin_p = False
    if begin_p:
        #if counter <50:
        #    print(a0)
        if a0.strip() == "[":
            begin_n = True
            ncd += 1
            continue
        elif a0.strip() =="]":
            begin_n = False
        if begin_n:
            if a0.strip() == "":
                esc +=1
                if rm_empty == "True":
                    continue
                else:
                    if node == 0:
                        result.append([""])
                        
                        node+=1
                    else:
                        result[-1].append("")
                        node += 1
                        
                        if node == n:
                            node = 0
            else:
                if node == 0:
                    result.append([a0.strip()])
                    node+=1
                else:
                    result[-1].append(a0.strip())
                    node += 1
                    if node == n:
                        node = 0



    else:
        break
#print(onc)
onc = len(result)
ncd = onc - ncd
if rm_empty == "True":
    esc1 = (n-len(result[-1]))-esc
    print(esc)
    esc = n-len(result[-1])

else:
    esc1 = n-len(result[-1])
    esc = esc + n - len(result[-1])
output.write(str(onc)+"\n")
output.write(str(ncd)+"\n")
output.write(str(esc1)+"\n")
output.write(str(esc)+"\n")
output.write("[\n")
counter = 0
#print("[")
for i in result:
    #print("[")
    counter = 0
    output.write("[\n")
    for j in i:
        counter +=1
        output.write(j+"\n")
        #print(j)
    for j in range(n - counter):
        output.write("\n")
    output.write("]\n")
    #print("]")
output.write("]\n")
#print("]")
