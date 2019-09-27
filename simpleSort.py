data = [64, 25, 12, 22, 11,-1, 1,2,44,3,122, 23, 34]

for i in range(len(data)):
    for j in range(i + 1, len(data)):

        if data[i] > data[j]:
           data[i], data[j] = data[j], data[i]
print(data)
