# DC47_VLCMerge
Creates a list of CMD commands for VLC that concatenates 1-min videos together.

Output is tailored for use with Windows Command Prompt.

Separate VLC installation is required.



Example:

vlc GRMN0001.MP4 GRMN0002.MP4 --sout "#gather:std{access=file,dst=1969.07.20_08.17.00PM.MP4}" --sout-keep
