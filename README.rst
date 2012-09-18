This application simplifies your video editing job by providing you neat
set of commands to cut,join or insert any video.
                                                    

Examples for each option
------------------------

#. Convert/Encode inVideo to outVideo.Must give extension to OutVideo.::
    
        $ vcutter 1 -i inVideo.ogv -o outVideo.webm


#. Add(-a) a video at the beginning(-b) or end(-e) of other video and stitch
   them as output(-o) video.::
    
        $ vcutter 2 -a smallClip.ogv -b  OrigVideo.ogv -o smallClipOrigVideo.ogv
                        (inVideo)            (inVideo)        (outVideo)


#. Cut and replace clip from testVideo at duration (t1) to (t2) and insert
   newClip in place of it, stich them as newVideo(-o) video.::
    
        $ vcutter 3 -c testVideo.ogv -t1 23:59:55.00 -t2 23:59:59.00 -I newClip.ogv -o newVideo.ogv 
                      (inVideo)                                          (inVideo)      (outVideo)

#. Cut(-c) the clip from (-t1) to (-t2) duration of testVideo and stich back 
   the remaining portion as output(-o) video.::

       $ vcutter 4 -c testVideo.ogv -t1 23:59:55.00 -t2 23:59:59.00 -o newVideo.ogv 
                       (inVideo)                                        (outVideo) 


#. Cut(-c) from (-t1) to (-t2) duration of testVideo and cut clip as newVideo.::

       $ vcutter 5 -c testVideo.ogv -t1 23:59:55.00 -t2 23:59:59.00 -o  newVideo.ogv 
                      (inVideo)                                         (outVideo)
                
#. Covert all videos in a directory to certain format.::

       $ vcutter sourceDir -f mp4  destDir
                 (inVideo)        (outVideo)



---------   
All flags
---------

::

     -a -> add   
     -b -> beginning
     -e -> end
     -c -> cut the clip
     -t1 & -t2 -> time in hh:mm:ss.msec
     -o -> output video
     -I -> insert a new clip
     -f -> give the output video format(eg: ogv, mp4, avi etc)

Please note, cut operation doesn't effect the original video.Your original
video remains intact.


