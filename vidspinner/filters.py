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
    ANIME = 'pp=be/hb/vb/dr/al,eq=brightness=0.05:saturation=1.2:contrast=1.2'
    CRACKLE = 'noise=alls=10:allf=t'
    FISHEYE = 'lenscorrection=cx=0.5:cy=0.5:k1=-0.4:k2=-0.4'

    @classmethod
    def get_filters(cls):
        return [filter for filter in dir(cls) if filter.isupper() and isinstance(getattr(cls, filter), str)]