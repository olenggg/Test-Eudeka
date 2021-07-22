sentence = input("Masukkan Kata:")

for char in range(len(sentence) - 1, -1, -1):
    print(sentence[char], end="")
print("\n")