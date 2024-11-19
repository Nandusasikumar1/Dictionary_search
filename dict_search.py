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

c = {2:{3:4,7:8,53:{877:231}},99:{23:9,77:{51:{812:77}}}}
def keypath(d,key):
    path = {}
    level = 1
    while d:
        level_name = f'level {level}'
        temp = {}
        if key in d:
            path[level_name] = key
            return {key:d[key]},path
        for k,v in d.items():
            if isinstance(v,dict):
                temp |= v
            
            if not level_name in path:
                path[level_name]=[k]
            else:
                path[level_name].append(k)
           
        
        level+=1
        d = temp
    else:
        return 'key not found',path


result,path=keypath(c,51)
print(path)

def search1(d,key):
    while d:
        temp = {}
        
        for k,v in d.items():
            if k == key:
                return {k:v}
            if isinstance(v,dict):
                if key in v:
                    return {key:v[key]}
                temp |= v
        d = temp
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
