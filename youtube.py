import pafy
from os import environ, path
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *

MODELDIR = "/usr/local/lib/python3.6/site-packages/pocketsphinx/model"
DATADIR = "/usr/local/lib/python3.6/site-packages/pocketsphinx/test/data"

# grab the url from trending
#url = "https://www.youtube.com/watch?v=OaRBPXLgKyg"
url = "https://youtu.be/-LWW4bglAqI"
video = pafy.new(url)

# print video title and viewcount
print(video.title, video.viewcount)

# download video audio
bestaudio = video.getbestaudio()
dl_filepath = "/data/file1." + bestaudio.extension
bestaudio.download(filepath=dl_filepath)

# Create a decoder with certain model
config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'en-us'))
config.set_string('-lm', path.join(MODELDIR, 'en-us.lm.bin'))
config.set_string('-dict', path.join(MODELDIR, 'cmudict-en-us.dict'))
decoder = Decoder(config)

# Decode streaming data
decoder = Decoder(config)
decoder.start_utt()
with open(dl_filepath, 'rb') as stream:
    while True:
        buf = stream.read(1024)
        if buf:
            decoder.process_raw(buf, False, False)
        else:
            break
decoder.end_utt()
print('Best Hypothesis segments:', [seg.word for seg in decoder.seg()])
