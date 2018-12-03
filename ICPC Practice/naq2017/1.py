n = int(input())
nums1 = []
nums2 = []
nums3 = []
ass=[]
for i in range(n):
    a,num = [x for x in input().split()]
    ass.append(a)
    nums1.append(str(int(num,10)))
    hexx = int(num,16)
    nums2.append(str(hexx))
    try:
        octt = int(num,8)
    except:
        octt = 0
    nums3.append(str(octt))
    #print(a,str(octt),num,str(hexx))
for i in range(n):
    print(ass[i] + " " + nums3[i] + " " + nums1[i] + " " + nums2[i])
