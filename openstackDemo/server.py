#! /usr/bin/env python

import sys
import time
import logging

from oslo_config import cfg
import oslo_messaging as messaging

class TestEndpoint(object):

    def __init__(self, server, target=None):
        self.server = server
        self.target = target

    def methodA(self, ctx, **args):
        print("%s::TestEndpoint::methodA( ctxt=%s arg=%s ) is called"
                    % (self.server, str(ctx),str(args)))
        print "success"
        return "success"

def main():
    url = 'rabbit://admin:admin@192.168.2.64:5672'
    exchange = 'my-exchange'
    topic = 'my-topic'
    namespace = 'my-namespace'
    argv = sys.argv[1:]
    if argv is None:
        print 'You should specify the server name'
        return -1
    server = argv[0]
    version = '1.1'
    logging.basicConfig(level=logging.INFO)
    transport = messaging.get_transport(cfg.CONF, url=url)
    target = messaging.Target(exchange=exchange,
                              topic=topic,
                              namespace=namespace,
                              server=server,
                              version=version)
    endpoints = [TestEndpoint(server, target)]
    server = messaging.get_rpc_server(transport, target, endpoints, executor = 'blocking', access_policy = messaging.rpc.dispatcher.DefaultRPCAccessPolicy)

    try:
        server.start()
        server.wait()
    except KeyboardInterrupt:
        server.stop()

if __name__ == "__main__":
    sys.exit(main()) 
