# Playlist creation and processing

This python project works with the list of tracks, it:

### 1. Creates list of tracks
### 2. Creates a remix of the last track and adds it to the list
- the remix creation is logged
### 3. Randomly reorders track items if user wants to
### 4. Creates a 32 character long playlist hash
### 5. Converts the playlist to a dataframe
### 6. Depending on user decision either ignores this step or visualizes the report:
- average and max loudness
- loudness horizontal bar chart
- total and average duration
- duration pie chart
### 7. Saves the playlist in the csv/excel/json format if user wants to

---

# Additional comments
### 1. The project is divided into folders:
- "code" for the source code
- "log" for logging remix creations
- "save" for storing the final playlist dataframe
### 2. The project uses two custom modules:
- "track" for handling track data easily
- "storage" for handling paths, dataframe storage, and logging