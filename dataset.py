import json, os, warnings, requests
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool
from tqdm import tqdm
from samplerate import resample
from librosa import load, output

warnings.filterwarnings('ignore')   # librosa warning "using audioread"


PARALLEL_DOWNLOAD = 40
PARALLEL_RESAMPLE = 12

MP3 = 'https://archive.org/download/{0}'


def getJson():
    with open('dataset.json', 'rb') as jf:
        js =  json.load(jf)
    return js

    
def download(f):
    splt = f[1].split('/')[-2:]
    makeDir(os.path.join('original_audio', f[0], splt[0]))
    target = os.path.join('original_audio', f[0], splt[0], splt[1])
    with open(target, "wb") as file:
        response = requests.get(f[1])
        file.write(response.content)


def resampleAudio(f):
    tuning = f[2]
    splt = f[1].split('/')[-2:]
    makeDir(os.path.join('dataset', f[0], splt[0]))
    source = os.path.join('original_audio', f[0], splt[0], splt[1])
    target = os.path.join('dataset', f[0], splt[0], splt[1][:-3] + 'wav')
    a, sr = load(source)   # TODO: write load function without librosa
    if tuning != 0:
        a = resample(a, tuning**-1, 'sinc_fastest')    # invert tunning?
    output.write_wav(target, a, sr)


def makeDir(d):
    if not os.path.exists(d):
        try: os.makedirs(d)
        except: pass


def main():
    makeDir('original_audio')
    makeDir('dataset')
    js = getJson()
    mp3s = []
    for song, items in js.items():
        makeDir(os.path.join('dataset', song))
        for loc, tuning in items.items():
            mp3s.append((song, MP3.format(loc), tuning))

    print('download audio files')
    pool = ThreadPool(PARALLEL_DOWNLOAD)
    list(tqdm(pool.imap_unordered(download, mp3s), total=len(mp3s), smoothing=0.1))
    pool.close()
    pool.join()

    print('resampling audio files')
    pool = Pool(PARALLEL_RESAMPLE)
    list(tqdm(pool.imap_unordered(resampleAudio, mp3s), total=len(mp3s), smoothing=0.1))
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()