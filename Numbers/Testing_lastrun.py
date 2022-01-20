#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Jan 19 20:10:11 2022
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
expName = 'Testing'  # from the Builder filename that created this script
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
    originPath='/Users/ishani/Desktop/school/neurotech/Numbers/Testing_lastrun.py',
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

# Initialize components for Routine "Choose_Number_"
Choose_Number_Clock = core.Clock()
button_1 = visual.ButtonStim(win, 
    text='1', font='Arvo',
    pos=(-.6, .25),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_1'
)
button_1.buttonClock = core.Clock()
button_05 = visual.ButtonStim(win, 
    text='5', font='Arvo',
    pos=(-.60, 0),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_05'
)
button_05.buttonClock = core.Clock()
button_08 = visual.ButtonStim(win, 
    text='8', font='Arvo',
    pos=(.3,0),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_08'
)
button_08.buttonClock = core.Clock()
button_02 = visual.ButtonStim(win, 
    text='2', font='Arvo',
    pos=(-.3,.25),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_02'
)
button_02.buttonClock = core.Clock()
button_06 = visual.ButtonStim(win, 
    text='6', font='Arvo',
    pos=(-.3, 0),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_06'
)
button_06.buttonClock = core.Clock()
button_03 = visual.ButtonStim(win, 
    text='3', font='Arvo',
    pos=(0,.25),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_03'
)
button_03.buttonClock = core.Clock()
button_07 = visual.ButtonStim(win, 
    text='7', font='Arvo',
    pos=(0, 0),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_07'
)
button_07.buttonClock = core.Clock()
button_00 = visual.ButtonStim(win, 
    text='0', font='Arvo',
    pos=(0,-.25),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_00'
)
button_00.buttonClock = core.Clock()
button_04 = visual.ButtonStim(win, 
    text='4', font='Arvo',
    pos=(.3,.25),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_04'
)
button_04.buttonClock = core.Clock()
button_09 = visual.ButtonStim(win, 
    text='9', font='Arvo',
    pos=(-.3,-.25),
    letterHeight=0.05,
    size=(.25,.20), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_09'
)
button_09.buttonClock = core.Clock()

