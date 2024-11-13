c = {1:{4:5,7:{8:9}}}
def search1(d,key):
    while True:
        temp = {}
        true_count = 0
        if key in d:
            return {key:d[key]}
        for v in d.values():
            if isinstance(v,dict):
                temp |= v
            true_count += 1
        d = temp
        if len(d) == true_count and key not in d:
            return 'key not found'


print(search(c,7))

c = {1:{4:5,34:{343:22,31:{28:0},7:{8:9}}}}
def search(d,key):
    temp = {}
    true_count = 0
    while True:
        if key in d:
            return {key:d[key]}
        for v in d.values():
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
