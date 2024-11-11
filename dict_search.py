c = {1:{4:5,7:{8:9}}}
def search(d,key):
    temp = {}
    endcheck = []
    while True:
        if key in d:
            return {key:d[key]}
        for k,v in d.items():
            if isinstance(v,dict):
                temp |= v
                endcheck.append(False)
            else:
                endcheck.append(True)
        if temp:
            d,temp = temp,{}
        if all(endcheck) and key not in d:
            return 'key not found'

        endcheck = []

print(search(c,7))
