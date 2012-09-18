#!/usr/bin/python -tt

import argparse
import sys
import os

class argParse:

    def parse(self):

        descriptionStr = "vCutter simplifies your video editing job by providing you neat\
        set of commands to cut,join or covert any video."
        
        parser = argparse.ArgumentParser(prog = "vCutter", description = descriptionStr,
                                         epilog="Epilog goes here",
                                         prefix_chars = '-',
                                         add_help = True)
        parser.add_argument('select',
                            metavar='N',
                            type = int,
                            nargs = 1,
                            help = 'See the help for correct option.')

        parser.add_argument('-i','--input',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'input: file name or path of the input video')
                             
        parser.add_argument('-a','--add',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'add: Enables adding a video in beginning or end of other video')
        
        parser.add_argument('-c','--cut',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'cut: cut the video at specified time')
    

        parser.add_argument('-b','--beginning',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'beginning: add in the beginning')
    
        parser.add_argument('-e','--end',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'end: add at the end')

        parser.add_argument('-t','--time',
                            dest = 'time',
                            type = str,
                            metavar = '',
                            nargs = 2,
                            default = False,
                            help = 'start_time, end_time')
         
        parser.add_argument('-I','--insert',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'beginning: add in the beginning')
    
        parser.add_argument('-o','--out',
                            metavar = '',
                            ## Removed FileType('w'),creates file unnecessary
                            help = 'output: output video')
        
        parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        
        if len(sys.argv) <= 4:
            parser.print_help()
            f = open('examples.txt','r')
            line = f.read()
            print line.strip('\n')
            f.close()
            parser.exit()
        else:    
            parser.parse_args()             # This will check the validity of options
            args = sys.argv[1:]             # If above line returns true then grab the args
        return args

