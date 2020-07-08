
import hashlib
import os 
# Path to the folder structure
path = "C:\\Users\\rasmu\\Google Drev\\Coding\\MD5 Hash\\"

files = []
# r = root, d = directories, f = files
for r, d, f in os.walk(path):
# Making a for loop 
	for file in f:
		files.append(os.path.join(r,file))

for f in files:
	result = hashlib.md5(f.encode())
	final_hash = result.hexdigest()
	print(final_hash, f)





