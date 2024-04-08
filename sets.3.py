# 3. Music Festival Playlist Organization
# Objective:
# The aim of this assignment is to develop your skills in using Python loops with sets, particularly for organizing and managing playlists for a music festival. You will work with sets to handle various artists and genres, ensuring no duplicates and maintaining a well-organized collection.

# Task 1: Artist Lineup Compilation
# You are provided with a list of artist names scheduled to perform at different stages of the music festival. 
# Using a loop, compile these artist names into a set to create a unique lineup without duplicates.

# Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set(artist_names)
print(f"Here is the unique artist list! {unique_artists}")
# Expected Outcome:
# A set containing unique artist names, such as {'The Lumineers', 'Tame Impala', 'Billie Eilish', 'Arctic Monkeys'}.

# Task 2: Genre Sorting
# You have a list of genres associated with each artist. 
# Using a loop with sets, categorize artists by their genres, 
# creating a set for each genre.

# Example Code:

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}

genre_sets = {}

for artist, genre in artists_genres.items():
    if genre not in genre_sets:
        genre_sets[genre] = set()
    genre_sets[genre].add(artist)

for genre, artists in genre_sets.items():
    print(f"Genre: {genre}, Artists: {artists}")
    
# Expected Outcome:
# A categorization of artists by genres, such as Genre: Folk, Artists: The Lumineers.

# Task 3: 

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}
playlists = [playlist1, playlist2, playlist3]


def check_duplicates(playlists):
    for i in range(len(playlists)):
        for j in range(i+1, len(playlists)):
            if playlists[i] == playlists[j]:
                print(f"Playlist {i+1} is a duplicate of Playlist {j+1}")
                return
    else:
        print("No duplicates found")

check_duplicates(playlists)
        

