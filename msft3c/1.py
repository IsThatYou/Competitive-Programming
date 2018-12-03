a = open("Data-consolidation_InputForSubmission_1.txt")
sums = 0
for i in a:
    x = [int(z) for z in i.strip().split(",")]
    size = len(x)
    for j in x:
        sums += j
result = round(sums/size)
print(result)
