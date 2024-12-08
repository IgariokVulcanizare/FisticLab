def find_key_length(ciphertext):
    def calculate_ic(text):
        n = len(text)
        freqs = [text.count(chr(i)) for i in range(65, 91)]
        if n <= 1:
            return 0
        ic = sum(f * (f - 1) for f in freqs) / (n * (n - 1))
        return ic

    likely_lengths = []
    for key_length in range(1, 21):
        groups = [''.join(ciphertext[i::key_length]) for i in range(key_length)]
        avg_ic = sum(calculate_ic(group) for group in groups) / key_length
        if avg_ic > 0.06:
            likely_lengths.append(key_length)

    return likely_lengths


def find_key(ciphertext, key_length):
    key = ""
    english_frequencies = {
        'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228,
        'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025,
        'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987,
        'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
        'Y': 1.974, 'Z': 0.074
    }
    for i in range(key_length):
        group = ''.join(ciphertext[j] for j in range(i, len(ciphertext), key_length))
        best_shift = 0
        highest_score = float('-inf')
        for shift in range(26):
            shifted_group = ''.join(chr((ord(c) - shift - 65) % 26 + 65) for c in group)
            score = sum(shifted_group.count(letter) * english_frequencies.get(letter, 0) for letter in shifted_group)
            if score > highest_score:
                highest_score = score
                best_shift = shift
        key += chr((26 - best_shift) % 26 + 65)
    return key



def decrypt_vigenere(ciphertext, key):
    key = (key * (len(ciphertext) // len(key) + 1))[:len(ciphertext)]
    plaintext = ''.join(chr((ord(c) - ord(k) + 26) % 26 + 65) for c, k in zip(ciphertext, key))
    return plaintext


if __name__ == "__main__":
    ciphertext = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"
    key_lengths = find_key_length(ciphertext)
    print(f"Likely key lengths: {key_lengths}")
    if key_lengths:
        key_length = key_lengths[0]
        key = find_key(ciphertext, key_length)
        print(f"Derived key: {key}")

        plaintext = decrypt_vigenere(ciphertext, key)
        print(f"Decrypted message: {plaintext}")
    else:
        print("Unable to determine key length. Attempting brute force.")

        for brute_key_length in range(1, 21):
            key = find_key(ciphertext, brute_key_length)
            plaintext = decrypt_vigenere(ciphertext, key)
            print(f"Trying key length {brute_key_length}: Key = {key}, Decrypted = {plaintext}")