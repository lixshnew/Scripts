# UniqueFileFilter.py

This script is used for filtering out duplication of jpg and avi files in a folder. 
Usually, we backup our  media files in a backup disk, for long time, some folders or files may backup two or more times in different sub-directories. It ocuppy non necessary space.

This script will caculate the MD5 signature and only keep one copy of the files. The output directory will be with 'out' prefix directory.

## Limitation
Only Windows path is supported. 

## Usage 

Python3 environment.

Usage: python UniqueFileFilter.py \<source absolute directory>

Source directory is absolute. 


Example:  
   
Source      c:\photos  
Output      c:\out\photos





