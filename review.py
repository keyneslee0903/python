data = []
count = 0

with open('reviews.txt' , 'r') as f:
    for line in f:
        data.append(line)
        count +=1
        if count % 50000 == 0:
            print(len(data))
#print(len(data))
#print(data[0])

sum_len = 0

for d in data:
    sum_len = sum_len + len(d)

print(sum_len/len(data))

new = []

for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new) , '筆資料 < 100')
print('第一筆資料內容如下' , new[0])

good = []

for d in data:
    if 'good' in d and 'nice' in d:
        good.append(d)
print(len(good))
print(good[0])


not_bad = [d for d in data if 'not bad' in d]
print(len(not_bad))