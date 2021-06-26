from struct import pack, unpack


data = bytes()

key, value, index = 'tagon', 'underline', '1.0'

data += pack('', key, value, index)

print(data)
