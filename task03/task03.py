f1 = open('content.txt', 'r')
f2 = open('copy.txt', 'a')
cnt = 0
for line in f1:
    cnt += 1
    if cnt != 5:
        f2.write(line)
f1.close()
f2.close()
