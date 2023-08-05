###7T PRE-SESSION ###

### 1 - SCREENING TASK - ###

# Import libraries
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from psychopy import event
import os
import random
import csv


#inizialize some variables - ENCODING
fixcross_size = (0.03, 0.03)
stimulus_size_enc = (0.35,0.35)
marker_size = (0.06,0.1)
central_pos = (0, 0.15)
left_img_pos = (-0.25, 0.15)
right_img_pos = (0.25, 0.15)

text_height = 0.035
number_height = 0.09

#durations
fixcross_duration = 1.0
stim_duration = 5.0
dst_inst_duration = 3.0
dst_task_duration = 60 #s
dst_results_duration = 5.0
dist_labels_height = 0.05

#colors
win_color = 'grey' #[0,0,0]
components_color = 'white'

#inizialize some variables for RETRIEVAL
fix_duration = 1.0
fix_size = (0.03, 0.03)
text_height = 0.035
cue_duration = 5.0
options_duration = 2.0
finalscreen_duration = 5.0
stimulus_size_retr = (0.25,0.25)
central_pos = (0, 0.15)

endscreen_duration = 5

win_color = 'grey' #[0,0,0]
components_color = 'white'

opt1label_pos  = (-0.3, 0.04)
opt2label_pos =  (0,  0.11)
opt3label_pos = (0.3, 0.04)
opt4label_pos = (0, -0.21) 
optlabel_height = 0.03
opt4_pos = (0, -0.22)
opt4_height = 0.030

# Show dlg
dlg = gui.Dlg(title="Practice Block", pos=(800,200))
dlg.addField('participant number:')
dlg.addField('hash code:')
dlg.show()

if dlg.OK:
    subject_number = dlg.data[0]
    hashcode = dlg.data[1]
else:
    core.quit()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'HippSubfields7T'  # from the Builder filename that created this script
expInfo = {}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

#set paths
# Get the current working directory
cwd = os.getcwd()
print(cwd)
path_param = cwd + '/param/'
path_stim= cwd + '/Stimuli_New/'

id_subj=f'{subject_number}/'

# Create a folder for the subject's data if it doesn't already exist
subject_folder = cwd + '/data/' + id_subj
if not os.path.exists(subject_folder):
    os.makedirs(subject_folder)

BUTTON_BOX = False
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
id_block = 'practice'
beh_filename = subject_folder + os.sep + u'sub-%s_task-%s' % (subject_number,id_block)

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=cwd + '/7Tscreening.py',
    savePickle=True, saveWideText=True,
    dataFileName=beh_filename)
