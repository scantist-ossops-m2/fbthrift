#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import folly.iobuf as _fbthrift_iobuf

import module.thrift_types as _fbthrift_current_module
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions



class Mixin1(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "field1",  # name
            "field1",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Mixin1"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_Mixin1()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.Mixin1, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.Mixin1, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.Mixin1, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.Mixin1, self)


class Mixin2(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "m1",  # name
            "m1",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(Mixin1),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "field2",  # name
            "field2",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Mixin2"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_Mixin2()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.Mixin2, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.Mixin2, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.Mixin2, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.Mixin2, self)


class Mixin3Base(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "field3",  # name
            "field3",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Mixin3Base"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_Mixin3Base()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.Mixin3Base, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.Mixin3Base, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.Mixin3Base, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.Mixin3Base, self)


class Foo(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "field4",  # name
            "field4",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "m2",  # name
            "m2",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(Mixin2),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "m3",  # name
            "m3",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(Mixin3Base),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Foo"

    @staticmethod
    def __get_thrift_uri__():
        return None

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_Foo()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.Foo, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.Foo, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.Foo, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.Foo, self)

# This unfortunately has to be down here to prevent circular imports
import module.thrift_metadata
from module.thrift_enums import *

_fbthrift_all_enums = [
]


def _fbthrift_metadata__struct_Mixin1():
    return module.thrift_metadata.gen_metadata_struct_Mixin1()


def _fbthrift_metadata__struct_Mixin2():
    return module.thrift_metadata.gen_metadata_struct_Mixin2()


def _fbthrift_metadata__struct_Mixin3Base():
    return module.thrift_metadata.gen_metadata_struct_Mixin3Base()


def _fbthrift_metadata__struct_Foo():
    return module.thrift_metadata.gen_metadata_struct_Foo()


_fbthrift_all_structs = [
    Mixin1,
    Mixin2,
    Mixin3Base,
    Foo,
]
_fbthrift_python_types.fill_specs(*_fbthrift_all_structs)

Mixin3 = _fbthrift_current_module.Mixin3Base
