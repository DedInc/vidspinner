class TextEffectBuilder:

  def __init__(self):
    self.effects = []
    self.BLINK = 'enable=lt(mod(n\\,{interval})\\,{interval_div})'
    self.SHADOW = 'shadowcolor={color}:shadowx={x}:shadowy={y}'
    self.SHAKE = 'x={x}+rand(-{amplitude}\\,{amplitude}):y={y}+rand(-{amplitude}\\,{amplitude})'
    self.FADE_IN = 'alpha=min(t/{duration}\\,1)'
    self.FADE_OUT = 'alpha=max(1-t/{duration}\\,0)'
    self.SCROLL_TB = 'y=-text_h+t/{duration}*text_h'
    self.SCROLL_LR = 'x=-text_w+t/{duration}*text_w'
    
  def add_effect(self, effect='BLINK', 
    interval=5, 
    x=5, 
    y=5, 
    amplitude=5, 
    start_duration=1, 
    end_duration=2, 
    duration=1, 
    color='black'
    ):
    effect = getattr(self, effect).format(
        interval=interval, 
        interval_div=interval // 2, x=x, y=y, 
        amplitude=amplitude, 
        start_duration=start_duration, 
        end_duration=end_duration, 
        duration=duration, 
        color=color
    )
    self.effects.append(effect)

  def add_custom_effect(self, effect_string):
    self.effects.append(effect_string)

  def build(self):
    return ':'.join(self.effects)

class TextBuilder:
  
  def __init__(self):
    self.text = ''
    self.update()

  def update(self, FONT = ''):
    self.CENTER = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=(w-text_w)/2:y=(h-text_h)/2'
    self.CENTER_RIGHT = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=w-tw-50:y=(h-text_h)/2'
    self.CENTER_LEFT = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=50:y=(h-text_h)/2'

    self.BOTTOM = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=(w-text_w)/2:y=h-th-10'
    self.BOTTOM_LEFT = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=50:y=h-th-10'
    self.BOTTOM_RIGHT = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=w-tw-50:y=h-th-10'
    self.BOTTOM_CENTER = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=(w-text_w)/2:y=h-th-10'

    self.TOP = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=(w-text_w)/2:y=50'
    self.TOP_RIGHT = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=w-tw-50:y=50'
    self.TOP_LEFT = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=50:y=50'
    self.TOP_CENTER = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x=(w-text_w)/2:y=50'

    self.COORDS = 'drawtext=text=\'{text}\':fontcolor={color}' + FONT + ':fontsize={size}:x={x}:y={y}'

  def set_params(self, position='CENTER', text = 'Sample Text', color='white', size=48, x=10, y=87):
    self.text = getattr(self, position).format(text=text, color=color, size=size, x=x, y=y)
    return self

  def add_effect(self, effect_builder):
    effects = effect_builder.build()
    if effects:
      self.text += f':{effects}'
    return self

  def set_font(self, font):
    self.update(f':fontfile={font}')

  def build(self):
    return self.text