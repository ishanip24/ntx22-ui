#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sun Jan 30 11:37:17 2022
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
    originPath='/Users/ishani/Desktop/school/neurotech/FreeResponse/s_w_lastrun.py',
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
left_top = visual.ShapeStim(
    win=win, name='left_top',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(-0.6, 0.25),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=1.0, depth=0.0, interpolate=True)
middle_top = visual.ShapeStim(
    win=win, name='middle_top',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, 0.25),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='yellow',
    opacity=1.0, depth=-1.0, interpolate=True)
right_top = visual.ShapeStim(
    win=win, name='right_top',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0.6, 0.25),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='purple',
    opacity=1.0, depth=-2.0, interpolate=True)
left_bottom = visual.ShapeStim(
    win=win, name='left_bottom',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(-0.6, -0.15),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='pink',
    opacity=1.0, depth=-3.0, interpolate=True)
middle_bottom = visual.ShapeStim(
    win=win, name='middle_bottom',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -0.15),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='green',
    opacity=1.0, depth=-4.0, interpolate=True)
right_bottom = visual.ShapeStim(
    win=win, name='right_bottom',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0.6, -0.15),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='red',
    opacity=1.0, depth=-5.0, interpolate=True)
s = visual.TextStim(win=win, name='s',
    text='S',
    font='Open Sans',
    pos=(-0.6, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
t_letter = visual.TextStim(win=win, name='t_letter',
    text='T',
    font='Open Sans',
    pos=(0.6, 0.15), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
u = visual.TextStim(win=win, name='u',
    text='U',
    font='Open Sans',
    pos=(-0.6, -0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
v = visual.TextStim(win=win, name='v',
    text='V',
    font='Open Sans',
    pos=(0, -0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
w = visual.TextStim(win=win, name='w',
    text='W',
    font='Open Sans',
    pos=(0.6, -0.05), height=0.02, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
textbar = visual.TextBox2(
     win, text='answer', font='Open Sans',
     pos=(0, 0.4),     letterHeight=0.05,
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
submit = visual.ButtonStim(win, 
    text='Submit', font='Arvo',
    pos=(0.3, -0.35),
    letterHeight=0.05,
    size=[.3, .15], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='submit'
)
submit.buttonClock = core.Clock()
back = visual.ButtonStim(win, 
    text='back', font='Arvo',
    pos=(-.3, -.35),
    letterHeight=0.05,
    size=[.3, .15], borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=1.0,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='back'
)
back.buttonClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
textbar.reset()
# keep track of which components have finished
trialComponents = [left_top, middle_top, right_top, left_bottom, middle_bottom, right_bottom, s, t_letter, u, v, w, textbar, submit, back]
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
    
    # *s* updates
    if s.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        s.frameNStart = frameN  # exact frame index
        s.tStart = t  # local t and not account for scr refresh
        s.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(s, 'tStartRefresh')  # time at next scr refresh
        s.setAutoDraw(True)
    if s.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > s.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            s.tStop = t  # not accounting for scr refresh
            s.frameNStop = frameN  # exact frame index
            win.timeOnFlip(s, 'tStopRefresh')  # time at next scr refresh
            s.setAutoDraw(False)
    
    # *t_letter* updates
    if t_letter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        t_letter.frameNStart = frameN  # exact frame index
        t_letter.tStart = t  # local t and not account for scr refresh
        t_letter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(t_letter, 'tStartRefresh')  # time at next scr refresh
        t_letter.setAutoDraw(True)
    if t_letter.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > t_letter.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            t_letter.tStop = t  # not accounting for scr refresh
            t_letter.frameNStop = frameN  # exact frame index
            win.timeOnFlip(t_letter, 'tStopRefresh')  # time at next scr refresh
            t_letter.setAutoDraw(False)
    
    # *u* updates
    if u.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        u.frameNStart = frameN  # exact frame index
        u.tStart = t  # local t and not account for scr refresh
        u.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(u, 'tStartRefresh')  # time at next scr refresh
        u.setAutoDraw(True)
    if u.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > u.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            u.tStop = t  # not accounting for scr refresh
            u.frameNStop = frameN  # exact frame index
            win.timeOnFlip(u, 'tStopRefresh')  # time at next scr refresh
            u.setAutoDraw(False)
    
    # *v* updates
    if v.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        v.frameNStart = frameN  # exact frame index
        v.tStart = t  # local t and not account for scr refresh
        v.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(v, 'tStartRefresh')  # time at next scr refresh
        v.setAutoDraw(True)
    if v.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > v.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            v.tStop = t  # not accounting for scr refresh
            v.frameNStop = frameN  # exact frame index
            win.timeOnFlip(v, 'tStopRefresh')  # time at next scr refresh
            v.setAutoDraw(False)
    
    # *w* updates
    if w.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        w.frameNStart = frameN  # exact frame index
        w.tStart = t  # local t and not account for scr refresh
        w.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(w, 'tStartRefresh')  # time at next scr refresh
        w.setAutoDraw(True)
    if w.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > w.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            w.tStop = t  # not accounting for scr refresh
            w.frameNStop = frameN  # exact frame index
            win.timeOnFlip(w, 'tStopRefresh')  # time at next scr refresh
            w.setAutoDraw(False)
    
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
    
    # *submit* updates
    if submit.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        submit.frameNStart = frameN  # exact frame index
        submit.tStart = t  # local t and not account for scr refresh
        submit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(submit, 'tStartRefresh')  # time at next scr refresh
        submit.setAutoDraw(True)
    if submit.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > submit.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            submit.tStop = t  # not accounting for scr refresh
            submit.frameNStop = frameN  # exact frame index
            win.timeOnFlip(submit, 'tStopRefresh')  # time at next scr refresh
            submit.setAutoDraw(False)
    if submit.status == STARTED:  # only update if drawing
        submit.setOpacity(sin(.39*t), log=False)
    if submit.status == STARTED:
        # check whether submit has been pressed
        if submit.isClicked:
            if not submit.wasClicked:
                submit.timesOn.append(submit.buttonClock.getTime()) # store time of first click
                submit.timesOff.append(submit.buttonClock.getTime()) # store time clicked until
            else:
                submit.timesOff[-1] = submit.buttonClock.getTime() # update time clicked until
            if not submit.wasClicked:
                continueRoutine = False  # end routine when submit is clicked
                None
            submit.wasClicked = True  # if submit is still clicked next frame, it is not a new click
        else:
            submit.wasClicked = False  # if submit is clicked next frame, it is a new click
    else:
        submit.wasClicked = False  # if submit is clicked next frame, it is a new click
    
    # *back* updates
    if back.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        back.frameNStart = frameN  # exact frame index
        back.tStart = t  # local t and not account for scr refresh
        back.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back, 'tStartRefresh')  # time at next scr refresh
        back.setAutoDraw(True)
    if back.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            back.tStop = t  # not accounting for scr refresh
            back.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back, 'tStopRefresh')  # time at next scr refresh
            back.setAutoDraw(False)
    if back.status == STARTED:  # only update if drawing
        back.setOpacity(sin(.285*t), log=False)
    if back.status == STARTED:
        # check whether back has been pressed
        if back.isClicked:
            if not back.wasClicked:
                back.timesOn.append(back.buttonClock.getTime()) # store time of first click
                back.timesOff.append(back.buttonClock.getTime()) # store time clicked until
            else:
                back.timesOff[-1] = back.buttonClock.getTime() # update time clicked until
            if not back.wasClicked:
                continueRoutine = False  # end routine when back is clicked
                None
            back.wasClicked = True  # if back is still clicked next frame, it is not a new click
        else:
            back.wasClicked = False  # if back is clicked next frame, it is a new click
    else:
        back.wasClicked = False  # if back is clicked next frame, it is a new click
    
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
thisExp.addData('s.started', s.tStartRefresh)
thisExp.addData('s.stopped', s.tStopRefresh)
thisExp.addData('t_letter.started', t_letter.tStartRefresh)
thisExp.addData('t_letter.stopped', t_letter.tStopRefresh)
thisExp.addData('u.started', u.tStartRefresh)
thisExp.addData('u.stopped', u.tStopRefresh)
thisExp.addData('v.started', v.tStartRefresh)
thisExp.addData('v.stopped', v.tStopRefresh)
thisExp.addData('w.started', w.tStartRefresh)
thisExp.addData('w.stopped', w.tStopRefresh)
thisExp.addData('textbar.text',textbar.text)
thisExp.addData('textbar.started', textbar.tStartRefresh)
thisExp.addData('textbar.stopped', textbar.tStopRefresh)
thisExp.addData('submit.started', submit.tStartRefresh)
thisExp.addData('submit.stopped', submit.tStopRefresh)
thisExp.addData('submit.numClicks', submit.numClicks)
if submit.numClicks:
   thisExp.addData('submit.timesOn', submit.timesOn)
   thisExp.addData('submit.timesOff', submit.timesOff)
else:
   thisExp.addData('submit.timesOn', "")
   thisExp.addData('submit.timesOff', "")
thisExp.addData('back.started', back.tStartRefresh)
thisExp.addData('back.stopped', back.tStopRefresh)
thisExp.addData('back.numClicks', back.numClicks)
if back.numClicks:
   thisExp.addData('back.timesOn', back.timesOn)
   thisExp.addData('back.timesOff', back.timesOff)
else:
   thisExp.addData('back.timesOn', "")
   thisExp.addData('back.timesOff', "")

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
