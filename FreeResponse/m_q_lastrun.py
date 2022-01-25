#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Jan 24 16:31:41 2022
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
expName = 'm_q'  # from the Builder filename that created this script
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
    originPath='/Users/jai/Desktop/Neurotech/PsychoPy/m_q_lastrun.py',
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

# Initialize components for Routine "m__r"
m__rClock = core.Clock()
left_top_circle = visual.ShapeStim(
    win=win, name='left_top_circle',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(-0.6, 0.2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='blue',
    opacity=1.0, depth=0.0, interpolate=True)
left_bottom_circle = visual.ShapeStim(
    win=win, name='left_bottom_circle',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(-.6, -.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='pink',
    opacity=1.0, depth=-1.0, interpolate=True)
center_top_circle = visual.ShapeStim(
    win=win, name='center_top_circle',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, .2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='yellow',
    opacity=1.0, depth=-2.0, interpolate=True)
center_bottom_circle = visual.ShapeStim(
    win=win, name='center_bottom_circle',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(0, -.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='green',
    opacity=1.0, depth=-3.0, interpolate=True)
right_top_circle = visual.ShapeStim(
    win=win, name='right_top_circle',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(.6, .2),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='purple',
    opacity=1.0, depth=-4.0, interpolate=True)
right_bottom_circle = visual.ShapeStim(
    win=win, name='right_bottom_circle',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=(.6, -.3),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='red',
    opacity=1.0, depth=-5.0, interpolate=True)
m = visual.TextStim(win=win, name='m',
    text='M',
    font='Open Sans',
    pos=(-.6, .05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
n = visual.TextStim(win=win, name='n',
    text='N\n',
    font='Open Sans',
    pos=(0, .05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
o = visual.TextStim(win=win, name='o',
    text='O\n',
    font='Open Sans',
    pos=(.6, .05), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
p = visual.TextStim(win=win, name='p',
    text='P',
    font='Open Sans',
    pos=(-.6, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
q = visual.TextStim(win=win, name='q',
    text='Q',
    font='Open Sans',
    pos=(0, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
r = visual.TextStim(win=win, name='r',
    text='R',
    font='Open Sans',
    pos=(.6, -.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
textbox = visual.TextBox2(
     win, text='answer', font='Open Sans',
     pos=(0, .35),     letterHeight=0.05,
     size=(.8, .1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor='white', borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='textbox',
     autoLog=True,
)
back = visual.ShapeStim(
    win=win, name='back',
    size=(0.1, 0.1), vertices='triangle',
    ori=0.0, pos=(-0.6, .4),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-13.0, interpolate=True)
back_text = visual.TextStim(win=win, name='back_text',
    text='back',
    font='Open Sans',
    pos=(-.6, .4), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "m__r"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
textbox.reset()
# keep track of which components have finished
m__rComponents = [left_top_circle, left_bottom_circle, center_top_circle, center_bottom_circle, right_top_circle, right_bottom_circle, m, n, o, p, q, r, textbox, back, back_text]
for thisComponent in m__rComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
m__rClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "m__r"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = m__rClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=m__rClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *left_top_circle* updates
    if left_top_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_top_circle.frameNStart = frameN  # exact frame index
        left_top_circle.tStart = t  # local t and not account for scr refresh
        left_top_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_top_circle, 'tStartRefresh')  # time at next scr refresh
        left_top_circle.setAutoDraw(True)
    if left_top_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > left_top_circle.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            left_top_circle.tStop = t  # not accounting for scr refresh
            left_top_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(left_top_circle, 'tStopRefresh')  # time at next scr refresh
            left_top_circle.setAutoDraw(False)
    if left_top_circle.status == STARTED:  # only update if drawing
        left_top_circle.setOpacity(sin(25.12*t), log=False)
    
    # *left_bottom_circle* updates
    if left_bottom_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        left_bottom_circle.frameNStart = frameN  # exact frame index
        left_bottom_circle.tStart = t  # local t and not account for scr refresh
        left_bottom_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(left_bottom_circle, 'tStartRefresh')  # time at next scr refresh
        left_bottom_circle.setAutoDraw(True)
    if left_bottom_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > left_bottom_circle.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            left_bottom_circle.tStop = t  # not accounting for scr refresh
            left_bottom_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(left_bottom_circle, 'tStopRefresh')  # time at next scr refresh
            left_bottom_circle.setAutoDraw(False)
    if left_bottom_circle.status == STARTED:  # only update if drawing
        left_bottom_circle.setOpacity(sin(81.68*t), log=False)
    
    # *center_top_circle* updates
    if center_top_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        center_top_circle.frameNStart = frameN  # exact frame index
        center_top_circle.tStart = t  # local t and not account for scr refresh
        center_top_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(center_top_circle, 'tStartRefresh')  # time at next scr refresh
        center_top_circle.setAutoDraw(True)
    if center_top_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > center_top_circle.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            center_top_circle.tStop = t  # not accounting for scr refresh
            center_top_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(center_top_circle, 'tStopRefresh')  # time at next scr refresh
            center_top_circle.setAutoDraw(False)
    if center_top_circle.status == STARTED:  # only update if drawing
        center_top_circle.setOpacity(sin(43.98*t), log=False)
    
    # *center_bottom_circle* updates
    if center_bottom_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        center_bottom_circle.frameNStart = frameN  # exact frame index
        center_bottom_circle.tStart = t  # local t and not account for scr refresh
        center_bottom_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(center_bottom_circle, 'tStartRefresh')  # time at next scr refresh
        center_bottom_circle.setAutoDraw(True)
    if center_bottom_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > center_bottom_circle.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            center_bottom_circle.tStop = t  # not accounting for scr refresh
            center_bottom_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(center_bottom_circle, 'tStopRefresh')  # time at next scr refresh
            center_bottom_circle.setAutoDraw(False)
    if center_bottom_circle.status == STARTED:  # only update if drawing
        center_bottom_circle.setOpacity(sin(100.53*t), log=False)
    
    # *right_top_circle* updates
    if right_top_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_top_circle.frameNStart = frameN  # exact frame index
        right_top_circle.tStart = t  # local t and not account for scr refresh
        right_top_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_top_circle, 'tStartRefresh')  # time at next scr refresh
        right_top_circle.setAutoDraw(True)
    if right_top_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_top_circle.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            right_top_circle.tStop = t  # not accounting for scr refresh
            right_top_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(right_top_circle, 'tStopRefresh')  # time at next scr refresh
            right_top_circle.setAutoDraw(False)
    if right_top_circle.status == STARTED:  # only update if drawing
        right_top_circle.setOpacity(sin(62.83*t), log=False)
    
    # *right_bottom_circle* updates
    if right_bottom_circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_bottom_circle.frameNStart = frameN  # exact frame index
        right_bottom_circle.tStart = t  # local t and not account for scr refresh
        right_bottom_circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_bottom_circle, 'tStartRefresh')  # time at next scr refresh
        right_bottom_circle.setAutoDraw(True)
    if right_bottom_circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_bottom_circle.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            right_bottom_circle.tStop = t  # not accounting for scr refresh
            right_bottom_circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(right_bottom_circle, 'tStopRefresh')  # time at next scr refresh
            right_bottom_circle.setAutoDraw(False)
    if right_bottom_circle.status == STARTED:  # only update if drawing
        right_bottom_circle.setOpacity(sin(119.38*t), log=False)
    
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
        if tThisFlipGlobal > n.tStartRefresh + 20.0-frameTolerance:
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
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    if textbox.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textbox.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            textbox.tStop = t  # not accounting for scr refresh
            textbox.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textbox, 'tStopRefresh')  # time at next scr refresh
            textbox.setAutoDraw(False)
    
    # *back* updates
    if back.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
    
    # *back_text* updates
    if back_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        back_text.frameNStart = frameN  # exact frame index
        back_text.tStart = t  # local t and not account for scr refresh
        back_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(back_text, 'tStartRefresh')  # time at next scr refresh
        back_text.setAutoDraw(True)
    if back_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > back_text.tStartRefresh + 20.0-frameTolerance:
            # keep track of stop time/frame for later
            back_text.tStop = t  # not accounting for scr refresh
            back_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(back_text, 'tStopRefresh')  # time at next scr refresh
            back_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in m__rComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "m__r"-------
for thisComponent in m__rComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('left_top_circle.started', left_top_circle.tStartRefresh)
thisExp.addData('left_top_circle.stopped', left_top_circle.tStopRefresh)
thisExp.addData('left_bottom_circle.started', left_bottom_circle.tStartRefresh)
thisExp.addData('left_bottom_circle.stopped', left_bottom_circle.tStopRefresh)
thisExp.addData('center_top_circle.started', center_top_circle.tStartRefresh)
thisExp.addData('center_top_circle.stopped', center_top_circle.tStopRefresh)
thisExp.addData('center_bottom_circle.started', center_bottom_circle.tStartRefresh)
thisExp.addData('center_bottom_circle.stopped', center_bottom_circle.tStopRefresh)
thisExp.addData('right_top_circle.started', right_top_circle.tStartRefresh)
thisExp.addData('right_top_circle.stopped', right_top_circle.tStopRefresh)
thisExp.addData('right_bottom_circle.started', right_bottom_circle.tStartRefresh)
thisExp.addData('right_bottom_circle.stopped', right_bottom_circle.tStopRefresh)
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
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
thisExp.addData('back.started', back.tStartRefresh)
thisExp.addData('back.stopped', back.tStopRefresh)
thisExp.addData('back_text.started', back_text.tStartRefresh)
thisExp.addData('back_text.stopped', back_text.tStopRefresh)

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
