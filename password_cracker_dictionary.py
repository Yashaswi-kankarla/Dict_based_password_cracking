import hashlib
def read_dictionary(file_path):
    with open(file_path, 'r')as file:
        return[line.strip()for line in file]
def hash_password(password):
    return(hashlib.sha256(password.encode()).hexdigest())
def crack_password(target_hash,dictionary):
    for word in dictionary:
        hashed_word=hash_password(word)
        if hashed_word==target_hash:
            return word
    return None
if __name__=="__main__":
    target_hash="fad222245f7dcb62e36f6ffef32f9c7e926b5e5ec4819a95e40141b513782e53"
    dictionary_file="password_cracker_dictionary.txt"
    dictionary=read_dictionary(dictionary_file)
    cracked_password=crack_password(target_hash,dictionary)
    if cracked_password:
        print(f"Password cracked! The password is:{cracked_password}")
    else:
        print("Password not found in the dictionary.")