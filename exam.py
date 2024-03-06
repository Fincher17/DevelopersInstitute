from utils import unzip_with_7z

zip_file_path = 'congrats.7z'  # keep as is
dest_path = '.'  # keep as is

find_me = ''  # 2 letters are missing!
secret_password = find_me + 'bcmpda'

# WRITE YOUR CODE BELOW
# ----------------------------------------
letters = [chr(c) for c in range(97, 123)]

def brute_force():
    for i in letters:
        for j in letters:
            password = i + j + secret_password
            if unzip_with_7z(zip_file_path, dest_path, password):
                return f'Missing part of password is {i + j}'


print(brute_force())
