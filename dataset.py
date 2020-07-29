import json, os
from urllib import request
from urllib.error import HTTPError
from multiprocessing.pool import ThreadPool
import multiprocessing as mp
from tqdm import tqdm
import requests
from pydub import AudioSegment


PARALLEL_DOWNLOADS = 40

SONGS = ["box_of_rain", 
        "china_doll", 
        "dancin'_in_the_street", 
        "eyes_of_the_world", 
        "ship_of_fools", 
        "casey_jones", 
        "cosmic_charlie", 
        "dark_star", 
        "franklin's_tower", 
        "sugar_magnolia", 
        "china_cat_sunflower", 
        "cumberland_blues", 
        "estimated_prophet", 
        "scarlet_begonias", 
        "truckin'"]

M3U = "https://archive.org/download/{0}/{0}_vbr.m3u"
MP3 = "https://archive.org/download/{0}"


def getJson():
    with open('dataset.json', 'rb') as jf:
        js =  json.load(jf)
    return js



def checkM3U(m3u):
    try:
        req = request.urlopen(m3u[1])
        if req.code == 200:
            #print('ok:', m3u)
            pass
        else:
            print(f'error {req.code}:', m3u[1])
    except HTTPError as err:
        print(f'error {err}:', m3u[1])

    
def download(f):
    splt = f[1].split('/')[-2:]
    makeDir(os.path.join('temp', f[0], splt[0]))
    target = os.path.join('temp', f[0], splt[0], splt[1])
    with open(target, "wb") as file:
        response = requests.get(f[1])
        file.write(response.content)



def makeDir(d):
    if not os.path.exists(d):
        try: os.makedirs(d)
        except: pass


def resampleAudio(f, tuning):
    a = AudioSegment.from_mp3("never_gonna_give_you_up.wav")
    if tuning != 0: 
        a = resample(a, tuning, 'sinc_fastest')
    
    a.export("mashup.mp3", format="wav")



def main():
    makeDir('temp')
    makeDir('dataset')
    js = getJson()
    mp3s = []
    for song, items in js.items():
        makeDir(os.path.join('dataset', song))
        for loc, tuning in items.items():
            #if loc.endswith('.mp3.wav'):
            #    loc = loc.replace('.mp3.wav', '.wav.mp3')
            mp3s.append((song, MP3.format(loc)))

    pool = ThreadPool(PARALLEL_DOWNLOADS)
    list(tqdm(pool.imap_unordered(download, mp3s), total=len(mp3s)))
    pool.close()
    pool.join()






        

if __name__ == '__main__':
    main()