**BUG**
Option 3, 4, 5 are not working with 12.10 Ubuntu

This application simplifies your video editing job by providing you neat
set of commands to cut, join or insert any video.
                                                    
Required packages (available on Ubuntu)
---------------------------------------

* ffmpeg

* ffmpeg2theora

* mpgtx


Examples for each option
------------------------

#. Convert/Encode inVideo to outVideo. Must give extension to OutVideo. ::
    
        $ ./vcutter.py 1 -i inVideo.ogv -o outVideo.webm


#. Add(-a) a video at the beginning(-b) or end(-e) of other video and stitch
   them as output(-o) video ::
    
        $ ./vcutter.py 2 -a smallClip.ogv -b  OrigVideo.ogv -o smallClipOrigVideo.ogv
                           (inVideo)            (inVideo)        (outVideo)


#. Cut and replace clip from testVideo and insert newClip in place of it, stich them as newVideo(-o) video ::
    
        $ ./vcutter.py 3 -c testVideo.ogv -t 23:59:55.00  23:59:59.00 -I newClip.ogv -o newVideo.ogv 
                            (inVideo)        (start time) (end time)      (inVideo)      (outVideo)

#. Cut(-c) clip of desired duration and stich back the remaining portion as output(-o) video ::

       $ ./vcutter.py 4 -c testVideo.ogv -t 23:59:55.00  23:59:59.00 -o newVideo.ogv 
                            (inVideo)       (start time) (end time)     (outVideo) 


#. Cut(-c) clip of desired duration and save the cut portion as newVideo ::

       $ ./vcutter.py 5 -c testVideo.ogv -t 23:59:55.00  23:59:59.00 -o  newVideo.ogv 
                           (inVideo)        (start time) (end time)      (outVideo)
                


---------   
All flags
---------

::

     -a -> add   
     -b -> beginning
     -e -> end
     -c -> cut the clip
     -t -> start time and end time in hh:mm:ss.msec
     -o -> output video
     -I -> insert a new clip
     -f -> give the output video format(eg: ogv, avi etc)

Please note, cut operation doesn't effect the original video.Your original
video remains intact.


