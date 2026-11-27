class UnsupportedFileTypeError(Exception):
    """The File Type Should Only Be .txt or .csv"""

class FileOpeningError(Exception):
    """The File is Unable to open"""

class EmptyFileError(Exception):
    """The File is Content is Empty"""

class SearchEngineUnavailableError(Exception):
    """can't connect or timed out"""


class SearchEngineError(Exception): 
    """the service answered with an error (including 401 and 422)"""
