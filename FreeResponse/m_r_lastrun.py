#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Feb  7 17:59:56 2022
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
expName = 'title'  # from the Builder filename that created this script
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
    originPath='/Users/jai/Desktop/Covid Spreader/ntx22-ui/FreeResponse/m_r_lastrun.py',
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
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='blue', colorSpace='rgb',
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
left_top = visual.ShapeStim(
    win=win, name='left_top',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(-0.6, 0.17),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='grey',
    opacity=1.0, depth=0.0, interpolate=True)
middle_top = visual.ShapeStim(
    win=win, name='middle_top',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, 0.17),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='grey',
    opacity=1.0, depth=-1.0, interpolate=True)
right_top = visual.ShapeStim(
    win=win, name='right_top',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0.6, 0.17),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='grey',
    opacity=1.0, depth=-2.0, interpolate=True)
left_bottom = visual.ShapeStim(
    win=win, name='left_bottom',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(-0.6, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='grey',
    opacity=1.0, depth=-3.0, interpolate=True)
middle_bottom = visual.ShapeStim(
    win=win, name='middle_bottom',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='grey',
    opacity=1.0, depth=-4.0, interpolate=True)
right_bottom = visual.ShapeStim(
    win=win, name='right_bottom',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0.6, -0.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='grey',
    opacity=1.0, depth=-5.0, interpolate=True)
m = visual.TextStim(win=win, name='m',
    text='M',
    font='Open Sans',
    pos=(-0.6, 0.05), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
n = visual.TextStim(win=win, name='n',
    text='N',
    font='Open Sans',
    pos=(0, 0.05), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
o = visual.TextStim(win=win, name='o',
    text='O',
    font='Open Sans',
    pos=(0.6, 0.05), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
p = visual.TextStim(win=win, name='p',
    text='P',
    font='Open Sans',
    pos=(-0.6, -0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
q = visual.TextStim(win=win, name='q',
    text='Q',
    font='Open Sans',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
r = visual.TextStim(win=win, name='r',
    text='R',
    font='Open Sans',
    pos=(0.6, -0.2), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
textbar = visual.TextBox2(
     win, text='answer', font='Open Sans',
     pos=(0, 0.37),     letterHeight=0.05,
     size=(0.8, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbar',
     autoLog=True,
)
undo = visual.ButtonStim(win, 
    text='Undo', font='Arvo',
    pos=(0.6, 0.35),
    letterHeight=0.05,
    size=[.2, .1], borderWidth=0.0,
    fillColor='black', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='undo'
)
undo.buttonClock = core.Clock()
home = visual.ButtonStim(win, 
    text='Home', font='Arvo',
    pos=(-.6, .35),
    letterHeight=0.05,
    size=[.2, .1], borderWidth=0.0,
    fillColor='black', borderColor='white',
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='home'
)
home.buttonClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
textbar.reset()
# setup some python lists for storing info about the mouse
mouse.x = []
mouse.y = []
mouse.leftButton = []
mouse.midButton = []
mouse.rightButton = []
mouse.time = []
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
trialComponents = [left_top, middle_top, right_top, left_bottom, middle_bottom, right_bottom, m, n, o, p, q, r, textbar, undo, home, mouse]
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
    
    # *left_top* updates
    if left_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_top.frameNStart = frameN  # exact frame index
        left_top.tStart = t  # local t and not account for scr refresh
        left_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_top, 'tStartRefresh')  # time at next scr refresh
        left_top.setAutoDraw(True)
    if left_top.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > left_top.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            left_top.tStop = t  # not accounting for scr refresh
            left_top.frameNStop = frameN  # exact frame index
            win.timeOnFlip(left_top, 'tStopRefresh')  # time at next scr refresh
            left_top.setAutoDraw(False)
    if left_top.status == STARTED:  # only update if drawing
        left_top.setOpacity(sin(1.57*t), log=False)
    
    # *middle_top* updates
    if middle_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        middle_top.frameNStart = frameN  # exact frame index
        middle_top.tStart = t  # local t and not account for scr refresh
        middle_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(middle_top, 'tStartRefresh')  # time at next scr refresh
        middle_top.setAutoDraw(True)
    if middle_top.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > middle_top.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            middle_top.tStop = t  # not accounting for scr refresh
            middle_top.frameNStop = frameN  # exact frame index
            win.timeOnFlip(middle_top, 'tStopRefresh')  # time at next scr refresh
            middle_top.setAutoDraw(False)
    if middle_top.status == STARTED:  # only update if drawing
        middle_top.setOpacity(sin(0.2*t), log=False)
    
    # *right_top* updates
    if right_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_top.frameNStart = frameN  # exact frame index
        right_top.tStart = t  # local t and not account for scr refresh
        right_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_top, 'tStartRefresh')  # time at next scr refresh
        right_top.setAutoDraw(True)
    if right_top.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_top.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            right_top.tStop = t  # not accounting for scr refresh
            right_top.frameNStop = frameN  # exact frame index
            win.timeOnFlip(right_top, 'tStopRefresh')  # time at next scr refresh
            right_top.setAutoDraw(False)
    if right_top.status == STARTED:  # only update if drawing
        right_top.setOpacity(sin(0.9*t), log=False)
    
    # *left_bottom* updates
    if left_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_bottom.frameNStart = frameN  # exact frame index
        left_bottom.tStart = t  # local t and not account for scr refresh
        left_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_bottom, 'tStartRefresh')  # time at next scr refresh
        left_bottom.setAutoDraw(True)
    if left_bottom.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > left_bottom.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            left_bottom.tStop = t  # not accounting for scr refresh
            left_bottom.frameNStop = frameN  # exact frame index
            win.timeOnFlip(left_bottom, 'tStopRefresh')  # time at next scr refresh
            left_bottom.setAutoDraw(False)
    if left_bottom.status == STARTED:  # only update if drawing
        left_bottom.setOpacity(sin(.224*t), log=False)
    
    # *middle_bottom* updates
    if middle_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        middle_bottom.frameNStart = frameN  # exact frame index
        middle_bottom.tStart = t  # local t and not account for scr refresh
        middle_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(middle_bottom, 'tStartRefresh')  # time at next scr refresh
        middle_bottom.setAutoDraw(True)
    if middle_bottom.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > middle_bottom.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            middle_bottom.tStop = t  # not accounting for scr refresh
            middle_bottom.frameNStop = frameN  # exact frame index
            win.timeOnFlip(middle_bottom, 'tStopRefresh')  # time at next scr refresh
            middle_bottom.setAutoDraw(False)
    if middle_bottom.status == STARTED:  # only update if drawing
        middle_bottom.setOpacity(sin(.63*t), log=False)
    
    # *right_bottom* updates
    if right_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_bottom.frameNStart = frameN  # exact frame index
        right_bottom.tStart = t  # local t and not account for scr refresh
        right_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_bottom, 'tStartRefresh')  # time at next scr refresh
        right_bottom.setAutoDraw(True)
    if right_bottom.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_bottom.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            right_bottom.tStop = t  # not accounting for scr refresh
            right_bottom.frameNStop = frameN  # exact frame index
            win.timeOnFlip(right_bottom, 'tStopRefresh')  # time at next scr refresh
            right_bottom.setAutoDraw(False)
    if right_bottom.status == STARTED:  # only update if drawing
        right_bottom.setOpacity(sin(.25*t), log=False)
    
    # *m* updates
    if m.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        m.frameNStart = frameN  # exact frame index
        m.tStart = t  # local t and not account for scr refresh
        m.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(m, 'tStartRefresh')  # time at next scr refresh
        m.setAutoDraw(True)
    if m.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > m.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            m.tStop = t  # not accounting for scr refresh
            m.frameNStop = frameN  # exact frame index
            win.timeOnFlip(m, 'tStopRefresh')  # time at next scr refresh
            m.setAutoDraw(False)
    
    # *n* updates
    if n.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        n.frameNStart = frameN  # exact frame index
        n.tStart = t  # local t and not account for scr refresh
        n.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(n, 'tStartRefresh')  # time at next scr refresh
        n.setAutoDraw(True)
    if n.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > n.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            n.tStop = t  # not accounting for scr refresh
            n.frameNStop = frameN  # exact frame index
            win.timeOnFlip(n, 'tStopRefresh')  # time at next scr refresh
            n.setAutoDraw(False)
    
    # *o* updates
    if o.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        o.frameNStart = frameN  # exact frame index
        o.tStart = t  # local t and not account for scr refresh
        o.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(o, 'tStartRefresh')  # time at next scr refresh
        o.setAutoDraw(True)
    if o.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > o.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            o.tStop = t  # not accounting for scr refresh
            o.frameNStop = frameN  # exact frame index
            win.timeOnFlip(o, 'tStopRefresh')  # time at next scr refresh
            o.setAutoDraw(False)
    
    # *p* updates
    if p.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        p.frameNStart = frameN  # exact frame index
        p.tStart = t  # local t and not account for scr refresh
        p.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(p, 'tStartRefresh')  # time at next scr refresh
        p.setAutoDraw(True)
    if p.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > p.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            p.tStop = t  # not accounting for scr refresh
            p.frameNStop = frameN  # exact frame index
            win.timeOnFlip(p, 'tStopRefresh')  # time at next scr refresh
            p.setAutoDraw(False)
    
    # *q* updates
    if q.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        q.frameNStart = frameN  # exact frame index
        q.tStart = t  # local t and not account for scr refresh
        q.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(q, 'tStartRefresh')  # time at next scr refresh
        q.setAutoDraw(True)
    if q.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > q.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            q.tStop = t  # not accounting for scr refresh
            q.frameNStop = frameN  # exact frame index
            win.timeOnFlip(q, 'tStopRefresh')  # time at next scr refresh
            q.setAutoDraw(False)
    
    # *r* updates
    if r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        r.frameNStart = frameN  # exact frame index
        r.tStart = t  # local t and not account for scr refresh
        r.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(r, 'tStartRefresh')  # time at next scr refresh
        r.setAutoDraw(True)
    if r.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > r.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            r.tStop = t  # not accounting for scr refresh
            r.frameNStop = frameN  # exact frame index
            win.timeOnFlip(r, 'tStopRefresh')  # time at next scr refresh
            r.setAutoDraw(False)
    
    # *textbar* updates
    if textbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbar.frameNStart = frameN  # exact frame index
        textbar.tStart = t  # local t and not account for scr refresh
        textbar.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbar, 'tStartRefresh')  # time at next scr refresh
        textbar.setAutoDraw(True)
    if textbar.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textbar.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            textbar.tStop = t  # not accounting for scr refresh
            textbar.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textbar, 'tStopRefresh')  # time at next scr refresh
            textbar.setAutoDraw(False)
    
    # *undo* updates
    if undo.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        undo.frameNStart = frameN  # exact frame index
        undo.tStart = t  # local t and not account for scr refresh
        undo.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(undo, 'tStartRefresh')  # time at next scr refresh
        undo.setAutoDraw(True)
    if undo.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > undo.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            undo.tStop = t  # not accounting for scr refresh
            undo.frameNStop = frameN  # exact frame index
            win.timeOnFlip(undo, 'tStopRefresh')  # time at next scr refresh
            undo.setAutoDraw(False)
    if undo.status == STARTED:  # only update if drawing
        undo.setOpacity(sin(.39*t), log=False)
    if undo.status == STARTED:
        # check whether undo has been pressed
        if undo.isClicked:
            if not undo.wasClicked:
                undo.timesOn.append(undo.buttonClock.getTime()) # store time of first click
                undo.timesOff.append(undo.buttonClock.getTime()) # store time clicked until
            else:
                undo.timesOff[-1] = undo.buttonClock.getTime() # update time clicked until
            if not undo.wasClicked:
                continueRoutine = False  # end routine when undo is clicked
                None
            undo.wasClicked = True  # if undo is still clicked next frame, it is not a new click
        else:
            undo.wasClicked = False  # if undo is clicked next frame, it is a new click
    else:
        undo.wasClicked = False  # if undo is clicked next frame, it is a new click
    
    # *home* updates
    if home.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        home.frameNStart = frameN  # exact frame index
        home.tStart = t  # local t and not account for scr refresh
        home.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(home, 'tStartRefresh')  # time at next scr refresh
        home.setAutoDraw(True)
    if home.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > home.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            home.tStop = t  # not accounting for scr refresh
            home.frameNStop = frameN  # exact frame index
            win.timeOnFlip(home, 'tStopRefresh')  # time at next scr refresh
            home.setAutoDraw(False)
    if home.status == STARTED:  # only update if drawing
        home.setOpacity(sin(.285*t), log=False)
    if home.status == STARTED:
        # check whether home has been pressed
        if home.isClicked:
            if not home.wasClicked:
                home.timesOn.append(home.buttonClock.getTime()) # store time of first click
                home.timesOff.append(home.buttonClock.getTime()) # store time clicked until
            else:
                home.timesOff[-1] = home.buttonClock.getTime() # update time clicked until
            if not home.wasClicked:
                continueRoutine = False  # end routine when home is clicked
                None
            home.wasClicked = True  # if home is still clicked next frame, it is not a new click
        else:
            home.wasClicked = False  # if home is clicked next frame, it is a new click
    else:
        home.wasClicked = False  # if home is clicked next frame, it is a new click
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
        if tThisFlipGlobal > mouse.tStartRefresh + 20.0-frameTolerance:
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
                    iter([left_top, middle_top, right_top, left_bottom, middle_bottom, right_bottom])
                    clickableList = [left_top, middle_top, right_top, left_bottom, middle_bottom, right_bottom]
                except:
                    clickableList = [[left_top, middle_top, right_top, left_bottom, middle_bottom, right_bottom]]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                x, y = mouse.getPos()
                mouse.x.append(x)
                mouse.y.append(y)
                buttons = mouse.getPressed()
                mouse.leftButton.append(buttons[0])
                mouse.midButton.append(buttons[1])
                mouse.rightButton.append(buttons[2])
                mouse.time.append(mouse.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
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
thisExp.addData('left_top.started', left_top.tStartRefresh)
thisExp.addData('left_top.stopped', left_top.tStopRefresh)
thisExp.addData('middle_top.started', middle_top.tStartRefresh)
thisExp.addData('middle_top.stopped', middle_top.tStopRefresh)
thisExp.addData('right_top.started', right_top.tStartRefresh)
thisExp.addData('right_top.stopped', right_top.tStopRefresh)
thisExp.addData('left_bottom.started', left_bottom.tStartRefresh)
thisExp.addData('left_bottom.stopped', left_bottom.tStopRefresh)
thisExp.addData('middle_bottom.started', middle_bottom.tStartRefresh)
thisExp.addData('middle_bottom.stopped', middle_bottom.tStopRefresh)
thisExp.addData('right_bottom.started', right_bottom.tStartRefresh)
thisExp.addData('right_bottom.stopped', right_bottom.tStopRefresh)
thisExp.addData('m.started', m.tStartRefresh)
thisExp.addData('m.stopped', m.tStopRefresh)
thisExp.addData('n.started', n.tStartRefresh)
thisExp.addData('n.stopped', n.tStopRefresh)
thisExp.addData('o.started', o.tStartRefresh)
thisExp.addData('o.stopped', o.tStopRefresh)
thisExp.addData('p.started', p.tStartRefresh)
thisExp.addData('p.stopped', p.tStopRefresh)
thisExp.addData('q.started', q.tStartRefresh)
thisExp.addData('q.stopped', q.tStopRefresh)
thisExp.addData('r.started', r.tStartRefresh)
thisExp.addData('r.stopped', r.tStopRefresh)
thisExp.addData('textbar.text',textbar.text)
thisExp.addData('textbar.started', textbar.tStartRefresh)
thisExp.addData('textbar.stopped', textbar.tStopRefresh)
thisExp.addData('undo.started', undo.tStartRefresh)
thisExp.addData('undo.stopped', undo.tStopRefresh)
thisExp.addData('undo.numClicks', undo.numClicks)
if undo.numClicks:
   thisExp.addData('undo.timesOn', undo.timesOn)
   thisExp.addData('undo.timesOff', undo.timesOff)
else:
   thisExp.addData('undo.timesOn', "")
   thisExp.addData('undo.timesOff', "")
thisExp.addData('home.started', home.tStartRefresh)
thisExp.addData('home.stopped', home.tStopRefresh)
thisExp.addData('home.numClicks', home.numClicks)
if home.numClicks:
   thisExp.addData('home.timesOn', home.timesOn)
   thisExp.addData('home.timesOff', home.timesOff)
else:
   thisExp.addData('home.timesOn', "")
   thisExp.addData('home.timesOff', "")
# store data for thisExp (ExperimentHandler)
if len(mouse.x): thisExp.addData('mouse.x', mouse.x[0])
if len(mouse.y): thisExp.addData('mouse.y', mouse.y[0])
if len(mouse.leftButton): thisExp.addData('mouse.leftButton', mouse.leftButton[0])
if len(mouse.midButton): thisExp.addData('mouse.midButton', mouse.midButton[0])
if len(mouse.rightButton): thisExp.addData('mouse.rightButton', mouse.rightButton[0])
if len(mouse.time): thisExp.addData('mouse.time', mouse.time[0])
if len(mouse.clicked_name): thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()

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
