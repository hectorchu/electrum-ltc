# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import mwebd_pb2 as mwebd__pb2


class RpcStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Status = channel.unary_unary(
                '/Rpc/Status',
                request_serializer=mwebd__pb2.StatusRequest.SerializeToString,
                response_deserializer=mwebd__pb2.StatusResponse.FromString,
                )
        self.Utxos = channel.unary_stream(
                '/Rpc/Utxos',
                request_serializer=mwebd__pb2.UtxosRequest.SerializeToString,
                response_deserializer=mwebd__pb2.Utxo.FromString,
                )
        self.Addresses = channel.unary_unary(
                '/Rpc/Addresses',
                request_serializer=mwebd__pb2.AddressRequest.SerializeToString,
                response_deserializer=mwebd__pb2.AddressResponse.FromString,
                )
        self.Spent = channel.unary_unary(
                '/Rpc/Spent',
                request_serializer=mwebd__pb2.SpentRequest.SerializeToString,
                response_deserializer=mwebd__pb2.SpentResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/Rpc/Create',
                request_serializer=mwebd__pb2.CreateRequest.SerializeToString,
                response_deserializer=mwebd__pb2.CreateResponse.FromString,
                )
        self.Broadcast = channel.unary_unary(
                '/Rpc/Broadcast',
                request_serializer=mwebd__pb2.BroadcastRequest.SerializeToString,
                response_deserializer=mwebd__pb2.BroadcastResponse.FromString,
                )


class RpcServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Utxos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Addresses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Spent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Broadcast(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=mwebd__pb2.StatusRequest.FromString,
                    response_serializer=mwebd__pb2.StatusResponse.SerializeToString,
            ),
            'Utxos': grpc.unary_stream_rpc_method_handler(
                    servicer.Utxos,
                    request_deserializer=mwebd__pb2.UtxosRequest.FromString,
                    response_serializer=mwebd__pb2.Utxo.SerializeToString,
            ),
            'Addresses': grpc.unary_unary_rpc_method_handler(
                    servicer.Addresses,
                    request_deserializer=mwebd__pb2.AddressRequest.FromString,
                    response_serializer=mwebd__pb2.AddressResponse.SerializeToString,
            ),
            'Spent': grpc.unary_unary_rpc_method_handler(
                    servicer.Spent,
                    request_deserializer=mwebd__pb2.SpentRequest.FromString,
                    response_serializer=mwebd__pb2.SpentResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=mwebd__pb2.CreateRequest.FromString,
                    response_serializer=mwebd__pb2.CreateResponse.SerializeToString,
            ),
            'Broadcast': grpc.unary_unary_rpc_method_handler(
                    servicer.Broadcast,
                    request_deserializer=mwebd__pb2.BroadcastRequest.FromString,
                    response_serializer=mwebd__pb2.BroadcastResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Rpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Rpc(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Status',
            mwebd__pb2.StatusRequest.SerializeToString,
            mwebd__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Utxos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Rpc/Utxos',
            mwebd__pb2.UtxosRequest.SerializeToString,
            mwebd__pb2.Utxo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Addresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Addresses',
            mwebd__pb2.AddressRequest.SerializeToString,
            mwebd__pb2.AddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Spent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Spent',
            mwebd__pb2.SpentRequest.SerializeToString,
            mwebd__pb2.SpentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Create',
            mwebd__pb2.CreateRequest.SerializeToString,
            mwebd__pb2.CreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Broadcast(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Rpc/Broadcast',
            mwebd__pb2.BroadcastRequest.SerializeToString,
            mwebd__pb2.BroadcastResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
