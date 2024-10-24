#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations


# EXPERIMENTAL - DO NOT USE !!!
# See `experimental_generate_mutable_types` documentation in thrift compiler

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
import test.fixtures.python_capi.module.thrift_abstract_types
import thrift.python.types as _fbthrift_python_types
import thrift.python.mutable_types as _fbthrift_python_mutable_types
import thrift.python.mutable_exceptions as _fbthrift_python_mutable_exceptions
import thrift.python.mutable_containers as _fbthrift_python_mutable_containers

import apache.thrift.type.id.thrift_types

import apache.thrift.type.schema.thrift_types

import test.fixtures.python_capi.serialized_dep.thrift_types

import test.fixtures.python_capi.thrift_dep.thrift_types

class _fbthrift_compatible_with_MyEnum:
    pass


class MyEnum(_fbthrift_python_types.Enum, int, test.fixtures.python_capi.module.thrift_abstract_types.MyEnum, _fbthrift_compatible_with_MyEnum):
    MyValue1: MyEnum = ...
    MyValue2: MyEnum = ...
    def _to_python(self) -> MyEnum: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...

class _fbthrift_compatible_with_AnnoyingEnum:
    pass


class AnnoyingEnum(_fbthrift_python_types.Enum, int, test.fixtures.python_capi.module.thrift_abstract_types.AnnoyingEnum, _fbthrift_compatible_with_AnnoyingEnum):
    FOO: AnnoyingEnum = ...
    BAR: AnnoyingEnum = ...
    def _to_python(self) -> AnnoyingEnum: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.AnnoyingEnum": ...  # type: ignore
    def _to_py_deprecated(self) -> int: ...


class _fbthrift_compatible_with_MyStruct:
    pass


class MyStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_MyStruct, test.fixtures.python_capi.module.thrift_abstract_types.MyStruct):
    inty: int = ...
    stringy: str = ...
    myItemy: MyDataItem = ...
    myEnumy: MyEnum = ...
    booly: bool = ...

    @property
    def floatListy(self) -> _fbthrift_python_mutable_containers.MutableList[float]: ...
    @floatListy.setter
    def floatListy(self, value: _fbthrift_python_mutable_containers.MutableList[float] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def strMappy(self) -> _typing.MutableMapping[bytes, str]: ...
    @strMappy.setter
    def strMappy(self, value: _typing.MutableMapping[bytes, str]): ...


    @property
    def intSetty(self) -> _typing.MutableSet[int]: ...
    @intSetty.setter
    def intSetty(self, value: _typing.MutableSet[int]): ...

    def __init__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[_fbthrift_compatible_with_MyDataItem]=...,
        myEnumy: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[float] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        strMappy: _typing.Optional[_typing.MutableMapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.MutableSet[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        inty: _typing.Optional[int]=...,
        stringy: _typing.Optional[str]=...,
        myItemy: _typing.Optional[_fbthrift_compatible_with_MyDataItem]=...,
        myEnumy: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        booly: _typing.Optional[bool]=...,
        floatListy: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[float] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        strMappy: _typing.Optional[_typing.MutableMapping[bytes, str]]=...,
        intSetty: _typing.Optional[_typing.MutableSet[int]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, str, MyDataItem, MyEnum, bool, _fbthrift_python_mutable_containers.MutableList[float], _typing.MutableMapping[bytes, str], _typing.MutableSet[int]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MyStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyStruct": ...  # type: ignore


class _fbthrift_compatible_with_MyDataItem:
    pass


class MyDataItem(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_MyDataItem, test.fixtures.python_capi.module.thrift_abstract_types.MyDataItem):
    s: str = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MyDataItem": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MyDataItem": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MyDataItem": ...  # type: ignore


class _fbthrift_compatible_with_TransitiveDoubler:
    pass


class TransitiveDoubler(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_TransitiveDoubler, test.fixtures.python_capi.module.thrift_abstract_types.TransitiveDoubler):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.TransitiveDoubler": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.TransitiveDoubler": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.TransitiveDoubler": ...  # type: ignore


class _fbthrift_compatible_with_DoubledPair:
    pass


class DoubledPair(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_DoubledPair, test.fixtures.python_capi.module.thrift_abstract_types.DoubledPair):
    s: str = ...
    x: int = ...
    def __init__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        s: _typing.Optional[str]=...,
        x: _typing.Optional[int]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, int]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.DoubledPair": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.DoubledPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.DoubledPair": ...  # type: ignore


class _fbthrift_compatible_with_StringPair:
    pass


class StringPair(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_StringPair, test.fixtures.python_capi.module.thrift_abstract_types.StringPair):
    normal: str = ...
    doubled: str = ...
    def __init__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        normal: _typing.Optional[str]=...,
        doubled: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.StringPair": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.StringPair": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.StringPair": ...  # type: ignore


class _fbthrift_compatible_with_EmptyStruct:
    pass


class EmptyStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_EmptyStruct, test.fixtures.python_capi.module.thrift_abstract_types.EmptyStruct):
    def __init__(
        self,
    ) -> None: ...

    def __call__(
        self,
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[None]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.EmptyStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.EmptyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.EmptyStruct": ...  # type: ignore


class _fbthrift_compatible_with_PrimitiveStruct:
    pass


class PrimitiveStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_PrimitiveStruct, test.fixtures.python_capi.module.thrift_abstract_types.PrimitiveStruct):
    booly: bool = ...
    charry: int = ...
    shorty: int = ...
    inty: int = ...
    longy: int = ...
    floaty: _typing.Optional[float] = ...
    dubby: _typing.Optional[float] = ...
    stringy: _typing.Optional[str] = ...
    bytey: _typing.Optional[bytes] = ...
    buffy: _fbthrift_iobuf.IOBuf = ...
    pointbuffy: _fbthrift_iobuf.IOBuf = ...
    patched_struct: MyStruct = ...
    empty_struct: EmptyStruct = ...
    fbstring: bytes = ...
    managed_string_view: str = ...
    some_error: test.fixtures.python_capi.thrift_dep.thrift_mutable_types.SomeError = ...
    def __init__(
        self, *,
        booly: _typing.Optional[bool]=...,
        charry: _typing.Optional[int]=...,
        shorty: _typing.Optional[int]=...,
        inty: _typing.Optional[int]=...,
        longy: _typing.Optional[int]=...,
        floaty: _typing.Optional[float]=...,
        dubby: _typing.Optional[float]=...,
        stringy: _typing.Optional[str]=...,
        bytey: _typing.Optional[bytes]=...,
        buffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        pointbuffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        patched_struct: _typing.Optional[_fbthrift_compatible_with_MyStruct]=...,
        empty_struct: _typing.Optional[_fbthrift_compatible_with_EmptyStruct]=...,
        fbstring: _typing.Optional[bytes]=...,
        managed_string_view: _typing.Optional[str]=...,
        some_error: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_SomeError]=...
    ) -> None: ...

    def __call__(
        self, *,
        booly: _typing.Optional[bool]=...,
        charry: _typing.Optional[int]=...,
        shorty: _typing.Optional[int]=...,
        inty: _typing.Optional[int]=...,
        longy: _typing.Optional[int]=...,
        floaty: _typing.Optional[float]=...,
        dubby: _typing.Optional[float]=...,
        stringy: _typing.Optional[str]=...,
        bytey: _typing.Optional[bytes]=...,
        buffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        pointbuffy: _typing.Optional[_fbthrift_iobuf.IOBuf]=...,
        patched_struct: _typing.Optional[_fbthrift_compatible_with_MyStruct]=...,
        empty_struct: _typing.Optional[_fbthrift_compatible_with_EmptyStruct]=...,
        fbstring: _typing.Optional[bytes]=...,
        managed_string_view: _typing.Optional[str]=...,
        some_error: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_SomeError]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[bool, int, int, int, int, float, float, str, bytes, _fbthrift_iobuf.IOBuf, _fbthrift_iobuf.IOBuf, MyStruct, EmptyStruct, bytes, str, test.fixtures.python_capi.thrift_dep.thrift_mutable_types.SomeError]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.PrimitiveStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.PrimitiveStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.PrimitiveStruct": ...  # type: ignore


class _fbthrift_compatible_with_AdaptedFields:
    pass


class AdaptedFields(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_AdaptedFields, test.fixtures.python_capi.module.thrift_abstract_types.AdaptedFields):
    adapted_int: int = ...

    @property
    def list_adapted_int(self) -> _fbthrift_python_mutable_containers.MutableList[int]: ...
    @list_adapted_int.setter
    def list_adapted_int(self, value: _fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def set_adapted_int(self) -> _typing.MutableSet[int]: ...
    @set_adapted_int.setter
    def set_adapted_int(self, value: _typing.MutableSet[int]): ...

    inline_adapted_int: int = ...
    def __init__(
        self, *,
        adapted_int: _typing.Optional[int]=...,
        list_adapted_int: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        set_adapted_int: _typing.Optional[_typing.MutableSet[int]]=...,
        inline_adapted_int: _typing.Optional[int]=...
    ) -> None: ...

    def __call__(
        self, *,
        adapted_int: _typing.Optional[int]=...,
        list_adapted_int: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        set_adapted_int: _typing.Optional[_typing.MutableSet[int]]=...,
        inline_adapted_int: _typing.Optional[int]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[int, _fbthrift_python_mutable_containers.MutableList[int], _typing.MutableSet[int], int]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.AdaptedFields": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.AdaptedFields": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.AdaptedFields": ...  # type: ignore


class _fbthrift_compatible_with_ListStruct:
    pass


class ListStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_ListStruct, test.fixtures.python_capi.module.thrift_abstract_types.ListStruct):

    @property
    def boolz(self) -> _fbthrift_python_mutable_containers.MutableList[bool]: ...
    @boolz.setter
    def boolz(self, value: _fbthrift_python_mutable_containers.MutableList[bool] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def intz(self) -> _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int]]: ...
    @intz.setter
    def intz(self, value: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def stringz(self) -> _typing.Optional[_fbthrift_python_mutable_containers.MutableList[str]]: ...
    @stringz.setter
    def stringz(self, value: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[str]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def encoded(self) -> _fbthrift_python_mutable_containers.MutableList[bytes]: ...
    @encoded.setter
    def encoded(self, value: _fbthrift_python_mutable_containers.MutableList[bytes] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def uidz(self) -> _fbthrift_python_mutable_containers.MutableList[int]: ...
    @uidz.setter
    def uidz(self, value: _fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def matrix(self) -> _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[float]]: ...
    @matrix.setter
    def matrix(self, value: _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[float]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def ucharz(self) -> _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]]: ...
    @ucharz.setter
    def ucharz(self, value: _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def voxels(self) -> _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]]]: ...
    @voxels.setter
    def voxels(self, value: _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def buf_ptrs(self) -> _fbthrift_python_mutable_containers.MutableList[_fbthrift_iobuf.IOBuf]: ...
    @buf_ptrs.setter
    def buf_ptrs(self, value: _fbthrift_python_mutable_containers.MutableList[_fbthrift_iobuf.IOBuf] | _fbthrift_python_mutable_types._ThriftListWrapper): ...

    def __init__(
        self, *,
        boolz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[bool] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        intz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        stringz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[str] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        encoded: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[bytes] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        uidz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        matrix: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[float]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        ucharz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        voxels: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        buf_ptrs: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_iobuf.IOBuf] | _fbthrift_python_mutable_types._ThriftListWrapper]=...
    ) -> None: ...

    def __call__(
        self, *,
        boolz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[bool] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        intz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        stringz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[str] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        encoded: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[bytes] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        uidz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[int] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        matrix: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[float]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        ucharz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        voxels: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        buf_ptrs: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_fbthrift_iobuf.IOBuf] | _fbthrift_python_mutable_types._ThriftListWrapper]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_fbthrift_python_mutable_containers.MutableList[bool], _fbthrift_python_mutable_containers.MutableList[int], _fbthrift_python_mutable_containers.MutableList[str], _fbthrift_python_mutable_containers.MutableList[bytes], _fbthrift_python_mutable_containers.MutableList[int], _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[float]], _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]], _fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[_fbthrift_python_mutable_containers.MutableList[int]]], _fbthrift_python_mutable_containers.MutableList[_fbthrift_iobuf.IOBuf]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.ListStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.ListStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ListStruct": ...  # type: ignore


class _fbthrift_compatible_with_SetStruct:
    pass


class SetStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_SetStruct, test.fixtures.python_capi.module.thrift_abstract_types.SetStruct):

    @property
    def enumz(self) -> _typing.MutableSet[MyEnum]: ...
    @enumz.setter
    def enumz(self, value: _typing.MutableSet[MyEnum]): ...


    @property
    def intz(self) -> _typing.Optional[_typing.MutableSet[int]]: ...
    @intz.setter
    def intz(self, value: _typing.Optional[_typing.MutableSet[int]]): ...


    @property
    def binnaz(self) -> _typing.Optional[_typing.MutableSet[bytes]]: ...
    @binnaz.setter
    def binnaz(self, value: _typing.Optional[_typing.MutableSet[bytes]]): ...


    @property
    def encoded(self) -> _typing.MutableSet[bytes]: ...
    @encoded.setter
    def encoded(self, value: _typing.MutableSet[bytes]): ...


    @property
    def uidz(self) -> _typing.MutableSet[int]: ...
    @uidz.setter
    def uidz(self, value: _typing.MutableSet[int]): ...


    @property
    def charz(self) -> _typing.MutableSet[int]: ...
    @charz.setter
    def charz(self, value: _typing.MutableSet[int]): ...


    @property
    def setz(self) -> _fbthrift_python_mutable_containers.MutableList[_typing.MutableSet[int]]: ...
    @setz.setter
    def setz(self, value: _fbthrift_python_mutable_containers.MutableList[_typing.MutableSet[int]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...

    def __init__(
        self, *,
        enumz: _typing.Optional[_typing.MutableSet[_fbthrift_compatible_with_MyEnum]]=...,
        intz: _typing.Optional[_typing.MutableSet[int]]=...,
        binnaz: _typing.Optional[_typing.MutableSet[bytes]]=...,
        encoded: _typing.Optional[_typing.MutableSet[bytes]]=...,
        uidz: _typing.Optional[_typing.MutableSet[int]]=...,
        charz: _typing.Optional[_typing.MutableSet[int]]=...,
        setz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_typing.MutableSet[int]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...
    ) -> None: ...

    def __call__(
        self, *,
        enumz: _typing.Optional[_typing.MutableSet[_fbthrift_compatible_with_MyEnum]]=...,
        intz: _typing.Optional[_typing.MutableSet[int]]=...,
        binnaz: _typing.Optional[_typing.MutableSet[bytes]]=...,
        encoded: _typing.Optional[_typing.MutableSet[bytes]]=...,
        uidz: _typing.Optional[_typing.MutableSet[int]]=...,
        charz: _typing.Optional[_typing.MutableSet[int]]=...,
        setz: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_typing.MutableSet[int]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.MutableSet[MyEnum], _typing.MutableSet[int], _typing.MutableSet[bytes], _typing.MutableSet[bytes], _typing.MutableSet[int], _typing.MutableSet[int], _fbthrift_python_mutable_containers.MutableList[_typing.MutableSet[int]]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.SetStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.SetStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.SetStruct": ...  # type: ignore


class _fbthrift_compatible_with_MapStruct:
    pass


class MapStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_MapStruct, test.fixtures.python_capi.module.thrift_abstract_types.MapStruct):

    @property
    def enumz(self) -> _typing.MutableMapping[MyEnum, str]: ...
    @enumz.setter
    def enumz(self, value: _typing.MutableMapping[MyEnum, str]): ...


    @property
    def intz(self) -> _typing.Optional[_typing.MutableMapping[int, str]]: ...
    @intz.setter
    def intz(self, value: _typing.Optional[_typing.MutableMapping[int, str]]): ...


    @property
    def binnaz(self) -> _typing.Optional[_typing.MutableMapping[bytes, PrimitiveStruct]]: ...
    @binnaz.setter
    def binnaz(self, value: _typing.Optional[_typing.MutableMapping[bytes, PrimitiveStruct]]): ...


    @property
    def encoded(self) -> _typing.MutableMapping[str, float]: ...
    @encoded.setter
    def encoded(self, value: _typing.MutableMapping[str, float]): ...


    @property
    def flotz(self) -> _typing.MutableMapping[int, float]: ...
    @flotz.setter
    def flotz(self, value: _typing.MutableMapping[int, float]): ...


    @property
    def map_list(self) -> _fbthrift_python_mutable_containers.MutableList[_typing.MutableMapping[int, int]]: ...
    @map_list.setter
    def map_list(self, value: _fbthrift_python_mutable_containers.MutableList[_typing.MutableMapping[int, int]] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def list_map(self) -> _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]: ...
    @list_map.setter
    def list_map(self, value: _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]): ...


    @property
    def fast_list_map(self) -> _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[float]]: ...
    @fast_list_map.setter
    def fast_list_map(self, value: _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[float]]): ...


    @property
    def buf_map(self) -> _typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf]: ...
    @buf_map.setter
    def buf_map(self, value: _typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf]): ...


    @property
    def unsigned_list_map(self) -> _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]: ...
    @unsigned_list_map.setter
    def unsigned_list_map(self, value: _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]): ...

    def __init__(
        self, *,
        enumz: _typing.Optional[_typing.MutableMapping[MyEnum, str]]=...,
        intz: _typing.Optional[_typing.MutableMapping[int, str]]=...,
        binnaz: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_compatible_with_PrimitiveStruct]]=...,
        encoded: _typing.Optional[_typing.MutableMapping[str, float]]=...,
        flotz: _typing.Optional[_typing.MutableMapping[int, float]]=...,
        map_list: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_typing.MutableMapping[int, int]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        list_map: _typing.Optional[_typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]]=...,
        fast_list_map: _typing.Optional[_typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[float]]]=...,
        buf_map: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf]]=...,
        unsigned_list_map: _typing.Optional[_typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]]=...
    ) -> None: ...

    def __call__(
        self, *,
        enumz: _typing.Optional[_typing.MutableMapping[MyEnum, str]]=...,
        intz: _typing.Optional[_typing.MutableMapping[int, str]]=...,
        binnaz: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_compatible_with_PrimitiveStruct]]=...,
        encoded: _typing.Optional[_typing.MutableMapping[str, float]]=...,
        flotz: _typing.Optional[_typing.MutableMapping[int, float]]=...,
        map_list: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[_typing.MutableMapping[int, int]] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        list_map: _typing.Optional[_typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]]=...,
        fast_list_map: _typing.Optional[_typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[float]]]=...,
        buf_map: _typing.Optional[_typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf]]=...,
        unsigned_list_map: _typing.Optional[_typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.MutableMapping[MyEnum, str], _typing.MutableMapping[int, str], _typing.MutableMapping[bytes, PrimitiveStruct], _typing.MutableMapping[str, float], _typing.MutableMapping[int, float], _fbthrift_python_mutable_containers.MutableList[_typing.MutableMapping[int, int]], _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]], _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[float]], _typing.MutableMapping[bytes, _fbthrift_iobuf.IOBuf], _typing.MutableMapping[int, _fbthrift_python_mutable_containers.MutableList[int]]]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.MapStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.MapStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.MapStruct": ...  # type: ignore


