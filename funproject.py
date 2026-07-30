import sys
import time

def print_lyrics():
    lyrics = [
        "Tujhse door main ek hi wajah ke liye hoon",
        "Kamzor ho jaata hoon main",
        "Tujhse door main ek hi wajah ke liye hoon",
        "Aawara ban jaata hoon main",
        "Tujhe choo loon toh kuch mujhe ho jaayega",
        "Jo main chahta na ho mujhko",
        "Tujhe milke yeh dil mera beh jaayega",
        "Isi baat ka darr hai mujhko",
        "Ke ho na jaaye pyaar tumse mujhe",
        "Kar dega barbaad ishq mujhe",
        "Ho na jaaye pyaar tumse mujhe",
        "Behad beshumar tumse mujhe",
    ]

    # Replace with your measured durations
    line_durations = [6.0, 3.0, 6.0, 4.0, 7.0, 4.0, 6.0, 4.0, 6.0, 7.0, 6.0, 6.0]

    for i, line in enumerate(lyrics):
        total_time = line_durations[i]
        char_delay = total_time / len(line)
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()

print_lyrics()