import sys
import base64


if not sys.argv[1:]:
    filepath = input("Image: ")
    if not filepath:
        sys.exit(0)
    sys.argv.append(filepath)


with open(sys.argv[1], 'rb') as file:
    data = file.read()


b64 = base64.standard_b64encode(data)

print(b64)
