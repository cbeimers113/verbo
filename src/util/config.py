import os
import pickle

from typing import Any, Dict, Optional

from .log import Log

LOG: Log = Log()

CONFIG_FILE: str = "verbo.pkl"

ERR_LOAD_CONF: str = f"Error loading config file  |  Eraro aperis dum la ŝarĝado de la agordan dosieron {CONFIG_FILE}"
ERR_SAVE_CONF: str = f"Error saving config file  |  Eraro aperis dum la ŝparado de la agordan dosieron {CONFIG_FILE}"
ERR_FIND_CONF: str = f"Could not find config file  |  Ne povis trovi la agordan dosieron {CONFIG_FILE}"
ERR_NO_CONFIG: str = "No config was initialized.  |  Neniu agordon komenciĝis."


class Config():

    def __init__(self) -> None:
        """Initialize the config object.  |  Komencigu la agordan objekton."""
        self._data: Optional[Dict[str, str]] = self.load_config()

        # If the config couldn't be loaded, create a new config instance
        if self._data is None:
            LOG.info("Creating new config.  |  Kreante novan agordon.")
            self._data = dict()

    def load_config(self) -> Optional[Dict[str, str]]:
        """Read in the config settings.  |  Legu la agordojn."""
        data: Optional[Dict[str, str]] = None

        if os.path.exists(CONFIG_FILE) and os.path.isfile(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'rb') as f:
                    data = pickle.load(f)
                    LOG.info(f"Loaded config from  |  Ŝarĝis agordojn el '{CONFIG_FILE}'")
            except Exception:
                LOG.error(ERR_LOAD_CONF)
        else:
            LOG.error(ERR_FIND_CONF)

        return data

    def save_config(self) -> None:
        """Save the config settings.  |  Ŝparu la agordojn."""
        try:
            with open(CONFIG_FILE, 'wb') as f:
                pickle.dump(self._data, f)
            LOG.info(f"Saved config to  | Ŝparis agordojn al '{CONFIG_FILE}'")
        except Exception:
            LOG.error(ERR_SAVE_CONF)

    def get_conf(self, key: str) -> Any:
        """Return the value stored with the given key.  |  Redonu la valoron kaŝiĝis per la ŝlosilo donita."""
        value: str = ""

        if self._data:
            if key in self._data.keys():
                value = self._data[key]
        else:
            LOG.error(ERR_FIND_CONF)

        return value

    def set_conf(self, key: str, val: Any) -> None:
        """Set the value stored at the specified key.  |  Agordu la valoron kiu kaŝiĝis per la ŝlosilo donita."""
        if self._data:
            self._data[key] = val
        else:
            LOG.error(ERR_FIND_CONF)

    def del_conf(self, key: str) -> None:
        """Delete the specified entry.  |  Forigu la valoron kaŝiĝis per la ŝlosilo donita."""
        if self._data:
            if self._data.get(key, None):
                del self._data[key]
        else:
            LOG.error(ERR_FIND_CONF)

    def __str__(self) -> str:
        """Return a string representation of the config state.  |  Redonu reprezenton de la agordoj kiel teksto."""
        string: str = ""

        for key, value in self._data.items():
            string += f"{key} = {value}\n"

        return string
