from concurrent import futures
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

class Transmitter(transmitter_pb2_grpc.TransmitterServicer):

    def Transmit(self, request, context):
        response_content = {
            "meta": {
                "code": 200
            }
        }
        
        if request.content:
            request_content = json.loads(request.content)
            if "username" in request_content and \
               "password" in request_content:
                username = request_content["username"]
                password = request_content["password"]
                if username == "haqaliz" and password == "king_1374":
                    response_content["meta"]["message"] = "logged in successfully"
                else:
                    response_content["meta"]["code"] = 404
                    response_content["meta"]["message"] = "username or password is wrong"
            else:
                response_content["meta"]["code"] = 400
                response_content["meta"]["message"] = "you must define username and password"
        return transmitter_pb2.Response(content=json.dumps(response_content))


def serve():
    RPC_PORT = os.environ.get('RPC_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transmitter_pb2_grpc.add_TransmitterServicer_to_server(Transmitter(), server)
    server.add_insecure_port(f'[::]:{RPC_PORT}')
    server.start()
    server.wait_for_termination()