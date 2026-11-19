# enJMLX-95 Decoder
# enJMLX stands for Encoding using JSON Mapped Lexicon
# This is the 95-Character version
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
class enJMLX95:
    def __init__(self):
        with open(BASE_DIR / "map.json", "r") as mapf: self.jmap = json.load(mapf)
    def getcd(self, code: str) -> list[str, int]:
        if len(code) != 2: raise ValueError("error: given code must be of 2 characters")
        ordinate = str(code[0])
        abscissa = int(code[1])
        if ordinate.upper() not in "0123456789ABCDEFGHI": raise ValueError("error: invalid code - ordinate out of range")
        if str(abscissa) not in "01234": raise ValueError("error: invalid code - abscissa out of range")
        charcd = [ordinate.upper(), abscissa]
        return charcd
    def getchar(self, code: str) -> str:
        charcd = self.getcd(code)
        ordinate = str(charcd[0])
        abscissa = int(charcd[1])
        char = self.jmap[ordinate][abscissa]
        return char
    def decode(self, string: str) -> str:
        codes = list(string.split(" "))
        decoded = []
        for i in codes:
            if len(i) != 2: raise ValueError(f"error: invalid encoded string - code '{i}' is {len(i)} characters long")
            ordinate = str(i[0])
            abscissa = int(i[1])
            if ordinate.upper() not in "0123456789ABCDEFGHI": raise ValueError(f"error: invalid encoded string - ordinate of code '{i}' out of range")
            if str(abscissa) not in "01234": raise ValueError(f"error: invalid encoded string - abscissa of code '{i}' out of range")
            char = self.getchar(i)
            decoded.append(char)
        return ''.join(decoded)
    def test(self):
        encoded = "84 F4 G2 D4 F2 00 81 G0 G3 H0 F2 00 71 F4 F1 F4 G2 00 A1 E3 G4 00 63 F2 D4 G4"
        print(self.decode(encoded))
