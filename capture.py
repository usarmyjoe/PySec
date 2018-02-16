#!/usr/bin/python3
import socket
import binascii
from struct import pack
import time

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    pcap = PCAPFile('./capture.pcap')
    while True:
        rawData, addr = conn.recvfrom(65500)
        pcap.write(rawData)
    pcap.close


class PCAPFile:
    def __init__(self, filename):
        self.fp = open(filename,'wb')
        fileHeader = pack('!IHHiIII', 0xa1b2c3d4, 2, 4, 0, 0, 65535, 1)
        self.fp.write(fileHeader)          

    def write(self, data):
        seconds, mseconds = [int(part) for part in str(time.time()).split('.')]
        length = len(data)
        message = pack('!IIII', seconds, mseconds, length, length)
        self.fp.write(message)
        self.fp.write(data)

    def close(self):
        self.fp.close()


if __name__ == '__main__':
	main()
