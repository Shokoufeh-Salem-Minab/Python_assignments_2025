import os

# save playlist to a file
def save_playlist(filename, songs):
    with open(filename, 'w') as f:
        for song in songs:
            f.write(f"{song}\n")
    print(f"saved playlist to {filename}")

# read playlist from a file
def read_playlist(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            songs = [line.strip() for line in f.readlines()]
        return songs
    else:
        print(f"playlist {filename} not found")
        return []

# add song to existing playlist
def add_to_playlist(filename, song):
    with open(filename, 'a') as f:
        f.write(f"{song}\n")
    print(f"added '{song}' to playlist")

# create playlist directory
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"created directory: {directory}")

# list all playlists in directory
def list_playlists(directory):
    if os.path.exists(directory):
        files = [f for f in os.listdir(directory) if f.endswith('.txt')]
        return files
    return []

# display playlist
def display_playlist(playlist_name, songs):
    print("=" * 40)
    print("playlist:", playlist_name)
    print("total songs:", len(songs))
    print("=" * 40)
    for i in range(len(songs)):
        print(f"{i+1}. {songs[i]}")
    print("=" * 40)
    print()