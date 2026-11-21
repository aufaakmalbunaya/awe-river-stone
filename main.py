"""Write one short relaxing text to /output/entry.txt.

Python 3.13, standard library only, no network.
The text is a single quiet image: a river stone kept warm in a pocket,
and the river still moving somewhere far away, in no hurry.
"""

import os

TEXT = (
    "A river stone, held all afternoon in a warm pocket, keeps a little "
    "of the sun after dark. You turn it over once. Somewhere the river "
    "is still moving, patient as ever, in no hurry to arrive."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
