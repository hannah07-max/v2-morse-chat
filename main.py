def on_logo_long_pressed():
    music.play(music.tone_playable(277, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_logo_pressed():
    music.play(music.tone_playable(784, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
# Dictionary to map integers to symbols
int_to_symbol = {
    1: ".",
    0: "_"
}

# Example usage
value1 = 1
value0 = 0

symbol1 = int_to_symbol[value1]
symbol0 = int_to_symbol[value0]

print("Symbol for 1:", symbol1)
print("Symbol for 0:", symbol0)
from microbit import *
import music

press_start_time = 0

# Diccionario para el Código Morse
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

def on_logo_pressed():
    global press_start_time
    press_start_time = running_time()

def on_logo_released():
    press_duration = running_time() - press_start_time
    if press_duration >= 1000:
        # Long press detected (1 second or more) - Dash
        music.play(music.tone_playable(277, music.beat(BeatFraction.WHOLE)),
                   music.PlaybackMode.UNTIL_DONE)
        display.show("-")
    else:
        # Short press detected (less than 1 second) - Dot
        music.play(music.tone_playable(784, music.beat(BeatFraction.QUARTER)),
                   music.PlaybackMode.UNTIL_DONE)
        display.show(".")

input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

# Función para reproducir código Morse para una letra dada
def play_morse(letter):
    code = morse_code.get(letter.upper())
    if code:
        for symbol in code:
            if symbol == '.':
                music.play(music.tone_playable(784, music.beat(BeatFraction.QUARTER)),
                           music.PlaybackMode.UNTIL_DONE)
                display.show(".")
            elif symbol == '-':
                music.play(music.tone_playable(277, music.beat(BeatFraction.WHOLE)),
                           music.PlaybackMode.UNTIL_DONE)
                display.show("-")
            sleep(500)  # Pausa entre símbolos

# Ejemplo de uso
play_morse('A')  # Reproduce el código Morse para 'A' que es .-
