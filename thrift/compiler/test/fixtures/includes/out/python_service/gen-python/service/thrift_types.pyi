#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import typing as _typing

import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions

import includes.thrift_types as _fbthrift__includes__thrift_types

import module.thrift_types as _fbthrift__module__thrift_types

import transitive.thrift_types as _fbthrift__transitive__thrift_types

from service.thrift_enums import *

IncludesIncluded = _fbthrift__includes__thrift_types.Included
IncludesTransitiveFoo = _fbthrift__transitive__thrift_types.Foo


class _fbthrift_MyService_query_args(_fbthrift_python_types.Struct):
    s: _typing.Final[_fbthrift__module__thrift_types.MyStruct] = ...
    i: _typing.Final[_fbthrift__includes__thrift_types.Included] = ...

    def __init__(
        self, *,
        s: _typing.Optional[_fbthrift__module__thrift_types.MyStruct]=...,
        i: _typing.Optional[_fbthrift__includes__thrift_types.Included]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _fbthrift__module__thrift_types.MyStruct, _fbthrift__includes__thrift_types.Included]]]: ...


class _fbthrift_MyService_query_result(_fbthrift_python_types.Struct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...


class _fbthrift_MyService_has_arg_docs_args(_fbthrift_python_types.Struct):
    s: _typing.Final[_fbthrift__module__thrift_types.MyStruct] = ...
    i: _typing.Final[_fbthrift__includes__thrift_types.Included] = ...

    def __init__(
        self, *,
        s: _typing.Optional[_fbthrift__module__thrift_types.MyStruct]=...,
        i: _typing.Optional[_fbthrift__includes__thrift_types.Included]=...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[None, _fbthrift__module__thrift_types.MyStruct, _fbthrift__includes__thrift_types.Included]]]: ...


class _fbthrift_MyService_has_arg_docs_result(_fbthrift_python_types.Struct):
    success: _typing.Final[None]

    def __init__(
        self, *, success: _typing.Optional[None] = ...
    ) -> None: ...

    def __iter__(self) -> _typing.Iterator[_typing.Tuple[
        str,
        _typing.Union[
            None,
        ]]]: ...
