# fifteen-songs-dataset
A small set of soundboard recordings of different performances of 15 grateful dead songs (2617 versions in total) published in the [Live Music Archive](https://archive.org/details/etree) of the Internet Archive. The songs are classified based on the metadata in the archive and some of them may be mislabeled.

The file `dataset.json` contains a dictionary with an entry for each song, consisting of a dictionary of all of its versions along with their suggested tuning ratios.

The `leadsheets` folder contains a leadsheet for each of the fifteen songs, compiled from our own transcriptions as well as leadsheets published online at [JDarks](http://jdarks.com/GDTab.html) and [Ultimate Guitar](https://tabs.ultimate-guitar.com).

## installation

Clone the repository and run `python dataset.py` (install any missing dependencies, e.g. `samplerate`, or `librosa`).

This will download and resample the audio files and save them into two directories: `original_audio` for the untuned and 'dataset' for the tuned files. Each of these folders contains separate subdirectories for each song.

## details

The 15 songs are (number of versions in parentheses): Box of Rain (85), Casey Jones (181), China Cat Sunflower (181), China Doll (65), Cosmic Charlie (56), Cumberland Blues (132), Dancin' in the Streets (68), Dark Star (139), Estimated Prophet (223), Eyes of the World (218), Franklin's Tower (126), Scarlet Begonias (184), Ship of Fools (138), Sugar Magnolia (351), and Truckin' (315). They were selected based on the criteria that a large number of versions exist and that a corresponding reference studio recording by the Grateful Dead is available (not part of the dataset).

This dataset was first used in: Florian Thalmann, Kazuyoshi Yoshii, Thomas Wilmering, Geraint Wiggins, Mark Sandler. *A Method for Analysis of Shared Structure in Large Music Collections using Techniques from Genetic Sequencing and Graph Theory*, ISMIR 2020. We kindly ask you to cite this paper if you use the dataset.
