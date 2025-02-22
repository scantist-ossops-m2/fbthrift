#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import typing as _typing

import module.thrift_types as _fbthrift_current_module
import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions

from module.thrift_enums import *


class _fbthrift_compatible_with_Limits:
    pass


class Limits(_fbthrift_python_types.Struct, _fbthrift_compatible_with_Limits):
    max_i64_field: _typing.Final[int] = ...
    min_i64_field: _typing.Final[int] = ...
    max_i32_field: _typing.Final[int] = ...
    min_i32_field: _typing.Final[int] = ...
    max_i16_field: _typing.Final[int] = ...
    min_i16_field: _typing.Final[int] = ...
    max_byte_field: _typing.Final[int] = ...
    min_byte_field: _typing.Final[int] = ...
    def __init__(
        self, *,
        max_i64_field: _typing.Optional[int]=...,
        min_i64_field: _typing.Optional[int]=...,
        max_i32_field: _typing.Optional[int]=...,
        min_i32_field: _typing.Optional[int]=...,
        max_i16_field: _typing.Optional[int]=...,
        min_i16_field: _typing.Optional[int]=...,
        max_byte_field: _typing.Optional[int]=...,
        min_byte_field: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        max_i64_field: _typing.Optional[int]=...,
        min_i64_field: _typing.Optional[int]=...,
        max_i32_field: _typing.Optional[int]=...,
        min_i32_field: _typing.Optional[int]=...,
        max_i16_field: _typing.Optional[int]=...,
        min_i16_field: _typing.Optional[int]=...,
        max_byte_field: _typing.Optional[int]=...,
        min_byte_field: _typing.Optional[int]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, int, int, int, int, int, int, int]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Limits": ...  # type: ignore
    def _to_py3(self) -> "module.types.Limits": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Limits": ...  # type: ignore


max_i64_const: int = ...

min_i64_const: int = ...

max_i32_const: int = ...

min_i32_const: int = ...

max_i16_const: int = ...

min_i16_const: int = ...

max_byte_const: int = ...

min_byte_const: int = ...
