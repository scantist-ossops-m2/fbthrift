
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

import enum as _enum


import folly.iobuf as _fbthrift_iobuf
import thrift.python.abstract_types as _fbthrift_python_abstract_types
from module.thrift_enums import _fbthrift_compatible_with_EmptyEnum
from module.thrift_enums import _fbthrift_compatible_with_City
from module.thrift_enums import _fbthrift_compatible_with_Company

from module.thrift_enums import *
class Internship(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def weeks(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def title(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def employer(self) -> _typing.Optional[_fbthrift_current_module.Company]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def compensation(self) -> _typing.Optional[float]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def school(self) -> _typing.Optional[str]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, _fbthrift_current_module.Company, float, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Internship": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.Internship": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.Internship": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.Internship": ...  # type: ignore

class Range(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def min(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def max(self) -> int: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Range": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.Range": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.Range": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.Range": ...  # type: ignore

class struct1(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def a(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def b(self) -> str: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.struct1": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.struct1": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.struct1": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.struct1": ...  # type: ignore

class struct2(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def a(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def b(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def c(self) -> _fbthrift_current_module.struct1: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def d(self) -> _typing.Sequence[int]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, _fbthrift_current_module.struct1, _typing.Sequence[int]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.struct2": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.struct2": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.struct2": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.struct2": ...  # type: ignore

class struct3(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def a(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def b(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def c(self) -> _fbthrift_current_module.struct2: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int, _fbthrift_current_module.struct2]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.struct3": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.struct3": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.struct3": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.struct3": ...  # type: ignore

class struct4(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def a(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def b(self) -> _typing.Optional[float]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def c(self) -> _typing.Optional[int]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, float, int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.struct4": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.struct4": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.struct4": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.struct4": ...  # type: ignore

class union1(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def i(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def d(self) -> float: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.union1": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.union1": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.union1": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.union1": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        i = 1
        d = 2

    FbThriftUnionFieldEnum.__name__ = "union1"
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Final[_typing.Union[None, int, float]]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> _typing.Final[FbThriftUnionFieldEnum]: ...


class union2(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def i(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def d(self) -> float: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def s(self) -> _fbthrift_current_module.struct1: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def u(self) -> _fbthrift_current_module.union1: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.union2": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.union2": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.union2": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.union2": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        i = 1
        d = 2
        s = 3
        u = 4

    FbThriftUnionFieldEnum.__name__ = "union2"
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_value(self) -> _typing.Final[_typing.Union[None, int, float, _fbthrift_current_module.struct1, _fbthrift_current_module.union1]]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def fbthrift_current_field(self) -> _typing.Final[FbThriftUnionFieldEnum]: ...


MyCompany = _fbthrift_current_module.Company
MyStringIdentifier = str
MyIntIdentifier = int
MyMapIdentifier = _typing.Mapping[str, str]
