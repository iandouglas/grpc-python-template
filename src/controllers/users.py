import definition_pb2


class UsersDefinition:
    def PingService(self, request, context):
        response = definition_pb2.PingResponse(ack="hola")
        return response
