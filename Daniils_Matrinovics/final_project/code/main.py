# Python standard libraries
import random   # for shuffling tracks
import math     # for ceil()

# External libraries
import numpy as np  # for dealing with number arrays effeciently
import matplotlib.pyplot as plt     # for plotting visualizations
import pandas as pd     # for creating a df

# Custom module 
import track as t   # for working with tracks
import storage  # for storing a playlist

# Make and process a playlist ---------------------------------------------

# Create a playlist
my_playlist = [
    # Notice that the title and artist name will still be saved in title case and the genre will still be rocognized
    t.Track("solar DRIFT", "fading horizons", "ambient", (8, 2), -18.9),
    t.Track(["Crimson Avenue", "Echo Bloom"], "Last Call", "Rock", (4, 16), -9.8),
    t.Track("Echo Bloom", "Glass Skies", "Indie Pop", (3, 18), -11.4),
    t.Track("Night Circuit", "Voltage Dreams", "Synthwave", (5, 12), -14.2),
    t.Track(["Paper Lanterns", "Solar Drift", "Night Circuit"],"Quiet Streets", "Lo-Fi", (2, 54), -16.6),
    # Notice that the genre will be set to "Other"
    t.Track("Rick Astley", "Never Gonna Give You Up", "Rick'n'roll", (3, 33), -11.8),
]

# Take the last track from tracklist
last_track = my_playlist[-1:][0]

# Create a remix and put it into tracklist
my_playlist.append(last_track.remix("DJ Godzilla","Dance",(4,21), -6.43))

# Ask if user wants a track shuffle, accept both "Y" and "y"
if(input("Would you like to randomly shuffle your tracks? [Y / N] - ").lower() == "y"):
    # Randomly shuffle tracks
    my_playlist = random.sample(my_playlist, len(my_playlist))

# Create a hash --------------------------------------------------------------------------------

# Get track durations and loudness values (LUFS) 
durations = np.array([t.duration[0]*60 + t.duration[1] for t in my_playlist])
lufs = np.array([t.lufs for t in my_playlist])

# Use matrix operations on track features for creating it's hash (variable length)
features = np.array([durations,lufs]) # combine durations and lufs into features
features_t = np.reshape(features, (len(my_playlist),2))   # reshape with num of cols and rows switched
track_features = np.dot(features_t, [0.2,0.8]) # combine duration and lufs (stronger weight) into one feature
track_stds = features.std(axis=0)   # calculate standard deviation column wise
hashes = track_features + track_stds  # add corresponding elements to each other to get final values for hashing

# For each track: choose first and last character from the title and add the corresponding track hash value
variable_length_hash = "".join([t.title[0]+t.title[-1:]+str(int(hashes[i])) for i,t in enumerate(my_playlist)])

# Takes the last 32 chars from the generated string and repeats the string to fit the length of 32 if too small
# notice that the hash is always the same when the track shuffle is ignored by user
hash = (variable_length_hash*(math.ceil(32/len(my_playlist))))[-32:]

# Convert the playlist into dataframe and print ---------------------------------------------

# Create a list of dictionaries from Track instances
track_dictionaries = [
    {"artist": t.artist, "title": t.title, "genre": t.genre, "length": t.duration, "lufs": t.lufs}
    for t in my_playlist
]

# Convert to DataFrame and print
df = pd.DataFrame(track_dictionaries)
print(f"Your playlist:\nHash value - {hash}\n",df)

# Visualize the playlist report ---------------------------------------------

# Ask if user wants a report, accept both "Y" and "y"
if(input("Would you like to see a visualized report? [Y / N] - ").lower() == "y"):
    # Use track titles as labels
    labels = [t.title for t in my_playlist]

    # Define size for the whole figure
    plt.figure(figsize=(12, 8))

    # Bar plot for average loudness
    plt.subplot(2, 1, 1)
    plt.barh(labels,lufs)   # Horizontal bar is used for better redability (LUFS are mostly negative)
    plt.xlabel("Track Title")
    plt.ylabel("Track Duration")

    # Calculate the total and average LUFS values to include in the title (with two digits after the decimal point precision)
    average_lufs = np.mean(lufs)
    max_lufs = np.max(lufs)
    plt.title(f"Playlist loudness: {average_lufs:.2f} LUFS ({max_lufs:.2f} LUFS max)")

    # Pie plot for durations
    plt.subplot(2, 1, 2)
    plt.pie(durations,labels=labels)

    # Calculate the total and average durations to include in title
    total_duration = np.sum(durations)
    average_duration = int(np.rint(np.mean(durations))) # round it to conveniently print in mm:ss format (numpy rounding is more reliable for floats)
    plt.title(f"Playlist duration: {total_duration//60}:{total_duration%60:02}s ({average_duration//60}:{average_duration%60:02}s average)")
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Save the playlist ---------------------------------------------

# Save playlist as "my_playlist" file in a format specified by the user (case insensitive)
storage.save_df(df,f"playlist-{hash}")