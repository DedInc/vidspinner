import subprocess

class AudioBuilder:

  def __init__(self):
    self.filters = []
    self.trash = []
  
  def set_volume(self, volume):
    self.filters.append(f'volume={volume}')
    return self
  
  def set_pitch(self, pitch):
    self.filters.append(f'rubberband=pitch={pitch}') 
    return self

  def set_speed(self, speed):
    self.filters.append(f'atempo={speed}')
    return self

  def trim_audio(self, filename, start_time, end_time, trimmed_file):
    ffmpeg_command = [
      'ffmpeg', '-y',
      '-ss', str(start_time), 
      '-to', str(end_time),
      '-i', filename,
      trimmed_file
    ]
    subprocess.run(ffmpeg_command)

  def set_audiotrack(self, filename, start_time, end_time):
    trimmed_file = 'trimmed.mp3'
    self.trim_audio(filename, start_time, end_time, trimmed_file)

    self.filters.append(f'amovie={trimmed_file}')
    if start_time > 0:
      self.filters.append(f'adelay={start_time}|{start_time}')

    self.trash.append(trimmed_file)

    return self


  def build(self):
    if not self.filters:
      return ''
    
    return ','.join(self.filters)