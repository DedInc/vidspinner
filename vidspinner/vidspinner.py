import os
import platform
import subprocess
import urllib.request
import zipfile
import math
from multiprocessing import cpu_count

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

class Init:
    def __init__(self):
        self.ffmpeg_bin = 'ffmpeg'
        self.ffmpeg_path = ''
        self.filename = ''
        self.os_type = self.get_os_type()
        self.download_and_extract_ffmpeg()

    def get_os_type(self):
        return platform.system()

    def set_os_specific_attributes(self):
        os_type = self.os_type
        if os_type == 'Windows':
            self.url = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip'
            self.filename = 'ffmpeg-latest-win64-static.zip'
            self.ffmpeg_path = os.path.join(CURRENT_DIR, 'ffmpeg-master-latest-win64-gpl', 'bin', 'ffmpeg.exe')
        elif os_type == 'Linux':
            self.url = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-linuxarm64-gpl.tar.xz'
            self.filename = 'ffmpeg-release-amd64-static.tar.xz'
            self.ffmpeg_path = os.path.join(CURRENT_DIR, 'ffmpeg-master-latest-linuxarm64-gpl', 'bin', 'ffmpeg')
        elif os_type == 'Darwin':
            self.url = 'https://evermeet.cx/ffmpeg/ffmpeg-6.0.zip'
            self.filename = 'ffmpeg.zip'
            self.ffmpeg_path = os.path.join(CURRENT_DIR, 'ffmpeg')

    def check_ffmpeg_exists(self):
        return os.path.exists(self.ffmpeg_path)

    def download_ffmpeg(self):
        print("FFmpeg not found! Downloading...")

        with urllib.request.urlopen(self.url) as response, open(self.filename, 'wb') as out_file:
            total_length = int(response.info().get('Content-Length'))
            downloaded = 0
            chunk_size = 1024

            while True:
                data = response.read(chunk_size)
                downloaded += len(data)

                progress_bar_length = 30
                progress_block_count = math.ceil(progress_bar_length * downloaded / total_length)
                downloaded_mb = downloaded / (1024 * 1024)
                total_mb = total_length / (1024 * 1024)

                print(f"{downloaded_mb:.2f}MB [", end='')
                print('#' * progress_block_count, end='')
                print(' ' * (progress_bar_length - progress_block_count), end=f'] {total_mb:.2f}MB')
                print('\r', end='')

                if not data:
                    break

                out_file.write(data)

        print("\nDownload complete!")

    def extract_downloaded_file(self):
      if self.os_type in ['Windows', 'Darwin']:
          with zipfile.ZipFile(self.filename, 'r') as zip_ref:
              zip_ref.extractall(CURRENT_DIR)
      elif self.os_type == 'Linux':
          subprocess.run(['tar', '-xf', self.filename, '-C', CURRENT_DIR])

    def download_and_extract_ffmpeg(self):
        self.set_os_specific_attributes()
        if not self.check_ffmpeg_exists():
            self.download_ffmpeg()
            self.extract_downloaded_file()
        if self.os_type != 'Windows':
            self.ffmpeg_bin = './' + self.ffmpeg_path
        else:
            self.ffmpeg_bin = self.ffmpeg_path


class MontageBuilder:
  Init()
  def __init__(self):
    self.input = None
    self.output = None 
    self.clear_meta_tags = False
    self.filters = []
    self.trash = []
    self.audio_filters = None

  def add_filter(self, filter_string, start_duration=None, end_duration=None):
    if start_duration is not None:
        filter_string += f':enable=\'between(t,{start_duration},{end_duration})\''

    self.filters.append(filter_string)

  def set_audio(self, audio_builder):
    self.audio_filters = audio_builder.build()
    self.trash = audio_builder.trash

  def build(self):
    command = ['ffmpeg', '-i', self.input]

    if self.filters:
        filters_string = ','.join(self.filters)
        command += ['-vf', filters_string]

    command += [
        '-y', 
        '-threads', str(cpu_count()),
        '-qscale:v', '0' 
    ]

    if self.clear_meta_tags:
        command += ['-map_metadata', '-1']

    if self.audio_filters:
        command += ['-filter_complex', self.audio_filters]

    command += [self.output]
    subprocess.run(command)

    if self.trash:
        for f in self.trash:
            os.remove(f)

    print(command)