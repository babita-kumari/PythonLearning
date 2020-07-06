"""
Write a programme  to retrieve the given document using the HTTP protocol in a way that you
can examine the HTTP Response headers.

"""

import socket

class ProcessHtmlFile:

    def get_input(self):
        mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mysock.connect(('data.pr4e.org',80))
        data='GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
        mysock.send(data)
        return mysock

    def read_input(self,mysock):
        while True:
            data=mysock.recv(500)
            if len(data)<1:
                break
            return data
        mysock.close()

    def print_data(self, data):
        print(data.decode())

    def processes(self):
        input=self.get_input();
        data=self.read_input(input);
        self.print_data(data)


data_bank=ProcessHtmlFile()
data_bank.processes()