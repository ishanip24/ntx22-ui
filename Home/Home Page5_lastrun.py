#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Jan 24 20:21:03 2022
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
expName = 'Home Page'  # from the Builder filename that created this script
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
    originPath='/Users/micahalon/Downloads/Home Page5_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='beige', colorSpace='rgb',
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Welcome to the Home Page',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
textbox = visual.TextBox2(
     win, text='Response Goes Here\n', font='Open Sans',
     pos=[0,.35],     letterHeight=0.05,
     size=[.8,.1], borderWidth=3.0,
     color='black', colorSpace='rgb',
     opacity=0.8,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)
Yes = visual.ButtonStim(win, 
    text='', font='Arvo',
    pos=(.15, .1),
    letterHeight=0.05,
    size=[.2,.1], borderWidth=2.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Yes'
)
Yes.buttonClock = core.Clock()
No = visual.ButtonStim(win, 
    text='No', font='Arvo',
    pos=(-.15, .1),
    letterHeight=0.05,
    size=[.2,.1], borderWidth=2.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='No'
)
No.buttonClock = core.Clock()
Number = visual.ButtonStim(win, 
    text='#', font='Arvo',
    pos=(-.3, -.1),
    letterHeight=0.05,
    size=[.2,.1], borderWidth=2.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Number'
)
Number.buttonClock = core.Clock()
MCQ = visual.ButtonStim(win, 
    text='MC', font='Arvo',
    pos=[0,-.1],
    letterHeight=0.05,
    size=[.2,.1], borderWidth=2.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='MCQ'
)
MCQ.buttonClock = core.Clock()
FRQ = visual.ButtonStim(win, 
    text='A B C', font='Arvo',
    pos=[.3,-.1],
    letterHeight=0.05,
    size=[.2,.1], borderWidth=2.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='FRQ'
)
FRQ.buttonClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
Submit = visual.ButtonStim(win, 
    text='Submit', font='Arvo',
    pos=[.3,-.35],
    letterHeight=0.05,
    size=[.3,.15], borderWidth=2.0,
    fillColor='white', borderColor='black',
    color='black', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='Submit'
)
Submit.buttonClock = core.Clock()
Delete = visual.ShapeStim(
    win=win, name='Delete', vertices='cross',
    size=[.2,.15],
    ori=0.0, pos=[-.2,-.35],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='black',
    opacity=1.0, depth=-8.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
welcomeComponents = [text_2]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
textbox.reset()
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [textbox, Yes, No, Number, MCQ, FRQ, mouse, Submit, Delete]
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
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # *Yes* updates
    if Yes.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Yes.frameNStart = frameN  # exact frame index
        Yes.tStart = t  # local t and not account for scr refresh
        Yes.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Yes, 'tStartRefresh')  # time at next scr refresh
        Yes.setAutoDraw(True)
    if Yes.status == STARTED:  # only update if drawing
        Yes.setOpacity(sin(25.12*t), log=False)
        Yes.setText('Yes', log=False)
    if Yes.status == STARTED:
        # check whether Yes has been pressed
        if Yes.isClicked:
            if not Yes.wasClicked:
                Yes.timesOn.append(Yes.buttonClock.getTime()) # store time of first click
                Yes.timesOff.append(Yes.buttonClock.getTime()) # store time clicked until
            else:
                Yes.timesOff[-1] = Yes.buttonClock.getTime() # update time clicked until
            if not Yes.wasClicked:
                None
            Yes.wasClicked = True  # if Yes is still clicked next frame, it is not a new click
        else:
            Yes.wasClicked = False  # if Yes is clicked next frame, it is a new click
    else:
        Yes.wasClicked = False  # if Yes is clicked next frame, it is a new click
    
    # *No* updates
    if No.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        No.frameNStart = frameN  # exact frame index
        No.tStart = t  # local t and not account for scr refresh
        No.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(No, 'tStartRefresh')  # time at next scr refresh
        No.setAutoDraw(True)
    if No.status == STARTED:  # only update if drawing
        No.setOpacity(sin(43.96*t), log=False)
    if No.status == STARTED:
        # check whether No has been pressed
        if No.isClicked:
            if not No.wasClicked:
                No.timesOn.append(No.buttonClock.getTime()) # store time of first click
                No.timesOff.append(No.buttonClock.getTime()) # store time clicked until
            else:
                No.timesOff[-1] = No.buttonClock.getTime() # update time clicked until
            if not No.wasClicked:
                None
            No.wasClicked = True  # if No is still clicked next frame, it is not a new click
        else:
            No.wasClicked = False  # if No is clicked next frame, it is a new click
    else:
        No.wasClicked = False  # if No is clicked next frame, it is a new click
    
    # *Number* updates
    if Number.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Number.frameNStart = frameN  # exact frame index
        Number.tStart = t  # local t and not account for scr refresh
        Number.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Number, 'tStartRefresh')  # time at next scr refresh
        Number.setAutoDraw(True)
    if Number.status == STARTED:  # only update if drawing
        Number.setOpacity(sin(62.8*t), log=False)
    if Number.status == STARTED:
        # check whether Number has been pressed
        if Number.isClicked:
            if not Number.wasClicked:
                Number.timesOn.append(Number.buttonClock.getTime()) # store time of first click
                Number.timesOff.append(Number.buttonClock.getTime()) # store time clicked until
            else:
                Number.timesOff[-1] = Number.buttonClock.getTime() # update time clicked until
            if not Number.wasClicked:
                None
            Number.wasClicked = True  # if Number is still clicked next frame, it is not a new click
        else:
            Number.wasClicked = False  # if Number is clicked next frame, it is a new click
    else:
        Number.wasClicked = False  # if Number is clicked next frame, it is a new click
    
    # *MCQ* updates
    if MCQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        MCQ.frameNStart = frameN  # exact frame index
        MCQ.tStart = t  # local t and not account for scr refresh
        MCQ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MCQ, 'tStartRefresh')  # time at next scr refresh
        MCQ.setAutoDraw(True)
    if MCQ.status == STARTED:  # only update if drawing
        MCQ.setOpacity(sin(81.64*t), log=False)
    if MCQ.status == STARTED:
        # check whether MCQ has been pressed
        if MCQ.isClicked:
            if not MCQ.wasClicked:
                MCQ.timesOn.append(MCQ.buttonClock.getTime()) # store time of first click
                MCQ.timesOff.append(MCQ.buttonClock.getTime()) # store time clicked until
            else:
                MCQ.timesOff[-1] = MCQ.buttonClock.getTime() # update time clicked until
            if not MCQ.wasClicked:
                None
            MCQ.wasClicked = True  # if MCQ is still clicked next frame, it is not a new click
        else:
            MCQ.wasClicked = False  # if MCQ is clicked next frame, it is a new click
    else:
        MCQ.wasClicked = False  # if MCQ is clicked next frame, it is a new click
    
    # *FRQ* updates
    if FRQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        FRQ.frameNStart = frameN  # exact frame index
        FRQ.tStart = t  # local t and not account for scr refresh
        FRQ.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FRQ, 'tStartRefresh')  # time at next scr refresh
        FRQ.setAutoDraw(True)
    if FRQ.status == STARTED:  # only update if drawing
        FRQ.setOpacity(sin(100.48*t), log=False)
    if FRQ.status == STARTED:
        # check whether FRQ has been pressed
        if FRQ.isClicked:
            if not FRQ.wasClicked:
                FRQ.timesOn.append(FRQ.buttonClock.getTime()) # store time of first click
                FRQ.timesOff.append(FRQ.buttonClock.getTime()) # store time clicked until
            else:
                FRQ.timesOff[-1] = FRQ.buttonClock.getTime() # update time clicked until
            if not FRQ.wasClicked:
                None
            FRQ.wasClicked = True  # if FRQ is still clicked next frame, it is not a new click
        else:
            FRQ.wasClicked = False  # if FRQ is clicked next frame, it is a new click
    else:
        FRQ.wasClicked = False  # if FRQ is clicked next frame, it is a new click
    
    # *Submit* updates
    if Submit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        Submit.frameNStart = frameN  # exact frame index
        Submit.tStart = t  # local t and not account for scr refresh
        Submit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
        Submit.setAutoDraw(True)
    if Submit.status == STARTED:  # only update if drawing
        Submit.setOpacity(sin(t*138.16), log=False)
    if Submit.status == STARTED:
        # check whether Submit has been pressed
        if Submit.isClicked:
            if not Submit.wasClicked:
                Submit.timesOn.append(Submit.buttonClock.getTime()) # store time of first click
                Submit.timesOff.append(Submit.buttonClock.getTime()) # store time clicked until
            else:
                Submit.timesOff[-1] = Submit.buttonClock.getTime() # update time clicked until
            if not Submit.wasClicked:
                None
            Submit.wasClicked = True  # if Submit is still clicked next frame, it is not a new click
        else:
            Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
    else:
        Submit.wasClicked = False  # if Submit is clicked next frame, it is a new click
    
    # *Delete* updates
    if Delete.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Delete.frameNStart = frameN  # exact frame index
        Delete.tStart = t  # local t and not account for scr refresh
        Delete.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Delete, 'tStartRefresh')  # time at next scr refresh
        Delete.setAutoDraw(True)
    if Delete.status == STARTED:  # only update if drawing
        Delete.setOpacity(sin(119.32*t), log=False)
    
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
thisExp.addData('textbox.text',textbox.text)
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
thisExp.addData('Yes.started', Yes.tStartRefresh)
thisExp.addData('Yes.stopped', Yes.tStopRefresh)
thisExp.addData('Yes.numClicks', Yes.numClicks)
if Yes.numClicks:
   thisExp.addData('Yes.timesOn', Yes.timesOn)
   thisExp.addData('Yes.timesOff', Yes.timesOff)
