
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

_fbthrift_property = property

import enum as _enum


import folly.iobuf as _fbthrift_iobuf


class ComplexUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def intValue(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def intListValue(self) -> _typing.Sequence[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def stringListValue(self) -> _typing.Sequence[str]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def stringValue(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def typedefValue(self) -> _typing.Mapping[int, str]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def stringRef(self) -> str: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ComplexUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.ComplexUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.ComplexUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.ComplexUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        intValue = 1
        intListValue = 2
        stringListValue = 3
        stringValue = 5
        typedefValue = 9
        stringRef = 14

    FbThriftUnionFieldEnum.__name__ = "ComplexUnion"

    fbthrift_current_value: _typing.Final[_typing.Union[None, int, _typing.Sequence[int], _typing.Sequence[str], str, _typing.Mapping[int, str], str]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]


class ListUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def intListValue(self) -> _typing.Sequence[int]: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def stringListValue(self) -> _typing.Sequence[str]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ListUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.ListUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.ListUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.ListUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        intListValue = 2
        stringListValue = 3

    FbThriftUnionFieldEnum.__name__ = "ListUnion"

    fbthrift_current_value: _typing.Final[_typing.Union[None, _typing.Sequence[int], _typing.Sequence[str]]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]


class DataUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def binaryData(self) -> bytes: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def stringData(self) -> str: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.DataUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.DataUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.DataUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.DataUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        binaryData = 1
        stringData = 2

    FbThriftUnionFieldEnum.__name__ = "DataUnion"

    fbthrift_current_value: _typing.Final[_typing.Union[None, bytes, str]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]


class Val(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def strVal(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def intVal(self) -> int: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def typedefValue(self) -> _typing.Mapping[int, str]: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int, _typing.Mapping[int, str]]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Val": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.Val": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.Val": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.Val": ...  # type: ignore

class ValUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def v1(self) -> Val: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def v2(self) -> Val: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.ValUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.ValUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.ValUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.ValUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        v1 = 1
        v2 = 2

    FbThriftUnionFieldEnum.__name__ = "ValUnion"

    fbthrift_current_value: _typing.Final[_typing.Union[None, Val, Val]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]


class VirtualComplexUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def thingOne(self) -> str: ...
    @_fbthrift_property
    @_abc.abstractmethod
    def thingTwo(self) -> str: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.VirtualComplexUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.VirtualComplexUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.VirtualComplexUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.VirtualComplexUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        thingOne = 1
        thingTwo = 2

    FbThriftUnionFieldEnum.__name__ = "VirtualComplexUnion"

    fbthrift_current_value: _typing.Final[_typing.Union[None, str, str]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]


class NonCopyableStruct(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def num(self) -> int: ...
    @_abc.abstractmethod
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int]]]: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.NonCopyableStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.NonCopyableStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.NonCopyableStruct": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.NonCopyableStruct": ...  # type: ignore

class NonCopyableUnion(_abc.ABC):
    @_fbthrift_property
    @_abc.abstractmethod
    def s(self) -> NonCopyableStruct: ...
    @_abc.abstractmethod
    def _to_mutable_python(self) -> "module.thrift_mutable_types.NonCopyableUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_python(self) -> "module.thrift_types.NonCopyableUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py3(self) -> "module.types.NonCopyableUnion": ...  # type: ignore
    @_abc.abstractmethod
    def _to_py_deprecated(self) -> "module.ttypes.NonCopyableUnion": ...  # type: ignore

    class FbThriftUnionFieldEnum(_enum.Enum):
        EMPTY = 0
        s = 1

    FbThriftUnionFieldEnum.__name__ = "NonCopyableUnion"

    fbthrift_current_value: _typing.Final[_typing.Union[None, NonCopyableStruct]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]


containerTypedef = _typing.Mapping[int, str]
