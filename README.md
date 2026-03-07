HOPLITE_2
This is a simple MP3 player featuring a live queue. once a sohg is added to the queue, it will automatically start playing and will continue to play as other songs are added over time. 
I stripped this player down to the bare essentials. The 'Song Hoard List' displays the file names of the mp3 files. It is suggested to use the mp3_file_renamer utility to ensure consistent naming of files.
Once your music library is loaded, simply highlight one song at a time and push the 'Add To Queue' button to add it to the play-list. 

mp3_file_renamer.py
This is a 'mostly' Gemini generated utility that uses the Python tinytag library to retrieve artist and title tags from .mp3 metadata and rename the file as 'artist-title.mp3'
This ensures consistant nameing of music files, which allows the file name to be displayed in an mp3 player without having to retrieve the metadata during operation.
