from PIL import Image
# Imports image library stuff
import random
# Import sys so we can access argv for command line args
import sys

class ImageEd(object):

	def __init__(self,argv):
	## Parse argv that was passed in to our class
		parts = {}

		for i in range(1,len(argv),2):
			parts[sys.argv[i]] = sys.argv[i+1]

		if '-i' in parts.keys():
			self.input_file = parts['-i']
			self.save_file = self.input_file 
			self.img = Image.open(self.input_file)

		if '-x' in parts.keys():
			self.method = parts['-x']

		if '-s' in parts.keys():
			self.save_file = parts['-s']
			self.save = True
		else:
			self.save = False

		if '-show' in parts.keys():
			self.show = parts['-show']
			if self.show == "1" or self.show == "True":
				self.show = True
			else:
				self.show = False

		## Parsing Done!

		# Get width and height of image so we can loop through it
		self.width = self.img.size[0]
		self.height = self.img.size[1]

		# Perform actions based on command line params set above
		if self.save:
			self.img.save(self.save_file)

		if self.show:
			self.img.show()

	def glass_effect(self):
		pass

	def flip(self,img=None):
		if not img == None:
			self.img = img

		for x in range(self.width):
			for y in range(self.height):
				opposite = self.width - y
				rgb = self.img.getpixel((x,y))
				rgb2 = self.img.getpixel(opposite,y)
				self.img.putpixel((x,y),rgb2)
				self.img.putpixel((opposite,y),rgb)

		return self.img

	def blur(self):
		pass

	def posterize(self):
		pass

	def solarize(self):
		pass

	def warhol(self):
		pass

	# Prints the usage as expected if we don't get enough params
	# Remember, we are NOT error checking and in the real world, you MUST!
	def print_usage():
		print("Error: \n   Url or filename needed")
		print("Usage: \n   python %s -u url [-o outputfile]\n   python %s -f filename [-s savefile, -show 1]" % (sys.argv[0],sys.argv[0]))
		print("Example: \n   python %s -u https://s-media-cache-ak0.pinimg.com/originals/05/b3/83/05b3831a2cefe769af2e9e5c877e6cc8.jpg -o negative.jpg -show 1" % (sys.argv[0]))
		print("   (this would open the url, process it, save it locally in 'negative.jpg' and also open the result")

	# Ummmm run me if this file called directly.
	if __name__=='__main__':
		if len(sys.argv) < 3:
			print_usage()
			sys.exit(0)
		else:
			pic = ImageEd(sys.argv)


	# NOT USED but I left it here 
	def random_color(self):
		return (random.randint(255),random.randint(255),random.randint(255))

