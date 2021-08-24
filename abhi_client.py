from pprint import pprint 
#from oslo.config import cfg 
from oslo_config import cfg 
#import oslo.messaging as om 
import oslo_messaging as om 

##Invoke "get_transport". This call will set default Configurations required to Create Messaging Transport 
#transport = om.get_transport(cfg.CONF)
 
##Set Configurations required to Create Messaging Transport 
#cfg.CONF.set_override('rabbit_host', '192.168.56.101') 
#cfg.CONF.set_override('rabbit_port', 5672) 
#cfg.CONF.set_override('username', 'admin') 
#cfg.CONF.set_override('password', 'hpinvent') 
#cfg.CONF.set_override('rabbit_login_method', 'AMQPLAIN') 
#cfg.CONF.set_override('rabbit_virtual_host', '/') 
#cfg.CONF.set_override('rpc_backend', 'rabbit') 

##Check Configurations 
#res = [{k:v} for k, v in cfg.CONF.iteritems()] 
#pprint(res)

##Create Messaging Transport 
transport = om.get_transport(cfg.CONF) 
##Create Target 
target = om.Target(topic='testme', server='127.0.0.1') 

##Create RPC Client 
client = om.RPCClient(transport, target) 
##Invoke remote method and wait for a reply. (call) 
arg = "Saju" 
ctxt = {} 
#print(client.call(ctxt, 'test_method1', arg=arg))


##Invoke remote method and return immediately. (cast)
print(client.cast(ctxt, 'test_method1', arg=arg))