class Log:
    """A simple logging tool.  |  Simpla tekstmontrilo."""

    def __init__(self) -> None:
        """Initialize the logger.  |  Komencigu la tekstmontrilon."""
        self._pref_info: str = "INFO"
        self._pref_warn: str = "AVER"
        self._pref_error: str = "ERAR"

    def info(self, message: str) -> None:
        """Log a message with the 'info' prefix.  |  Montru mesaĝon kun la prefixo 'info'."""
        print(f"[{self._pref_info}] {message}", flush=True)

    def warn(self, message: str) -> None:
        """Log a message with the 'warn' prefix.  |  Montru mesaĝon kun la prefixo 'avertu'."""
        print(f"[{self._pref_warn}] {message}", flush=True)

    def error(self, message: str) -> None:
        """Log a message with the 'error' prefix.  |  Montru mesaĝon kun la prefixo 'eraro'."""
        print(f"[{self._pref_error}] {message}", flush=True)
