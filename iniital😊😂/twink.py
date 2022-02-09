f = open('te.txt')
t = f.read()
if 'twinkle' in t: #captial is excption 
    print("twinkle is present") 
else:
    print("twinkle is not present ")

    f.close()