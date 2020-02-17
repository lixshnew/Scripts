'''
Unique file filter 

Author: Li Xinsheng <lixshnew@gmail.com>

Usage: python UniqueFileFilter.py <source absolute directory>

Source directory is absolute. This script only works in Windows.

The output directory is with prefix 'out'

such as :

source    c:\photos
output    c:\out\photos
'''

import os
import shutil
import hashlib
import sys

if len(sys.argv)<2:
    print("Usage : python UniqueFileFilter.py <source absolute directory>")
    exit(1)

path=sys.argv[1]

if not os.path.exists(path):
    print("Source directory does not exist.")
    exit(1)


hashset=set()
exts=['jpg','JPG','avi','AVI']


for root,dirs,files in os.walk(path):
    for name in files:
        ext=name.split('.')
        if len(ext)>=2 and ext[1] in exts:
            srcname=os.path.join(root,name)
            h=hashlib.md5(open(srcname,'rb').read()).hexdigest()
            
            if  h not in hashset:
                hashset.add(h)
                p=root.split(':')
                dest=p[0]+':\\out'+p[1]

                if not os.path.exists(dest):
                    os.makedirs(dest)
                
                destname=os.path.join(dest,name)

                shutil.copy2(srcname,destname)

                print(srcname+" --> "+destname)
            

print(str(len(hashset))+" Unique file processed.")

