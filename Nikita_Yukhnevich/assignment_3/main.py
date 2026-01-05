import random
import playlist_manager as pm

# create directory for playlists
playlists_dir = "my_playlists"
pm.create_directory(playlists_dir)

print("=== music playlist manager ===\n")

# create workout playlist
workout_songs = [
    "Dua Lipa - Levitating",
    "The Weeknd - Blinding Lights",
    "Doja Cat - Woman",
    "Travis Scott - SICKO MODE"
]
pm.save_playlist(f"{playlists_dir}/workout.txt", workout_songs)

# create chill vibes playlist
chill_songs = [
    "Frank Ocean - Pink + White",
    "Tyler, The Creator - See You Again",
    "Mac Miller - Come Back to Earth"
]
pm.save_playlist(f"{playlists_dir}/chill_vibes.txt", chill_songs)

# add more songs to workout
print("\nadding song to workout:")
pm.add_to_playlist(f"{playlists_dir}/workout.txt", "Kendrick Lamar - HUMBLE")

# list all playlists
print("\nyour playlists:")
all_playlists = pm.list_playlists(playlists_dir)
for playlist in all_playlists:
    print(f"- {playlist}")

# read and display a playlist
print("\nshowing chill vibes:")
chill_content = pm.read_playlist(f"{playlists_dir}/chill_vibes.txt")
pm.display_playlist("chill vibes", chill_content)

# shuffle workout playlist using random library
print("\nshuffled workout:")
workout_content = pm.read_playlist(f"{playlists_dir}/workout.txt")
shuffled = workout_content.copy()
random.shuffle(shuffled)
pm.display_playlist("workout (shuffled)", shuffled)

# random song picker
print("\nrandom song of the day:")
random_playlist = random.choice(all_playlists)
random_songs = pm.read_playlist(f"{playlists_dir}/{random_playlist}")
random_song = random.choice(random_songs)
print(f"from '{random_playlist}': {random_song}")

print("\ndone!")