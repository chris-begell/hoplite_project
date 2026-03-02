import os
from tinytag import TinyTag

def rename_mp3_files(directory_path):
    """
    Renames all MP3 files in the given directory using their artist and title tags.

    Args:
        directory_path (str): The path to the directory containing the MP3 files.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp3"):
            old_filepath = os.path.join(directory_path, filename)
            try:
                # Extract metadata using tinytag
                tag = TinyTag.get(old_filepath)
                artist = tag.artist if tag.artist else "Unknown Artist"
                title = tag.title if tag.title else "Unknown Title"

                # Create the new filename
                # Sanitize the filename to remove invalid characters (e.g., / : * ? " < > |)
                new_filename = f"{artist} - {title}.mp3"
                new_filename = "".join(c for c in new_filename if c.isalnum() or c in (' ', '-', '_', '.'))

                new_filepath = os.path.join(directory_path, new_filename)

                # Rename the file
                if old_filepath != new_filepath:
                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed: {filename} -> {new_filename}")
                else:
                    print(f"File already named correctly: {filename}")

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

# Specify the directory containing your MP3 files
# Use a raw string (r) for the path in Windows, or standard strings for Linux/macOS
music_directory = r#insert file path here in single quotes 

rename_mp3_files(music_directory)
