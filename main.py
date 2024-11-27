import logging

from internal.bootstrap.GRPCServer import grpc_serve

if __name__ == "__main__":
    logging.basicConfig()
    grpc_serve()