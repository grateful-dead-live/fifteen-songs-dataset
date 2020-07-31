# fifteen-songs-dataset
A small set of soundboard recordings of different performances of 15 grateful dead songs (2617 versions in total) published in the [Live Music Archive](https://archive.org/details/etree) of the Internet Archive. The songs are classified based on the metadata in the archive and some of them may be mislabeled.

The file `dataset.json` contains a dictionary with an entry for each song, consisting of a dictionary of all of its versions along with their suggested tuning ratios.

The `leadsheets` folder contains a leadsheet for each of the fifteen songs, compiled from our own transcriptions as well as leadsheets published online at [JDarks](http://jdarks.com/GDTab.html) and [Ultimate Guitar](https://tabs.ultimate-guitar.com).

## installation

Clone the repository and run `python dataset.py` (install any missing dependencies, e.g. `samplerate`, or `librosa`).

This will download and resample the audio files and save them into two directories: `original_audio` for the untuned and 'dataset' for the tuned files. Each of these folders contains separate subdirectories for each song.
