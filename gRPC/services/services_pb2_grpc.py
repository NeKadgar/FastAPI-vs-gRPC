# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import services_pb2 as services__pb2


class GreeterStub(object):
    """Hello Name
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/Greeter/SayHello',
                request_serializer=services__pb2.HelloRequest.SerializeToString,
                response_deserializer=services__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """Hello Name
    """

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=services__pb2.HelloRequest.FromString,
                    response_serializer=services__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Hello Name
    """

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Greeter/SayHello',
            services__pb2.HelloRequest.SerializeToString,
            services__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class UserServiceStub(object):
    """Auth/Create User
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddUser = channel.unary_unary(
                '/UserService/AddUser',
                request_serializer=services__pb2.AddUserRequest.SerializeToString,
                response_deserializer=services__pb2.AddUserResponse.FromString,
                )
        self.AuthUser = channel.unary_unary(
                '/UserService/AuthUser',
                request_serializer=services__pb2.AuthUserRequest.SerializeToString,
                response_deserializer=services__pb2.AuthUserResponse.FromString,
                )


class UserServiceServicer(object):
    """Auth/Create User
    """

    def AddUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUser,
                    request_deserializer=services__pb2.AddUserRequest.FromString,
                    response_serializer=services__pb2.AddUserResponse.SerializeToString,
            ),
            'AuthUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthUser,
                    request_deserializer=services__pb2.AuthUserRequest.FromString,
                    response_serializer=services__pb2.AuthUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Auth/Create User
    """

    @staticmethod
    def AddUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/AddUser',
            services__pb2.AddUserRequest.SerializeToString,
            services__pb2.AddUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserService/AuthUser',
            services__pb2.AuthUserRequest.SerializeToString,
            services__pb2.AuthUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
