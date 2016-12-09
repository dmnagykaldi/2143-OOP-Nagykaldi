import imageEdit
import sys

flags = ['-i','-x','-s','-show']

commands = {}

for i in range(1,len(sys.argv),2):
    commands[sys.argv[i]] = sys.argv[i+1]

commands['-i'] = commands['-i'].split(',')

ie = imageEdit.ImageEd(commands)
if(commands['-x'] == 'flip'):
	ie.flip()