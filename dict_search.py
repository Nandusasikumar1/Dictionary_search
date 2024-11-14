c  = {1:{4:{8:{9:10,11:33}}},44:73,32:89,77:{23:34,66:89}}

def search1(d,key):
    while d:
        temp = {}
        if key in d:
            return {key:d[key]}
        for v in d.values():
            if isinstance(v,dict):
                temp |= v
        d = temp
    return 'key not found'
 
 
print(search1(c,676))
 


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
