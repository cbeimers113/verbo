"""Functions to translate verbo source to C++.  |  Funcioj pri la tradukado de fontkodo de verbo al C++."""
import os

from .data import BASE_SOURCE, VERBO_SRC_EXTENSION


def dump_source(name: str, source: str) -> None:
    """Append the given lines to the base source code.  |  Aldonu la frasojn donitjan al la baza fontkodo."""
    with open(name, 'w', encoding="utf-8") as f:
        f.write(BASE_SOURCE(source))


# TODO: Tokenizer


def temp(file):
    """Temporary function."""
    rules = {
        "!": ";",
        "montru": "std::cout << "
    }
    name = ""

    with open(file, 'r') as f:
        source = f.read()

        for src, dest in rules.items():
            source = source.replace(src, dest)

        name = file.replace(VERBO_SRC_EXTENSION, ".cpp")
        outname = name.replace(".cpp", "")
        dump_source(name, source)

    os.system(f"g++ {name} -o {outname}")
