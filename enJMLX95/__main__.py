# enJMLX-95 MAIN
# enJMLX stands for Encoding using JSON Mapped Lexicon
# This is the 95-Character version
from .encoder import enJMLX95 as encoder
from .decoder import enJMLX95 as decoder

encoder = encoder()
decoder = decoder()

encoder.test()
input("\nPress enter to continue . . .\n")
decoder.test()