class _fbthrift_compatible_with_ComposeStruct:
    pass


class ComposeStruct(_fbthrift_python_mutable_types.MutableStruct, _fbthrift_compatible_with_ComposeStruct, test.fixtures.python_capi.module.thrift_abstract_types.ComposeStruct):
    enum_: MyEnum = ...
    renamed_: AnnoyingEnum = ...
    primitive: PrimitiveStruct = ...
    aliased: ListStruct = ...
    xenum: test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepEnum = ...
    xstruct: test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct = ...

    @property
    def friends(self) -> _fbthrift_python_mutable_containers.MutableList[test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct]: ...
    @friends.setter
    def friends(self, value: _fbthrift_python_mutable_containers.MutableList[test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct] | _fbthrift_python_mutable_types._ThriftListWrapper): ...

    serial_struct: test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedStruct = ...
    serial_union: test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedUnion = ...
    serial_error: test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedError = ...
    def __init__(
        self, *,
        enum_: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        renamed_: _typing.Optional[_fbthrift_compatible_with_AnnoyingEnum]=...,
        primitive: _typing.Optional[_fbthrift_compatible_with_PrimitiveStruct]=...,
        aliased: _typing.Optional[_fbthrift_compatible_with_ListStruct]=...,
        xenum: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepEnum]=...,
        xstruct: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct]=...,
        friends: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        serial_struct: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedStruct]=...,
        serial_union: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedUnion]=...,
        serial_error: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedError]=...
    ) -> None: ...

    def __call__(
        self, *,
        enum_: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        renamed_: _typing.Optional[_fbthrift_compatible_with_AnnoyingEnum]=...,
        primitive: _typing.Optional[_fbthrift_compatible_with_PrimitiveStruct]=...,
        aliased: _typing.Optional[_fbthrift_compatible_with_ListStruct]=...,
        xenum: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepEnum]=...,
        xstruct: _typing.Optional[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct]=...,
        friends: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[test.fixtures.python_capi.thrift_dep.thrift_mutable_types._fbthrift_compatible_with_DepStruct] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        serial_struct: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedStruct]=...,
        serial_union: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedUnion]=...,
        serial_error: _typing.Optional[test.fixtures.python_capi.serialized_dep.thrift_mutable_types._fbthrift_compatible_with_SerializedError]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[MyEnum, AnnoyingEnum, PrimitiveStruct, ListStruct, test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepEnum, test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct, _fbthrift_python_mutable_containers.MutableList[test.fixtures.python_capi.thrift_dep.thrift_mutable_types.DepStruct], test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedStruct, test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedUnion, test.fixtures.python_capi.serialized_dep.thrift_mutable_types.SerializedError]]]: ...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.ComposeStruct": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.ComposeStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.ComposeStruct": ...  # type: ignore


