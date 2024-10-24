#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

from abc import ABCMeta
import typing as _typing

import folly.iobuf as _fbthrift_iobuf

import apache.thrift.metadata.thrift_types as _fbthrift_metadata
from thrift.python.mutable_serializer import serialize_iobuf, deserialize, Protocol
from thrift.python.server import ServiceInterface, RpcKind, PythonUserException

import test.fixtures.interactions.module.thrift_mutable_types
import test.fixtures.interactions.module.thrift_metadata
import test.fixtures.another_interactions.shared.thrift_services
import test.fixtures.another_interactions.shared.thrift_mutable_types

class MyServiceInterface(
    ServiceInterface,
    metaclass=ABCMeta
):

    @staticmethod
    def service_name() -> bytes:
        return b"MyService"

    def getFunctionTable(self) -> _typing.Mapping[bytes, _typing.Callable[..., object]]:
        functionTable = {
            b"foo": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_foo),
            b"interact": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_interact),
            b"interactFast": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_interactFast),
            b"serialize": (RpcKind.SINGLE_REQUEST_STREAMING_RESPONSE, self._fbthrift__handler_serialize),
        }
        return {**super().getFunctionTable(), **functionTable}

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyService"

    @staticmethod
    def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
        return test.fixtures.interactions.module.thrift_metadata.gen_metadata_service_MyService()

    @staticmethod
    def __get_metadata_service_response__() -> _fbthrift_metadata.ThriftServiceMetadataResponse:
        return test.fixtures.interactions.module.thrift_metadata._fbthrift_metadata_service_response_MyService()



    async def foo(
            self
        ) -> None:
        raise NotImplementedError("async def foo is not implemented")

    async def _fbthrift__handler_foo(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_foo_args, args, protocol)
        value = await self.foo()
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_foo_result()
        return serialize_iobuf(return_struct, protocol)


    async def interact(
            self,
            arg: int
        ) -> None:
        raise NotImplementedError("async def interact is not implemented")

    async def _fbthrift__handler_interact(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_interact_args, args, protocol)
        value = await self.interact(args_struct.arg,)
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_interact_result()
        return serialize_iobuf(return_struct, protocol)


    async def interactFast(
            self
        ) -> int:
        raise NotImplementedError("async def interactFast is not implemented")

    async def _fbthrift__handler_interactFast(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_interactFast_args, args, protocol)
        value = await self.interactFast()
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_interactFast_result(success=value)
        return serialize_iobuf(return_struct, protocol)


    async def serialize(
            self
        ) -> _typing.Tuple[int, _typing.Awaitable[_typing.AsyncIterator[int]] | _typing.AsyncIterator[int]]:
        raise NotImplementedError("async def serialize is not implemented")

    async def _fbthrift__stream_wrapper_serialize(self, stream_generator: _typing.AsyncIterator[int], protocol: Protocol) -> _typing.AsyncIterator[_fbthrift_iobuf.IOBuf]:
        async for item in stream_generator:
            yield serialize_iobuf(test.fixtures.interactions.module.thrift_types._fbthrift_MyService_serialize_result_stream(success=item), protocol)

    async def _fbthrift__handler_serialize(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _typing.Tuple[_fbthrift_iobuf.IOBuf, _typing.AsyncIterator[_fbthrift_iobuf.IOBuf]]:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_serialize_args, args, protocol)
        value = self.serialize()
        value, stream = await value
        if not isinstance(stream, _typing.AsyncIterator):
            stream = await stream
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_MyService_serialize_result(success=value)
        return_stream = self._fbthrift__stream_wrapper_serialize(stream, protocol)
        return (serialize_iobuf(return_struct, protocol), return_stream)

