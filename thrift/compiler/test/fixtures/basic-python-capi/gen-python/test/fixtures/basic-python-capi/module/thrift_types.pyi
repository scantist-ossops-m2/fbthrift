#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations


import typing as _typing

import enum

import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions


class MyEnum(_fbthrift_python_types.Enum, int):
    MyValue1: MyEnum = ...
    MyValue2: MyEnum = ...
    def _to_python(self) -> MyEnum: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class MyStruct(_fbthrift_python_types.Struct):
    MyIntField: _typing.Final[int] = ...
    MyStringField: _typing.Final[str] = ...
    MyDataField: _typing.Final[MyDataItem] = ...
    myEnum: _typing.Final[MyEnum] = ...
    oneway: _typing.Final[bool] = ...
    floatList: _typing.Final[_typing.Sequence[float]] = ...
    strMap: _typing.Final[_typing.Mapping[bytes, str]] = ...
    floatSet: _typing.Final[_typing.AbstractSet[int]] = ...
    def __init__(
        self, *,
        MyIntField: _typing.Optional[int]=...,
        MyStringField: _typing.Optional[str]=...,
        MyDataField: _typing.Optional[MyDataItem]=...,
        myEnum: _typing.Optional[MyEnum]=...,
        oneway: _typing.Optional[bool]=...,
        floatList: _typing.Optional[_typing.Sequence[float]]=...,
        strMap: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        floatSet: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        MyIntField: _typing.Optional[int]=...,
        MyStringField: _typing.Optional[str]=...,
        MyDataField: _typing.Optional[MyDataItem]=...,
        myEnum: _typing.Optional[MyEnum]=...,
        oneway: _typing.Optional[bool]=...,
        floatList: _typing.Optional[_typing.Sequence[float]]=...,
        strMap: _typing.Optional[_typing.Mapping[bytes, str]]=...,
        floatSet: _typing.Optional[_typing.AbstractSet[int]]=...
    ) -> MyStruct: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, MyDataItem, MyEnum, bool, _typing.Sequence[float], _typing.Mapping[bytes, str], _typing.AbstractSet[int]]]]: ...
    def _to_python(self) -> MyStruct: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...  # type: ignore


class MyDataItem(_fbthrift_python_types.Struct):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> MyDataItem: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> MyDataItem: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyDataItem": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItem": ...  # type: ignore


class TransitiveDoubler(_fbthrift_python_types.Struct):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> TransitiveDoubler: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> TransitiveDoubler: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.TransitiveDoubler": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.TransitiveDoubler": ...  # type: ignore


class DoubledPair(_fbthrift_python_types.Struct):
    s: _typing.Final[str] = ...
    x: _typing.Final[int] = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> DoubledPair: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int]]]: ...
    def _to_python(self) -> DoubledPair: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.DoubledPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.DoubledPair": ...  # type: ignore


class StringPair(_fbthrift_python_types.Struct):
    normal: _typing.Final[str] = ...
    doubled: _typing.Final[str] = ...
    def __init__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> StringPair: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    def _to_python(self) -> StringPair: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.StringPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.StringPair": ...  # type: ignore


class MyUnion(_fbthrift_python_types.Union):
    myEnum: _typing.Final[MyEnum] = ...
    myStruct: _typing.Final[MyStruct] = ...
    myDataItem: _typing.Final[MyDataItem] = ...
    doubleSet: _typing.Final[_typing.AbstractSet[int]] = ...
    doubleList: _typing.Final[_typing.Sequence[float]] = ...
    strMap: _typing.Final[_typing.Mapping[bytes, str]] = ...
    def __init__(
        self, *,
        myEnum: _typing.Optional[MyEnum]=...,
        myStruct: _typing.Optional[MyStruct]=...,
        myDataItem: _typing.Optional[MyDataItem]=...,
        doubleSet: _typing.Optional[_typing.AbstractSet[int]]=...,
        doubleList: _typing.Optional[_typing.Sequence[float]]=...,
        strMap: _typing.Optional[_typing.Mapping[bytes, str]]=...
    ) -> None: ...


    class Type(enum.Enum):
        EMPTY: MyUnion.Type = ...
        myEnum: MyUnion.Type = ...
        myStruct: MyUnion.Type = ...
        myDataItem: MyUnion.Type = ...
        doubleSet: MyUnion.Type = ...
        doubleList: MyUnion.Type = ...
        strMap: MyUnion.Type = ...

    @classmethod
    def fromValue(cls, value: _typing.Union[None, MyEnum, MyStruct, MyDataItem, _typing.AbstractSet[int], _typing.Sequence[float], _typing.Mapping[bytes, str]]) -> MyUnion: ...
    value: _typing.Final[_typing.Union[None, MyEnum, MyStruct, MyDataItem, _typing.AbstractSet[int], _typing.Sequence[float], _typing.Mapping[bytes, str]]]
    type: Type
    def get_type(self) -> Type:...
    def _to_python(self) -> MyUnion: ...
    def _to_py3(self) -> "test.fixtures.basic-python-capi.module.types.MyUnion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyUnion": ...  # type: ignore
