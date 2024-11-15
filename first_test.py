from psychopy import visual, core, event, data, gui
import random

# Adding a little

# Set up the experiment window
win = visual.Window(size=(800, 600), color=(1, 1, 1), units='pix')

# Define stimuli and trial parameters
stimuli = [str(i) for i in range(1, 10)]
n_trials = 100
stim_duration = 0.25  # duration of each stimulus in seconds
isi = 1.0  # inter-stimulus interval in seconds

# Create a trial handler
trials = data.TrialHandler(stimuli * (n_trials // len(stimuli)), 1, method='random')

# Create a text stimulus for displaying numbers
text_stim = visual.TextStim(win, text='', color=(-1, -1, -1), height=50)

# Create a clock to keep track of time
clock = core.Clock()

# Instructions
instructions = visual.TextStim(win, text='Press space when you see any number except 3.\nPress any key to start.', color=(-1, -1, -1), height=30)
instructions.draw()
win.flip()
event.waitKeys()

# Run the trials
responses = []
for trial in trials:
    text_stim.text = trial
    text_stim.draw()
    win.flip()
    clock.reset()
    
    keys = event.waitKeys(maxWait=stim_duration + isi, keyList=['space'], timeStamped=clock)
    
    if keys:
        key, rt = keys[0]
        correct = (trial != '3')
    else:
        rt = None
        correct = (trial == '3')
    
    responses.append({'stimulus': trial, 'response': keys, 'rt': rt, 'correct': correct})
    
    win.flip()
    core.wait(isi)

# Save the data
data_file = open('sart_data.csv', 'w')
data_file.write('stimulus,response,rt,correct\n')
for response in responses:
    data_file.write(f"{response['stimulus']},{response['response']},{response['rt']},{response['correct']}\n")
data_file.close()

# Close the experiment
win.close()
core.quit()