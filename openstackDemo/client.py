#! /usr/bin/env python
import sys
import time
import logging

from oslo_config import cfg
import oslo_messaging as messaging

def main(argv=None):
    url = 'rabbit://admin:admin@192.168.2.64:5672'
    exchange = 'my-exchange'
    topic = 'my-topic'
    namespace = 'my-namespace'
    version = '1.1'
    logging.basicConfig(level=logging.INFO)
    transport = messaging.get_transport(cfg.CONF, url=url)
    target = messaging.Target(exchange=exchange,
                              topic=topic,
                              namespace=namespace,
                              version=version)
    client = messaging.RPCClient(transport, target, version_cap=version)
    test_context = {"application": "my-client",
                    "time": time.ctime(),
                    "cast": False}
    args = {}
    print client.call(test_context, 'methodA', **args)
    transport.cleanup()

if __name__ == "__main__":
    sys.exit(main()) 
