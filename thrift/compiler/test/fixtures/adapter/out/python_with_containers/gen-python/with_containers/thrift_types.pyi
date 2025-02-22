#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import typing as _typing

import with_containers.thrift_types as _fbthrift_current_module
import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions
import my

from with_containers.thrift_enums import *


class _fbthrift_compatible_with__fbthrift_unadapted_AnnotationWithContainers:
    pass


class _fbthrift_unadapted_AnnotationWithContainers(_fbthrift_python_types.Struct, _fbthrift_compatible_with__fbthrift_unadapted_AnnotationWithContainers):
    names: _typing.Final[_typing.Sequence[str]] = ...
    counts: _typing.Final[_typing.Mapping[str, int]] = ...
    def __init__(
        self, *,
        names: _typing.Optional[_typing.Sequence[str]]=...,
        counts: _typing.Optional[_typing.Mapping[str, int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        names: _typing.Optional[_typing.Sequence[str]]=...,
        counts: _typing.Optional[_typing.Mapping[str, int]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[_typing.Sequence[str], _typing.Mapping[str, int]]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "with_containers.types._fbthrift_unadapted_AnnotationWithContainers": ...  # type: ignore
    def _to_py_deprecated(self) -> "with_containers.ttypes._fbthrift_unadapted_AnnotationWithContainers": ...  # type: ignore
AnnotationWithContainers = my.AdaptedType[_fbthrift_unadapted_AnnotationWithContainers]


class _fbthrift_compatible_with__fbthrift_unadapted_MyStruct:
    pass


class _fbthrift_unadapted_MyStruct(_fbthrift_python_types.Struct, _fbthrift_compatible_with__fbthrift_unadapted_MyStruct):
    abc: _typing.Final[my.AdaptedType[int]] = ...
    def __init__(
        self, *,
        abc: _typing.Optional[my.AdaptedType[int]]=...
    ) -> None: ...

    def __call__(
        self, *,
        abc: _typing.Optional[my.AdaptedType[int]]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[my.AdaptedType[int]]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "with_containers.types._fbthrift_unadapted_MyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "with_containers.ttypes._fbthrift_unadapted_MyStruct": ...  # type: ignore
MyStruct = my.AdaptedType[_fbthrift_unadapted_MyStruct]
