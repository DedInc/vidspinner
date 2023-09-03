import os
import platform
import subprocess
import urllib.request
import zipfile
from PIL import Image
from random import randint
from multiprocessing import cpu_count

class Filter:
	SEPIA = 'colorchannelmixer=.393:.769:.189:0:.349:.686:.168:0:.272:.534:.131'
	RETRO = 'curves=vintage,format=yuv420p'
	BLACK_WHITE = 'hue=s=0:b=0'
	INVERT = 'negate'
	SKETCH = 'edgedetect=mode=colormix'
	VIGNETTE = 'vignette=PI/4'
	COLORIZE = 'hue=s=2'
	PSYCHEDELIC = 'hue=H=0.15,vibrance=intensity=1.5'
	SHARPEN = 'unsharp=5:5:0.8:5:5:0.8'	
	BRIGHT_LIGHTS = 'curves=lighter'
	DARK_SHADOWS = 'curves=darker'
	MIRRORS = 'hflip,vflip'	
	DREAMY = 'gblur=sigma=5'	
	VINTAGE = 'curves=vintage,format=yuv420p,vignette=\'PI/5\''


	@classmethod
	def get_filters(cls):
	    return [filter for filter in dir(cls) if filter.isupper() and isinstance(getattr(cls, filter), str)]

class VidSpinner:
	def __init__(self):
	    self.ffmpeg_bin = 'ffmpeg'
	    self.current_dir = os.path.abspath(os.path.dirname(__file__))
	    self.ffmpeg_path = ''
	    self.filename = ''
	    self.os_type = self.get_os_type()
	    self.download_and_extract_ffmpeg()

	def get_os_type(self):
	    return platform.system()

	def set_os_specific_attributes(self):
	    os_type = self.os_type
	    if os_type == 'Windows':
	        self.url = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-lgpl-shared.zip'
	        self.filename = 'ffmpeg-latest-win64-static.zip'
	        self.ffmpeg_path = os.path.join(self.current_dir, 'ffmpeg-master-latest-win64-lgpl-shared', 'bin', 'ffmpeg.exe')
	    elif os_type == 'Linux':
	        self.url = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linuxarm64-lgpl-shared.tar.xz'
	        self.filename = 'ffmpeg-release-amd64-static.tar.xz'
	        self.ffmpeg_path = os.path.join(self.current_dir, 'ffmpeg-master-latest-win64-lgpl-shared', 'bin', 'ffmpeg')
	    elif os_type == 'Darwin':
	        self.url = 'https://evermeet.cx/ffmpeg/ffmpeg-6.0.zip'
	        self.filename = 'ffmpeg.zip'
	        self.ffmpeg_path = os.path.join(self.current_dir, 'ffmpeg')

	def check_ffmpeg_exists(self):
	    return os.path.exists(self.ffmpeg_path)

	def download_ffmpeg(self):
	    print(f'FFmpeg not found! downloading...')
	    urllib.request.urlretrieve(self.url, self.filename)
	    print('Download complete!')

	def extract_downloaded_file(self):
	    if self.os_type in ['Windows', 'Darwin']:
	        with zipfile.ZipFile(self.filename, 'r') as zip_ref:
	            zip_ref.extractall('.')
	    elif self.os_type == 'Linux':
	        subprocess.run(['tar', '-xf', self.filename])

	def download_and_extract_ffmpeg(self):
	    self.set_os_specific_attributes()
	    if not self.check_ffmpeg_exists():
	        self.download_ffmpeg()
	        self.extract_downloaded_file()
	    if self.os_type != 'Windows':
	        self.ffmpeg_bin = './' + self.ffmpeg_path
	    else:
	        self.ffmpeg_bin = self.ffmpeg_path

	@staticmethod
	def generate_pixel(image_path, output_path):
	    img = Image.open(image_path)
	    img = img.convert('RGBA')
	    datas = img.getdata()

	    newData = []
	    for item in datas:
	        if item[0] == 255 and item[1] == 255 and item[2] == 255:
	            newData.append((255, 255, 255, 0))
	        else:
	            if item[0] > 150:
	                newData.append((randint(0, 255), randint(0, 255), randint(0, 255), 255))
	            else:
	                newData.append(item)

	    img.putdata(newData)
	    img.save(output_path, 'PNG')

	def unique_by_pixel(self, input, output):
		if not os.path.exists(input):
		    raise Exception('Video does not exist!')
		else:
			pixel_path = os.path.join(self.current_dir, 'pixel.png')
			processed_pixel_path = 'gpixel.png'
			self.generate_pixel(pixel_path, processed_pixel_path)
			filter_string = f"movie='{processed_pixel_path}' [logo]; [in][logo] overlay=0:0 [out]"
			ffmpeg_command = [
			    self.ffmpeg_bin, "-i", input, "-vf", filter_string,
			    "-y", "-threads", str(cpu_count()), "-q:v", "0", "-map_metadata", "-1", output
			]
			subprocess.run(ffmpeg_command)
			os.remove(processed_pixel_path)

	def unique_by_filter(self, input, output, filter_command):
	    if not os.path.exists(input):
	        raise Exception('Video does not exist!')
	    else:
	        subprocess.run([
	            self.ffmpeg_bin, "-i", input, "-vf", filter_command,
	            "-y", "-threads", str(cpu_count()), "-qscale", "0", "-map_metadata", "-1", output
	     	])