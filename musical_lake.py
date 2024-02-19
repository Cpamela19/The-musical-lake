# Dictionary mapping animal sounds to the remaining sounds of each song
songs = {
    'brr': ['fiu', 'cric-cric', 'brrah'],
    'fiu': ['cric-cric', 'brrah'],
    'cric-cric': ['brrah'],
    'brrah': [''],
    'pep': ['birip', 'trri-trri', 'croac'],
    'birip': ['trri-trri', 'croac'],
    'trri-trri': ['croac'],
    'croac': [''],
    'bri-bri': ['plop', 'cric-cric', 'brrah'],
    'plop': ['cric-cric', 'brrah']
}

def get_remaining_sounds(sound_given):
    # Check if the given sound is in the dictionary
    if sound_given in songs:
        return songs[sound_given]
    else:
        return []

# Request the user to enter a sound
sound_given = input("Enter a sound: ")

# Get the remaining sounds
remaining_sounds = get_remaining_sounds(sound_given)

# Print the remaining sounds
if remaining_sounds:
    print(", ".join(remaining_sounds))
else:
    print("No sounds available")