# Initialize components for Routine "routine_1"
routine_1Clock = core.Clock()
txt1 = visual.TextStim(win=win, name='txt1',
    text='1',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_2"
routine_2Clock = core.Clock()
txt2 = visual.TextStim(win=win, name='txt2',
    text='2',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_3"
routine_3Clock = core.Clock()
txt3 = visual.TextStim(win=win, name='txt3',
    text='3',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_4"
routine_4Clock = core.Clock()
txt4 = visual.TextStim(win=win, name='txt4',
    text='4',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_5"
routine_5Clock = core.Clock()
text5 = visual.TextStim(win=win, name='text5',
    text='5',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_6"
routine_6Clock = core.Clock()
text6 = visual.TextStim(win=win, name='text6',
    text='6',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_7"
routine_7Clock = core.Clock()
text7 = visual.TextStim(win=win, name='text7',
    text='7',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_8"
routine_8Clock = core.Clock()
text8 = visual.TextStim(win=win, name='text8',
    text='8',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_9"
routine_9Clock = core.Clock()
text9 = visual.TextStim(win=win, name='text9',
    text='9',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "routine_0"
routine_0Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='0',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Choose_Number_"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
Choose_Number_Components = [button_1, button_05, button_08, button_02, button_06, button_03, button_07, button_00, button_04, button_09]
for thisComponent in Choose_Number_Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choose_Number_Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choose_Number_"-------
while continueRoutine:
    # get current time
    t = Choose_Number_Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choose_Number_Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *button_1* updates
    if button_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_1.frameNStart = frameN  # exact frame index
        button_1.tStart = t  # local t and not account for scr refresh
        button_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_1, 'tStartRefresh')  # time at next scr refresh
        button_1.setAutoDraw(True)
    if button_1.status == STARTED:  # only update if drawing
        button_1.setOpacity(sin(t*10), log=False)
    if button_1.status == STARTED:
        # check whether button_1 has been pressed
        if button_1.isClicked:
            if not button_1.wasClicked:
                button_1.timesOn.append(button_1.buttonClock.getTime()) # store time of first click
                button_1.timesOff.append(button_1.buttonClock.getTime()) # store time clicked until
            else:
                button_1.timesOff[-1] = button_1.buttonClock.getTime() # update time clicked until
            if not button_1.wasClicked:
                continueRoutine = False  # end routine when button_1 is clicked
                None
            button_1.wasClicked = True  # if button_1 is still clicked next frame, it is not a new click
        else:
            button_1.wasClicked = False  # if button_1 is clicked next frame, it is a new click
    else:
        button_1.wasClicked = False  # if button_1 is clicked next frame, it is a new click
    
    # *button_05* updates
    if button_05.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_05.frameNStart = frameN  # exact frame index
        button_05.tStart = t  # local t and not account for scr refresh
        button_05.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_05, 'tStartRefresh')  # time at next scr refresh
        button_05.setAutoDraw(True)
    if button_05.status == STARTED:  # only update if drawing
        button_05.setOpacity(sin(t*20), log=False)
    if button_05.status == STARTED:
        # check whether button_05 has been pressed
        if button_05.isClicked:
            if not button_05.wasClicked:
                button_05.timesOn.append(button_05.buttonClock.getTime()) # store time of first click
                button_05.timesOff.append(button_05.buttonClock.getTime()) # store time clicked until
            else:
                button_05.timesOff[-1] = button_05.buttonClock.getTime() # update time clicked until
            if not button_05.wasClicked:
                continueRoutine = False  # end routine when button_05 is clicked
                None
            button_05.wasClicked = True  # if button_05 is still clicked next frame, it is not a new click
        else:
            button_05.wasClicked = False  # if button_05 is clicked next frame, it is a new click
    else:
        button_05.wasClicked = False  # if button_05 is clicked next frame, it is a new click
    
    # *button_08* updates
    if button_08.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_08.frameNStart = frameN  # exact frame index
        button_08.tStart = t  # local t and not account for scr refresh
        button_08.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_08, 'tStartRefresh')  # time at next scr refresh
        button_08.setAutoDraw(True)
    if button_08.status == STARTED:  # only update if drawing
        button_08.setOpacity(sin(t*15), log=False)
    if button_08.status == STARTED:
        # check whether button_08 has been pressed
        if button_08.isClicked:
            if not button_08.wasClicked:
                button_08.timesOn.append(button_08.buttonClock.getTime()) # store time of first click
                button_08.timesOff.append(button_08.buttonClock.getTime()) # store time clicked until
            else:
                button_08.timesOff[-1] = button_08.buttonClock.getTime() # update time clicked until
            if not button_08.wasClicked:
                continueRoutine = False  # end routine when button_08 is clicked
                None
            button_08.wasClicked = True  # if button_08 is still clicked next frame, it is not a new click
        else:
            button_08.wasClicked = False  # if button_08 is clicked next frame, it is a new click
    else:
        button_08.wasClicked = False  # if button_08 is clicked next frame, it is a new click
    
    # *button_02* updates
    if button_02.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_02.frameNStart = frameN  # exact frame index
        button_02.tStart = t  # local t and not account for scr refresh
        button_02.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_02, 'tStartRefresh')  # time at next scr refresh
        button_02.setAutoDraw(True)
    if button_02.status == STARTED:  # only update if drawing
        button_02.setOpacity(sin(t*25), log=False)
    if button_02.status == STARTED:
        # check whether button_02 has been pressed
        if button_02.isClicked:
            if not button_02.wasClicked:
                button_02.timesOn.append(button_02.buttonClock.getTime()) # store time of first click
                button_02.timesOff.append(button_02.buttonClock.getTime()) # store time clicked until
            else:
                button_02.timesOff[-1] = button_02.buttonClock.getTime() # update time clicked until
            if not button_02.wasClicked:
                continueRoutine = False  # end routine when button_02 is clicked
                None
            button_02.wasClicked = True  # if button_02 is still clicked next frame, it is not a new click
        else:
            button_02.wasClicked = False  # if button_02 is clicked next frame, it is a new click
    else:
        button_02.wasClicked = False  # if button_02 is clicked next frame, it is a new click
    
    # *button_06* updates
    if button_06.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_06.frameNStart = frameN  # exact frame index
        button_06.tStart = t  # local t and not account for scr refresh
        button_06.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_06, 'tStartRefresh')  # time at next scr refresh
        button_06.setAutoDraw(True)
    if button_06.status == STARTED:  # only update if drawing
        button_06.setOpacity(sin(t*30), log=False)
    if button_06.status == STARTED:
        # check whether button_06 has been pressed
        if button_06.isClicked:
            if not button_06.wasClicked:
                button_06.timesOn.append(button_06.buttonClock.getTime()) # store time of first click
                button_06.timesOff.append(button_06.buttonClock.getTime()) # store time clicked until
            else:
                button_06.timesOff[-1] = button_06.buttonClock.getTime() # update time clicked until
            if not button_06.wasClicked:
                continueRoutine = False  # end routine when button_06 is clicked
                None
            button_06.wasClicked = True  # if button_06 is still clicked next frame, it is not a new click
        else:
            button_06.wasClicked = False  # if button_06 is clicked next frame, it is a new click
    else:
        button_06.wasClicked = False  # if button_06 is clicked next frame, it is a new click
    
    # *button_03* updates
    if button_03.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_03.frameNStart = frameN  # exact frame index
        button_03.tStart = t  # local t and not account for scr refresh
        button_03.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_03, 'tStartRefresh')  # time at next scr refresh
        button_03.setAutoDraw(True)
    if button_03.status == STARTED:  # only update if drawing
        button_03.setOpacity(sin(t*5), log=False)
    if button_03.status == STARTED:
        # check whether button_03 has been pressed
        if button_03.isClicked:
            if not button_03.wasClicked:
                button_03.timesOn.append(button_03.buttonClock.getTime()) # store time of first click
                button_03.timesOff.append(button_03.buttonClock.getTime()) # store time clicked until
            else:
                button_03.timesOff[-1] = button_03.buttonClock.getTime() # update time clicked until
            if not button_03.wasClicked:
                continueRoutine = False  # end routine when button_03 is clicked
                None
            button_03.wasClicked = True  # if button_03 is still clicked next frame, it is not a new click
        else:
            button_03.wasClicked = False  # if button_03 is clicked next frame, it is a new click
    else:
        button_03.wasClicked = False  # if button_03 is clicked next frame, it is a new click
    
    # *button_07* updates
    if button_07.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_07.frameNStart = frameN  # exact frame index
        button_07.tStart = t  # local t and not account for scr refresh
        button_07.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_07, 'tStartRefresh')  # time at next scr refresh
        button_07.setAutoDraw(True)
    if button_07.status == STARTED:  # only update if drawing
        button_07.setOpacity(sin(t*40), log=False)
    if button_07.status == STARTED:
        # check whether button_07 has been pressed
        if button_07.isClicked:
            if not button_07.wasClicked:
                button_07.timesOn.append(button_07.buttonClock.getTime()) # store time of first click
                button_07.timesOff.append(button_07.buttonClock.getTime()) # store time clicked until
            else:
                button_07.timesOff[-1] = button_07.buttonClock.getTime() # update time clicked until
            if not button_07.wasClicked:
                continueRoutine = False  # end routine when button_07 is clicked
                None
            button_07.wasClicked = True  # if button_07 is still clicked next frame, it is not a new click
        else:
            button_07.wasClicked = False  # if button_07 is clicked next frame, it is a new click
    else:
        button_07.wasClicked = False  # if button_07 is clicked next frame, it is a new click
    
    # *button_00* updates
    if button_00.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_00.frameNStart = frameN  # exact frame index
        button_00.tStart = t  # local t and not account for scr refresh
        button_00.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_00, 'tStartRefresh')  # time at next scr refresh
        button_00.setAutoDraw(True)
    if button_00.status == STARTED:  # only update if drawing
        button_00.setOpacity(sin(t*32), log=False)
    if button_00.status == STARTED:
        # check whether button_00 has been pressed
        if button_00.isClicked:
            if not button_00.wasClicked:
                button_00.timesOn.append(button_00.buttonClock.getTime()) # store time of first click
                button_00.timesOff.append(button_00.buttonClock.getTime()) # store time clicked until
            else:
                button_00.timesOff[-1] = button_00.buttonClock.getTime() # update time clicked until
            if not button_00.wasClicked:
                continueRoutine = False  # end routine when button_00 is clicked
                None
            button_00.wasClicked = True  # if button_00 is still clicked next frame, it is not a new click
        else:
            button_00.wasClicked = False  # if button_00 is clicked next frame, it is a new click
    else:
        button_00.wasClicked = False  # if button_00 is clicked next frame, it is a new click
    
    # *button_04* updates
    if button_04.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_04.frameNStart = frameN  # exact frame index
        button_04.tStart = t  # local t and not account for scr refresh
        button_04.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_04, 'tStartRefresh')  # time at next scr refresh
        button_04.setAutoDraw(True)
    if button_04.status == STARTED:  # only update if drawing
        button_04.setOpacity(sin(t*50), log=False)
    if button_04.status == STARTED:
        # check whether button_04 has been pressed
        if button_04.isClicked:
            if not button_04.wasClicked:
                button_04.timesOn.append(button_04.buttonClock.getTime()) # store time of first click
                button_04.timesOff.append(button_04.buttonClock.getTime()) # store time clicked until
            else:
                button_04.timesOff[-1] = button_04.buttonClock.getTime() # update time clicked until
            if not button_04.wasClicked:
                continueRoutine = False  # end routine when button_04 is clicked
                None
            button_04.wasClicked = True  # if button_04 is still clicked next frame, it is not a new click
        else:
            button_04.wasClicked = False  # if button_04 is clicked next frame, it is a new click
    else:
        button_04.wasClicked = False  # if button_04 is clicked next frame, it is a new click
    
    # *button_09* updates
    if button_09.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_09.frameNStart = frameN  # exact frame index
        button_09.tStart = t  # local t and not account for scr refresh
        button_09.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_09, 'tStartRefresh')  # time at next scr refresh
        button_09.setAutoDraw(True)
    if button_09.status == STARTED:  # only update if drawing
        button_09.setOpacity(sin(t*35), log=False)
    if button_09.status == STARTED:
        # check whether button_09 has been pressed
        if button_09.isClicked:
            if not button_09.wasClicked:
                button_09.timesOn.append(button_09.buttonClock.getTime()) # store time of first click
                button_09.timesOff.append(button_09.buttonClock.getTime()) # store time clicked until
            else:
                button_09.timesOff[-1] = button_09.buttonClock.getTime() # update time clicked until
            if not button_09.wasClicked:
                continueRoutine = False  # end routine when button_09 is clicked
                None
            button_09.wasClicked = True  # if button_09 is still clicked next frame, it is not a new click
        else:
            button_09.wasClicked = False  # if button_09 is clicked next frame, it is a new click
    else:
        button_09.wasClicked = False  # if button_09 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choose_Number_Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choose_Number_"-------
