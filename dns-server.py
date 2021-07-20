    """
    A simple server used to demonstrate the return of an IPv4 address from an APL query.
    APL address incomplete and needs the submask to be calculateddatetime A combination of a date and a time. 
    Record_APL was added to dns.py at lines 39, 86, 189, 224 and 1262.
    """
from twisted.internet import task
from twisted.names import dns
from twisted.python import util as tputil


def main(reactor):
    proto = dns.DNSDatagramProtocol(controller=None)
    reactor.listenUDP(0, proto)
    d = proto.query(('8.8.8.8', 53), [dns.Query('www.example.com', dns.APL)])
    d.addCallback(printResult)
    return d

def printResult(res):
    print ('ANSWERS: ', [a.payload for a in res.answers])


task.react(main)
