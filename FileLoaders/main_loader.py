from pathlib import Path
from  FileLoaders.base_loader  import Base
from exceptions import UnsupportedFileTypeError
from FileLoaders.loaders import TextLoader, CsvLoader

class MainLoader:
    """Factory class to instantiate the appropriate file loader based on extension."""

    @staticmethod
    def get_loader(file_path:Path) -> Base:
        ext = file_path.suffix.lower()

        if ext == '.txt':
            return TextLoader()

        elif ext == '.csv':
            return CsvLoader()

        else :
            raise UnsupportedFileTypeError(
                f"Unsupported file format '{ext}'. Only .txt and .csv are supported."
            )
        