for thisComponent in Choose_Number_Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_1.started', button_1.tStartRefresh)
thisExp.addData('button_1.stopped', button_1.tStopRefresh)
thisExp.addData('button_1.numClicks', button_1.numClicks)
if button_1.numClicks:
   thisExp.addData('button_1.timesOn', button_1.timesOn)
   thisExp.addData('button_1.timesOff', button_1.timesOff)
else:
   thisExp.addData('button_1.timesOn', "")
   thisExp.addData('button_1.timesOff', "")
thisExp.addData('button_05.started', button_05.tStartRefresh)
thisExp.addData('button_05.stopped', button_05.tStopRefresh)
thisExp.addData('button_05.numClicks', button_05.numClicks)
if button_05.numClicks:
   thisExp.addData('button_05.timesOn', button_05.timesOn)
   thisExp.addData('button_05.timesOff', button_05.timesOff)
else:
   thisExp.addData('button_05.timesOn', "")
   thisExp.addData('button_05.timesOff', "")
thisExp.addData('button_08.started', button_08.tStartRefresh)
thisExp.addData('button_08.stopped', button_08.tStopRefresh)
thisExp.addData('button_08.numClicks', button_08.numClicks)
if button_08.numClicks:
   thisExp.addData('button_08.timesOn', button_08.timesOn)
   thisExp.addData('button_08.timesOff', button_08.timesOff)