# save a log file for detail verbose info
logFile = logging.LogFile(beh_filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Set up the window and stimuli
# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
yes_text = visual.TextStim(win, text='YES', pos=(-0.2, -0.23), color='white', height=dist_labels_height)
no_text = visual.TextStim(win, text='NO', pos=(0.2, -0.23), color='white',height=dist_labels_height)
question_text = visual.TextStim(win, text='Can you recognize it?', pos=(0, 0.23), color='white',height=dist_labels_height)
instructions_screening = visual.TextStim(win, text="Welcome to the practice session! \n\n\n\n In this first part, you will be presented with a series of images and you will be asked to indicate whether or not you recognize the person or place represented in the image. \n\n If you recognize the person or place, \n press the LEFT ARROW to indicate 'YES'. \n\n If you do not recognize the person or place, \n press the RIGHT ARROW to indicate 'NO'. \n\n\n\n Press the SPACEBAR to start",
    color='white',
    height=0.025,
    alignText='center')
instructions_enc_practice = visual.TextStim(win, text='Now you will begin the experiment that you will perform in the fMRI scanner. \n\nJust a reminder:\n This first session of the experiment is composed of two tasks: \n\n Task 1: In this task, you will be presented with pairings of places and people. \nYour task is to imagine how plausible it is to find that person in that place, and evaluate it on a 4-item scale that ranges from "not plausible at all" to "highly plausible". \n To move on the scale, use the left and right arrows. \nOnce you have chosen your answer, confirm your response by pressing the down arrow. \n\n\n Task 2: In this task, numbers will be presented to you and you will need to decide whether the number is odd or even. \nTo respond, use the left arrow for odd numbers and the right arrow for even numbers.\n\n\n\n\n  Please let the experimenter know if you have any questions before we begin \n otherwise, press the SPACEBAR to start',
    color='white',
    alignText='center', 
    height = 0.02)
instructions_retr_practice = visual.TextStim(win, text="You will now see the stimuli that were shown to you earlier appear on the screen. \n\n When the target face/place is shown, your task is to try to remember the face/place associated. \n\n After a few seconds, the response options will appear on the screen. \n\nAnswer using keys '1', '2', or '3' corresponding to your choice. \n Press '4' if you do not remember the association. \n\n Please be aware: \n Try to remember the associated face/place when the target image is first presented alone on the screen. \nIf you only remember the association when the options are shown, \n select '4' to indicate that you did not remember the association in the first place. \n\n\n\n\n  Please let the experimenter know if you have any questions before we begin \n otherwise, press the SPACEBAR to start",
    color='white',
    alignText='center', 
    height = 0.02)
end_practice = visual.TextStim(win, text='Congratulations! \nYou have completed the practice session. \n\n\n\n Thank you for your participation!',
    color='white',
    alignText='center', 
    height = 0.04)
    
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

thisExp.addData('nSubj',subject_number)
thisExp.addData('Hashcode',hashcode)

# Set up the stimulus list
stim_list = []
y = 0
for stimulus_name in os.listdir(path_stim):
    if stimulus_name.endswith('c.jpg'):
        y = y+1
        stim_list.append(stimulus_name)

# Shuffle the stimulus list and make sure no category is presented more than 3 times in a row
random.shuffle(stim_list)
# Set up the response recording and timing
responses = []
rt = []
clock = core.Clock()
win.mouseVisible = False
continueRoutine = True 

# Show instructions
while continueRoutine:
    instructions_screening.draw()
    win.flip()
    key = event.waitKeys(keyList=['space', 'escape'])
    if 'space' in key:
        continueRoutine = False
    if 'escape' in key:
        core.quit()
    
# Present each stimulus and record responses and RT
for stim_file in stim_list:
    # Load the current stimulus image and display it
    stimulus_image = visual.ImageStim(win,size=stimulus_size_enc,interpolate=True)
    stimulus_image.setImage(os.path.join(path_stim,stim_file))
    stimulus_image.draw()
    yes_text.draw()
    no_text.draw()
    question_text.draw()
    win.flip()
    clock.reset()

    # Record the response and RT
    key = event.waitKeys(keyList=['left', 'right', 'escape'])
    rt.append(clock.getTime())
    if key[0] == 'left':
        response = '1'
    elif key[0] == 'right':
        response = '0'
    if 'escape' in key:
        break
    responses.append(response[0])

yes_indices_f = sorted([i for i, r in enumerate(responses) if r == '1' and stim_list[i].startswith('f')], key=lambda i: rt[i])
no_indices_f = sorted([i for i, r in enumerate(responses) if r == '0' and stim_list[i].startswith('f')], key=lambda i: rt[i])
yes_indices_p = sorted([i for i, r in enumerate(responses) if r == '1' and stim_list[i].startswith('p')], key=lambda i: rt[i])
no_indices_p = sorted([i for i, r in enumerate(responses) if r == '0' and stim_list[i].startswith('p')], key=lambda i: rt[i])
cat_number = y/2

# Save the response and RT data to a CSV file
screening_file = subject_folder + '/subj-%s_task-screening.csv' % (subject_number)
with open(screening_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Stimulus', 'Response', 'RT', 'Known Faces', 'Known Places'])  # Add column headers
    # Write the rows for the 'yes' items starting with 'f'
    for i in yes_indices_f:
        if i == yes_indices_f[0]:
            writer.writerow([stim_list[i], responses[i], rt[i], len(yes_indices_f), len(yes_indices_p)])
        else:
            writer.writerow([stim_list[i], responses[i], rt[i], '', ''])
    # Write the rows for the 'no' items starting with 'f'
    for i in no_indices_f:
        writer.writerow([stim_list[i], responses[i], rt[i]])
    # Write the rows for the 'yes' items starting with 'p'
    for i in yes_indices_p:
        writer.writerow([stim_list[i], responses[i], rt[i]])
    # Write the rows for the 'no' items starting with 'p'
    for i in no_indices_p:
        writer.writerow([stim_list[i], responses[i], rt[i]])

f_stimuli = []
p_stimuli = []
f_30 = []
p_30 = []
with open(screening_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0].startswith('f'):
            f_stimuli.append(row[0])
        elif row[0].startswith('p'):
            p_stimuli.append(row[0])

# Replace 'c' with 'a' to create the stimuli names
f_first_30a = [s.replace('c', 'a') for s in f_stimuli[:30]]
p_first_30a = [s.replace('c', 'a') for s in p_stimuli[:30]]
f_first_30b = [s.replace('c', 'b') for s in f_stimuli[:30]]
p_first_30b = [s.replace('c', 'b') for s in p_stimuli[:30]]

f_30 = f_first_30a + f_first_30b
p_30 = p_first_30a + p_first_30b
#15 stimuli for the practice block
f_practice = [s.replace('c', 'a') for s in f_stimuli[30:44]]
p_practice = [s.replace('c', 'a') for s in p_stimuli[30:44]]
# Add the first stimulus to f_practice with a 'b' instead of 'a'
first_f = f_stimuli[30].replace('c', 'b')
f_practice.append(first_f)
first_p = p_stimuli[30].replace('c', 'b')
p_practice.append(first_p)
random.shuffle(p_practice)
random.shuffle(f_practice)
pairings = list(zip(f_practice, p_practice))

# Define the column headers and data for the practice block
headers = ['nTrial', 'left_image', 'right_image', 'resp_duration']
enc_stimuli = []
resp_duration = [6, 7.5, 9, 6, 3, 4.5, 7.5, 3, 9, 4.5, 7.5, 3, 6, 4.5, 9] 
# Generate a list of random boolean values with the same length as 'pairings'
swap_flags = [random.choice([True, False]) for _ in range(len(pairings))]
# Swap the first and second element of the pairings if the corresponding flag is True
swapped_pairings = [(p[1], p[0]) if flag else p for p, flag in zip(pairings, swap_flags)]
# Create the stimuli list with the row values
for i, pair in enumerate(swapped_pairings):
    nTrial = i + 1
    left_image = pair[0]
    right_image = pair[1]
    duration = resp_duration[i]
    row = [nTrial, left_image, right_image, duration]
    enc_stimuli.append(row)

# Write the data to a CSV file
subject_param = path_param + '/' + id_subj
if not os.path.exists(subject_param):
    os.makedirs(subject_param)
filename_enc = subject_param + '/enc_practice.csv'
with open(filename_enc, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers) # write the header row
    writer.writerows(enc_stimuli) # write the data rows

#save data for the fMRI session
# Create a list of tuples combining faces and places
fMRI_stimuli = list(zip(f_30, p_30))
csv_fMRI_stimuli = path_param + id_subj + 'fMRI_stimlist.csv'
# Write the data to a CSV file with headers
with open(csv_fMRI_stimuli, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['faces', 'places'])
    writer.writerows(fMRI_stimuli)

###create the retrieval parameters file###
# Extract the left_image and right_image columns and swap them
swapped_stimuli = [[row[2], row[1]] for row in enc_stimuli]
# Extract the left_image and right_image columns from enc_stimuli
nonswapped_stimuli = [[row[1], row[2]] for row in enc_stimuli]
# Concatenate the original and swapped stimuli lists
all_stimuli = swapped_stimuli + nonswapped_stimuli
#shuffle the rows
random.shuffle(all_stimuli)

used_distractors = set()

def generate_distractor(row):
    category = row[1][0] # Extract the first letter of the second column
    category_stimuli = [r[1] for r in all_stimuli if r[1].startswith(category)]
    # Filter the stimuli by the category of the second column
    category_stimuli.remove(row[1]) # Remove the stimulus in the second column from the list
    if len(row)>2:
        category_stimuli.remove(row[2]) 
    available_distractors = set(category_stimuli) - used_distractors # Filter out already used distractors
    if not available_distractors: # If all distractors have been used, reset the used_distractors set
        used_distractors.clear()
        available_distractors = set(category_stimuli) - used_distractors
    distractor = random.choice(list(available_distractors)) # Choose a random stimulus from the remaining list
    while distractor[0:3] == row[1][0:3]:
        available_distractors -= set([distractor])  # Remove the current distractor from the set of available distractors
        if not available_distractors: # If all distractors used distractors.clear()
            used_distractors.clear()
            available_distractors = set(category_stimuli)
        distractor = random.choice(list(available_distractors))
    used_distractors.add(distractor) # Add the chosen distractor to the used_distractors set
    return distractor

# Create the response options (3 options)
for row in all_stimuli:
    distractor = generate_distractor(row)
    row.append(distractor)
    
for row in all_stimuli[:15]:
    distractor = generate_distractor(row)
    row.append(distractor)

for row in all_stimuli[15:23]:
    stname = row[1]
    if 'a' in stname:
        stname = stname.replace('a', 'b')
    elif 'b' in stname:
        stname = stname.replace('b', 'a')
    row.append(stname)

for row in all_stimuli[23:]:
    stname = row[2]
    if 'a' in stname:
        stname = stname.replace('a', 'b')
    elif 'b' in stname:
        stname = stname.replace('b', 'a')
    row.append(stname)

# Shuffle the rows avoiding direct repetitions of values
shuffled_rows = all_stimuli.copy()
while True:
    random.shuffle(shuffled_rows)
    if all(shuffled_rows[i][3] != shuffled_rows[i+1][3] for i in range(len(shuffled_rows)-1)):
        break

#create the retrieval parameters file
#set paths
input_file = path_param + '/param_retr.csv'
csv_file_enc = path_param + id_subj + 'enc_practice.csv'
csv_file_retr = path_param + id_subj + '/retr_practice.csv'

# Open the input and output files
with open(input_file, "r", encoding='utf-8-sig') as f_input, open(csv_file_retr, "w", newline='') as f_output:
    # Create a CSV reader and writer objects
    reader = csv.reader(f_input)
    writer = csv.writer(f_output)
    
    # Find the index of the columns to insert before
    header = next(reader)
    nTrial_index = header.index("nTrial")
    pos1_index = header.index("pos_1")
    
    # Insert the column headers for the new columns
    header[nTrial_index+1:nTrial_index+1] = ["cue", "target", "stim_2", "stim_3"]
    writer.writerow(header)
    
    # Write each row from the input file and insert the new columns with values from shuffled_rows
    for i, row in enumerate(reader, start=1):
        writer.writerow(row[:nTrial_index+1] + shuffled_rows[i-1] + row[pos1_index:])

continueRoutine = True
core.wait(0.1)
while continueRoutine:
    instructions_enc_practice.draw()
    win.flip()

    # Record the response and RT
    key = event.waitKeys(keyList=['space', 'escape'])
    if 'space' in key:
        continueRoutine = False
    if 'escape' in key:
        core.quit()

# Initialize components for Routine "dlg_1"
dlg_1Clock = core.Clock()
timer = core.Clock()

# Initialize components for Routine "Wait_Trigger"
Wait_TriggerClock = core.Clock()
scanner_message = visual.TextStim(win=win, name='scanner_message',
    text='Waiting for the scanner... \n\nThe task will start shortly\n\n\n\nPlease stay still',
    font='Open Sans',
    pos=central_pos, height=text_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "FixCross"
FixCrossClock = core.Clock()
FixationCross = visual.ShapeStim(
    win=win, name='FixationCross', vertices='cross',
    size=fixcross_size,
    ori=0.0, pos=central_pos, anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=components_color, fillColor=components_color,
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Stim_Pairs"
Stim_PairsClock = core.Clock()
Left_side = visual.ImageStim(
    win=win,
    name='Left_side', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=left_img_pos, size=stimulus_size_enc,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Right_side = visual.ImageStim(
    win=win,
    name='Right_side', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=right_img_pos, size=stimulus_size_enc,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "Enc_Task"
Enc_TaskClock = core.Clock()
Encoding_Task = visual.TextStim(win=win, name='Encoding_Task',
    text='',
    font='Open Sans',
    pos=central_pos, height=text_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

ratingScale = visual.RatingScale(
    win, pos=(0,0), choices=['\nnot at all', '\nsomewhat \n implausible','\nsomewhat \n plausible', '\nhighly \nplausible'], low=1, high=4, markerStart=1, marker = 'circle',
    stretch=2, noMouse = True, textColor = components_color, tickHeight = 3, showAccept = False)
ratingScale.marker.setSize(marker_size)  # Set the marker size

# Initialize components for Routine "Instructions_Dst"
Instructions_DstClock = core.Clock()
distractor_inst = visual.TextStim(win=win, name='distractor_inst',
    text='ODD-EVEN JUDGEMENT\n\nRemember:\nLeft - Odd \nRight - Even\n',
    font='Open Sans',
    pos=central_pos, height=text_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
odd_txt = visual.TextStim(win=win, name='odd_txt',
    text='ODD',
    font='Open Sans',
    pos=(-0.25, 0), height=dist_labels_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
even_txt = visual.TextStim(win=win, name='even_txt',
    text='EVEN',
    font='Open Sans',
    pos=(0.25, 0), height=dist_labels_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Distractor_task"
Distractor_taskClock = core.Clock()
number = visual.TextStim(win=win, name='number',
    text='',
    font='Open Sans',
    pos=central_pos, height=number_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
R2 = keyboard.Keyboard()

# Initialize components for Routine "Result_Dst"
Result_DstClock = core.Clock()
Task_Results_2 = visual.TextStim(win=win, name='Task_Results_2',
    text='',
    font='Open Sans',
    pos=central_pos, height=text_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Retrieval"
RetrievalClock = core.Clock()
Cue = visual.ImageStim(
    win=win,
    name='Cue', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.27), size=(0.3,0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
img_1 = visual.ImageStim(
    win=win,
    name='img_1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=stimulus_size_retr,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
img_2 = visual.ImageStim(
    win=win,
    name='img_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=stimulus_size_retr,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
img_3 = visual.ImageStim(
    win=win,
    name='img_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=stimulus_size_retr,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
Opt_1 = visual.TextStim(win=win, name='Opt_1',
    text='1',
    font='Open Sans',
    pos=opt1label_pos, height=optlabel_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
Opt_2 = visual.TextStim(win=win, name='Opt_2',
    text='2',
    font='Open Sans',
    pos=opt2label_pos, height=optlabel_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
Opt_3 = visual.TextStim(win=win, name='Opt_3',
    text='3',
    font='Open Sans',
    pos=opt3label_pos, height=optlabel_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
Opt_4 = visual.TextStim(win=win, name='Opt_4',
    text='4\n',
    font='Open Sans',
    pos=opt4label_pos, height=optlabel_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
Opt4_text = visual.TextStim(win=win, name='Opt4_text',
    text="I don't remember",
    font='Open Sans',
    pos=opt4_pos, height=opt4_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
Blank = visual.TextStim(win=win, name='Blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "End_Block"
End_BlockClock = core.Clock()
block_end_screen = visual.TextStim(win=win, name='block_end_screen',
    text='This block is finished!\n\nWait for instructions...\n\n',
    font='Open Sans',
    pos=(0, 0), height=text_height, wrapWidth=None, ori=0.0, 
    color=components_color, colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
    
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

### TASK STARTING FROM HERE ###
## ------Prepare to start Routine "dlg_1"-------
continueRoutine = True
# update component parameters for each repeat
# Hide the mouse cursor
win.mouseVisible = False
# keep track of which components have finished
dlg_1Components = []
for thisComponent in dlg_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
dlg_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

## -------Run Routine "dlg_1"-------
while continueRoutine:
    # get current time
    t = dlg_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=dlg_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in dlg_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "dlg_1"-------
for thisComponent in dlg_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "dlg_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Wait_Trigger"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Wait_TriggerComponents = [scanner_message, key_resp]
for thisComponent in Wait_TriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Wait_TriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait_Trigger"-------
while continueRoutine:
    # get current time
    t = Wait_TriggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Wait_TriggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *scanner_message* updates
    if scanner_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scanner_message.frameNStart = frameN  # exact frame index
        scanner_message.tStart = t  # local t and not account for scr refresh
        scanner_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scanner_message, 'tStartRefresh')  # time at next scr refresh
        scanner_message.setAutoDraw(True)
        # *block_end_screen* updates
    if scanner_message.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > scanner_message.tStartRefresh + endscreen_duration-frameTolerance:
            # keep track of stop time/frame for later
            scanner_message.tStop = t  # not accounting for scr refresh
            scanner_message.frameNStop = frameN  # exact frame index
            win.timeOnFlip(scanner_message, 'tStopRefresh')  # time at next scr refresh
            scanner_message.setAutoDraw(False)
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

start_time = timer.getTime()
# -------Ending Routine "Wait_Trigger"-------
for thisComponent in Wait_TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('scanner_message.started', scanner_message.tStartRefresh)

thisExp.nextEntry()
# the Routine "Wait_Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_enc = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(filename_enc),
    seed=None, name='trials_enc')
thisExp.addLoop(trials_enc)  # add the loop to the experiment
thisTrials_enc = trials_enc.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_enc.rgb)
if thisTrials_enc != None:
    for paramName in thisTrials_enc:
        exec('{} = thisTrials_enc[paramName]'.format(paramName))

for thisTrials_enc in trials_enc:
    currentLoop = trials_enc
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_enc.rgb)
    if thisTrials_enc != None:
        for paramName in thisTrials_enc:
            exec('{} = thisTrials_enc[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(fixcross_duration)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCrossComponents = [FixationCross]
    for thisComponent in FixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCross* updates
        if FixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCross.frameNStart = frameN  # exact frame index
            FixationCross.tStart = t  # local t and not account for scr refresh
            FixationCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCross, 'tStartRefresh')  # time at next scr refresh
            FixationCross.setAutoDraw(True)
        if FixationCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCross.tStartRefresh + fixcross_duration-frameTolerance:
                # keep track of stop time/frame for later
                FixationCross.tStop = t  # not accounting for scr refresh
                FixationCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCross, 'tStopRefresh')  # time at next scr refresh
                FixationCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross"-------
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_enc.addData('FixationCross.started', FixationCross.tStartRefresh)
    
    # ------Prepare to start Routine "Stim_Pairs"-------
    continueRoutine = True
    routineTimer.add(stim_duration)
    # update component parameters for each repeat
    # Get the participant's response for the block number
    
    im_l = path_stim + left_image;
    im_r = path_stim + right_image;
    
    #dur_images = 5;#duration*60; #60fps 
    
    thisExp.addData('im_l',left_image)
    thisExp.addData('im_r',right_image)
    
    Left_side.setImage(im_l)
    Right_side.setImage(im_r)
    # keep track of which components have finished
    Stim_PairsComponents = [Left_side, Right_side]
    for thisComponent in Stim_PairsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Stim_PairsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Stim_Pairs"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Stim_PairsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Stim_PairsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Left_side* updates
        if Left_side.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Left_side.frameNStart = frameN  # exact frame index
            Left_side.tStart = t  # local t and not account for scr refresh
            Left_side.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Left_side, 'tStartRefresh')  # time at next scr refresh
            Left_side.setAutoDraw(True)
        if Left_side.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Left_side.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                Left_side.tStop = t  # not accounting for scr refresh
                Left_side.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Left_side, 'tStopRefresh')  # time at next scr refresh
                Left_side.setAutoDraw(False)
        
        # *Right_side* updates
        if Right_side.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Right_side.frameNStart = frameN  # exact frame index
            Right_side.tStart = t  # local t and not account for scr refresh
            Right_side.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Right_side, 'tStartRefresh')  # time at next scr refresh
            Right_side.setAutoDraw(True)
        if Right_side.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Right_side.tStartRefresh + stim_duration-frameTolerance:
                # keep track of stop time/frame for later
                Right_side.tStop = t  # not accounting for scr refresh
                Right_side.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Right_side, 'tStopRefresh')  # time at next scr refresh
                Right_side.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Stim_PairsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Stim_Pairs"-------
    for thisComponent in Stim_PairsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_enc.addData('Left_side.started', Left_side.tStartRefresh)
    trials_enc.addData('Right_side.started', Right_side.tStartRefresh)
    
    # ------Prepare to start Routine "Enc_Task"-------
    continueRoutine = True
    # update component parameters for each repeat
    Encoding_Task.setText('How plausible is this pair?\n\n')
    event.clearEvents('keyboard')

    # keep track of which components have finished
    Enc_TaskComponents = [Encoding_Task, ratingScale]
    for thisComponent in Enc_TaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Enc_TaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    ratingScale.reset()
     

    response = None
    rt = None
    # -------Run Routine "Enc_Task"-------
    while continueRoutine:
        # get current time
        t = Enc_TaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Enc_TaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        
        # *Encoding_Task* updates
        if Encoding_Task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Encoding_Task.frameNStart = frameN  # exact frame index
            Encoding_Task.tStart = t  # local t and not account for scr refresh
            Encoding_Task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Encoding_Task, 'tStartRefresh')  # time at next scr refresh
            Encoding_Task.setAutoDraw(True)
        if Encoding_Task.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Encoding_Task.tStartRefresh + resp_duration-frameTolerance:
                # keep track of stop time/frame for later
                Encoding_Task.tStop = t  # not accounting for scr refresh
                Encoding_Task.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Encoding_Task, 'tStopRefresh')  # time at next scr refresh
                Encoding_Task.setAutoDraw(False)
        
        # *rating* updates
        if ratingScale.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ratingScale.frameNStart = frameN  # exact frame index
            ratingScale.tStart = t  # local t and not account for scr refresh
            ratingScale.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ratingScale, 'tStartRefresh')  # time at next scr refresh
            ratingScale.setAutoDraw(True)
            win.flip()
            # add timestamp to datafile
            
        if ratingScale.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ratingScale.tStartRefresh + resp_duration-frameTolerance:
                # keep track of stop time/frame for later
                ratingScale.tStop = t  # not accounting for scr refresh
                ratingScale.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                ratingScale.setAutoDraw(False)
        
        # initialize previous button state
        prev_state = 0
        curr_state = 0
        if BUTTON_BOX:
            button_state = button_thread.button_state
            prev_state = button_state['state']
            while True:
                button_state = button_thread.button_state
                curr_state = button_state['state']
                # check for change from 0 to 1 in left button
                if curr_state[2] == 1 and prev_state[2] == 0:
                    ratingScale.markerPlacedAt -= 1
                    ratingScale.draw()
                    if ratingScale.markerPlacedAt < 0:
                        ratingScale.markerPlacedAt = 0  # Clamp to the lower boundary
                # check for change from 0 to 1 in right button
                elif curr_state[0] == 1 and prev_state[0] == 0:
                    ratingScale.markerPlacedAt += 1
                    ratingScale.draw()
                    if ratingScale.markerPlacedAt > 3:
                        ratingScale.markerPlacedAt = 3  # Clamp to the upper boundary
                # check for down button
                elif curr_state[3] == 1:
                    response = ratingScale.markerPlacedAt + 1
                    rt = ratingScale.getRT()
                    ratingScale.noResponse = False
                    logging.log('Button press: {}\n'.format(response), level=logging.DATA)
                    break
                prev_state = curr_state
        else:
            keys = event.getKeys(keyList=['left', 'right', 'down'])
            if keys:
                key = keys[0]
                if key == 'left':
                    ratingScale.markerPlacedAt -= 1
                    ratingScale.draw()
                    if ratingScale.markerPlacedAt < 0:
                        ratingScale.markerPlacedAt = 0  # Clamp to the lower boundary
                elif key == 'right':
                    ratingScale.markerPlacedAt += 1
                    ratingScale.draw()
                    if ratingScale.markerPlacedAt > 3:
                        ratingScale.markerPlacedAt = 3  # Clamp to the lower boundary
                elif key == 'down':
                    response = ratingScale.markerPlacedAt + 1
                    rt = ratingScale.getRT()
                    ratingScale.noResponse = False
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Enc_TaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "Enc_Task"-------
    for thisComponent in Enc_TaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_enc.addData('Encoding_Task.started', Encoding_Task.tStartRefresh)
    thisExp.addData("resp.Rating", response)
    thisExp.addData("rt.Rating", rt)
    # the Routine "Enc_Task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_enc'

### DISTRACTOR TASK ####
# ------Prepare to start Routine "Instructions_Dst"-------
continueRoutine = True
routineTimer.add(dst_inst_duration)
# update component parameters for each repeat
# keep track of which components have finished
Instructions_DstComponents = [distractor_inst]
for thisComponent in Instructions_DstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instructions_DstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions_Dst"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Instructions_DstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instructions_DstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *distractor_inst* updates
    if distractor_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        distractor_inst.frameNStart = frameN  # exact frame index
        distractor_inst.tStart = t  # local t and not account for scr refresh
        distractor_inst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(distractor_inst, 'tStartRefresh')  # time at next scr refresh
        distractor_inst.setAutoDraw(True)
    if distractor_inst.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > distractor_inst.tStartRefresh + dst_inst_duration-frameTolerance:
            # keep track of stop time/frame for later
            distractor_inst.tStop = t  # not accounting for scr refresh
            distractor_inst.frameNStop = frameN  # exact frame index
            win.timeOnFlip(distractor_inst, 'tStopRefresh')  # time at next scr refresh
            distractor_inst.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_DstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_Dst"-------
for thisComponent in Instructions_DstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('distractor_inst.started', distractor_inst.tStartRefresh)

# set up handler to look after randomisation of conditions etc
trials_dst = data.TrialHandler(nReps = 200, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_dst')
thisExp.addLoop(trials_dst)  # add the loop to the experiment
thisTrials_dst = trials_dst.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_dst.rgb)
if thisTrials_dst != None:
    for paramName in thisTrials_dst:
        exec('{} = thisTrials_dst[paramName]'.format(paramName))

# clear the keyboard buffer
nb = 0
nCorr = 0;
wm_perf = 0;
x = 0;
event.clearEvents(eventType='keyboard')
for thisTrials_dst in trials_dst:
    currentLoop = trials_dst
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_dst.rgb)
    if thisTrials_dst != None:
        for paramName in thisTrials_dst:
            exec('{} = thisTrials_dst[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Distractor_task"-------
    continueRoutine = True
    # update component parameters for each repeat
    if trials_dst.thisN == 0: # only on the first iteration,
      loop_timer = core.Clock() # start a new timer
      
    rand_number = randint(1,99);
    
    thisExp.addData('rand_number',rand_number)
    number.setText(rand_number)
    R2.keys = []
    R2.rt = []
    _R2_allKeys = []
    # keep track of which components have finished
    Distractor_taskComponents = [number, R2]
    for thisComponent in Distractor_taskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Distractor_taskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    prev_button_state = 0 
    # -------Run Routine "Distractor_task"-------
    while continueRoutine:
        # get current time
        t = Distractor_taskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Distractor_taskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        if loop_timer.getTime() >= dst_task_duration:
            continueRoutine = False
            trials_dst.finished = True
        
        # *number* updates
        if number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            number.frameNStart = frameN  # exact frame index
            number.tStart = t  # local t and not account for scr refresh
            number.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(number, 'tStartRefresh')  # time at next scr refresh
            number.setAutoDraw(True)
            odd_txt.setAutoDraw(True)
            even_txt.setAutoDraw(True)
    
        # *R2* updates
        win.callOnFlip(R2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(R2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        keys = event.getKeys()
        
        # dist_task response
        if BUTTON_BOX:
            while True: 
                button_state = button_thread.button_state
        else:
            if len(keys) > 0:
                x = x + 1
                R2.keys = keys[0]
                R2.rt = Distractor_taskClock.getTime() - number.tStart
                if R2.keys == 'left' and (rand_number % 2) == 0:
                    wm_perf += 0
                elif R2.keys == 'left' and (rand_number % 2) != 0:
                    wm_perf += 1
                elif R2.keys == 'right' and (rand_number % 2) == 0:
                    wm_perf += 1
                elif R2.keys == 'right' and (rand_number % 2) != 0:
                    wm_perf += 0
                else:
                    wm_perf += 0
                # a response ends the routine
                continueRoutine = False
                
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Distractor_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Distractor_task"-------
    for thisComponent in Distractor_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            odd_txt.setAutoDraw(False)
            even_txt.setAutoDraw(False)
    
    # check responses
    if R2.keys in ['', [], None]:  # No response was made
        R2.keys = None
    trials_dst.addData('R2.keys',R2.keys)
    if R2.keys != None:  # we had a response
        trials_dst.addData('R2.rt', R2.rt)
    
    # the Routine "Distractor_task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# 'trials_dst' completed 

# ------Prepare to start Routine "Result_Dst"-------
continueRoutine = True
routineTimer.add(dst_results_duration)
# update component parameters for each repeat
if wm_perf == 0:
    nCorr = 0
else:
    nCorr = (wm_perf/(x))*100


thisExp.addData('nCorr',wm_perf)
thisExp.addData('%_nCorr',nCorr)
thisExp.addData('nTrials',x)
feedback_txt = "You completed %i trials and got %i percent correct. \n\n This block is finished! \n\n Wait for instructions... " %((x),nCorr)
Task_Results_2.setText(feedback_txt)
# keep track of which components have finished
Result_DstComponents = [Task_Results_2]
for thisComponent in Result_DstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Result_DstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Result_Dst"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Result_DstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Result_DstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Task_Results_2* updates
    if Task_Results_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Task_Results_2.frameNStart = frameN  # exact frame index
        Task_Results_2.tStart = t  # local t and not account for scr refresh
        Task_Results_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Task_Results_2, 'tStartRefresh')  # time at next scr refresh
        Task_Results_2.setAutoDraw(True)
    if Task_Results_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Task_Results_2.tStartRefresh + dst_results_duration-frameTolerance:
            # keep track of stop time/frame for later
            Task_Results_2.tStop = t  # not accounting for scr refresh
            Task_Results_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Task_Results_2, 'tStopRefresh')  # time at next scr refresh
            Task_Results_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Result_DstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Result_Dst"-------
for thisComponent in Result_DstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

thisExp.addData('Task_Results_2.started', Task_Results_2.tStartRefresh)

### RETRIEVAL TASK ###
continueRoutine = True 

# Show instructions
while continueRoutine:
    instructions_retr_practice.draw()
    win.flip()
    key = event.waitKeys(keyList=['space', 'escape'])
    if 'space' in key:
        continueRoutine = False
    if 'escape' in key:
        core.quit()

# ------Prepare to start Routine "Wait_Trigger"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Wait_TriggerComponents = [scanner_message, key_resp]
for thisComponent in Wait_TriggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Wait_TriggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait_Trigger"-------
while continueRoutine:
    # get current time
    t = Wait_TriggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Wait_TriggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *scanner_message* updates
    if scanner_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        scanner_message.frameNStart = frameN  # exact frame index
        scanner_message.tStart = t  # local t and not account for scr refresh
        scanner_message.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(scanner_message, 'tStartRefresh')  # time at next scr refresh
        scanner_message.setAutoDraw(True)
        # *block_end_screen* updates
    if scanner_message.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > scanner_message.tStartRefresh + endscreen_duration-frameTolerance:
            # keep track of stop time/frame for later
            scanner_message.tStop = t  # not accounting for scr refresh
            scanner_message.frameNStop = frameN  # exact frame index
            win.timeOnFlip(scanner_message, 'tStopRefresh')  # time at next scr refresh
            scanner_message.setAutoDraw(False)
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_TriggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait_Trigger"-------
for thisComponent in Wait_TriggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('scanner_message.started', scanner_message.tStartRefresh)

# the Routine "Wait_Trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

## -------Starting Routine "Retrieval_task"-------

# set up handler to look after randomisation of conditions etc
trials_ret = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(csv_file_retr),
    seed=None, name='trials_ret')
thisExp.addLoop(trials_ret)  # add the loop to the experiment
thisTrials_ret = trials_ret.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_ret.rgb)
if thisTrials_ret != None:
    for paramName in thisTrials_ret:
        exec('{} = thisTrials_ret[paramName]'.format(paramName))

num_correct = 0

for thisTrials_ret in trials_ret:
    currentLoop = trials_ret
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_ret.rgb)
    if thisTrials_ret != None:
        for paramName in thisTrials_ret:
            exec('{} = thisTrials_ret[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FixCross"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    FixCrossComponents = [FixationCross]
    for thisComponent in FixCrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FixCrossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FixCross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FixCrossClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FixCrossClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixationCross* updates
        if FixationCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationCross.frameNStart = frameN  # exact frame index
            FixationCross.tStart = t  # local t and not account for scr refresh
            FixationCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCross, 'tStartRefresh')  # time at next scr refresh
            FixationCross.setAutoDraw(True)
        if FixationCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixationCross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FixationCross.tStop = t  # not accounting for scr refresh
                FixationCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixationCross, 'tStopRefresh')  # time at next scr refresh
                FixationCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixCrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FixCross"-------
    for thisComponent in FixCrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_ret.addData('fixation_cross.started', FixationCross.tStartRefresh)
    
    # ------Prepare to start Routine "Retrieval"-------
    continueRoutine = True
    # update component parameters for each repeat
    response = None

    cue_img = path_stim + cue;
    target_img = path_stim + target;
    image_2 = path_stim + stim_2;
    image_3 = path_stim + stim_3;

    # Extract only the filename from the full path
    cue_image = os.path.basename(cue_img)
    target_image = os.path.basename(target_img)
    image2 = os.path.basename(image_2)
    image3 = os.path.basename(image_3)
    
    thisExp.addData('cue',cue_image)
    thisExp.addData('target',target_image)
    thisExp.addData('pos_target',pos_1)
    thisExp.addData('option_2',image2)
    thisExp.addData('pos_opt2',pos_2)
    thisExp.addData('option_3',image3)
    thisExp.addData('pos_opt3',pos_3)
    Cue.setImage(cue_img)
    img_1.setPos(pos_1)
    img_1.setImage(target_img)
    img_2.setPos(pos_2)
    img_2.setImage(image_2)
    img_3.setPos(pos_3)
    img_3.setImage(image_3)

    # keep track of which components have finished
    RetrievalComponents = [Cue, img_1, img_2, img_3, Opt_1, Opt_2, Opt_3, Opt_4, Opt4_text]
    for thisComponent in RetrievalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RetrievalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Retrieval"-------
    response_retr = None
    rt_retr = None
    while continueRoutine:
        # get current time
        t = RetrievalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RetrievalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
        # Run 'Each Frame' code from code_retr_task
        response_map = {'left': 1, 'up': 2, 'right': 3, 'down': 4}
        keys = event.getKeys()
        # get the correct response for this trial
        corr_resp = thisTrials_ret['corr_resp']
        if img_1.tStart: 
            if len(keys) > 0:
                if keys[0] in response_map:
                    response_retr = response_map[keys[0]]
                    rt_retr =  RetrievalClock.getTime() - img_1.tStart
                    if response_retr == int(corr_resp):
                        num_correct += 1
                    
        # *Cue* updates
        if Cue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cue.frameNStart = frameN  # exact frame index
            Cue.tStart = t  # local t and not account for scr refresh
            Cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cue, 'tStartRefresh')  # time at next scr refresh
            Cue.setAutoDraw(True)
        if Cue.status == STARTED:
            if bool(img_1.status==FINISHED):
                # keep track of stop time/frame for later
                Cue.tStop = t  # not accounting for scr refresh
                Cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cue, 'tStopRefresh')  # time at next scr refresh
                Cue.setAutoDraw(False)
        
        # *img_1* updates
        if img_1.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            img_1.frameNStart = frameN  # exact frame index
            img_1.tStart = t  # local t and not account for scr refresh
            img_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_1, 'tStartRefresh')  # time at next scr refresh
            img_1.setAutoDraw(True)
        if img_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_1.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                img_1.tStop = t  # not accounting for scr refresh
                img_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_1, 'tStopRefresh')  # time at next scr refresh
                img_1.setAutoDraw(False)
        
        # *img_2* updates
        if img_2.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            img_2.frameNStart = frameN  # exact frame index
            img_2.tStart = t  # local t and not account for scr refresh
            img_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_2, 'tStartRefresh')  # time at next scr refresh
            img_2.setAutoDraw(True)
        if img_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_2.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                img_2.tStop = t  # not accounting for scr refresh
                img_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_2, 'tStopRefresh')  # time at next scr refresh
                img_2.setAutoDraw(False)
        
        # *img_3* updates
        if img_3.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            img_3.frameNStart = frameN  # exact frame index
            img_3.tStart = t  # local t and not account for scr refresh
            img_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_3, 'tStartRefresh')  # time at next scr refresh
            img_3.setAutoDraw(True)
        if img_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_3.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                img_3.tStop = t  # not accounting for scr refresh
                img_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_3, 'tStopRefresh')  # time at next scr refresh
                img_3.setAutoDraw(False)
        
        # *Opt_1* updates
        if Opt_1.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            Opt_1.frameNStart = frameN  # exact frame index
            Opt_1.tStart = t  # local t and not account for scr refresh
            Opt_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Opt_1, 'tStartRefresh')  # time at next scr refresh
            Opt_1.setAutoDraw(True)
        if Opt_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Opt_1.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                Opt_1.tStop = t  # not accounting for scr refresh
                Opt_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Opt_1, 'tStopRefresh')  # time at next scr refresh
                Opt_1.setAutoDraw(False)
        
        # *Opt_2* updates
        if Opt_2.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            Opt_2.frameNStart = frameN  # exact frame index
            Opt_2.tStart = t  # local t and not account for scr refresh
            Opt_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Opt_2, 'tStartRefresh')  # time at next scr refresh
            Opt_2.setAutoDraw(True)
        if Opt_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Opt_2.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                Opt_2.tStop = t  # not accounting for scr refresh
                Opt_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Opt_2, 'tStopRefresh')  # time at next scr refresh
                Opt_2.setAutoDraw(False)
        
        # *Opt_3* updates
        if Opt_3.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            Opt_3.frameNStart = frameN  # exact frame index
            Opt_3.tStart = t  # local t and not account for scr refresh
            Opt_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Opt_3, 'tStartRefresh')  # time at next scr refresh
            Opt_3.setAutoDraw(True)
        if Opt_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Opt_3.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                Opt_3.tStop = t  # not accounting for scr refresh
                Opt_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Opt_3, 'tStopRefresh')  # time at next scr refresh
                Opt_3.setAutoDraw(False)
        
        # *Opt_4* updates
        if Opt_4.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            Opt_4.frameNStart = frameN  # exact frame index
            Opt_4.tStart = t  # local t and not account for scr refresh
            Opt_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Opt_4, 'tStartRefresh')  # time at next scr refresh
            Opt_4.setAutoDraw(True)
        if Opt_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Opt_4.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                Opt_4.tStop = t  # not accounting for scr refresh
                Opt_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Opt_4, 'tStopRefresh')  # time at next scr refresh
                Opt_4.setAutoDraw(False)
        
        # *Opt4_text* updates
        if Opt4_text.status == NOT_STARTED and tThisFlip >= cue_duration-frameTolerance:
            # keep track of start time/frame for later
            Opt4_text.frameNStart = frameN  # exact frame index
            Opt4_text.tStart = t  # local t and not account for scr refresh
            Opt4_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Opt4_text, 'tStartRefresh')  # time at next scr refresh
            Opt4_text.setAutoDraw(True)
        if Opt4_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Opt4_text.tStartRefresh + options_duration-frameTolerance:
                # keep track of stop time/frame for later
                Opt4_text.tStop = t  # not accounting for scr refresh
                Opt4_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Opt4_text, 'tStopRefresh')  # time at next scr refresh
                Opt4_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetrievalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Retrieval"-------
    for thisComponent in RetrievalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # Run 'End Routine' code from code_retr_task
    thisExp.addData("Resp", response_retr)
    thisExp.addData("RT", rt_retr)
    
    trials_ret.addData('cue.started', Cue.tStartRefresh)
    trials_ret.addData('options.started', img_1.tStartRefresh)
 
    # the Routine "Retrieval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [Blank]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Blank* updates
        if Blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Blank.frameNStart = frameN  # exact frame index
            Blank.tStart = t  # local t and not account for scr refresh
            Blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Blank, 'tStartRefresh')  # time at next scr refresh
            Blank.setAutoDraw(True)
        if Blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Blank.tStartRefresh + resp_duration-frameTolerance:
                # keep track of stop time/frame for later
                Blank.tStop = t  # not accounting for scr refresh
                Blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Blank, 'tStopRefresh')  # time at next scr refresh
                Blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_ret.addData('blank.started', Blank.tStartRefresh)
    # the Routine "blank" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_ret'


