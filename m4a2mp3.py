#!/usr/bin/env python

from argparse import ArgumentParser
import os
from subprocess import call


def m4a2mp3(path, force=False):
    files = os.listdir(path)

    for file in files:
        if file.split('.')[-1] == 'm4a':
            prefix = os.path.join(path, '.'.join(file.split('.')[0:-1]))
            outfile_name = prefix + ".mp3"

            # Do not overwrite unless force is True
            if (not os.path.isfile(outfile_name)) or force:
                infile_name = prefix + ".m4a"
                ffmpeg_command = 'ffmpeg -y "{}" -i "{}" -codec:a libmp3lame -qscale:a 1'.format(outfile_name, infile_name)
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
        '-f',
        '--force',
        action='store_true',
        help='force overwrite of mp3 file(s)'
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
                m4a2mp3(path, args.force)
    else:
        m4a2mp3(args.path, args.force)
