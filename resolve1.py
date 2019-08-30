# Python 100 days - simple dns resolver
# Tested in native 3.6.5 and 3.7.2.  Socket package not available in Anaconda
# Added some requests activity

import socket
import requests

class Resolver:
    """
    Simple class to perform DNS resolution
    """

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


if __name__ == "__main__":
    testresolve = Resolver()
    testresult = testresolve("google.com")
    print(testresult)
    webcheck = requests.get('http://google.com')
    print ('request get result: ', webcheck)
    print ('Request response code: ', webcheck.status_code)
    print ('Requested contents: ', webcheck.content)
