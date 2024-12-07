def basic_encrypt(mes, key):
    m = ord(mes)
    k = ord(key)
    em = m * k
    return em

def main():
    print(basic_encrypt("a", "a"))

if __name__ == "__main__":
    main()
