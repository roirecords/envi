from pyModbusTCP.server import ModbusServer

c = ModbusServer(host='localhost', port=60000, no_block=False, ipv6=False)
print("Creating ModbusServer")
print("Establishing host")
print("Establishing port and connecting")
c.start()

# managing TCP sessions with call to c.open()/c.close()