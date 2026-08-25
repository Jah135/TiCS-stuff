from ANSI import tint, Palette, PaletteColor

# this program encodes scenes as a not-so-binary tree or DAG (directed acyclic graph)
# with branch-specific classes that store description text for each choice
# this way of formatting is not very readable but luckily it doesnt need to be for the program to run :)


class SceneChoice:
    text: str
    resulting_scene: Scene

    def __init__(self, text: str, resulting_scene: Scene) -> None:
        self.text = text
        self.resulting_scene = resulting_scene


class Scene:
    text: str
    choices: list[SceneChoice]

    def __init__(self, text: str, choices: list[SceneChoice]) -> None:
        self.text = text
        self.choices = choices


ROOT_SCENE = Scene(
    "you're taking an absolutely wonderful stroll through the forest when suddenly you're jumped by a gang of GOBLINS!!!!!!!! what do you do?",
    [
        SceneChoice(
            "scream and run around in circles",
            Scene(
                "SCENE 1 TEXT",
                [
                    SceneChoice("OPTION TEXT 1-1", Scene("SCENE 1-1 TEXT", [])),
                    SceneChoice("OPTION TEXT 1-2", Scene("SCENE 1-2 TEXT", [])),
                ],
            ),
        ),
        SceneChoice("OPTION TEXT 2", Scene("SCENE 2 TEXT", [])),
    ],
)


def run_scene(scene: Scene):
    print("\n---------------------------------------\n\n" + scene.text)

    num_scene_choices = len(scene.choices)

    if num_scene_choices == 0:
        print("\n" + tint("Game over!", Palette(PaletteColor.Red), True))
        return

    print("\nChoices:")
    for index, choice in enumerate(scene.choices):
        print(tint(str(index + 1) + ". ", Palette(PaletteColor.Yellow)) + choice.text)

    while True:
        user_choice = input(
            "\n" + tint("Make a choice: ", Palette(PaletteColor.BrightMagenta))
        )

        try:
            choice_index = int(user_choice) - 1

            if choice_index < 0 or choice_index >= num_scene_choices:
                raise Exception("hell")  # raise hell, metaphorically

            chosen_choice = scene.choices[choice_index]
            break
        except:
            print(
                tint(
                    "Invalid choice! Enter a valid choice index.",
                    Palette(PaletteColor.BrightRed),
                )
            )

    run_scene(chosen_choice.resulting_scene)  # recursion maxxing


run_scene(ROOT_SCENE)
