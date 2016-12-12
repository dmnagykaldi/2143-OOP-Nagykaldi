import imageEdit
import sys

flags = ['-i','-x','-s','-show']

commands = {}

for i in range(1,len(sys.argv),2):
    commands[sys.argv[i]] = sys.argv[i+1]

commands['-i'] = commands['-i'].split(',')

ie = imageEdit.ImageEd(commands)

if(commands['-x'] == 'flip'):
	flipped = ie.flip()
	flipped.show()

if(commands['-x'] == 'glass_effect'):
	glass = ie.glass_effect()
	glass.show()

if(commands['-x'] == 'blur'):
	blurry = ie.blur()
	blurry.show()