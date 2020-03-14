#!/usr/bin/env python

from argparse import ArgumentParser
import os
from subprocess import call


def m4a2mp3(path):
    files = os.listdir(path)

    for file in files:
        if file.split('.')[-1] == 'm4a':
            prefix = os.path.join(path, '.'.join(file.split('.')[0:-1]))
            ffmpeg_command = 'ffmpeg "{}.mp3" -i "{}.m4a" -codec:a libmp3lame -qscale:a 1'.format(prefix, prefix)
            print(ffmpeg_command)
            call(ffmpeg_command, shell=True)


if __name__=='__main__':
    parser = ArgumentParser(description='convert m4a files to mp3')
    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        help='convert files throughout the directory tree'
    )
    parser.add_argument(
        'path',
        type=str,
        help='path to the directory that contains the m4a files'
    )

    args = parser.parse_args()
    if args.recursive:
        for path, _, files in os.walk(args.path):
            if len(files) > 0:
                m4a2mp3(path)
    else:
        m4a2mp3(args.path)