class _fbthrift_compatible_with_Onion:
    pass


class Onion(_fbthrift_python_mutable_types.MutableUnion, _fbthrift_compatible_with_Onion, test.fixtures.python_capi.module.thrift_abstract_types.Onion):
    myEnum: MyEnum = ...
    myStruct: PrimitiveStruct = ...
    myString: str = ...

    @property
    def intSet(self) -> _typing.MutableSet[int]: ...
    @intSet.setter
    def intSet(self, value: _typing.MutableSet[int]): ...


    @property
    def doubleList(self) -> _fbthrift_python_mutable_containers.MutableList[float]: ...
    @doubleList.setter
    def doubleList(self, value: _fbthrift_python_mutable_containers.MutableList[float] | _fbthrift_python_mutable_types._ThriftListWrapper): ...


    @property
    def strMap(self) -> _typing.MutableMapping[bytes, str]: ...
    @strMap.setter
    def strMap(self, value: _typing.MutableMapping[bytes, str]): ...

    adapted_int: int = ...
    def __init__(
        self, *,
        myEnum: _typing.Optional[_fbthrift_compatible_with_MyEnum]=...,
        myStruct: _typing.Optional[_fbthrift_compatible_with_PrimitiveStruct]=...,
        myString: _typing.Optional[str]=...,
        intSet: _typing.Optional[_typing.MutableSet[int]]=...,
        doubleList: _typing.Optional[_fbthrift_python_mutable_containers.MutableList[float] | _fbthrift_python_mutable_types._ThriftListWrapper]=...,
        strMap: _typing.Optional[_typing.MutableMapping[bytes, str]]=...,
        adapted_int: _typing.Optional[int]=...
    ) -> None: ...


    class FbThriftUnionFieldEnum(enum.Enum):
        EMPTY: Onion.FbThriftUnionFieldEnum = ...
        myEnum: Onion.Type = ...
        myStruct: Onion.Type = ...
        myString: Onion.Type = ...
        intSet: Onion.Type = ...
        doubleList: Onion.Type = ...
        strMap: Onion.Type = ...
        adapted_int: Onion.Type = ...

    fbthrift_current_value: _typing.Final[_typing.Union[None, MyEnum, PrimitiveStruct, str, _typing.MutableSet[int], _fbthrift_python_mutable_containers.MutableList[float], _typing.MutableMapping[bytes, str], int]]
    fbthrift_current_field: _typing.Final[FbThriftUnionFieldEnum]
    def get_type(self) -> FbThriftUnionFieldEnum:...
    def _to_python(self) -> "test.fixtures.python_capi.module.thrift_types.Onion": ...  # type: ignore
    def _to_mutable_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "test.fixtures.python_capi.module.types.Onion": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Onion": ...  # type: ignore

uint64 = int
ui64 = int
signed_byte = int
IOBuf = _fbthrift_iobuf.IOBuf
IOBufPtr = _fbthrift_iobuf.IOBuf
ListAlias = ListStruct
