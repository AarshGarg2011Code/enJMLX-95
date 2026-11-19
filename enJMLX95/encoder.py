# enJMLX-95 Encoder
# enJMLX stands for Encoding using JSON Mapped Lexicon
# This is the 95-Character version
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
class enJMLX95:
    def __init__(self):
        with open(BASE_DIR / "coordinates.json", "r") as cdsf: self.coordinates = json.load(cdsf)
    def getcd(self, char: str) -> list[str, int]:
        if len(char) != 1: raise ValueError("error: given str must be a single character")
        if char not in list(self.coordinates.keys()): raise ValueError("error: given char is undefined in enJMLX-95")
        return self.coordinates[char]
    def getcode(self, char: str): return f"{self.getcd(char)[0]}{str(self.getcd(char)[1])}"
    def encode(self, string: str): return " ".join([self.getcode(i) for i in string])
    def test(self): print(self.encode("Lorem Ipsum Dolor Sit Amet"))
