from socketserver import ThreadingMixIn
from xmlrpc.server import SimpleXMLRPCServer

class SimpleThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass
