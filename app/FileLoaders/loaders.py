from FileLoaders.base_loader import Base
from pathlib import Path
from exceptions import UnsupportedFileTypeError,FileOpeningError,EmptyFileError
import csv

class TextLoader(Base):

   def validate_file(self, file_path: Path) -> bool:
        """Validates if the provided path is a .txt file."""

        if file_path.suffix.lower() != ".txt":

            raise UnsupportedFileTypeError("File extension must be .txt")
        
        return True

    
   def read_file(self, file_path: Path) -> str:
            
        """Reads file content and returns it as a string."""
        try :
            with open(file_path, "r", encoding="utf-8") as file:
                # content = file.read()
                if file_path.stat().st_size == 0:
                     raise EmptyFileError ("File Contents is Empty")
                return file.read()

        except PermissionError :
             raise FileOpeningError ("File is Unable to Open")
        

class CsvLoader(Base):
    def validate_file(self, file_path: Path) -> bool:
            """Validates if the provided path is a .csv file."""
    
            if file_path.suffix.lower() != ".csv":
    
                raise UnsupportedFileTypeError("File extension must be .csv")
            
            return True
    
        
    def read_file(self, file_path: Path) -> str:
                
            """Reads file content and returns it as a string."""
            formatted_rows = []
        
            with open(file_path, "r",encoding="utf-8") as file:
                if file_path.stat().st_size == 0:
                    raise EmptyFileError ("File Contents is Empty")

                csv_reader = csv.DictReader(file)  

                # i is index and row is data (id : "1" , Name : "Jon" )
                for i , row in enumerate(csv_reader,start=1): 

                    row_str = ", ".join([f"{key}: {value}" for key, value in row.items()])
                    formatted_rows.append(f"Row {i} -> {row_str}")
                return "\n".join(formatted_rows)