else:
   thisExp.addData('button_08.timesOn', "")
   thisExp.addData('button_08.timesOff', "")
thisExp.addData('button_02.started', button_02.tStartRefresh)
thisExp.addData('button_02.stopped', button_02.tStopRefresh)
thisExp.addData('button_02.numClicks', button_02.numClicks)
if button_02.numClicks:
   thisExp.addData('button_02.timesOn', button_02.timesOn)
   thisExp.addData('button_02.timesOff', button_02.timesOff)
else:
   thisExp.addData('button_02.timesOn', "")
   thisExp.addData('button_02.timesOff', "")
thisExp.addData('button_06.started', button_06.tStartRefresh)
thisExp.addData('button_06.stopped', button_06.tStopRefresh)
thisExp.addData('button_06.numClicks', button_06.numClicks)
if button_06.numClicks:
   thisExp.addData('button_06.timesOn', button_06.timesOn)
   thisExp.addData('button_06.timesOff', button_06.timesOff)
else:
   thisExp.addData('button_06.timesOn', "")
   thisExp.addData('button_06.timesOff', "")
thisExp.addData('button_03.started', button_03.tStartRefresh)
thisExp.addData('button_03.stopped', button_03.tStopRefresh)
thisExp.addData('button_03.numClicks', button_03.numClicks)
if button_03.numClicks:
   thisExp.addData('button_03.timesOn', button_03.timesOn)
   thisExp.addData('button_03.timesOff', button_03.timesOff)
