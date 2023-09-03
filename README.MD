<h1 align="center">-- vidspinner --</h1>

<br/>

VidSpinner is a Python library that allows you to create unique versions of a video. This can be used for a variety of applications such as avoiding duplicate content detection algorithms or for creating visually distinct versions of the same video.

<h2>🔧 Installation</h2>

To install VidSpinner, use pip:

```bash
pip install vidspinner
```

<h2>🚀 Quick Start</h2>

Import VidSpinner, create a VidSpinner instance, and then use the `unique_by_pixel` method to create a unique video:

```python
from vidspinner import VidSpinner

vs = VidSpinner()
vs.unique_by_pixel('input.mp4', 'output.mp4')
```

This will create a unique version of 'input.mp4' and save it as 'output.mp4'. The video is made unique by adding a 1x1 pixel logo in the upper left corner.

<h3>🌈 Using Filter Effects</h3>

You can also make a video unique using an overlay filter effect. For example, to add a retro filter:

```python
from vidspinner import Filter

vs.unique_by_pixel('input.mp4', 'output.mp4', Filter.RETRO)
```

<h2>🎨 Available Filters</h2>

You can view all available filter presets using the `get_filters` method:

```python
from vidspinner import Filter

print(Filter.get_filters())
```

<h2>📄 License</h2>

VidSpinner is [MIT licensed](LICENSE).