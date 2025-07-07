# generate_files.py
import os

folder = "fake_files"
os.makedirs(folder, exist_ok=True)

for i in range(1, 101):  # Adjust range for number of files
    with open(f"{folder}/file_{i}.txt", "w") as f:
        f.write(f"This is fake file number {i}\n")
