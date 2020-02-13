a = 1
progress = True
while progress:
    print(a)
    a += 1
    if a > 10:
        progress = False
        # break
else:
    print('finish')
