handle = "the best of the best of the world"

count = dict()
for line in handle:
    words = line.split()
    for word in words:
        count[word] = count.get("line", 0) + 1

bigcount = 0
bigword = 0
for word, count in words: 
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)