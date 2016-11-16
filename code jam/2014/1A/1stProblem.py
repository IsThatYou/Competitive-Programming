def main():
    a = open('A-small-attempt0.in.txt', 'r')
    test = a.read()
    #test = raw_input()
    test2 = test.replace('\n', ',')
    allinfo = test2.split(',')
    testcase = int(allinfo[0])

    for i in range(1, testcase + 1):
        patterns = []
        devices = allinfo[i * 3 - 1].split(' ')
        outlets = allinfo[i * 3].split(' ')
        devices = [int(x, 2) for x in devices]
        outlets = [int(x, 2) for x in outlets]
        
    
        for a,outlet in enumerate(outlets):
            possible_pattern = int(devices[0]) ^ int(outlet)
        
            if set(x ^ possible_pattern for x in outlets) == set(devices):
                patterns.append(possible_pattern)

        if patterns:
            value = min(bin(pattern).lstrip("0b").count("1") for pattern in patterns)
            print ("Case #{0}: {1}".format(i, value))
        else:
            print ("Not Possible")
main()


