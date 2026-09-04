from pseudoenglish import analyze_text, TextGenerator

data = ""

for file in ["shrek.txt", "seals.txt", "bees.txt"]:
    with open(file, "r", encoding="utf8") as f:
        data = f.read()

analysis = analyze_text(data, 1)
generator = TextGenerator(analysis.lingo)

print(generator.generate_text("Thinking", 500))
