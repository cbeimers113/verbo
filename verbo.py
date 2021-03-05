"""
Program starts here.  |  Ĉi tie komencas la programo.
"""
import os
import sys
from typing import List

from src.data import VERBO_SRC_EXTENSION
from src.translate import temp
from src.util.log import Log

LOG: Log = Log()

if __name__ == "__main__":
    """Inspect arguments.  |  Inspektu argumentojn."""
    args: List[str] = sys.argv

    if len(args) == 0:
        # No argument, show usage.  |  Neniu argumento, montru uzadon.
        LOG.info("Usage  | Uzado: verbo.py <f1.verbo> <f2.verbo> ...")
    else:
        # Translate each file.  |  Traduku ĉiun dosieron.
        for arg in args[1:]:
            # Check if file exists.  |  Sciiĝu ĉu la dosiero ekzistas.
            if os.path.exists(arg):
                # Check if the file is a verbo source file.  |  Sciiĝu ĉu la dosiero estas fontdosiero de verbo.
                if arg.endswith(VERBO_SRC_EXTENSION):
                    LOG.info(f"Processing  |  Prilaborante {arg}")
                    temp(arg)
                else:
                    LOG.error(f"File is not a {VERBO_SRC_EXTENSION} source file  |  Dosiero ne estas fontdosiero de {VERBO_SRC_EXTENSION}")
            else:
                LOG.error(f"File does not exist  |  Dosiero ne ekzistas {arg}")
