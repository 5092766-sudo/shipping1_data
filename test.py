import os

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

with open("product level.csv", "r") as f:
    print("CSV Found Successfully")