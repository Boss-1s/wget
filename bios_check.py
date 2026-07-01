import os
import hashlib
import zlib

# Change this if your file has a different name
file_path = "gba_bios.bin"

# Expected official values
EXPECTED_SIZE = 16384
EXPECTED_MD5 = "a860e8c0b6d573d191e4ec7db1b1e4f6"
EXPECTED_CRC32 = "81977335"

if not os.path.exists(file_path):
    print(f"Error: {file_path} not found in the current directory.")
else:
    # 1. Check File Size
    file_size = os.path.getsize(file_path)
    print(f"File Size: {file_size} bytes")
    
    # 2. Read file and calculate hashes
    with open(file_path, "rb") as f:
        file_data = f.read()
        
    md5_hash = hashlib.md5(file_data).hexdigest()
    sha256_hash = hashlib.sha256(file_data).hexdigest()
    # Format CRC32 as an 8-character lowercase hexadecimal string
    crc32_hash = format(zlib.crc32(file_data) & 0xffffffff, "08x")
    
    print(f"MD5:       {md5_hash}")
    print(f"CRC32:     {crc32_hash}")
    print(f"SHA-256:   {sha256_hash}")
    print("-" * 40)
    
    # 3. Validation Logic
    if file_size == EXPECTED_SIZE and md5_hash == EXPECTED_MD5:
        print("SUCCESS: This is a verified, authentic GBA BIOS file!")
    elif file_size == EXPECTED_SIZE and crc32_hash == "a6473709":
        print("SUCCESS: This is a valid GBA BIOS dumped from a Nintendo DS.")
    else:
        print("WARNING: File size or hashes do not match the official GBA BIOS.")
