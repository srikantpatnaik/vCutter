#!/usr/bin/python -tt

import arguments
import os
import sys
import time
from datetime import datetime
from subprocess import Popen, PIPE

def selectOperation():
    argsObj          = arguments.argParse()  #create object of argParse class
    cliArgs_list     = argsObj.parse()       #catching return value of the fn
    flag = 'Option_%s' %(cliArgs_list[0])
    exec('process'+ flag + '(cliArgs_list)') #calling a fn based on 1st integer arg

def convert(infile, outfile):
    if '.ogv' in outfile:
        os.system('ffmpeg2theora ' + infile + ' -o ' + outfile)
    else:
        os.system('ffmpeg -y -i  ' + infile + ' ' + outfile)


def cutVideo(videoTobeCut, initialTime, finalTime, outputVideo):
    timeDifference = diffTime(initialTime, finalTime)
    os.system('ffmpeg -y -i ' + videoTobeCut + ' -sameq -ss ' \
               + initialTime + ' -t ' + timeDifference + ' ' + outputVideo)


def joinVideo(*anyNumberOfVideos):
    #the last name should be output video name
    videosToBeAdded = ''
    anyNumberOfVideos = list(anyNumberOfVideos)
    anyNumberOfVideos.reverse()
    for eachVideo in anyNumberOfVideos[1:]:
        videosToBeAdded = eachVideo + ' ' + videosToBeAdded
    os.system('mpgtx -j ' + videosToBeAdded + ' -o ' + anyNumberOfVideos[0])

def getTotalTime(videoName):
    findLength = "ffmpeg -i %s 2>&1 | grep Duration | cut -d ' ' -f 4 |sed s/,//"\
                    %(videoName)
    return Popen(findLength, shell=True, stdout=PIPE).stdout.read().strip('\n')                    


def diffTime(initialTime, finalTime):
    fmt = '%H:%M:%S.%f'
    tdelta = datetime.strptime(finalTime,fmt) - datetime.strptime(initialTime,fmt)
    return time.strftime('%H:%M:%S.%f', time.gmtime(tdelta.seconds))

###############################################################################

def processOption_1(cliArgs_list):
    ## eg: vcutter 1 -i inVideo.ogv -o outVideo.webm
    ## Presently works with 'ogv','wmv','avi'. Need to work on others
    mustFlags = ['-i', '-o']   #recommended flags for this option
    finalArgs = doubleCheck(mustFlags, cliArgs_list)
    convert(cliArgs_list[cliArgs_list.index('-i') + 1],\
            cliArgs_list[cliArgs_list.index('-o') + 1])


def processOption_2(cliArgs_list):
    ## eg: vcutter 2 -a smallClip.ogv -b  OrigVideo.ogv -o smallClipOrigVideo.ogv
    ## only works with same aspect ratio videos, which is always true in case of ST
    if '-b' in cliArgs_list:
        mustFlags = ['-a', '-b', '-o']
        finalArgs = doubleCheck(mustFlags, cliArgs_list)
        convert(finalArgs[finalArgs.index('-a') + 1], '.rawTobeAddedVideo1.mpg')
        convert(finalArgs[finalArgs.index('-b') + 1], '.rawTobeAddedVideo2.mpg')
        joinVideo('.rawTobeAddedVideo1.mpg', '.rawTobeAddedVideo2.mpg', '.rawAddedVideo.mpg')        
    elif '-e' in cliArgs_list:
        mustFlags = ['-a', '-e', '-o']
        finalArgs = doubleCheck(mustFlags, cliArgs_list)
        convert(finalArgs[finalArgs.index('-a') + 1], '.rawTobeAddedVideo1.mpg')
        convert(finalArgs[finalArgs.index('-e') + 1], '.rawTobeAddedVideo2.mpg')
        joinVideo('.rawTobeAddedVideo2.mpg', '.rawTobeAddedVideo1.mpg', '.rawAddedVideo.mpg')        
    convert('.rawAddedVideo.mpg', finalArgs[finalArgs.index('-o') + 1])
    os.system('rm .raw*')


