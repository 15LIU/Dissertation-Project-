# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:53:58 2022

"""

#%%
"ENCODING LISTS RANDOMIZATION"
"Clear all variables before running using %reset -f"
%reset -f

#%%
"generate two lists of stimuli, faces and places; with each face/place having two different shots (a and b)"

#%reset -f #run this line to delete all variables

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import random
import csv
import os

nsubj = 3

parameters_path = 'C:/Users/eleonorm/OneDrive - University of Glasgow/Desktop/practice_block/param/'
outputfolder_path = r'C:\Users\eleonorm\OneDrive - University of Glasgow\Desktop\practice_block\param_fMRI-session'

outputfile_path = os.path.join(outputfolder_path, str(nsubj)) 
if not os.path.exists(outputfile_path):
    os.mkdir(outputfile_path)

#
nstim=60;
cnt=0;
chk=0;

input_file = parameters_path + str(nsubj) + '/fMRI_stimlist.csv'

"Read the csv file containing the stimuli names for the fMRI session"
"and create different lists for faces and places"
facelist = []
placelist = []
with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    #skip header
    next(csv_reader)
    for row in csv_reader:
        facelist.append(row[0])
        placelist.append(row[1])


        
while chk!=nstim:
    stimpairs = []
    tmpfacstim = []
    tmpplcstim = []
    newListF = []
    newListP = []
    newListMrg = []
    
    "Randomly pair faces and places, but such that a certain face-place"
    "combination (i.e. face1 - place 2) only occurs once, regardless of shots;"
    "sample without replacement"
    rows = 60
    cols = 2
    stimpairs=[[0 for _ in range(cols)] for _ in range(rows)]
    
            
    random.shuffle(facelist)
    random.shuffle(placelist) 

    idx= list(range(0,nstim,2));

    for sp in range(0,int(nstim)):
        stimpairs[sp][0]=facelist[sp]
        stimpairs[sp][1]=placelist[sp]

    #shuffle rows
    np.random.shuffle(stimpairs)
    
    "Check that no identical stimulus pairings occur"
    for c in range(0,nstim):
        tmpfacstm=str(stimpairs[c][0])
        tmpfacstim.append(tmpfacstm)
        tmpplcstm=str(stimpairs[c][1])
        tmpplcstim.append(tmpplcstm)
    newListF = [string[0:-5] for string in tmpfacstim]
    newListP = [string[0:-5] for string in tmpplcstim]
    
    #merge faces and places and transform in dataframe
    newListMrg = np.column_stack((newListF, newListP))
    dfnl = pd.DataFrame(newListMrg)
    dfnl.columns = ['Face', 'Place']
         
    #check number of unique pairings (discounting a/b); if there are less than 60 then go back and re-run
    chklst = dfnl.apply(lambda x: ''.join(x.dropna().astype(str)),axis=1)
    #create a new dictionary with the element of 'chklst' (dictionaries cannot have duplicates, so it will remove them)
    chk = len(list(dict.fromkeys(chklst)))
    print(chk)
    if chk!=60:
        print('WARNING! the unique pairings are less than 60')
    
        
        
    "shuffle the stimuli (mantaining an equal number of stimulus types presented to L and R hemifield)"  
    #transform the variable stimpairs from a list to an array
    stimpairs_array = np.array(stimpairs)     
    #determine the halfway point of the array's first dimension (i.e., number of rows)
    halfway = stimpairs_array.shape[0]//2
    #slice the array into two halves
    first_half = stimpairs_array[:halfway]
    second_half = stimpairs_array[halfway:]
    #swap the columns of the second half of the rows
    second_half_swapped = second_half[:,::-1]
    #concatenate the two halves back together
    stimpairs_swapped = np.concatenate([first_half, second_half_swapped], axis=0)
    #shuffle rows with constrain (no more than 3 consecutive p/f)
    while True:
        np.random.shuffle(stimpairs_swapped)
        if all([stimpairs_swapped[i,0][0] != stimpairs_swapped[i+1,0][0] or stimpairs_swapped[i+1,0][0] != stimpairs_swapped[i+2,0][0] or stimpairs_swapped[i+2,0][0] != stimpairs_swapped[i+3,0][0] for i in range(len(stimpairs_swapped)-3)]):
            break
   
    #transform in dataframe
    rnd_stimpairs = pd.DataFrame(stimpairs_swapped)
    rnd_stimpairs.columns = ['left_image', 'right_image']
    rnd_stimpairs.index.name = 'nTrial'

    "save the stimuli pairs array shuffled"    
    rnd_stimpairs.to_csv(outputfile_path + '/stimpairslist.csv')
    
    "divide into 4 different files (4 blocks x 15 trials) and reindex them"
    encoding_blocks = rnd_stimpairs.copy(deep=True)
    splitted_array = np.array_split(rnd_stimpairs, 4)
    
    "create a duration vector"
    duration = np.concatenate([np.arange(3, 10, 1.5) for _ in range(3)]) 
        
    for i in range(len(splitted_array)):
        splitted_array[i].set_axis([np.arange(1,16)], axis='index', copy=False, inplace=True)
        splitted_array[i].rename_axis('nTrial', axis='rows', inplace=True)
        #shuffle durations
        random.shuffle(duration)
        # check there are no subsequent repetitions
        last_index = np.where(duration == 9)[0][-1]  # find the index of the last '9'
        duration[-1], duration[last_index] = duration[last_index], duration[-1]  # swap with the last value of the shuffled array
        last_item = duration[-1]  # save the last item
        duration_1 = duration[:-1]  # slice the list to exclude the last item
        while any([duration[j] == duration[j+1] or duration[j] == duration[j+2]  for j in range(len(duration)-2)]):
            random.shuffle(duration_1) 
        duration = np.append(duration_1, last_item)
       #add it to the array 
        splitted_array[i]['resp_duration'] = duration
    # save 4 enc files
    for index, encoding_blocks in enumerate(splitted_array):
        enc_filename =f'enc_{index+1}.csv'
        path = os.path.join(outputfile_path, enc_filename)
        encoding_blocks.to_csv(path)
    
    "save the stimuli pairs array divided in f/p (col1=faces, col2=places)"
    arr = rnd_stimpairs.values
    # Create two lists of values based on starting letter
    faces = [row[0] if row[0].startswith('f') else row[1] for row in arr]
    places = [row[0] if row[0].startswith('p') else row[1] for row in arr]
    stmprs = pd.DataFrame({'Faces': faces, 'Places': places})
    stmprs.to_csv(outputfile_path + '\stimlist_f_p_.csv') 
 
"Check how many 50% overlap and 0% overlaps we have"
    
ol_mat=np.ones((nstim,nstim)) # setup overlap matrix

for e in range(0,nstim):
    for r in range(0,nstim):
        fc_ol = newListMrg[e][0] == newListMrg[r][0] # Calculate overlap for face stimuli
        pc_ol = newListMrg[e][1] == newListMrg[r][1] # Calculate overlap for place stimuli
    
        ol_chk=fc_ol+pc_ol;
        
        if ol_chk == 2:
            ol_mat[e][r]=100
        elif ol_chk == 1:
            ol_mat[e][r]=50
        else:
            ol_mat[e][r]=0
        
N100 = np.sum(ol_mat==100)
N50= np.sum(ol_mat==50)
N0= np.sum(ol_mat==0)
N1= np.sum(ol_mat==1)
print(N100, N50, N0, N1)
print('WARNING! CHECK THIS. The values should always be: 60 120 3420 0!')

plt.imshow(ol_mat) #create figure
plt.title('N 100% overlap:' + str(N100) + '--N 50% overlap:' + str(N50) + '--N 0% overlap:' + str(N0))  # add title


#%%
"RETRIEVAL LISTS RANDOMIZATION"
"Clear all variables before running using %reset -f"
%reset -f

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
import random
import csv
import os

#%% define paths and file names

nsubj = 3

inputfolder_path = r'C:\Users\eleonorm\OneDrive - University of Glasgow\Desktop\practice_block\param_fMRI-session'
file_path = os.path.join(inputfolder_path, str(nsubj)) 
file_names = ['enc_1.csv', 'enc_2.csv', 'enc_3.csv', 'enc_4.csv']
fp_file = pd.read_csv(os.path.join(inputfolder_path, str(nsubj),'stimlist_f_p_.csv'))
stimuli_x_block = np.array_split(fp_file, 4)

# define a function that returns the opposite of a value
def opposite_char(x, char):
    if char in x:
        return x.replace(char, 'b')
    else:
        return x.replace('b','a')

#define a function that returns two distractors
def get_distractors(target, ser, prev1, prev2):
    similar_no = target.split('.')[0][:-1]
    dist_list = [x for x in ser if x.split('.')[0][:-1] != similar_no and x != prev1 and x != prev2]
    if len(dist_list) < 2:
        return None, None
    rand1, rand2 = random.sample(dist_list, 2)
    if rand1[:3] == rand2[:3]:
        return None, None
    return rand1, rand2

    
# create empty lists to store DataFrames

retrieval_lists = []
face_stimuli = []
place_stimuli = []

# randomization of stimuli position on the screen 

pos1 = "[-0.3, -0.1]"
pos2 = "[0, -0.03]"
pos3 = "[0.3, -0.1]"

# create all the possible combinations of the 3 positions on the screen without repetitions
#combinations = set(itertools.permutations([(pos1[0], pos1[1]), (pos2[0], pos2[1]), (pos3[0], pos3[1])], 3))
combinations = set(itertools.permutations([(pos1), (pos2), (pos3)], 3))

# Repeat combinations 20 times
repeated_combinations = list(itertools.chain.from_iterable([combinations] * 20))

# convert to DataFrame and shuffle rows
columns = ['pos_1', 'pos_2', 'pos_3']
combs = pd.DataFrame(repeated_combinations, columns=columns)
np.random.shuffle(combs.values)

# check and swap after 3 consecutive repetitions
for i in range(1, len(combs)-1):
    if np.all(combs.iloc[i-1]['pos_1'] == combs.iloc[i]['pos_1']) and np.all(combs.iloc[i]['pos_1'] == combs.iloc[i+1]['pos_1']) and i < len(combs)-2 and np.all(combs.iloc[i+1]['pos_1'] == combs.iloc[i+2]['pos_1']):
        # select a new random row until it is different from the one being swapped
        new_row_idx = np.random.randint(i+2, len(combs))

        while np.all(combs.iloc[new_row_idx]['pos_1'] == combs.iloc[i]['pos_1']):
            new_row_idx = np.random.randint(i+2, len(combs))
        # swap the rows
        combs.iloc[i+1], combs.iloc[new_row_idx] = combs.iloc[new_row_idx].copy(), combs.iloc[i+1].copy()


# Divide DataFrame in 4 parts (=nBlocks)
screen_position = np.array_split(combs, 4)

# Create a new variable to control the possible conditions
 # create a new vector of [1,2,3] to control the condition type (2inst targ, 2inst dist, 2random dist - 30/30/60)
 #condition 1 -> 1 random distractor + 2 instances of the target
 #condition 2 -> 2 instances of the distractors + the target 
 #condition 3 -> 3 different images (2 random distractors + the target)
length = 60
c = [3] * length + [1] * (int(length/2)) + [2] * (int(length/2))
# shuffle the list until no item occurs more than three times in a row
while True:
    np.random.shuffle(c)
    if all([c[i] != c[i+1] or c[i+1] != c[i+2] or c[i+2] != c[i+3] for i in range(len(c)-3)]):
        break

col =  ['condition']
#cond = pd.DataFrame(c, columns=col)
conditions = np.array_split(c, 4)

# Create retrieval files (4 blocks, 120 trials)

# loop through the encoding file names and read in each file
for block, file in enumerate(file_names):
    df = pd.read_csv(os.path.join(file_path, file), usecols=[0, 1, 2])
    df = df.iloc[np.random.permutation(len(df))]  

    #switch the columns and append the result to the original DataFrame
    switch = df.copy()
    switch['left_image'], switch['right_image'] = switch['right_image'],switch['left_image']
    df = pd.concat([switch, df], ignore_index=True)
    
    # Shuffle two intervals of rows
    selected_rows = df.loc[15:21], df.loc[22:]
    selected_rows_shuffled = selected_rows[0].sample(frac=1), selected_rows[1].sample(frac=1)
    selected_rows_concat = pd.concat([selected_rows_shuffled[0], selected_rows_shuffled[1]], ignore_index=True)
    df.loc[15:29] = selected_rows_concat.values

    #add a new column containing the 2nd instance of the target
    #apply the function and create a new column 
    char_to_check = 'a'
    df['targ_2inst'] = df['right_image'].apply(lambda x: opposite_char(x, char_to_check))
    df = df.rename(columns={'left_image':'cue', 'right_image':'target'})
    
    #add a new column containing the condition
    df['condition'] = conditions[block]
        
    
    while True:
        extra_val_1 = []
        extra_val_2 = []
        p_ser = pd.concat([stimuli_x_block[block]['Places'], stimuli_x_block[block]['Places']], ignore_index=True)
        f_ser = pd.concat([stimuli_x_block[block]['Faces'], stimuli_x_block[block]['Faces']], ignore_index=True)
    
        #avoid direct repetitions
        prev_p1 = None
        prev_p2 = None
        prev_f1 = None
        prev_f2 = None
    
        for idx, row in df.iterrows():
            auto_check = True
    
            if 'f' in row.cue:
                rand1, rand2 = get_distractors(row.target, p_ser, prev_p1, prev_p2)
                if rand1 is None:
                    auto_check = False
                    break
                extra_val_1.append(rand1)
                extra_val_2.append(rand2)
                prev_p1 = rand1
                prev_p2 = rand2
                p_ser = p_ser.drop(p_ser[p_ser == rand1].index[0])
                p_ser = p_ser.drop(p_ser[p_ser == rand2].index[0])
            elif 'p' in row.cue:
                rand1, rand2 = get_distractors(row.target, f_ser, prev_f1, prev_f2)
                if rand1 is None:
                    auto_check = False
                    break
                extra_val_1.append(rand1)
                extra_val_2.append(rand2)
                prev_f1 = rand1
                prev_f2 = rand2
                f_ser = f_ser.drop(f_ser[f_ser == rand1].index[0])
                f_ser = f_ser.drop(f_ser[f_ser == rand2].index[0])
    
        if auto_check:
            break
    
    df['dist_1'] = extra_val_1
    df['dist_2'] = extra_val_2
        
    # create a new column with the second istance of the distractor
    char_to_check = 'a'
    df['dist_2inst'] = df['dist_1'].apply(lambda x: opposite_char(x, char_to_check))
    
    #add stimuli position on the screen
    #reset index
    screen_position[block].index = np.arange(len(screen_position[block].index))
    #concatenate
    df = pd.concat([df,screen_position[block]], axis = 1)
    
    #correct response
    # Define a dictionary to map screen positions to response values
    pos_to_resp = {('[-0.3, -0.1]'): 1, ('[0, -0.03]'): 2, ('[0.3, -0.1]'): 3}
        
    # Create a column with the correct response option
    df['corr_resp'] = [pos_to_resp[str(pos)] for pos in df["pos_1"]]

    duration = []
    for dr in range(2):
        duration.append(np.concatenate([np.arange(1, 8, 1.5) for _ in range(3)]))
        random.shuffle(duration[dr])
        
        # check there are no subsequent repetitions
        while any([duration[dr][i] == duration[dr][i+1] or duration[dr][i] == duration[dr][i+2] for i in range(len(duration[dr])-2)]):
            random.shuffle(duration[dr])
    duration = np.concatenate(duration)[:30]
    #the last interval should be the longest one
    last_index = np.where(duration == 7)[0][-1]  # find the index of the last '7'
    duration[-1], duration[last_index] = duration[last_index], duration[-1]  # swap with the last value of the shuffled array
    df['resp_duration'] = duration
    
    #reset nTrial index
    df = df.drop('nTrial', axis=1) #delete column 1 to avoid repetitions
    df.set_axis([np.arange(1,31)], axis='index', copy=False, inplace=True) #reset rows index
    df.rename_axis('nTrial', axis='rows', inplace=True) #rename the first column
    
    file_name = f'retr_{block+1}.csv'
    path = os.path.join(file_path, file_name)
    df.to_csv(path)
    #
    retrieval_lists.append(df)
    
