from struct import unpack
import socket

def MacAddr(byteString):
    return ':'.join('{:02x}'.format(piece) for piece in byteString)

class EtherFrame:
    length = 14
    def __init__(self, data):
        unpackedData = unpack('!6s6sH', data[0:self.length])
        self.protocol = socket.ntohs(unpackedData[2])
        self.dst = MacAddr(data[0:6])
        self.src = MacAddr(data[6:12])
        self.bucket = data[self.length:]