else:
   thisExp.addData('button_03.timesOn', "")
   thisExp.addData('button_03.timesOff', "")
thisExp.addData('button_07.started', button_07.tStartRefresh)
thisExp.addData('button_07.stopped', button_07.tStopRefresh)
thisExp.addData('button_07.numClicks', button_07.numClicks)
if button_07.numClicks:
   thisExp.addData('button_07.timesOn', button_07.timesOn)
   thisExp.addData('button_07.timesOff', button_07.timesOff)
else:
   thisExp.addData('button_07.timesOn', "")
   thisExp.addData('button_07.timesOff', "")
thisExp.addData('button_00.started', button_00.tStartRefresh)
thisExp.addData('button_00.stopped', button_00.tStopRefresh)
thisExp.addData('button_00.numClicks', button_00.numClicks)
if button_00.numClicks:
   thisExp.addData('button_00.timesOn', button_00.timesOn)
   thisExp.addData('button_00.timesOff', button_00.timesOff)
else:
   thisExp.addData('button_00.timesOn', "")
   thisExp.addData('button_00.timesOff', "")
thisExp.addData('button_04.started', button_04.tStartRefresh)
thisExp.addData('button_04.stopped', button_04.tStopRefresh)
thisExp.addData('button_04.numClicks', button_04.numClicks)
if button_04.numClicks:
   thisExp.addData('button_04.timesOn', button_04.timesOn)
   thisExp.addData('button_04.timesOff', button_04.timesOff)
else:
   thisExp.addData('button_04.timesOn', "")
   thisExp.addData('button_04.timesOff', "")
thisExp.addData('button_09.started', button_09.tStartRefresh)
thisExp.addData('button_09.stopped', button_09.tStopRefresh)
thisExp.addData('button_09.numClicks', button_09.numClicks)
if button_09.numClicks:
   thisExp.addData('button_09.timesOn', button_09.timesOn)
   thisExp.addData('button_09.timesOff', button_09.timesOff)
else:
   thisExp.addData('button_09.timesOn', "")
   thisExp.addData('button_09.timesOff', "")
# the Routine "Choose_Number_" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "routine_1"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_1Components = [txt1]
for thisComponent in routine_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt1* updates
    if txt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt1.frameNStart = frameN  # exact frame index
        txt1.tStart = t  # local t and not account for scr refresh
        txt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt1, 'tStartRefresh')  # time at next scr refresh
        txt1.setAutoDraw(True)
    if txt1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt1.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            txt1.tStop = t  # not accounting for scr refresh
            txt1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt1, 'tStopRefresh')  # time at next scr refresh
            txt1.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_1"-------
for thisComponent in routine_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt1.started', txt1.tStartRefresh)
thisExp.addData('txt1.stopped', txt1.tStopRefresh)

# ------Prepare to start Routine "routine_2"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_2Components = [txt2]
for thisComponent in routine_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt2* updates
    if txt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt2.frameNStart = frameN  # exact frame index
        txt2.tStart = t  # local t and not account for scr refresh
        txt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt2, 'tStartRefresh')  # time at next scr refresh
        txt2.setAutoDraw(True)
    if txt2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt2.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            txt2.tStop = t  # not accounting for scr refresh
            txt2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt2, 'tStopRefresh')  # time at next scr refresh
            txt2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_2"-------
for thisComponent in routine_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt2.started', txt2.tStartRefresh)
thisExp.addData('txt2.stopped', txt2.tStopRefresh)

# ------Prepare to start Routine "routine_3"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_3Components = [txt3]
for thisComponent in routine_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt3* updates
    if txt3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt3.frameNStart = frameN  # exact frame index
        txt3.tStart = t  # local t and not account for scr refresh
        txt3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt3, 'tStartRefresh')  # time at next scr refresh
        txt3.setAutoDraw(True)
    if txt3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt3.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            txt3.tStop = t  # not accounting for scr refresh
            txt3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt3, 'tStopRefresh')  # time at next scr refresh
            txt3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_3"-------
