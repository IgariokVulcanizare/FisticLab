import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_candidate(length):
    # Generate an odd integer randomly
    candidate = random.getrandbits(length)
    candidate |= (1 << length - 1) | 1
    return candidate

def generate_prime_number(length=8):
    candidate = 4
    while not is_prime(candidate):
        candidate = generate_prime_candidate(length)
    return candidate

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keypair(keysize):
    p = generate_prime_number(keysize // 2)
    q = generate_prime_number(keysize // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

if __name__ == "__main__":
    keysize = 50

    print("Generating keypair...")
    public_key, private_key = generate_keypair(keysize)
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter a message to encrypt: ")
    encrypted_msg = encrypt(public_key, message)

    remove_formatting = True

    if remove_formatting:
        encrypted_output = ' '.join(map(str, encrypted_msg))
    else:
        encrypted_output = str(encrypted_msg)

    print("Encrypted message:", encrypted_output)

    if remove_formatting:
        decrypted_msg = decrypt(private_key, list(map(int, encrypted_output.split())))
    else:
        decrypted_msg = decrypt(private_key, encrypted_msg)

    print("Decrypted message:", decrypted_msg)
