
import re 

class WORLD:
    def __init__(self,world,ping):
        self.world = world
        self.ping = ping

    def print_(self):
        print('world: ',self.world," ping : ",self.ping)


def get_worlds(file):
    worlds = []
    with open(file,'r+') as f:
        for line in f.readlines():
            final = re.findall(r'\d+', line)
            worlds.append(WORLD(int(final[0]),int(final[1])))

    worlds.sort(key= lambda x: int(x.world))

    return worlds

def best_common(worlds1,worlds2,maxping):
    best = []  

    for i in range(len(worlds1)):
        sum = worlds1[i].ping + worlds2[i].ping
        if int(worlds1[i].ping) <= maxping and int(worlds2[i].ping) <= maxping:
            best.append((worlds1[i],worlds2[i],sum))

    best.sort(key = lambda x: x[2])
    try:
        print(f'best world is: {best[0][0].world} with a pings of {best[0][0].ping} and {best[0][1].ping}.')
    except :
        pass

    return best



    


world1 = get_worlds('worlds.txt')
world2 = get_worlds('whines.txt')


for i in range(300):
    best = best_common(world1,world2,i)








