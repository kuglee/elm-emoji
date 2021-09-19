#inspired by the code in the official emojione repo
#requires having the emoji.json from https://github.com/joypixels/emoji-toolkit v6.6.0 in the same folder
#generates a file called "generated_valid.elm" with the list literal to fill into Valid.elm

import json

json_package_path = './emoji.json'
data_dict = json.loads(open(json_package_path).read())
unicode_replace = {}
lines = []
exceptions = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "#", "*"]
for i, (key, value) in enumerate(data_dict.items()):
    unicode_hex = value['code_points']['fully_qualified']
    unicode_parts = unicode_hex.split('-') if '-'in unicode_hex else [ unicode_hex ]
    unicode_char = ''.join(chr(int(part, 16)) for part in unicode_parts)

    if unicode_char in exceptions:
        continue

    unicode_replace[unicode_char.encode('utf-8')] = unicode_parts
    formated_parts = ["\"{0}\"".format(part) for part in unicode_parts]
    parts_as_output = ', '.join(formated_parts)
    shortname = value['shortname']
    lines.append("    " + ("[" if i == 0 else ",") + " ( \"{0}\", [ {1} ], \"{2}\" )\n".format(unicode_char, parts_as_output, shortname))
output_path = './generated_valid.elm'
file = open(output_path, 'w')
file.writelines(lines)
file.close()
