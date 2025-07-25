# French-Flash-Cards
A Python Tkinter flashcard app to learn French words with English meanings. Shows a French word, flips to English after 3s. Known words are removed from the list to track progress. Uses pandas for data handling. Simple, effective vocabulary learning tool.

The code implements a French-English flashcard learning app with:

Random word selection

Automatic card flipping after 3 seconds

User marking known words (removing them from learning list)

Persistent progress saving via CSV updates

Intuitive GUI with image-backed cards and action buttons

#Code Details

✅ Imports:

tkinter for GUI

pandas for data handling

random for random selection

✅ Data Handling:

Reads words from Words_to_learn.csv if present, else from french_words.csv.

Converts CSV data to a list of dictionaries (dict_data) for easy access.

✅ Core Functions:

word_selection()

Cancels any running flip timer.

Selects a random French word.

Updates canvas with French word and image.

Starts a 3-second timer to flip the card.

flip_card()

Changes the card to show the English meaning after 3 seconds.

Updates image and text to English meaning.

is_known()

Removes the known word from data.

Updates Words_to_learn.csv with remaining words.

Generates a new random word.

✅ UI Features:

Tkinter window with title “Flash Card” and background colour #B1DDC6.

Uses Canvas to display cards:

Front and back images (card_front.png and card_back.png).

French/English words shown dynamically.

Buttons:

✅ Right button (calls is_known) – marks word as known.

❌ Wrong button (calls word_selection) – skips to next word.

✅ Timer Functionality:

Uses window.after to set 3-second auto flip timer.

Uses window.after_cancel to cancel previous timer before starting a new one.

✅ File Structure Assumption:

Images:

./images/card_front.png

./images/card_back.png

./images/right.png

./images/wrong.png

Data:

./data/french_words.csv

./data/Words_to_learn.csv
