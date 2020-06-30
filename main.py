import os
import subprocess
import re


class WORLD:
    def __init__(self,world,ping):
        self.world = world
        self.ping = ping

    def print_(self):
        print('world: ',self.world," ping : ",self.ping)

worlds = []
sub = 0
cur = 0

print('checking ping on all available worlds on runescape.com!')

for i in range(1,130):
    sub = subprocess.Popen(f'ping world{i}.runescape.com -n 1 | FIND "time="',shell=True,stdout=subprocess.PIPE)
    ret = sub.stdout.read().decode()
    try:
        short = ret[ret.index('time='):ret.index('time=')+10]
    except:
        pass
    final = re.findall(r'\d+', short)

    try:
        cur = WORLD(i,int(final[0]))
    except:
        #print(f'world {i} does not exist')
        pass

    if cur:
        worlds.append(cur)
        #print(f'checking world: {i}')
        #os.system('cls')

worlds.sort(key = lambda x: x.ping)

for world in worlds:
    world.print_()

    
input()

