#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 19, 2022, at 18:09
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Flickering Muliple Choice'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\sinha\\Documents\\Davis Documents B)\\personal project moment\\neurotech\\psychopy\\Flickering Muliple Choice_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
uprighttangle = visual.Rect(
    win=win, name='uprighttangle',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.2, 0.2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
downrighttangle = visual.Rect(
    win=win, name='downrighttangle',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.2, -0.2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
downlefttangle = visual.Rect(
    win=win, name='downlefttangle',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.2, -0.2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
uplefttangle = visual.Rect(
    win=win, name='uplefttangle',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.2, 0.2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
uprtext = visual.TextStim(win=win, name='uprtext',
    text='B',
    font='Open Sans',
    pos=(0.2, 0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='red', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
downrtext = visual.TextStim(win=win, name='downrtext',
    text='D',
    font='Open Sans',
    pos=(0.2, -0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='green', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
downltext = visual.TextStim(win=win, name='downltext',
    text='C',
    font='Open Sans',
    pos=(-0.2, -0.3), height=0.1, wrapWidth=None, ori=0.0, 
    color='blue', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
upltext = visual.TextStim(win=win, name='upltext',
    text='A',
    font='Open Sans',
    pos=(-0.2, 0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='purple', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [uprighttangle, downrighttangle, downlefttangle, uplefttangle, mouse, uprtext, downrtext, downltext, upltext]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *uprighttangle* updates
    if uprighttangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uprighttangle.frameNStart = frameN  # exact frame index
        uprighttangle.tStart = t  # local t and not account for scr refresh
        uprighttangle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uprighttangle, 'tStartRefresh')  # time at next scr refresh
        uprighttangle.setAutoDraw(True)
    if uprighttangle.status == STARTED:
        # is it time to stop? (based on local clock)
        if tThisFlip > 5-frameTolerance:
            # keep track of stop time/frame for later
            uprighttangle.tStop = t  # not accounting for scr refresh
            uprighttangle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(uprighttangle, 'tStopRefresh')  # time at next scr refresh
            uprighttangle.setAutoDraw(False)
    if uprighttangle.status == STARTED:  # only update if drawing
        uprighttangle.setOpacity(sin(20*t), log=False)
    
    # *downrighttangle* updates
    if downrighttangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        downrighttangle.frameNStart = frameN  # exact frame index
        downrighttangle.tStart = t  # local t and not account for scr refresh
        downrighttangle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(downrighttangle, 'tStartRefresh')  # time at next scr refresh
        downrighttangle.setAutoDraw(True)
    if downrighttangle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > downrighttangle.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            downrighttangle.tStop = t  # not accounting for scr refresh
            downrighttangle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(downrighttangle, 'tStopRefresh')  # time at next scr refresh
            downrighttangle.setAutoDraw(False)
    if downrighttangle.status == STARTED:  # only update if drawing
        downrighttangle.setOpacity(sin(15*t), log=False)
    
    # *downlefttangle* updates
    if downlefttangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        downlefttangle.frameNStart = frameN  # exact frame index
        downlefttangle.tStart = t  # local t and not account for scr refresh
        downlefttangle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(downlefttangle, 'tStartRefresh')  # time at next scr refresh
        downlefttangle.setAutoDraw(True)
    if downlefttangle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > downlefttangle.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            downlefttangle.tStop = t  # not accounting for scr refresh
            downlefttangle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(downlefttangle, 'tStopRefresh')  # time at next scr refresh
            downlefttangle.setAutoDraw(False)
    if downlefttangle.status == STARTED:  # only update if drawing
        downlefttangle.setOpacity(sin(10*t), log=False)
    
    # *uplefttangle* updates
    if uplefttangle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uplefttangle.frameNStart = frameN  # exact frame index
        uplefttangle.tStart = t  # local t and not account for scr refresh
        uplefttangle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uplefttangle, 'tStartRefresh')  # time at next scr refresh
        uplefttangle.setAutoDraw(True)
    if uplefttangle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > uplefttangle.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            uplefttangle.tStop = t  # not accounting for scr refresh
            uplefttangle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(uplefttangle, 'tStopRefresh')  # time at next scr refresh
            uplefttangle.setAutoDraw(False)
    if uplefttangle.status == STARTED:  # only update if drawing
        uplefttangle.setOpacity(sin(25*t), log=False)
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mouse.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            mouse.tStop = t  # not accounting for scr refresh
            mouse.frameNStop = frameN  # exact frame index
            win.timeOnFlip(mouse, 'tStopRefresh')  # time at next scr refresh
            mouse.status = FINISHED
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([uprighttangle, downrighttangle, downrighttangle, uplefttangle])
                    clickableList = [uprighttangle, downrighttangle, downrighttangle, uplefttangle]
                except:
                    clickableList = [[uprighttangle, downrighttangle, downrighttangle, uplefttangle]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # *uprtext* updates
    if uprtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        uprtext.frameNStart = frameN  # exact frame index
        uprtext.tStart = t  # local t and not account for scr refresh
        uprtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(uprtext, 'tStartRefresh')  # time at next scr refresh
        uprtext.setAutoDraw(True)
    if uprtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > uprtext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            uprtext.tStop = t  # not accounting for scr refresh
            uprtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(uprtext, 'tStopRefresh')  # time at next scr refresh
            uprtext.setAutoDraw(False)
    
    # *downrtext* updates
    if downrtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        downrtext.frameNStart = frameN  # exact frame index
        downrtext.tStart = t  # local t and not account for scr refresh
        downrtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(downrtext, 'tStartRefresh')  # time at next scr refresh
        downrtext.setAutoDraw(True)
    if downrtext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > downrtext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            downrtext.tStop = t  # not accounting for scr refresh
            downrtext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(downrtext, 'tStopRefresh')  # time at next scr refresh
            downrtext.setAutoDraw(False)
    
    # *downltext* updates
    if downltext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        downltext.frameNStart = frameN  # exact frame index
        downltext.tStart = t  # local t and not account for scr refresh
        downltext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(downltext, 'tStartRefresh')  # time at next scr refresh
        downltext.setAutoDraw(True)
    if downltext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > downltext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            downltext.tStop = t  # not accounting for scr refresh
            downltext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(downltext, 'tStopRefresh')  # time at next scr refresh
            downltext.setAutoDraw(False)
    
    # *upltext* updates
    if upltext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        upltext.frameNStart = frameN  # exact frame index
        upltext.tStart = t  # local t and not account for scr refresh
        upltext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(upltext, 'tStartRefresh')  # time at next scr refresh
        upltext.setAutoDraw(True)
    if upltext.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > upltext.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            upltext.tStop = t  # not accounting for scr refresh
            upltext.frameNStop = frameN  # exact frame index
            win.timeOnFlip(upltext, 'tStopRefresh')  # time at next scr refresh
            upltext.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('uprighttangle.started', uprighttangle.tStartRefresh)
thisExp.addData('uprighttangle.stopped', uprighttangle.tStopRefresh)
thisExp.addData('downrighttangle.started', downrighttangle.tStartRefresh)
thisExp.addData('downrighttangle.stopped', downrighttangle.tStopRefresh)
thisExp.addData('downlefttangle.started', downlefttangle.tStartRefresh)
thisExp.addData('downlefttangle.stopped', downlefttangle.tStopRefresh)
thisExp.addData('uplefttangle.started', uplefttangle.tStartRefresh)
thisExp.addData('uplefttangle.stopped', uplefttangle.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter([uprighttangle, downrighttangle, downrighttangle, uplefttangle])
        clickableList = [uprighttangle, downrighttangle, downrighttangle, uplefttangle]
    except:
        clickableList = [[uprighttangle, downrighttangle, downrighttangle, uplefttangle]]
    for obj in clickableList:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
thisExp.addData('uprtext.started', uprtext.tStartRefresh)
thisExp.addData('uprtext.stopped', uprtext.tStopRefresh)
thisExp.addData('downrtext.started', downrtext.tStartRefresh)
thisExp.addData('downrtext.stopped', downrtext.tStopRefresh)
thisExp.addData('downltext.started', downltext.tStartRefresh)
thisExp.addData('downltext.stopped', downltext.tStopRefresh)
thisExp.addData('upltext.started', upltext.tStartRefresh)
thisExp.addData('upltext.stopped', upltext.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
