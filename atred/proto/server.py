from concurrent import futures
import os
import json
import grpc

try:
    from atred.proto import transmitter_pb2, transmitter_pb2_grpc
    from atred.modules.general import prepare_message, check_keys_existence, first_available_key
    from atred.modules.routes import prepare_route
except:
    pass

try:
    import transmitter_pb2
    import transmitter_pb2_grpc
except:
    pass

class Transmitter(transmitter_pb2_grpc.TransmitterServicer):

    def Transmit(self, request, context):
        response_content = {}
        
        if request.content:
            request_content = json.loads(request.content)
            route = first_available_key([ "path", "endpoint", "route" ], request_content)
            content = first_available_key([ "content", "context", "data" ], request_content)

            if route != None and content != None:
                response_content = prepare_route(route, content)
            else:
                response_content = prepare_message(code=500, message="Declare a parameter for your target path.")

        return transmitter_pb2.Response(content=json.dumps(response_content))

def serve():
    RPC_PORT = os.environ.get('RPC_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transmitter_pb2_grpc.add_TransmitterServicer_to_server(Transmitter(), server)
    server.add_insecure_port(f'[::]:{RPC_PORT}')
    server.start()
    server.wait_for_termination()