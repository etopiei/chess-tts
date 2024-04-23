# Chess TTS

Tool to help learn chess visualisation by listening to games.

## Pre-requisites

```
python -m pip install python-chess
```

## Generating audio (macOS only)

To generate a audio recording of a game:

```
python make_transcript.py test.pgn | say -v "Samantha" -o out.aiff
```

This will generate a file called 'out.aiff' which reads out the game.

You can read an example of the transcript text [here](transcript.txt).

And you can listen to an example of how the game sounds [here](test.aiff)

## Generating batches of audio from PGN database

There is a helper script in this repo called `make_audio_files` which generates audios from all games in a database in PGN format. It can be used like so:

```
mkdir audio_games
python make_audio_files.py '~/Downloads/Lichess Elite Database' audio_games
```

Note: it also optionally supports a final argument which limits the number of moves in a game, so to get all games that have 10 moves or less do:

```
mkdir under11
python make_audio_files.py '~/Downloads/Lichess Elite Database' under11 10
```

This is particularly good for starting out with visualisation, as it can be hard to keep positions of long games in your head.

## Non macOS

I tried a bunch of different tts tools, but had trouble getting good quality recordings, so this is sadly no cross platform currently. My best results that would work anywhere came from coqui-tts so that might be worth a go if you are using Windows or Linux. The transcript can be generated in the same way, which may be a good starting point. Probably the only other thing to change would be to remove the blocks with [[slnc 1000]] which cause the macOS TTS to be silent for 1000ms but I'm sure this can be replaced by a pause in some other way.