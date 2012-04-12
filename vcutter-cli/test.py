#!/usr/bin/python -tt

import argparse
import sys
from  lib.terminalColor import color


def parse():

    descriptionStr = "%s simplifies your video editing job by providing you neat\
set of commands to cut,join or covert any video." %(color.cyan("vCutter"))

    parser = argparse.ArgumentParser(prog = "vCutter", description = descriptionStr,
                                     epilog="Epilog goes here",
                                     prefix_chars = '-',
                                     add_help = True)
    
    parser.add_argument('inVideofile',
                        #                    type = argparse.FileType('r'),
                        action = 'store',
                        nargs='?',
                        type=argparse.FileType('r'),
                        #                    default=sys.stdin,
                        #                    default = None,
                        help = 'file name or path of the input video')

    # parser.add_argument("query_terms" , nargs=argparse.REMAINDER)
    
    parser.add_argument('-a','--add',
                        #                     action = 'store_true',
                        #                     default = False,
                        #                     dest = 'add',
                        metavar = '',
                        type = argparse.FileType('r'),
                        help = 'add: Enables adding a video in beginning or end of other video')

    parser.add_argument('-c','--cut',
                        #                     action = 'store_true',
                        #                     default = False,
                        #                     dest = 'cut',
                        metavar = '',
                        type = argparse.FileType('r'),
                        help = 'cut: cut the video at specified time')

# parser.add_argument('inVideofile',
#                     action = 'store',
#                     nargs='?',
#                     type=argparse.FileType('r'),
#                     default=sys.stdin,
#                     help = 'file name or path of the input video')

    parser.add_argument('-b','--beginning',
                        #                     action = 'store_true',
                        #                     default = False,
                        #                     dest = 'cut',
                        metavar = '',
                        type = argparse.FileType('r'),
                        help = 'beginning: add in the beginning')

    parser.add_argument('-e','--end',
                        #                     action = 'store_true',
                        #                     default = False,
                        #                     dest = 'cut',
                        metavar = '',
                        type = argparse.FileType('r'),
                        help = 'end: add at the end')

    parser.add_argument('-i','--insert',
                        #                     action = 'store_true',
                        #                     default = False,
                        #                     dest = 'cut',
                        metavar = '',
                        type = argparse.FileType('r'),
                        help = 'beginning: add in the beginning')
    
    parser.add_argument('-t','--time',
                        dest = 'time',
                        type = str,
                        metavar = '',
                        nargs = 2,
                        default = False,
                        help = 'start_time, end_time')
    
    parser.add_argument('-o','--out',
                        metavar = '',
                        type = argparse.FileType('w'),
                        help = 'output: output video')
    
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')

    args = parser.parse_args()
#args1 = parse_args(sys.argv[1])
    print parser.print_help()
    print "===================="
    print '--add =', args.add
    print '--cut =', args.cut
    print '--time =', args.time
    print '--beg =', args.beginning
    print '--end =', args.end
    print '--out = ', args.out
    print '--insert = ', args.insert
    print '--inVideofile =', args.inVideofile
#print 'query_term =', args.query_term


def main():
    parse()



if __name__ == "__main__":
    if len(sys.argv) == 1 :
        print "%s: Incorrect usage, please see 'vCutter.py --help' " % ( color.cyan("vCutter") ) 
    else :
        main()
        

        
"""

parser.add_argument('-s',
                    type = str,
                    help = 'save: save the cut portion')

parser.add_argument('-f',
                    type = str,
                    help = 'format: give the output video format')

parser.add_argument('outVideofile',
                    nargs='?',
                    type=argparse.FileType('w'),
                    default=sys.stdout,
                    help = 'file name or path of the output video')

args = parser.parse_args()
print parser.print_help()


ref:

# time format -
# http://stackoverflow.com/questions/9852226/python-argparse-with-time-format

# http://webworxshop.com/2011/01/20/python-module-of-the-week-0-argparse

# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html

# metavar -
# http://stackoverflow.com/questions/9642692/argparse-help-without-duplicate-allcaps

"""

