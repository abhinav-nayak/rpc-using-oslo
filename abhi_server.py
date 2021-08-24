from pprint import pprint 
#from oslo.config import cfg 
from oslo_config import cfg
#import oslo.messaging as om 
import oslo_messaging as om 
import time

##Invoke "get_transport". This call will set default Configurations required to Create Messaging Transport 
#transport = om.get_transport(cfg.CONF)
 
##Set/Override Configurations required to Create Messaging Transport 
#cfg.CONF.set_override('rabbit_host', '192.168.56.101') 
#cfg.CONF.set_override('rabbit_port', 5672) 
#cfg.CONF.set_override('username', 'admin') 
#cfg.CONF.set_override('password', 'hpinvent') 
#cfg.CONF.set_override('rabbit_login_method', 'AMQPLAIN') 
#cfg.CONF.set_override('rabbit_virtual_host', '/') 
#cfg.CONF.set_override('rpc_backend', 'rabbit') 

##Check the Configurations 
#res = [{k:v} for k, v in cfg.CONF.iteritems()] 
#pprint(res)

##Create Messaging Transport 
transport = om.get_transport(cfg.CONF) 
##Create Target (Exchange, Topic and Server to listen on) 
target = om.Target(topic='testme', server='127.0.0.1')
 
##Create EndPoint 
class TestEndpoint(object): 
    def test_method1(self, ctx, arg): 
        res = "Result from test_method1 " + str(arg) 
        print(res) 
        return res 
    def test_method2(self, ctx, arg): 
        res = "Result from test_method2 " + str(arg) 
        print(res) 
        return res 
        
##Create EndPoint List 
endpoints = [TestEndpoint(),]

##Create RPC Server 
server = om.get_rpc_server(transport, target, endpoints, executor='blocking') 
##Start RPC Server 
try:
    server.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping server")

server.stop()
server.wait()
