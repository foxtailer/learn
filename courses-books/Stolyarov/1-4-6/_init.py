import struct


numbers = [1000 + i * 1001 for i in range(100)]


# --- text file ---
with open("numbers.txt", "w", encoding="utf-8") as f:
    for n in numbers:
        f.write(f"{n}\n")


# --- binary file ---
with open("numbers.bin", "wb") as f:
    for n in numbers:
        f.write(struct.pack("i", n))   # "i" = 4-byte signed int


# --- to read binary ---
"""
with open("numbers.bin", "rb") as f:
    while chunk := f.read(4):
        print(struct.unpack("i", chunk)[0])
"""

