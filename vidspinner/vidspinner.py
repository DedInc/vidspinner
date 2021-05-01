from PIL import Image
from random import randint as rnt
from os.path import dirname, abspath, join, exists
from os import remove, system
from multiprocessing import cpu_count as cpu

def genPixel():
	print('Generating pixel...')
	cdir = dirname(abspath(__file__))
	img = Image.open(join(cdir, 'pixel.png'))
	img = img.convert('RGBA')
	datas = img.getdata()

	newData = []
	for item in datas:
	    if item[0] == 255 and item[1] == 255 and item[2] == 255:
	        newData.append((255, 255, 255, 0))
	    else:
	        if item[0] > 150:
	            newData.append((rnt(rnt(0, 150), rnt(150, 255)), rnt(rnt(0, 150), rnt(150, 255)), rnt(rnt(0, 150), rnt(150, 255)), 255))
	        else:
	            newData.append(item)

	img.putdata(newData)
	img.save(join(cdir, 'gpixel.png'), 'PNG')
	print('Generated!')

def unique(input, output):
	if not exists(input):
		print('Video is not exists!')
	else:
		genPixel()
		cdir = dirname(abspath(__file__))
		system(cdir + "\\ffmpeg -i \"{}\" -vf \"movie=\\'{}\\' [logo]; [in][logo] overlay=0:0 [out]\"  -y -threads {} -qscale 0 \"{}\"".format(input, cdir.replace('\\', '\\\\') + '\\\\gpixel.png', cpu(), output))
		remove(join(cdir, 'gpixel.png'))
		print('Video has been uniqualized!')