def secret(a, b):
    result = ""
    for i in range(len(a)):
        result += chr(ord(a[i]) ^ ord(b[i % len(b)]))
    return result

def main():
    ctf_flag = "1j;i-~&{	YAS@"
    decrypted = secret(ctf_flag, "r=")
print(decrypted)

if __name__ == "__main__":
    main()