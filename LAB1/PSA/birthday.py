import string
import random
import hashlib

def generate_collision_md5(bits):
    k=0
    seen_hashes={}
    num_hexa_char = bits // 4 #hex digit = 4 bits

    while (True):
        #generate a string and encode it
        rand_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8)).encode()
        md5_hash = hashlib.md5(rand_string).hexdigest()
        truncated_hash = md5_hash[:num_hexa_char]

        if truncated_hash in seen_hashes:
            return rand_string.decode(), seen_hashes[truncated_hash],k
        else:
            seen_hashes[truncated_hash] = rand_string.decode()
            k+=1

same_hash_1, same_hash_2, number_of_atempts = generate_collision_md5(20)
print("Here are the strings: ",same_hash_1, same_hash_2)
print("Here the hashes, see that first 5 characters coincide: ",hashlib.md5(same_hash_1.encode()).hexdigest(),
      hashlib.md5(same_hash_2.encode()).hexdigest())
print("number of attempts: ",number_of_atempts)

same_hash_1, same_hash_2, number_of_atempts = generate_collision_md5(40)
print("Here are the strings: ",same_hash_1, same_hash_2)
print("Here the hashes, see that first 10 characters coincide: ",hashlib.md5(same_hash_1.encode()).hexdigest(),
      hashlib.md5(same_hash_2.encode()).hexdigest())
print("number of attempts: ",number_of_atempts)