else:
   thisExp.addData('Yes.timesOn', "")
   thisExp.addData('Yes.timesOff', "")
thisExp.addData('No.started', No.tStartRefresh)
thisExp.addData('No.stopped', No.tStopRefresh)
thisExp.addData('No.numClicks', No.numClicks)
if No.numClicks:
   thisExp.addData('No.timesOn', No.timesOn)
   thisExp.addData('No.timesOff', No.timesOff)
else:
   thisExp.addData('No.timesOn', "")
   thisExp.addData('No.timesOff', "")
thisExp.addData('Number.started', Number.tStartRefresh)
thisExp.addData('Number.stopped', Number.tStopRefresh)
thisExp.addData('Number.numClicks', Number.numClicks)
if Number.numClicks:
   thisExp.addData('Number.timesOn', Number.timesOn)
   thisExp.addData('Number.timesOff', Number.timesOff)
else:
   thisExp.addData('Number.timesOn', "")
   thisExp.addData('Number.timesOff', "")
thisExp.addData('MCQ.started', MCQ.tStartRefresh)
thisExp.addData('MCQ.stopped', MCQ.tStopRefresh)
thisExp.addData('MCQ.numClicks', MCQ.numClicks)
if MCQ.numClicks:
   thisExp.addData('MCQ.timesOn', MCQ.timesOn)
   thisExp.addData('MCQ.timesOff', MCQ.timesOff)
