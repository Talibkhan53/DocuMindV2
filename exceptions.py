class UnsupportedFileTypeError(Exception):
    """The File Type Should Only Be .txt or .csv"""

class FileOpeningError(Exception):
    """The File is Unable to open"""

class EmptyFileError(Exception):
    """The File is Content is Empty"""