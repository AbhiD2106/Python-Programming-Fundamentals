import os
import time

print("=" * 50)
print("OS MODULE EXAMPLES")
print("=" * 50)

# 1. Current Working Directory
print("\n1. Current Directory")
print(os.getcwd())

# 2. Create Folder
print("\n2. Create Folder")
if not os.path.exists("Demo"):
    os.mkdir("Demo")
    print("Demo folder created")

# 3. Create Nested Folders
print("\n3. Create Nested Folders")
if not os.path.exists("path"):
    os.makedirs("path")
    print("Nested folders created")

# 4. List Files and Folders
print("\n4. List Directory")
print(os.listdir())

# 5. Check Path Exists
print("\n5. Check Path")
print(os.path.exists("Demo"))

# 6. Check Folder
print("\n6. Is Directory?")
print(os.path.isdir("Demo"))

# 7. Create File
print("\n7. Create File")
with open("sample.txt", "w") as f:
    f.write("Hello Python")

print("sample.txt created")

# 8. Check File
print("\n8. Is File?")
print(os.path.isfile("sample.txt"))

# 9. Absolute Path
print("\n9. Absolute Path")
print(os.path.abspath("sample.txt"))

# 10. Join Path
print("\n10. Join Path")
path = os.path.join("Demo", "test.txt")
print(path)

# 11. File Size
print("\n11. File Size")
print(os.path.getsize("sample.txt"), "bytes")

# 12. Modified Time
print("\n12. Last Modified Time")
t = os.path.getmtime("sample.txt")
print(time.ctime(t))

# 13. Rename File
print("\n13. Rename File")
os.rename("sample.txt", "data.txt")
print("sample.txt -> data.txt")

# 14. Split Path
print("\n14. Split Path")
print(os.path.basename("Demo/test.txt"))
print(os.path.dirname("Demo/test.txt"))
print(os.path.splitext("Demo/test.txt"))

# 15. Environment Variable
print("\n15. PATH Variable")
print(os.environ.get("PATH"))

# 16. CPU Count
print("\n16. CPU Count")
print(os.cpu_count())

# 17. Process ID
print("\n17. Process ID")
print(os.getpid())

# 18. Walk Directory
print("\n18. Walk Directory")
for root, dirs, files in os.walk("."):
    print("Folder:", root)
    print("Directories:", dirs)
    print("Files:", files)
    print("-" * 30)

# 19. Remove File
print("\n19. Remove File")
os.remove("data.txt")
print("data.txt deleted")

# 20. Remove Empty Folders
print("\n20. Remove Folders")
os.rmdir("Demo")
os.removedirs("path")
print("Folders deleted")

print("\nProgram Finished Successfully!")