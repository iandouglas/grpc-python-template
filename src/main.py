import grpc
from grpc_reflection.v1alpha import reflection
from concurrent import futures

import definition_pb2 
import definition_pb2_grpc


class Definitions(definition_pb2_grpc.DefinitionsServicer):
    def PingService(self, request, context):
        response = definition_pb2.PingResponse(ack="hola")
        return response


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    definition_pb2_grpc.add_DefinitionsServicer_to_server(Definitions(), server)

    SERVICE_NAMES = (
        definition_pb2.DESCRIPTOR.services_by_name['Definitions'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:80')
    server.start()

    print("gRPC server working...")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
