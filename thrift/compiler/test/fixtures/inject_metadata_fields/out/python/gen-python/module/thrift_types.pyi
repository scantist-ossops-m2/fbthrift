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

import foo.thrift_types as _fbthrift__foo__thrift_types

from module.thrift_enums import *


class _fbthrift_compatible_with_Fields:
    pass


class Fields(_fbthrift_python_types.Struct, _fbthrift_compatible_with_Fields):
    injected_field: _typing.Final[str] = ...
    def __init__(
        self, *,
        injected_field: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        injected_field: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "module.types.Fields": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.Fields": ...  # type: ignore


class _fbthrift_compatible_with_FieldsInjectedToEmptyStruct:
    pass


class FieldsInjectedToEmptyStruct(_fbthrift_python_types.Struct, _fbthrift_compatible_with_FieldsInjectedToEmptyStruct):
    injected_field: _typing.Final[str] = ...
    def __init__(
        self, *,
        injected_field: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        injected_field: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "module.types.FieldsInjectedToEmptyStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.FieldsInjectedToEmptyStruct": ...  # type: ignore


class _fbthrift_compatible_with_FieldsInjectedToStruct:
    pass


class FieldsInjectedToStruct(_fbthrift_python_types.Struct, _fbthrift_compatible_with_FieldsInjectedToStruct):
    injected_field: _typing.Final[str] = ...
    string_field: _typing.Final[str] = ...
    def __init__(
        self, *,
        injected_field: _typing.Optional[str]=...,
        string_field: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        injected_field: _typing.Optional[str]=...,
        string_field: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "module.types.FieldsInjectedToStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.FieldsInjectedToStruct": ...  # type: ignore


class _fbthrift_compatible_with_FieldsInjectedWithIncludedStruct:
    pass


class FieldsInjectedWithIncludedStruct(_fbthrift_python_types.Struct, _fbthrift_compatible_with_FieldsInjectedWithIncludedStruct):
    injected_unstructured_annotation_field: _typing.Final[_typing.Optional[str]] = ...
    injected_structured_annotation_field: _typing.Final[_typing.Optional[str]] = ...
    injected_field: _typing.Final[str] = ...
    string_field: _typing.Final[str] = ...
    def __init__(
        self, *,
        injected_unstructured_annotation_field: _typing.Optional[str]=...,
        injected_structured_annotation_field: _typing.Optional[str]=...,
        injected_field: _typing.Optional[str]=...,
        string_field: _typing.Optional[str]=...
    ) -> None: ...

    def __call__(
        self, *,
        injected_unstructured_annotation_field: _typing.Optional[str]=...,
        injected_structured_annotation_field: _typing.Optional[str]=...,
        injected_field: _typing.Optional[str]=...,
        string_field: _typing.Optional[str]=...
    ) -> _typing.Self: ...
    def __iter__(self) -> _typing.Iterator[_typing.Tuple[str, _typing.Union[str, str, str, str]]]: ...
    def _to_python(self) -> _typing.Self: ...
    def _to_py3(self) -> "module.types.FieldsInjectedWithIncludedStruct": ...  # type: ignore
    def _to_py_deprecated(self) -> "module.ttypes.FieldsInjectedWithIncludedStruct": ...  # type: ignore