def processOption_3(cliArgs_list):
    ## eg: vcutter 3 -c testVideo.ogv -t 23:59:55.00 23:59:59.00 -I newClip.ogv -o newVideo.ogv
    ## works with mpg,flv and ogv only
    mustFlags = ['-c', '-t', '-I', '-o']       #recommended flags for this option
    finalArgs = doubleCheck(mustFlags, cliArgs_list)
    convert(finalArgs[finalArgs.index('-c') + 1], '.rawtoBeCutFile.mpg')
    convert(finalArgs[finalArgs.index('-I') + 1], '.rawtoBeInsertedFile.mpg')
    cutVideo('.rawtoBeCutFile.mpg', '00:00:00.00', \
             finalArgs[finalArgs.index('-t') + 1], ' .rawCutfile1.mpg')
    cutVideo('.rawtoBeCutFile.mpg', finalArgs[finalArgs.index('-t') + 2], \
             getTotalTime(finalArgs[finalArgs.index('-c') + 1]), ' .rawCutfile2.mpg')
    joinVideo('.rawCutfile1.mpg', '.rawtoBeInsertedFile.mpg', '.rawCutfile2.mpg',\
              '.rawAddedVideo.mpg')
    convert('.rawAddedVideo.mpg', cliArgs_list[cliArgs_list.index('-o') + 1])
    os.system('rm .raw*')


def processOption_4(cliArgs_list):
    ## eg: vcutter 4 -c testVideo.ogv -t 23:59:55.00 23:59:59.00 -o newVideo.ogv
    mustFlags = ['-c', '-t', '-o']       #recommended flags for this option
    finalArgs = doubleCheck(mustFlags, cliArgs_list)
    convert(finalArgs[finalArgs.index('-c') + 1], '.rawtoBeCutFile.mpg')
    cutVideo('.rawtoBeCutFile.mpg', '00:00:00.00', \
             finalArgs[finalArgs.index('-t') + 1], ' .rawCutfile1.mpg')
    cutVideo('.rawtoBeCutFile.mpg', finalArgs[finalArgs.index('-t') + 2], \
             getTotalTime(finalArgs[finalArgs.index('-c') + 1]), ' .rawCutfile2.mpg')
    joinVideo('.rawCutfile1.mpg', '.rawCutfile2.mpg', '.rawAddedVideo.mpg')
    convert('.rawAddedVideo.mpg', cliArgs_list[cliArgs_list.index('-o') + 1])
    os.system('rm .raw*')


def processOption_5(cliArgs_list):
    ## eg: vcutter 5 -c testVideo.ogv -t 23:59:55 23:59:59 -o newVideo.ogv
    ## works with flv, ogv only
    mustFlags = ['-c', '-t', '-o']       #recommended flags for this option
    finalArgs = doubleCheck(mustFlags, cliArgs_list)
    convert(finalArgs[finalArgs.index('-c') + 1], '.rawtoBeCutFile.mpg')
    cutVideo('.rawtoBeCutFile.mpg', finalArgs[finalArgs.index('-t') + 1],\
                finalArgs[finalArgs.index('-t') + 2], '.rawCutfile.mpg')
    convert('.rawCutfile.mpg', finalArgs[finalArgs.index('-o') + 1])
    os.system('rm .raw*')


def doubleCheck(mustFlags, cliArgs_list):
    ## The 'if' stmt is to check for correctness of user entered flags
    comparedFlags = list(set(cliArgs_list) & set(mustFlags))
    if not mustFlags.sort() == comparedFlags.sort():
        print 'Flags mismatch. Please see --help for examples.'
        sys.exit(1)
    else:
        cliArgs_list = cliArgs_list[1:]   # excluding first select option arg
    return cliArgs_list


if __name__ == "__main__":
    selectOperation()
