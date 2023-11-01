import sys

"""process = sys.argv[1]
filename= sys.argv[2]
key = sys.argv[3]"""
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET_SIZE = 26


def look_up(alphabet, target):
    for item in range(0, len(alphabet)):
        if alphabet[item] == target.lower() or alphabet[item] == target.upper():
            return item
    return -1


"@Part One"


def compute_cipher(n, pairs = None, is_subs = False):
    resulting_alphabet = [""] * ALPHABET_SIZE
    if not is_subs:
        for item in range(0, len(ALPHABET)):
            if item + n > ALPHABET_SIZE - 1:
                resulting_alphabet[item + n - ALPHABET_SIZE] = ALPHABET[item]
            else:
                resulting_alphabet[item + n] = ALPHABET[item]
        return resulting_alphabet
    else:
        resulting_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for item in range(0, len(pairs)):
            matching_pairs = list(pairs[item])
            index = look_up(ALPHABET, matching_pairs[0])
            resulting_alphabet[index] = matching_pairs[1].lower()
        return resulting_alphabet


def encrypt_char(alphabet, cipher, ch):
    if ch.isalpha():
        index = look_up(alphabet, ch)
        if index != -1:
            if ch.islower():
                return cipher[index]
            else:
                return cipher[index].upper()
    return ch


def encrypt_str(alphabet, cipher, s):
    str_arr = list(s)
    result = ""
    for ch in range(0, len(str_arr)):
        result += encrypt_char(alphabet, cipher, str_arr[ch])
    return result


def decrypt_str(alphabet, cipher, s):
    str_arr = list(s)
    result = ""
    for ch in range(0, len(str_arr)):
        result += encrypt_char(alphabet, cipher, str_arr[ch])
    return result


"""
def encrypt_file(filename, alphabet, n):


def decrypt_file(filename, alphabet, n):
"""

"""
if process.lower() == "-encrypt":
    print("b")

elif process.lower() == "-decrypt":
    print("a")
else:

    print("unknown command")"""


#part1
#arr = compute_cipher(20)
#encrypted = encrypt_str(ALPHABET, arr, "Et tu, Brute?")
#print(encrypted)

#part2
arr2 = ["AR", "GK", "OX"]
temp = compute_cipher(20, arr2, is_subs=True)
encrypted = encrypt_str(ALPHABET, temp, "agoago")
