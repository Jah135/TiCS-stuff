from pseudoenglish import analyze_text, AbstractTextGenerator
from random import choices


class tg(AbstractTextGenerator):
    def determine_next_word(self) -> str:
        total_weights: dict[str, float] = dict()

        reach = min(len(self.history), self.lingo.window_size)

        for word, distance in map(lambda x: (self.history[-x - 1], x), range(reach)):
            weights = self.lingo.get_future_associations(word, distance)
            total_weights.update(
                {
                    key: (weight / (distance + 1)) ** 2
                    for (key, weight) in weights.items()
                }
            )

        return choices(list(total_weights.keys()), list(total_weights.values()), k=1)[0]


data = ""

for file in ["seals.txt"]:
    with open(file, "r", encoding="utf8") as f:
        data += f.read()

analysis = analyze_text(data, 1)

print(analysis.word_set)
# print(analysis.lingo.get_future_associations("the", 1))

# generator = tg(analysis.lingo)
# print(generator.generate_text("the", 200))
