
numbers = ["1","2","3"]
shades = ["E","F","S"]
colors = ["G","P","R"]
shape = ["O","D","S"]
filename = open("Set-Game_InputForSubmission_1.txt")
out = open("output.txt","w")
counter = 0
for a0 in filename:
    if counter != 0:
        a, b = [x for x in a0.strip().split()]
        
        if a[0] == b[0]:
            n1 = a[0]
        else:
            n1 = 0
            for i in numbers:
                if i != a[0] and i != b[0]:
                    n1 = i
                    break
        if a[1] == b[1]:
            n2 = a[1]
        else:
            n2 = 0
            for i in shades:
                if i != a[1] and i != b[1]:
                    n2 = i
                    break
        if a[2] == b[2]:
            n3 = a[2]
        else:
            n3 = 0
            for i in colors:
                if i != a[2] and i != b[2]:
                    n3 = i
                    break

        if a[3] == b[3]:
            n4 = a[3]
        else:
            n4 = 0
            for i in shape:
                if i != a[3] and i != b[3]:
                    n4 = i
                    break
        out.write("Group " +str(counter) +": " + n1+n2+n3+n4+"\n")
        print("Group " +str(counter) +": " + n1+n2+n3+n4)
    counter+=1
