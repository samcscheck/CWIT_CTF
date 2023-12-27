# YOU MAY NOT EDIT THIS FILE!
# YOU MAY NOT EDIT THIS FILE!
# YOU MAY NOT EDIT THIS FILE!

import os

def secret(a, b):
    result = ""
    for i in range(len(a)):
        result += chr(ord(a[i]) ^ ord(b[i % len(b)]))
    return result

def main():
    file_path = 'flag.txt'

    ctf_flag = "`3cw;iw\"QMW]|OWW"

    # Check if the file already exists
    if os.path.exists(file_path):
        # Write the CTF flag to the file
        with open(file_path, 'w') as file:
            file.write(secret(ctf_flag, "#d*"))
        print("CTF flag has been written to the file.")
    # If the file does not exist
    else:
        print("Sorry... Keep trying ;)")

if __name__ == "__main__":
    main()

# YOU MAY NOT EDIT THIS FILE!
# YOU MAY NOT EDIT THIS FILE!
# YOU MAY NOT EDIT THIS FILE!