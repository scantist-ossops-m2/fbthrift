#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import folly.iobuf as _fbthrift_iobuf

import test.fixtures.python_capi.containers.thrift_types as _fbthrift_current_module
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions



class TemplateLists(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "std_string",  # name
            "std_string",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "deque_string",  # name
            "deque_string",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_binary),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "small_vector_iobuf",  # name
            "small_vector_iobuf",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_iobuf),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "nested_small_vector",  # name
            "nested_small_vector",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_string)),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            5,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "small_vector_tensor",  # name
            "small_vector_tensor",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_string))),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.TemplateLists"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/TemplateLists"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_TemplateLists()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.TemplateLists, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.TemplateLists, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.TemplateLists, self)


class TemplateSets(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "std_set",  # name
            "std_set",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "std_unordered",  # name
            "std_unordered",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_fast",  # name
            "folly_fast",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_node",  # name
            "folly_node",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            5,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_value",  # name
            "folly_value",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            6,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_vector",  # name
            "folly_vector",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            7,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_sorted_vector",  # name
            "folly_sorted_vector",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.TemplateSets"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/TemplateSets"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_TemplateSets()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.TemplateSets, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.TemplateSets, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.TemplateSets, self)


class TemplateMaps(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "std_map",  # name
            "std_map",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "std_unordered",  # name
            "std_unordered",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_fast",  # name
            "folly_fast",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_node",  # name
            "folly_node",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            5,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_value",  # name
            "folly_value",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            6,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_vector",  # name
            "folly_vector",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            7,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "folly_sorted_vector",  # name
            "folly_sorted_vector",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.TemplateMaps"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/TemplateMaps"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_TemplateMaps()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.TemplateMaps, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.TemplateMaps, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.TemplateMaps, self)


class TWrapped(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "fieldA",  # name
            "fieldA",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "fieldB",  # name
            "fieldB",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_binary,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            9, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.TWrapped"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/TWrapped"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_TWrapped()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.TWrapped, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.TWrapped, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.TWrapped, self)


class IndirectionA(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "lst",  # name
            "lst",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.StructTypeInfo(TWrapped)),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.IndirectionA"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/IndirectionA"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_IndirectionA()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.IndirectionA, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.IndirectionA, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.IndirectionA, self)


class IndirectionB(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "lst",  # name
            "lst",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.StructTypeInfo(TWrapped)),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.IndirectionB"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/IndirectionB"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_IndirectionB()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.IndirectionB, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.IndirectionB, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.IndirectionB, self)


class IndirectionC(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "lst",  # name
            "lst",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.StructTypeInfo(TWrapped)),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "containers.IndirectionC"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/python_capi/IndirectionC"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_IndirectionC()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.python_capi.containers.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.IndirectionC, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.IndirectionC, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("containers.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.IndirectionC, self)

# This unfortunately has to be down here to prevent circular imports
import test.fixtures.python_capi.containers.thrift_metadata
from test.fixtures.python_capi.containers.thrift_enums import *

_fbthrift_all_enums = [
]


def _fbthrift_metadata__struct_TemplateLists():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_TemplateLists()


def _fbthrift_metadata__struct_TemplateSets():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_TemplateSets()


def _fbthrift_metadata__struct_TemplateMaps():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_TemplateMaps()


def _fbthrift_metadata__struct_TWrapped():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_TWrapped()


def _fbthrift_metadata__struct_IndirectionA():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_IndirectionA()


def _fbthrift_metadata__struct_IndirectionB():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_IndirectionB()


def _fbthrift_metadata__struct_IndirectionC():
    return test.fixtures.python_capi.containers.thrift_metadata.gen_metadata_struct_IndirectionC()


_fbthrift_all_structs = [
    TemplateLists,
    TemplateSets,
    TemplateMaps,
    TWrapped,
    IndirectionA,
    IndirectionB,
    IndirectionC,
]
_fbthrift_python_types.fill_specs(*_fbthrift_all_structs)

IOBuf = _fbthrift_iobuf.IOBuf
small_vector_iobuf = _fbthrift_python_types.ListTypeFactory(_fbthrift_python_types.typeinfo_iobuf)
fbvector_string = _fbthrift_python_types.ListTypeFactory(_fbthrift_python_types.typeinfo_string)
fbvector_fbvector_string = _fbthrift_python_types.ListTypeFactory(_fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_string))
CppWrapper = _fbthrift_current_module.TWrapped
ListOfWrapped = _fbthrift_python_types.ListTypeFactory(_fbthrift_python_types.StructTypeInfo(TWrapped))
VecOfWrapped = _fbthrift_python_types.ListTypeFactory(_fbthrift_python_types.StructTypeInfo(TWrapped))
ListOfWrappedAlias = _fbthrift_python_types.ListTypeFactory(_fbthrift_python_types.StructTypeInfo(TWrapped))
