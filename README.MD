<h1 align="center">-- vidspinner --</h1>

vidspinner is a Python library for easily creating unique versions of videos using filters, text, and audio effects.

<h2>📥 Installation</h2>

```
pip install vidspinner
```

<h2>💡 Quick Start</h2>

```python
from vidspinner import MontageBuilder
from vidspinner.filters import Filter
from vidspinner.builders.text import TextBuilder, TextEffectBuilder
from vidspinner.builders.audio import AudioBuilder

mb = MontageBuilder()

mb.input = 'input.mp4'
mb.output = 'output.mp4'
mb.clear_meta_tags = True # clear meta tags

mb.add_filter(Filter.RETRO)

########### Test text ############ 
tb = TextBuilder()
tb.set_params(text='Wow! It is a simple text!')
mb.add_filter(tb.build(), start_duration=2, end_duration=5) # add text
##################################

####################### Fisheye effect ################
mb.add_filter(Filter.FISHEYE, start_duration=3, end_duration=5.8)
########################################################


############## Creating logo ###########
tb.set_font('comic_sans.ttf')
tb.set_params(color='cyan', text='VidSpinner', size=48)

teb = TextEffectBuilder()
teb.add_effect(effect='SHADOW', x=5, y=5, color='black')
teb.add_effect(effect='SHAKE', x=0, y=1850, amplitude=6) # for the shake effect you need to set the position of the text relative to its current coordinates.

box_effect = 'box=1:boxcolor={color}@{transparency}:boxborderw={width}' # custom text effect

teb.add_custom_effect(box_effect.format(
  color='lime',
  transparency=0.3,
  width=3
))

tb.add_effect(teb)

mb.add_filter(tb.build())
#######################################

########### Audio manipulations ############
ab = AudioBuilder()
ab.set_pitch(1.5)
mb.set_audio(ab)
#####################################

mb.build() # build result
```

<h2>🎥 Example (Quickstart Result):</h2>

<h3>📹 Input:</h3>

https://github.com/DedInc/test/assets/41906303/30282cf8-43d9-4fe1-abce-857e363c7189

<h3>🔮 Output:</h3>

https://github.com/DedInc/test/assets/41906303/079c245a-79b0-4f47-bb36-934d0a1afa6e

<h2>🎨 Features</h2>

- 16 built-in filters like retro, black & white, psychedelic etc.
- Add custom text with control over font, size, position  
- Animate text with scroll, shake, blink and more
- Trim, pitch shift, speed up/slow down audio
- Clear metadata to avoid detection

<h2>🧰 Built-in Filters</h2>

```python
from vidspinner.filters import Filter

print(Filter.get_filters()) # to see all filters 
```

<h3>🎨 Working with Filters</h3>

Add a filter:

```python 
mb = MontageBuilder()
mb.add_filter(Filter.RETRO) # add filter
mb.add_filter(Filter.VIGNETTE) # add several filters
```

Add a custom filter:

```python
mb.add_filter('rotate=PI/4') 
```

<h3>🖌️ Working with Text</h3>

Add text:

```python
from vidspinner.builders.text import TextBuilder

tb = TextBuilder()
tb.set_params(
  text='Hello World!',
  position='CENTER' 
)
text = tb.build()
mb.add_filter(text)
```

Stylize text and custom position:

```python
from vidspinner.builders.text import TextBuilder

tb = TextBuilder()
tb.set_font('comic_sans.ttf')
tb.set_params(
  position='COORDS',
  text='Hello World', 
  color='blue',
  size=32,
  x=0,
  y=0
)
text = tb.build()
mb.add_filter(text)
```

Some text positions:

```
'CENTER' - Center text horizontally and vertically
'CENTER_RIGHT' - Center vertically, align right
'CENTER_LEFT' - Center vertically, align left

'BOTTOM' - Align text to bottom center  
'BOTTOM_LEFT' - Align text to bottom left
'BOTTOM_RIGHT' - Align text to bottom right
'BOTTOM_CENTER' - Align text to bottom center

'TOP' - Align text to top center
'TOP_RIGHT' - Align text to top right
'TOP_LEFT' - Align text to top left 
'TOP_CENTER' - Align text to top center

'COORDS' - Specify x and y coordinates
```


Add text with effects:

```python 
from vidspinner.builders.text import TextBuilder, TextEffectBuilder

tb = TextBuilder()

te = TextEffectBuilder()
te.add_effect('BLINK', interval=3)
te.add_effect('SHADOW', color='gray', x=5, y=5)

tb.set_params(
  text='Hello World!'
)

tb.add_effect(te) 

text = tb.build()

mb.add_filter(text)
```

Some text effects:

```
'BLINK' - Text blinks
'SHADOW' - Text shadow
'SHAKE' - Shake text randomly
'SCROLL_TB' - Scroll text top to bottom 
'SCROLL_LR' - Scroll text left to right
'FADE_IN' - Fade in text over duration
'FADE_OUT' - Fade out text over duration
```

Some common effect parameters:

- `BLINK` - `interval` 
- `SHADOW` - `color, x, y`
- `SHAKE` - `amplitude`
- `FADE_IN` - `duration`
- `FADE_OUT` - `duration`  
- `SCROLL_TB` - `duration`
- `SCROLL_LR` - `duration`


<h3>🎙️ Working with Audio</h3>

Change audio track:

```python
from vidspinner.builders.audio import AudioBuilder

ab = AudioBuilder()
ab.set_audiotrack('track.mp3', start_time=10, end_time=20)
mb.set_audio(ab)
```

Change volume:

```python
ab.set_volume(0.5)
```

Pitch shift: 

```python 
ab.set_pitch(1.5)
```

<h3>🗑️ Clearing Metadata</h3>

To clear metadata tags and avoid detection:

```python
mb.clear_meta_tags = True 
```

This will add the `-map_metadata -1` flag to ffmpeg to clear metadata tags like title, author, etc.

<h2>📄 License</h2>

VidSpinner is [MIT licensed](LICENSE).