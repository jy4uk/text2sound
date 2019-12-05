"""
James Yang
Developed 12.2019
Text to Sound project
"""

from midiutil import MIDIFile
from tqdm import tqdm
import random


#creating a midi object
track = 0
channel = 0
time = 0    # In beats
duration = 1   # In beats
tempo = 60   # In BPM
volume = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)
MyMIDI.addTempo(track, time, tempo)

"""function that takes in a character and then outputs different values that will affect
 a note's specific parameters like midi-note, length, volume"""


# calculate the midi note value for what the pitch of the note should be
def get_pitch(character):
    first_letter = int(ord(character[0]))
    if first_letter > 108:
        # diff_fl = first_letter - 90
        first_letter = first_letter - 36
    return first_letter


# calculate the duration of the note
def get_duration(character):
    char_length = int(len(character))
    return char_length


# randomly assign the note a volume
def get_volume():
    volume_val = random.randint(50, 100)
    return int(volume_val)


# takes user input for what test file they want the midi notes to come from
file_name = input("What .txt file would you like to use? ")
file_name = file_name + ".txt"

# calculates the number of lines and how long the while loop below should run
test_file = open(file_name, "r")
count = len(test_file.readlines())
test_file.close()

# adds all the notes to the midi file
test_file2 = open(file_name, "r")
x = 0
for i in tqdm(range(count)):
    while x < count:
        character_array = test_file2.readline()
        MyMIDI.addNote(track, channel, get_pitch(character_array), time + x, get_duration(character_array), get_volume())
        x += 1
test_file2.close()


# The commented code below allows the user to directly input into the program as opposed to loading a .txt file
'''
first_input = input("What is the first word going to be?")
MyMIDI.addNote(track, channel, get_pitch(first_input), time, get_duration(first_input), get_volume())
i = 0
while i < 30:
    value = input("Next Word: ")
    MyMIDI.addNote(track, channel, get_pitch(value), time + i, get_duration(value), get_volume())
    i += 1
'''

# create the output file to put into DAW
with open("3390_output.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)


