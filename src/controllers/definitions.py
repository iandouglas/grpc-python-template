import definition_pb2_grpc
from controllers.users import UsersDefinition


class Definitions(UsersDefinition, definition_pb2_grpc.DefinitionsServicer):
    pass