for thisComponent in routine_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt3.started', txt3.tStartRefresh)
thisExp.addData('txt3.stopped', txt3.tStopRefresh)

# ------Prepare to start Routine "routine_4"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_4Components = [txt4]
for thisComponent in routine_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt4* updates
    if txt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt4.frameNStart = frameN  # exact frame index
        txt4.tStart = t  # local t and not account for scr refresh
        txt4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt4, 'tStartRefresh')  # time at next scr refresh
        txt4.setAutoDraw(True)
    if txt4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt4.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            txt4.tStop = t  # not accounting for scr refresh
            txt4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt4, 'tStopRefresh')  # time at next scr refresh
            txt4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_4"-------
for thisComponent in routine_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt4.started', txt4.tStartRefresh)
thisExp.addData('txt4.stopped', txt4.tStopRefresh)

# ------Prepare to start Routine "routine_5"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_5Components = [text5]
for thisComponent in routine_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_5"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text5* updates
    if text5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text5.frameNStart = frameN  # exact frame index
        text5.tStart = t  # local t and not account for scr refresh
        text5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text5, 'tStartRefresh')  # time at next scr refresh
        text5.setAutoDraw(True)
    if text5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text5.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text5.tStop = t  # not accounting for scr refresh
            text5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text5, 'tStopRefresh')  # time at next scr refresh
            text5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_5"-------
for thisComponent in routine_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text5.started', text5.tStartRefresh)
thisExp.addData('text5.stopped', text5.tStopRefresh)

# ------Prepare to start Routine "routine_6"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_6Components = [text6]
for thisComponent in routine_6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_6"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text6* updates
    if text6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text6.frameNStart = frameN  # exact frame index
        text6.tStart = t  # local t and not account for scr refresh
        text6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text6, 'tStartRefresh')  # time at next scr refresh
        text6.setAutoDraw(True)
    if text6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text6.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text6.tStop = t  # not accounting for scr refresh
            text6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text6, 'tStopRefresh')  # time at next scr refresh
            text6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_6"-------
for thisComponent in routine_6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text6.started', text6.tStartRefresh)
thisExp.addData('text6.stopped', text6.tStopRefresh)

# ------Prepare to start Routine "routine_7"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_7Components = [text7]
for thisComponent in routine_7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_7"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_7Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_7Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text7* updates
    if text7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text7.frameNStart = frameN  # exact frame index
        text7.tStart = t  # local t and not account for scr refresh
        text7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text7, 'tStartRefresh')  # time at next scr refresh
        text7.setAutoDraw(True)
    if text7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text7.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text7.tStop = t  # not accounting for scr refresh
            text7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text7, 'tStopRefresh')  # time at next scr refresh
            text7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_7"-------
for thisComponent in routine_7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text7.started', text7.tStartRefresh)
thisExp.addData('text7.stopped', text7.tStopRefresh)

# ------Prepare to start Routine "routine_8"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_8Components = [text8]
for thisComponent in routine_8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_8"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_8Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_8Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text8* updates
    if text8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text8.frameNStart = frameN  # exact frame index
        text8.tStart = t  # local t and not account for scr refresh
        text8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text8, 'tStartRefresh')  # time at next scr refresh
        text8.setAutoDraw(True)
    if text8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text8.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text8.tStop = t  # not accounting for scr refresh
            text8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text8, 'tStopRefresh')  # time at next scr refresh
            text8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_8"-------
for thisComponent in routine_8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text8.started', text8.tStartRefresh)
thisExp.addData('text8.stopped', text8.tStopRefresh)

# ------Prepare to start Routine "routine_9"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_9Components = [text9]
for thisComponent in routine_9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_9"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_9Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_9Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text9* updates
    if text9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text9.frameNStart = frameN  # exact frame index
        text9.tStart = t  # local t and not account for scr refresh
        text9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text9, 'tStartRefresh')  # time at next scr refresh
        text9.setAutoDraw(True)
    if text9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text9.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            text9.tStop = t  # not accounting for scr refresh
            text9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text9, 'tStopRefresh')  # time at next scr refresh
            text9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_9"-------
for thisComponent in routine_9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text9.started', text9.tStartRefresh)
thisExp.addData('text9.stopped', text9.tStopRefresh)

# ------Prepare to start Routine "routine_0"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
routine_0Components = [text]
for thisComponent in routine_0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
routine_0Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "routine_0"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = routine_0Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routine_0Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in routine_0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "routine_0"-------
for thisComponent in routine_0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

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
