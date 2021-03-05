"""Store constants that are used throughout the program.  |  Enhavu konstantojn kiuj uziĝas per la programo."""

VERBO_SRC_EXTENSION = ".verbo"


def BASE_SOURCE(src) -> str:
    """Return the entire source code.  |  Redonua la tutan fontkodon."""
    return """// This file was machine-generated.  |  Ĉi tiu dosiero generiĝis per maŝino
// Includes  |  Postuloj
#include <iostream>

// Translated source code  |  Tradukitaj fontkodo
int main(void) {
""" + src + '\n}'
