#!/usr/bin/env python

from os import listdir
from subprocess import call

files = listdir()

for file in listdir():
    # print(file + ' -- ' + '.'.join(file.split('.')[0:-1]) + '.mp3')
    if file.split('.')[-1] == 'm4a':
        # print('YAY')
        prefix = '.'.join(file.split('.')[0:-1])
        ffmpeg_command = 'ffmpeg "{}.mp3" -i "{}.m4a" -codec:a libmp3lame -qscale:a 1'.format(prefix, prefix)
        print(ffmpeg_command)
        call(ffmpeg_command, shell=True)
