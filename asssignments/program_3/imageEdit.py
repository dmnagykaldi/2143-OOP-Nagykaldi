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

	def glass_effect(self, img=None, dist = 5):
		if not img == None:
			self.img = img
		
		distance = dist
		for x in range(self.width):
			for y in range(self.height):
				xnums = [i for i in range(x - distance, x + distance) if i >= 0 and i <= self.width -1]
				xchoice = random.choice(xnums)
				ynums = [j for j in range(y - distance, y + distance) if j >= 0 and j <= self.height -1]
				ychoice = random.choice(ynums)
				self.img.putpixel((x,y),self.img.getpixel((xchoice,ychoice)))
				
		return self.img

	def flip(self,img=None):
		if not img == None:
			self.img = img

		for x in range(self.width):
			for y in range(self.height//2):
				opposite = (self.height - 1) - y
				rgb = self.img.getpixel((x,y))
				rgb2 = self.img.getpixel((x,opposite))
				self.img.putpixel((x,y),rgb2)
				self.img.putpixel((x,opposite),rgb)

		return self.img

	def blur(self, img=None, krn=5):
		if not img == None:
			self.img = img
		
		kernel = krn
		if(kernel % 2 == 1):
			ker2 = (kernel-1) * (kernel-1)
		else:
			ker2 = kernel * kernel
		for x in range(kernel,self.width-kernel):
			for y in range(kernel,self.height-kernel):
				meanr = 0
				meang = 0
				meanb = 0
				for i in range(0-(kernel//2),(kernel//2)):
					for j in range(0-(kernel//2),(kernel//2)):
						current = self.img.getpixel((x + i,y + j))
						meanr += current[0]
						meang += current[1]
						meanb += current[2]
				mean = (meanr//ker2,meang//ker2,meanb//ker2)
				self.img.putpixel((x,y),mean)
		
		return self.img

	def posterize(self, img=None, snap = 64):
		if not img == None:
			self.img = img
		
		for x in range(self.width):
			for y in range(self.height):
				color = self.img.getpixel((x,y))
				r = color[0] % snap
				g = color[1] % snap
				b = color[2] % snap
				if r < (snap // 2):
					newr = color[0] - r
				else:
					newr = color[0] + (snap - r)
				if g < (snap // 2):
					newg = color[1] - g
				else:
					newg = color[1] + (snap - g)
				if b < (snap // 2):
					newb = color[2] - b
				else:
					newb = color[2] + (snap - b)
				self.img.putpixel((x,y),(newr,newg,newb))
		
		return self.img
		
	def solarize(self, img=None, threshold = 125):
		if not img == None:
			self.img = img
		
		for x in range(self.width):
			for y in range(self.height):
				color = self.img.getpixel((x,y))
				if(color[0] < threshold):
					newr = 255 - color[0]
				else:
					newr = color[0]
				if(color[1] < threshold):
					newg = 255 - color[1]
				else:
					newg = color[1]
				if(color[2] < threshold):
					newb = 255 - color[2]
				else:
					newb = color[2]
				self.img.putpixel((x,y),(newr,newg,newb))
		
		return self.img

	def warhol(self, img=None, interval = 32):
		if not img == None:
			self.img = img
		
		for x in range(self.width):
			for y in range(self.height):
				color = self.img.getpixel((x,y))
				avg = (color[0] + color[1] + color[2]) // 3
				self.img.putpixel((x,y),(avg,avg,avg))
				
		self.posterize(snap = interval)
		war_color = []
		
		for i in range(256//interval):
			war_color.append((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
			
		for x in range(self.width):
			for y in range(self.height):
				color = self.img.getpixel((x,y))
				self.img.putpixel((x,y),war_color[color[0]//interval])
				
		return self.img

