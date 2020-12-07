from __future__ import print_function
import logging
import os
import json
import grpc

try:
    from atred.proto import transmitter_pb2, transmitter_pb2_grpc
except:
    pass

try:
    import transmitter_pb2
    import transmitter_pb2_grpc
except:
    pass

def emit(data):
    RPC_PORT = os.environ.get('RPC_PORT')
    with grpc.insecure_channel(f'localhost:{RPC_PORT}') as channel:
        stub = transmitter_pb2_grpc.TransmitterStub(channel)
        data_content = json.dumps(data)
        response = stub.Transmit(transmitter_pb2.Request(content=data_content))

    return json.loads(response.content)