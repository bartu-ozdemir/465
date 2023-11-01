from ceaser import compute_cipher

keyboard_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotorI = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotorII = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotorIII = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotorIV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotorV = "VZBRGITYUPSDNHLXAWMJQOFECK"
reflector_A = "EJMZALYXVBWFCRQUONTSPIKHGD"
reflector_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflector_C = "FVPJIAOYEDRZXWGCTKUQSBNMHL"


class Enigma:
    def __init__(self, keyboard, plugboard, rotor_list, reflector):
        self.keyboard = keyboard
        self.plugboard = plugboard
        self.rotor_list = rotor_list
        self.reflector = reflector


class Keyboard:
    def __init__(self, signal, alphabet):
        self.signal = signal
        self.alphabet = alphabet

    def receive_signal(self):
        print(self.signal)


class Plugboard:
    output = ""
    plug_alphabet = keyboard_alphabet

    def __init__(self, sub_pairs):
        self.sub_pairs = sub_pairs

    def generate_output(self):
        return self.output

    def substitute(self):
        return compute_cipher(0, self.sub_pairs, True)


class Rotor:
    def __init__(self, alphabet, starting_point, notch_point, turnover_count):
        self.alphabet = alphabet
        self.starting_point = starting_point
        self.notch_point = notch_point
        self.turnover_count = turnover_count


class Reflector:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def reflect(self):
        return "1"


filename = "settings"
settings = []

with open(filename) as settings_file:
    for line in settings_file:
        settings.append(line.rstrip("\n"))

rotors = settings[0].split("-")
reflector_type = settings[1]
starting_points = list(settings[2])
ring_positions = settings[3].split(",")
subs_pairs = settings[4].split(" ")
input_text = "selamlar"

def set_all(rotors, reflector_type, starting_points, ring_positions, subs_pairs, input_text):
    rotor_number = len(rotors)
    rotor_alphabet = ""
    notch_point = ""
    rotor_list = []
    if reflector_type == "A":
        reflector_alphabet = reflector_A
    if reflector_type == "B":
        reflector_alphabet = reflector_B
    if reflector_type == "C":
        reflector_alphabet = reflector_C

    keyboard = Keyboard(input_text, keyboard_alphabet)
    plugboard = Plugboard(subs_pairs)
    reflector = Reflector(reflector_alphabet)
    for i in range(0, rotor_number):
        if rotors[i] == "I":
            rotor_alphabet = rotorI
            notch_point = "Q"
        if rotors[i] == "II":
            rotor_alphabet = rotorII
            notch_point = "E"
        if rotors[i] == "III":
            rotor_alphabet = rotorIII
            notch_point = "V"
        if rotors[i] == "IV":
            rotor_alphabet = rotorIV
            notch_point = "J"
        if rotors[i] == "V":
            rotor_alphabet = rotorV
            notch_point = "Z"
        rotor = Rotor(rotor_alphabet, starting_points[i], notch_point, turnover_count=int(ring_positions[i]))
        rotor_list.append(rotor)

    return keyboard, plugboard, rotor_list, reflector


if __name__ == "__main__":
    print("1")
    keyboard, plug, rotor_list, reflector = set_all(rotors, reflector_type, starting_points, ring_positions,
                                                    subs_pairs, input_text)
    enigma = Enigma(keyboard, plug, rotor_list, reflector)
