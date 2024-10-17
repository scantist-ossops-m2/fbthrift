#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/basic-enum/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import enum as _python_std_enum
import folly.iobuf as _fbthrift_iobuf
import thrift.py3.types
import thrift.py3.exceptions
import typing as _typing

import sys
import itertools


class EmptyEnum(thrift.py3.types.Enum):
    def _to_python(self) -> "test.fixtures.enumstrict.module.thrift_types.EmptyEnum": ...   # type: ignore
    def _to_py3(self) -> EmptyEnum: ...
    def _to_py_deprecated(self) -> int: ...


class MyEnum(thrift.py3.types.Enum):
    ONE: MyEnum = ...
    TWO: MyEnum = ...
    def _to_python(self) -> "test.fixtures.enumstrict.module.thrift_types.MyEnum": ...   # type: ignore
    def _to_py3(self) -> MyEnum: ...
    def _to_py_deprecated(self) -> int: ...


class MyUseIntrinsicDefaultEnum(thrift.py3.types.Enum):
    ZERO: MyUseIntrinsicDefaultEnum = ...
    ONE: MyUseIntrinsicDefaultEnum = ...
    TWO: MyUseIntrinsicDefaultEnum = ...
    def _to_python(self) -> "test.fixtures.enumstrict.module.thrift_types.MyUseIntrinsicDefaultEnum": ...   # type: ignore
    def _to_py3(self) -> MyUseIntrinsicDefaultEnum: ...
    def _to_py_deprecated(self) -> int: ...


class MyBigEnum(thrift.py3.types.Enum):
    UNKNOWN: MyBigEnum = ...
    ONE: MyBigEnum = ...
    TWO: MyBigEnum = ...
    THREE: MyBigEnum = ...
    FOUR: MyBigEnum = ...
    FIVE: MyBigEnum = ...
    SIX: MyBigEnum = ...
    SEVEN: MyBigEnum = ...
    EIGHT: MyBigEnum = ...
    NINE: MyBigEnum = ...
    TEN: MyBigEnum = ...
    ELEVEN: MyBigEnum = ...
    TWELVE: MyBigEnum = ...
    THIRTEEN: MyBigEnum = ...
    FOURTEEN: MyBigEnum = ...
    FIFTEEN: MyBigEnum = ...
    SIXTEEN: MyBigEnum = ...
    SEVENTEEN: MyBigEnum = ...
    EIGHTEEN: MyBigEnum = ...
    NINETEEN: MyBigEnum = ...
    def _to_python(self) -> "test.fixtures.enumstrict.module.thrift_types.MyBigEnum": ...   # type: ignore
    def _to_py3(self) -> MyBigEnum: ...
    def _to_py_deprecated(self) -> int: ...


class MyStruct(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        myEnum: bool
        myBigEnum: bool
        pass

    myEnum: _typing.Final[MyEnum] = ...
    myBigEnum: _typing.Final[MyBigEnum] = ...

    def __init__(
        self, *,
        myEnum: _typing.Optional[MyEnum]=None,
        myBigEnum: _typing.Optional[MyBigEnum]=None
    ) -> None: ...

    def __call__(
        self, *,
        myEnum: _typing.Union[MyEnum, None]=None,
        myBigEnum: _typing.Union[MyBigEnum, None]=None
    ) -> MyStruct: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['MyStruct'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'MyStruct') -> bool: ...
    def __gt__(self, other: 'MyStruct') -> bool: ...
    def __le__(self, other: 'MyStruct') -> bool: ...
    def __ge__(self, other: 'MyStruct') -> bool: ...

    def _to_python(self) -> "test.fixtures.enumstrict.module.thrift_types.MyStruct": ...   # type: ignore
    def _to_py3(self) -> MyStruct: ...
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...   # type: ignore

class Map__MyEnum_string(_typing.Mapping[MyEnum, str], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Mapping[MyEnum, str]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Mapping[MyEnum, str]: ...
    def __getitem__(self, key: MyEnum) -> str: ...
    def __iter__(self) -> _typing.Iterator[MyEnum]: ...


kOne: MyEnum = ...
enumNames: Map__MyEnum_string = ...
