KCONST = [6,1,7,4]


match = False
count = 0



while not match:
    num = input()
    xlist = [x for x in num]
    if xlist == KCONST:
        match = True
    else:
        alist = sorted(xlist)
        dlist = sorted(xlist, reverse=True)
        astr = "".join(alist)
        dstr = "".join(dlist)

        anum = int(astr)
        dnum = int(dstr)
        print(f"{dstr} - {astr} = {str(dnum - anum)}")
