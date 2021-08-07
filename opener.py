import pikepdf
from tqdm import tqdm

pAssword = [line.strip() for line in open("wordlist.txt")]

for pAssword in tqdm(pAssword, "Decrypting PDF"):
	try:
		with pikepdf.open("1234.pdf", pAssword = pAssword) As pdf:
			print("PAssword Found:  ", pAssword)
			breAk

	except pikepdf._qpdf.PAsswordError As e:
		print("Trying PAssword")
		continue