# ------Prepare to start Routine "End_Block"-------
continueRoutine = True
routineTimer.add(endscreen_duration)
# update component parameters for each repeat
# keep track of which components have finished
End_BlockComponents = [block_end_screen]
for thisComponent in End_BlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
End_BlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End_Block"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = End_BlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=End_BlockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *block_end_screen* updates
    if block_end_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        block_end_screen.frameNStart = frameN  # exact frame index
        block_end_screen.tStart = t  # local t and not account for scr refresh
        block_end_screen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(block_end_screen, 'tStartRefresh')  # time at next scr refresh
        block_end_screen.setAutoDraw(True)
    if block_end_screen.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > block_end_screen.tStartRefresh + endscreen_duration-frameTolerance:
            # keep track of stop time/frame for later
            block_end_screen.tStop = t  # not accounting for scr refresh
            block_end_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(block_end_screen, 'tStopRefresh')  # time at next scr refresh
            block_end_screen.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in End_BlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# calculate the accuracy
accuracy = num_correct/30*100 #/ len(trials_ret.trialList)
print('the number of stimuli for the screening session is:', y)
how_many_known = "known faces: %i/%i. known places: %i/%i" %(len(yes_indices_f),cat_number,len(yes_indices_p),cat_number)
print(how_many_known)
if len(yes_indices_f) < 30:
    print('WARNING! known faces < 30')
