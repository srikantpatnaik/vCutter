#!/usr/bin/python -tt
"""
   This application simplifies your video editing job by providing you neat
   set of commands to cut,join or insert any video.
                                                    
   Examples for each option:
   -------------------------
   1.Convert/Encode inVideo to outVideo.Must give extension to OutVideo.
   $ vcutter inVideo.ogv outVideo.webm


   2.Add(-a) a video at the beginning(-b) or end(-e) of other video and stitch
     them as output(-o) video. 
   $ vcutter -a smallClip.ogv -b  OrigVideo.ogv -o smallClipOrigVideo.ogv
                (inVideo)         (inVideo)        (outVideo)

   3.Cut and replace clip from testVideo at duration (t1) to (t2) and insert
     newClip in place of it, stich them as newVideo(-o) video.
   $ vcutter -c testVideo.ogv -t1 23:59:55 -t2 23:59:59 -i newClip.ogv -o newVideo.ogv 
                (inVideo)                                  (inVideo)      (outVideo)

   4.Cut(-c) the clip from (-t1) to (-t2) duration of testVideo and stich back 
     the remaining portion as output(-o) video.
   $ vcutter -c testVideo.ogv -t1 23:59:55 -t2 23:59:59 -o newVideo.ogv 
                (inVideo)                                  (outVideo) 


   5.Cut(-c) from (-t1) to (-t2) duration of testVideo and cut clip as newVideo. 
   $ vcutter -c testVideo.ogv -t1 23:59:55 -t2 23:59:59 -s -o  newVideo.ogv 
                (inVideo)                                      (outVideo)
                
   6.Covert all videos in a directory to certain format.
   $ vcutter sourceDir -f mp4 destDir
             (inVideo)        (outVideo)
   Source dir must contain all videos in same format.
   
   All flags:
   ----------
     -a -> add   
     -b -> beginning
     -e -> end
     -c -> cut the clip
     -t1 & -t2 -> time in hh:mm:ss
     -o -> output video
     -s -> save the cut portion
     -i -> insert the new clip
     -f -> give the output video format(eg: ogv, mp4, avi etc)

   Please note, cut operation doesn't effect the original video.Your original
   video remains intact.

"""

import argparse
import sys
from lib.terminalColor import color


class argParse:

    def parse(self):

        descriptionStr = "%s simplifies your video editing job by providing you neat\
        set of commands to cut,join or covert any video." %(color.cyan("vCutter"))
        
        parser = argparse.ArgumentParser(prog = "vCutter", description = descriptionStr,
                                         epilog="Epilog goes here",
                                         prefix_chars = '-',
                                         add_help = True)
        
        parser.add_argument('-a','--add',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'add: Enables adding a video in beginning or end of other video')
        
        parser.add_argument('-c','--cut',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'cut: cut the video at specified time')
    
        parser.add_argument('inVideofile',
                            action = 'store',
                            nargs='?',
                            type=argparse.FileType('r'),
                            help = 'file name or path of the input video')
    
        parser.add_argument('-b','--beginning',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'beginning: add in the beginning')
    
        parser.add_argument('-e','--end',
                            metavar = '',
                            type = argparse.FileType('r'),
                            help = 'end: add at the end')
        
        parser.add_argument('-i','--insert',
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
        
        parser.add_argument('inVideofile',
                            action = 'store',
                            nargs='?',
                            type=argparse.FileType('r'),
                            help = 'file name or path of the input video')
    
        parser.add_argument('-o','--out',
                            metavar = '',
                            type = argparse.FileType('w'),
                            help = 'output: output video')
        
        parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    


        args = parser.parse_args()
        print parser.print_help()
        print ""
        print "===================="
        print ""
        print '--add =', args.add
        print '--cut =', args.cut
        print '--time =', args.time
        print '--beg =', args.beginning
        print '--end =', args.end
        print '--out =', args.out
        print '--insert =', args.insert
        print '--inVideofile =', args.inVideofile



if __name__ == "__main__":
    if len(sys.argv) == 1 :
        print "%s: Incorrect usage, please see 'vCutter.py --help' " % ( color.cyan("vCutter") ) 
    else :
        main=argParse()
        main.parse()
        


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

"""
