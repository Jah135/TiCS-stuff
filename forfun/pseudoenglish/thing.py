from pseudoenglish import analyze_text_patterns, generate_text

def intput(prompt: str, default: int | None = None) -> int:
	while True:
		try:
			text = input(prompt)

			if text == "" and default != None:
				return default

			return int(text)
		except:
			print("Invalid integer.")

INPUT_DATA = ""


while True:
	try:
		file_name = input("Target file: ")
		with open(file_name, "+r") as f:
			print(f"Reading file '{file_name}'...\n")

			INPUT_DATA += f.read()

			break
	except Exception:
		print("Invalid file.")


PATTERN_SIZE = intput("Pattern size (default 6): ", 6)
READBACK_SIZE = intput("Readback size (default 6): ", 6)
TOKEN_SIZE = intput("Token size (default 3): ", 3)

pattern_associations = analyze_text_patterns(INPUT_DATA, PATTERN_SIZE, TOKEN_SIZE)

print(f"\nInput Data Size: {len(INPUT_DATA)}\nAssociation Count: {len(pattern_associations)}\n\nPattern Size: {PATTERN_SIZE}\nReadback Size: {READBACK_SIZE}\nToken Size: {TOKEN_SIZE}\n")

while True:
	seed = input("Input seed: ")
	count = intput("Input count: ")

	output_text = generate_text(pattern_associations, seed, count, READBACK_SIZE)
	print(f"{'-' * 50}\n{output_text}\n{'-' * 50}")