if len(yes_indices_p) < 30:
    print('WARNING! known places < 30')
print('WM performance:', nCorr)
print('Number of remembered pairings:', num_correct)
print('Accuracy %:',accuracy)
if accuracy < 75:
    print('WARNING! Performance threshold NOT REACHED')

thisExp.addData('numCorr',num_correct)
thisExp.addData('Accuracy',accuracy)

# -------Ending Routine "End_Block"-------
for thisComponent in End_BlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('block_end_screen.started', block_end_screen.tStartRefresh)

### END PRACTICE SESSION ###
continueRoutine = True 

# Show instructions
while continueRoutine:
    end_practice.draw()
    win.flip()
    key = event.waitKeys(keyList=['space', 'escape'])
    if 'space' in key:
        continueRoutine = False
    if 'escape' in key:
        core.quit()
        
# --- End experiment --- # 
end_time = timer.getTime()
task_dur = end_time - start_time
task_minutes = task_dur/60
#print("Experiment duration: ", task_dur)
print("Experiment duration in min: ", task_minutes)

thisExp.addData('nSubj',subject_number)
thisExp.addData('Hashcode',hashcode)
thisExp.addData('Block',id_block)
# --- End experiment ---

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(beh_filename+'.csv', delim='auto')
thisExp.saveAsPickle(beh_filename)
logging.flush()

# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()


# Close the window and exit
win.close()