from abc import ABC, abstractmethod
from pathlib import Path

class Base(ABC):
    """Abstract Base Class for all document loaders."""

    @abstractmethod
    def validate_file(self, file_path: Path) -> bool:
        """Validates whether  has the correct extension.

        Must raise an exception or return False if invalid.
        """
        pass

    @abstractmethod
    def read_file(self, file_path: Path) -> str:
        """Reads the file and returns its content formatted as a string."""
        pass