from pickle import dumps
from zlib import compress
from base64 import b64encode



font = {
    "0": " ### "\
         "#   #"\
         "#   #"\
         "#   #"\
         " ### ",

    "1": "   # "\
         "  ## "\
         " # # "\
         "   # "\
         "   # ",

    "2": " ### "\
         "#   #"\
         "   # "\
         "  #  "\
         "#####",

    "3": " ### "\
         "#   #"\
         "  ## "\
         "#   #"\
         " ### ",

    "4": "  ## "\
         " # # "\
         "#  # "\
         "#### "\
         "   # ",

    "5": "#####"\
         "#    "\
         "#### "\
         "    #"\
         "#### ",

    "6": " ####"\
         "#    "\
         "#### "\
         "#   #"\
         " ### ",

    "7": "#####"\
         "   # "\
         "  #  "\
         " #   "\
         " #   ",

    "8": " ### "\
         "#   #"\
         " ### "\
         "#   #"\
         " ### ",

    "9": " ### "\
         "#   #"\
         " ### "\
         "    #"\
         " ### ",

    ":": "     "\
         "  #  "\
         "     "\
         "  #  "\
         "     ",
}


font = {x: [c == "#" for c in y] for x, y in font.items()}

enc_data = b64encode(compress(dumps(font)))

print("from base64 import b64decode")
print("from zlib import decompress")
print("from pickle import loads")
print(f"font = loads(decompress(b64decode({repr(enc_data)})))")


