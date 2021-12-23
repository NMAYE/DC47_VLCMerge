"""
    Title:          DC47_VLCMerge
    Date:           06 December 2021
    Description:    Creates a list of CMD commands for VLC that concatenates 
                    1-min videos together.
                    Example:
                        vlc GRMN0001.MP4 GRMN0002.MP4 --sout 
                        "#gather:std{access=file,dst=
                        1969.07.20_08.17.00PM.MP4}" --sout-keep
        V01-    Initial release
        V02-    Applies the date to the name of the merged video (Current 
                version 2021.12.22)
        V03-    TODO - Auto-detect the end of one trip and the beginning of 
                the next (time gap greater than ____ hours implies a new trip)
        V04-    TODO - generate side-by-side video synced in time for front 
                and rear dashcams (*cough* Dakota *cough*)
"""

import os
import time

## USER VARIABLES ##
# file location for 1-minute dashcam videos (may not be F drive for your PC)
src=r'F:\DCIM\105UNSVD'
# max length of each merged video in minutes
mergeVideoLength=60

gfiles=[]
mergedVideoNames=[]
# navigate to Garmin dashcam
try:
    os.chdir(src)
except:
    print('Cannot locate', src)
    print('Searching', os.getcwd())
files=os.listdir()
i=0
numVideos=0
nL='\n\n'+'-'*80+'\n'
print('Copy these into CMD:', nL)
print('vlc', end=' ')
# g[0] is the first video in each merged set
g=[]
for f in files:
    if f[:4]=='GRMN' and f[-4:]=='.MP4':
        g.append(f)
        if i%mergeVideoLength==mergeVideoLength-1:
            mergedVideoNames.append(time.strftime('%Y.%m.%d_%I.%M.%S%p.MP4',\
            time.localtime(os.path.getctime(g[0]))))
            print('vlc', end=' ')
        gfiles.append(f)
        print(f, end=' ')
        i+=1
        if i%mergeVideoLength==0:
            print('--sout "#gather:std{access=file,dst='+\
            #mergedVideoNames[numVideos]+'}" --sout-keep\n\n')
            mergedVideoNames[numVideos]+'}" --sout-keep', nL)
            numVideos+=1
            g=[]
if len(g)>0:
    mergedVideoNames.append(time.strftime('%Y.%m.%d_%I.%M.%S%p.MP4',\
    time.localtime(os.path.getctime(g[0]))))
    print('--sout "#gather:std{access=file,dst='+mergedVideoNames[numVideos]+\
    '}" --sout-keep', nL)
    print('Merged videos to be created:', numVideos+1)
else:
    print('No dashcam video files found')
input()
