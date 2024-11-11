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

c = {1:{4:5,34:{343:22,31:{28:0},7:{8:9}}}}
def search(d,key):
    temp = {}
    true_count = 0
    while True:
        if key in d:
            return {key:d[key]}
        for k,v in d.items():
            if isinstance(v,dict):
                temp |= v
                if true_count > 0:
                    true_count -= 1
            else:
                true_count += 1
        if temp:
            d,temp = temp,{}
        if len(d) == true_count and key not in d:
            return 'key not found'

        true_count = 0

print(search(c,288))
