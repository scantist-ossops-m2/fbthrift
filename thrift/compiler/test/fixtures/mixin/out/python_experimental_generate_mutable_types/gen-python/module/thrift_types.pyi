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

from module.thrift_enums import *


class _fbthrift_compatible_with_Mixin1:
    pass


class Mixin1(_fbthrift_python_types.Struct, _fbthrift_compatible_with_Mixin1):
    field1: _typing.Final[str] = ...
    def __init__(
        self, *,
        field1: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        field1: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Mixin1": ...  # type: ignore
    def _to_py3(self) -> "module.types.Mixin1": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Mixin1": ...  # type: ignore


class _fbthrift_compatible_with_Mixin2:
    pass


class Mixin2(_fbthrift_python_types.Struct, _fbthrift_compatible_with_Mixin2):
    m1: _typing.Final[Mixin1] = ...
    field2: _typing.Final[_typing.Optional[str]] = ...
    def __init__(
        self, *,
        m1: _typing.Optional[_fbthrift_compatible_with_Mixin1]=...,
        field2: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        m1: _typing.Optional[_fbthrift_compatible_with_Mixin1]=...,
        field2: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[Mixin1, str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Mixin2": ...  # type: ignore
    def _to_py3(self) -> "module.types.Mixin2": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Mixin2": ...  # type: ignore


class _fbthrift_compatible_with_Mixin3Base:
    pass


class Mixin3Base(_fbthrift_python_types.Struct, _fbthrift_compatible_with_Mixin3Base):
    field3: _typing.Final[str] = ...
    def __init__(
        self, *,
        field3: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        field3: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Mixin3Base": ...  # type: ignore
    def _to_py3(self) -> "module.types.Mixin3Base": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Mixin3Base": ...  # type: ignore


class _fbthrift_compatible_with_Foo:
    pass


class Foo(_fbthrift_python_types.Struct, _fbthrift_compatible_with_Foo):
    field4: _typing.Final[str] = ...
    m2: _typing.Final[Mixin2] = ...
    m3: _typing.Final[Mixin3Base] = ...
    def __init__(
        self, *,
        field4: _typing.Optional[str]=...,
        m2: _typing.Optional[_fbthrift_compatible_with_Mixin2]=...,
        m3: _typing.Optional[_fbthrift_compatible_with_Mixin3Base]=...
    ) -> None: ...

    def __call__(
        self, *,
        field4: _typing.Optional[str]=...,
        m2: _typing.Optional[_fbthrift_compatible_with_Mixin2]=...,
        m3: _typing.Optional[_fbthrift_compatible_with_Mixin3Base]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, Mixin2, Mixin3Base]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_mutable_python(self) -> "module.thrift_mutable_types.Foo": ...  # type: ignore
    def _to_py3(self) -> "module.types.Foo": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Foo": ...  # type: ignore

Mixin3 = Mixin3Base