else:
   thisExp.addData('MCQ.timesOn', "")
   thisExp.addData('MCQ.timesOff', "")
thisExp.addData('FRQ.started', FRQ.tStartRefresh)
thisExp.addData('FRQ.stopped', FRQ.tStopRefresh)
thisExp.addData('FRQ.numClicks', FRQ.numClicks)
if FRQ.numClicks:
   thisExp.addData('FRQ.timesOn', FRQ.timesOn)
   thisExp.addData('FRQ.timesOff', FRQ.timesOff)
else:
   thisExp.addData('FRQ.timesOn', "")
   thisExp.addData('FRQ.timesOff', "")
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter([MCQ, FRQ, No, Yes, Delete, Number])
        clickableList = [MCQ, FRQ, No, Yes, Delete, Number]
    except:
        clickableList = [[MCQ, FRQ, No, Yes, Delete, Number]]
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
thisExp.addData('Submit.started', Submit.tStartRefresh)
thisExp.addData('Submit.stopped', Submit.tStopRefresh)
thisExp.addData('Submit.numClicks', Submit.numClicks)
if Submit.numClicks:
   thisExp.addData('Submit.timesOn', Submit.timesOn)
   thisExp.addData('Submit.timesOff', Submit.timesOff)
else:
   thisExp.addData('Submit.timesOn', "")
   thisExp.addData('Submit.timesOff', "")
thisExp.addData('Delete.started', Delete.tStartRefresh)
thisExp.addData('Delete.stopped', Delete.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