class FactoriesInterface(
    ServiceInterface,
    metaclass=ABCMeta
):

    @staticmethod
    def service_name() -> bytes:
        return b"Factories"

    def getFunctionTable(self) -> _typing.Mapping[bytes, _typing.Callable[..., object]]:
        functionTable = {
            b"foo": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_foo),
            b"interact": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_interact),
            b"interactFast": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_interactFast),
            b"serialize": (RpcKind.SINGLE_REQUEST_STREAMING_RESPONSE, self._fbthrift__handler_serialize),
        }
        return {**super().getFunctionTable(), **functionTable}

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Factories"

    @staticmethod
    def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
        return test.fixtures.interactions.module.thrift_metadata.gen_metadata_service_Factories()

    @staticmethod
    def __get_metadata_service_response__() -> _fbthrift_metadata.ThriftServiceMetadataResponse:
        return test.fixtures.interactions.module.thrift_metadata._fbthrift_metadata_service_response_Factories()



    async def foo(
            self
        ) -> None:
        raise NotImplementedError("async def foo is not implemented")

    async def _fbthrift__handler_foo(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_foo_args, args, protocol)
        value = await self.foo()
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_foo_result()
        return serialize_iobuf(return_struct, protocol)


    async def interact(
            self,
            arg: int
        ) -> None:
        raise NotImplementedError("async def interact is not implemented")

    async def _fbthrift__handler_interact(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_interact_args, args, protocol)
        value = await self.interact(args_struct.arg,)
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_interact_result()
        return serialize_iobuf(return_struct, protocol)


    async def interactFast(
            self
        ) -> int:
        raise NotImplementedError("async def interactFast is not implemented")

    async def _fbthrift__handler_interactFast(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_interactFast_args, args, protocol)
        value = await self.interactFast()
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_interactFast_result(success=value)
        return serialize_iobuf(return_struct, protocol)


    async def serialize(
            self
        ) -> _typing.Tuple[int, _typing.Awaitable[_typing.AsyncIterator[int]] | _typing.AsyncIterator[int]]:
        raise NotImplementedError("async def serialize is not implemented")

    async def _fbthrift__stream_wrapper_serialize(self, stream_generator: _typing.AsyncIterator[int], protocol: Protocol) -> _typing.AsyncIterator[_fbthrift_iobuf.IOBuf]:
        async for item in stream_generator:
            yield serialize_iobuf(test.fixtures.interactions.module.thrift_types._fbthrift_Factories_serialize_result_stream(success=item), protocol)

    async def _fbthrift__handler_serialize(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _typing.Tuple[_fbthrift_iobuf.IOBuf, _typing.AsyncIterator[_fbthrift_iobuf.IOBuf]]:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_serialize_args, args, protocol)
        value = self.serialize()
        value, stream = await value
        if not isinstance(stream, _typing.AsyncIterator):
            stream = await stream
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Factories_serialize_result(success=value)
        return_stream = self._fbthrift__stream_wrapper_serialize(stream, protocol)
        return (serialize_iobuf(return_struct, protocol), return_stream)

class PerformInterface(
    ServiceInterface,
    metaclass=ABCMeta
):

    @staticmethod
    def service_name() -> bytes:
        return b"Perform"

    def getFunctionTable(self) -> _typing.Mapping[bytes, _typing.Callable[..., object]]:
        functionTable = {
            b"foo": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_foo),
        }
        return {**super().getFunctionTable(), **functionTable}

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Perform"

    @staticmethod
    def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
        return test.fixtures.interactions.module.thrift_metadata.gen_metadata_service_Perform()

    @staticmethod
    def __get_metadata_service_response__() -> _fbthrift_metadata.ThriftServiceMetadataResponse:
        return test.fixtures.interactions.module.thrift_metadata._fbthrift_metadata_service_response_Perform()



    async def foo(
            self
        ) -> None:
        raise NotImplementedError("async def foo is not implemented")

    async def _fbthrift__handler_foo(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Perform_foo_args, args, protocol)
        value = await self.foo()
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_Perform_foo_result()
        return serialize_iobuf(return_struct, protocol)

class InteractWithSharedInterface(
    ServiceInterface,
    metaclass=ABCMeta
):

    @staticmethod
    def service_name() -> bytes:
        return b"InteractWithShared"

    def getFunctionTable(self) -> _typing.Mapping[bytes, _typing.Callable[..., object]]:
        functionTable = {
            b"do_some_similar_things": (RpcKind.SINGLE_REQUEST_SINGLE_RESPONSE, self._fbthrift__handler_do_some_similar_things),
        }
        return {**super().getFunctionTable(), **functionTable}

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.InteractWithShared"

    @staticmethod
    def __get_metadata__() -> _fbthrift_metadata.ThriftMetadata:
        return test.fixtures.interactions.module.thrift_metadata.gen_metadata_service_InteractWithShared()

    @staticmethod
    def __get_metadata_service_response__() -> _fbthrift_metadata.ThriftServiceMetadataResponse:
        return test.fixtures.interactions.module.thrift_metadata._fbthrift_metadata_service_response_InteractWithShared()



    async def do_some_similar_things(
            self
        ) -> test.fixtures.another_interactions.shared.thrift_mutable_types.DoSomethingResult:
        raise NotImplementedError("async def do_some_similar_things is not implemented")

    async def _fbthrift__handler_do_some_similar_things(self, args: _fbthrift_iobuf.IOBuf, protocol: Protocol) -> _fbthrift_iobuf.IOBuf:
        args_struct = deserialize(test.fixtures.interactions.module.thrift_mutable_types._fbthrift_InteractWithShared_do_some_similar_things_args, args, protocol)
        value = await self.do_some_similar_things()
        return_struct = test.fixtures.interactions.module.thrift_mutable_types._fbthrift_InteractWithShared_do_some_similar_things_result(success=value)
        return serialize_iobuf(return_struct, protocol)

