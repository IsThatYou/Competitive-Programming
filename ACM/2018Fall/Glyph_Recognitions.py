import math
pi = math.pi
n = int(input())
arr = []
for i in range(n):
    x,y = [int(x) for x in input().split()]

    arr.append((x,y))
ansn = 3
ans = 0
for k in range(3,9):
    center_angle = (2 * pi)/k
    side_angle = math.radians(((k-2) * 180)/k)
    start = 0
    end = 10e7
    arr2 = []
    for point in arr:
        x = point[0]
        y = point[1]
        p_from_o = (x**2 + y**2)**0.5
        p_angle = math.atan2(y,x)
        p_angle = p_angle%center_angle
        p_angle2 = side_angle/2.0
        p_angle3 = pi - p_angle2 - p_angle
        arr2.append((p_from_o,p_angle,p_angle2,p_angle3))
    for i in range(100):
        mid = (start + end)/2
        less = 0
        for point in arr2:

            p_from_o = point[0]
            p_angle = point[1]
            p_angle2 = point[2]
            p_angle3 = point[3]
            supposed_len = (mid/(math.sin(p_angle3))) * math.sin(p_angle2)
            #print(mid,supposed_len, p_from_o)
            #print(p_angle,p_angle2,p_angle3, center_angle,math.atan2(y,x))
            if p_from_o < supposed_len:
                less +=1
        if less == n:
            end = mid
        else:
            start = mid
    outter = mid
    apothem = outter * math.sin(side_angle)
    side_length = 2*((outter**2 + apothem**2)**0.5)
    outter_area = 0.5 * apothem * side_length * k
    start = 0
    end = 10e7
    last_end = 10e7
    for i in range(100):
        mid = (start + end)/2
        less = 0
        for point in arr2:

            p_from_o = point[0]
            p_angle = point[1]
            p_angle2 = point[2]
            p_angle3 = point[3]
            supposed_len = (mid/(math.sin(p_angle3))) * math.sin(p_angle2)
            #print(mid,supposed_len, p_from_o)
            #print(p_angle,p_angle2,p_angle3, center_angle,math.atan2(y,x))
            if p_from_o < supposed_len:
                less +=1
        #print(mid)
        if less==0:
            start = mid
            #end = last_end
        else:
            #last_end = end
            end = mid
    inner = mid
    apothem = inner * math.sin(side_angle)
    side_length = 2*((inner**2 + apothem**2)**0.5)
    inner_area = 0.5 * apothem * side_length * k

    ratio = inner_area/outter_area
    if ratio > ans:
        ansn = k
        ans = ratio

print(ansn,ans)