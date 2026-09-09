from pseudoenglish import analyze_text, TextGenerator
from collections import Counter
from random import choices

class CustomTextGenerator(TextGenerator):
    def determine_next_word(self) -> str:
        total_weights: Counter[str] = Counter()

        reach = min(len(self.history) - 1, 5)

        total_weights["a"] = 1

        for word, distance in map(lambda x: (self.history[-x - 1], x), range(reach)):
            print(word, distance)

        return choices(list(total_weights.keys()), list(total_weights.values()), k=1)[0]

data = ""

for file in ["shrek.txt", "seals.txt", "bees.txt"]:
    with open(file, "r", encoding="utf8") as f:
        data += f.read()

analysis = analyze_text(data, 3)
generator = CustomTextGenerator(analysis.lingo)

print(generator.generate_text("Shrek!", 1))
