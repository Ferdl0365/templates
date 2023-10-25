import sys
# Check for python version (necessary since the robot uses python 2.7)
if sys.version_info[0:2] == (2, 7):
    from SimpleXMLRPCServer import SimpleXMLRPCServer
    port = 42069
else:
    from xmlrpc.server import SimpleXMLRPCServer
    port = 8080
host = "127.0.0.1"


### Pattern Dictionary ###
serverlist_dict = {
    "1": [[0, 0, 0], [0, 0.0615, 0], [0, 0.123, 0], [0, 0.1845, 0], [0, 0.246, 0], [0, 0.3075, 0], [0, 0.369, 0], [0, 0.4305, 0], [0.1375, 0, 0], [0.1375, 0.0615, 0], [0.1375, 0.123, 0], [0.1375, 0.1845, 0], [0.1375, 0.246, 0], [0.1375, 0.3075, 0], [0.1375, 0.369, 0], [0.1375, 0.4305, 0], [0.275, 0, 90], [0.275, 0.1375, 90], [0.275, 0.275, 90]],
    "2": [[0, 0, 0], [0.092, 0, 0], [0.184, 0, 0], [0.276, 0, 90], [0, 0.055, 0], [0.092, 0.055, 0], [0.184, 0.055, 0], [0, 0.11, 0], [0.092, 0.11, 0], [0.184, 0.11, 0], [0.276, 0.092, 90], [0, 0.165, 0], [0.092, 0.165, 0], [0.184, 0.165, 0], [0, 0.22, 0], [0.092, 0.22, 0], [0.184, 0.22, 0], [0.276, 0.184, 90], [0, 0.275, 0], [0.092, 0.275, 0], [0.184, 0.275, 0], [0.276, 0.276, 90], [0, 0.33, 0], [0.092, 0.33, 0], [0.184, 0.33, 0], [0, 0.385, 0], [0.092, 0.385, 0], [0.184, 0.385, 0], [0.276, 0.368, 90], [0, 0.44, 0], [0.092, 0.44, 0], [0.184, 0.44, 0]],
    "3": [[0, 0, 0], [0, 0.118, 0], [0, 0.236, 0], [0, 0.354, 0], [0.05, 0, 0], [0.05, 0.118, 0], [0.05, 0.236, 0], [0.05, 0.354, 0], [0.1, 0, 0], [0.1, 0.118, 0], [0.1, 0.236, 0], [0.1, 0.354, 0], [0, 0.472, 270], [0.15, 0, 0], [0.15, 0.118, 0], [0.15, 0.236, 0], [0.15, 0.354, 0], [0.2, 0, 0], [0.2, 0.118, 0], [0.2, 0.236, 0], [0.2, 0.354, 0], [0.25, 0, 0], [0.25, 0.118, 0], [0.25, 0.236, 0], [0.25, 0.354, 0], [0.21, 0.472, 270], [0.3, 0, 0], [0.3, 0.118, 0], [0.3, 0.236, 0], [0.3, 0.354, 0]],
    "register_value": 'return_value'
}

class RemoteRobotFunctions:

    def get_length_of_list(self, register_value):
        return len(serverlist_dict[register_value])
    
    def get_current_dropoff(self, register_value, counter):
        idx=counter%len(serverlist_dict[register_value])
        return serverlist_dict[register_value][idx]
    
# Create server instance on localhost
server = SimpleXMLRPCServer((host, port))

# Register functions
server.register_instance(RemoteRobotFunctions())

# Start server
server.serve_forever()