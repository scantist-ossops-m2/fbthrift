
# EXPERIMENTAL - DO NOT USE !!!
# See `experimental_generate_abstract_types` documentation in thrift compiler

#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import abc as _abc
import typing as _typing

import module.thrift_abstract_types as _fbthrift_current_module
_fbthrift_property = property


import folly.iobuf as _fbthrift_iobuf
import thrift.python.abstract_types as _fbthrift_python_abstract_types

from module.thrift_enums import *
class Limits(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def max_i64_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def min_i64_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def max_i32_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def min_i32_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def max_i16_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def min_i16_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def max_byte_field(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def min_byte_field(self) -> int: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, int, int, int, int, int, int, int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Limits": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.Limits": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.Limits": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.Limits": ...  # type: ignore
