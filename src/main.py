import logging
import grpc
from grpc_reflection.v1alpha import reflection
from concurrent import futures

import definition_pb2
import definition_pb2_grpc
from controllers.definitions import Definitions
from config import get_settings

logging.basicConfig(
    format="%(asctime)s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S"
)

settings = get_settings()


def main():
    logging.info(f"Creating server with maximum {settings.max_workers} workers...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=settings.max_workers))

    logging.info(f"Defining services...")
    definition_pb2_grpc.add_DefinitionsServicer_to_server(Definitions(), server)

    logging.info(f"Enabling server reflection...")
    SERVICE_NAMES = (
        definition_pb2.DESCRIPTOR.services_by_name["Definitions"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    logging.info(f"Setting ports...")
    server.add_insecure_port("[::]:8080")

    logging.info(f"Initializing server...")
    server.start()

    logging.info(f"The server is already online!")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
