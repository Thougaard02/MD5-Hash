
import hashlib
import os 
# Path to the folder structure
path = "C:\\Users\\rasmu\\Pictures\\Documents\\MD5-Hash-master"

files = []
# r = root, d = directories, f = files
for r, d, f in os.walk(path):
#Loopet gør at for hver gang der er en fil, går den ind og læser hvad der er i filen.
#Append tilføjer et element til slutning af listen
#join tager alle elementerne og slutter dem sammen i en string
	for file in f:
		files.append(os.path.join(r,file))
#Loopet gør for hver gang der er en fil encoder den filen til md5 hash og udskriver det i hexdicimial
for f in files:
	result = hashlib.md5(f.encode())
	final_hash = result.hexdigest()
	print(final_hash, f)





