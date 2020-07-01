import os
import subprocess
import re
from tqdm import tqdm



'''author - whine n dine'''


class WORLD:
    def __init__(self,world,ping):
        self.world = world
        self.ping = ping

    def print_(self):
        print('world: ',self.world," ping : ",self.ping)

worlds = []
sub = 0
cur = 0

print('checking for requirements...')
print('requirements satisfied')

print('checking ping on all available worlds on runescape.com!')

for i in tqdm(range(130),desc = "loading...",ascii =False,ncols=75):
    sub = subprocess.Popen(f'ping world{i}.runescape.com -n 1 | FIND "time="',shell=True,stdout=subprocess.PIPE)
    ret = sub.stdout.read().decode()
    try:
        short = ret[ret.index('time='):ret.index('time=')+10]
        final = re.findall(r'\d+', short)

    except:
        pass

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

##########################################
input('press any key to continue...')
###########################################


