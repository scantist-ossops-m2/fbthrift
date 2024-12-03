#
# Autogenerated by Thrift
#
# DO NOT EDIT
#  @generated
#

from __future__ import annotations

import folly.iobuf as _fbthrift_iobuf
import thrift.python.types as _fbthrift_python_types
import thrift.python.exceptions as _fbthrift_python_exceptions



class MyStruct(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyIntField",  # name
            "MyIntField",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyStringField",  # name
            "MyStringField",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyDataField",  # name
            "MyDataField",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyDataItem),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myEnum",  # name
            "myEnum",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.EnumTypeInfo(MyEnum),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            10, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            5,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "oneway",  # name
            "oneway",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_bool,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            1, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            6,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "readonly",  # name
            "readonly",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_bool,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            1, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            7,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "idempotent",  # name
            "idempotent",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_bool,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            1, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            8,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "floatSet",  # name
            "floatSet",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_float),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            9,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "no_hack_codegen_field",  # name
            "no_hack_codegen_field",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyStruct"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/MyStruct"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_MyStruct()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.MyStruct, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyStruct, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.MyStruct, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.MyStruct, self)


class Containers(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "I32List",  # name
            "I32List",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_i32),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            14, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "StringSet",  # name
            "StringSet",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "StringToI64Map",  # name
            "StringToI64Map",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.typeinfo_i64),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            16, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.Containers"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/Containers"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_Containers()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.Containers, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.Containers, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.Containers, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.Containers, self)


class MyDataItem(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyDataItem"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/MyDataItem"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_MyDataItem()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.MyDataItem, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyDataItem, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.MyDataItem, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.MyDataItem, self)


class MyUnion(metaclass=_fbthrift_python_types.UnionMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myEnum",  # name
            "myEnum",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.EnumTypeInfo(MyEnum),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            10, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myStruct",  # name
            "myStruct",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyStruct),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myDataItem",  # name
            "myDataItem",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyDataItem),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "floatSet",  # name
            "floatSet",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_float),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            15, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyUnion"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/MyUnion"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_MyUnion()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.MyUnion, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyUnion, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.MyUnion, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.MyUnion, self)


class MyException(metaclass=_fbthrift_python_exceptions.GeneratedErrorMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyIntField",  # name
            "MyIntField",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyStringField",  # name
            "MyStringField",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myStruct",  # name
            "myStruct",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyStruct),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myUnion",  # name
            "myUnion",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyUnion),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyException"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/MyException"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__exception_MyException()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.MyException, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyException, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.MyException, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.MyException, self)


class MyExceptionWithMessage(metaclass=_fbthrift_python_exceptions.GeneratedErrorMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyIntField",  # name
            "MyIntField",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyStringField",  # name
            "MyStringField",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myStruct",  # name
            "myStruct",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyStruct),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myUnion",  # name
            "myUnion",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(MyUnion),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyExceptionWithMessage"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/MyExceptionWithMessage"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__exception_MyExceptionWithMessage()


    def __str__(self):
        field = self.MyStringField
        if field is None:
            return str(field)
        return field

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.MyExceptionWithMessage, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyExceptionWithMessage, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.MyExceptionWithMessage, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.MyExceptionWithMessage, self)


class ReservedKeyword(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "reserved_field",  # name
            "reserved_field",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i32,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            4, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.ReservedKeyword"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/ReservedKeyword"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_ReservedKeyword()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.ReservedKeyword, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.ReservedKeyword, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.ReservedKeyword, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.ReservedKeyword, self)


class UnionToBeRenamed(metaclass=_fbthrift_python_types.UnionMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "reserved_field",  # name
            "reserved_field",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i32,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            4, # IDL type (see BaseTypeEnum)
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.UnionToBeRenamed"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic/UnionToBeRenamed"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_UnionToBeRenamed()

    def _to_python(self):
        return self

    def _to_mutable_python(self):
        import thrift.python.mutable_converter
        import importlib
        mutable_types = importlib.import_module("test.fixtures.basic.module.thrift_mutable_types")
        return thrift.python.mutable_converter.to_mutable_python_struct_or_union(mutable_types.UnionToBeRenamed, self)

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.UnionToBeRenamed, self)

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        try:
            py_deprecated_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_deprecated_types.UnionToBeRenamed, self)
        except ModuleNotFoundError:
            py_asyncio_types = importlib.import_module("module.ttypes")
            return thrift.util.converter.to_py_struct(py_asyncio_types.UnionToBeRenamed, self)

# This unfortunately has to be down here to prevent circular imports
import test.fixtures.basic.module.thrift_metadata
from test.fixtures.basic.module.thrift_enums import *

_fbthrift_all_enums = [
    MyEnum,
    HackEnum,
]


def _fbthrift_metadata__struct_MyStruct():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_struct_MyStruct()


def _fbthrift_metadata__struct_Containers():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_struct_Containers()


def _fbthrift_metadata__struct_MyDataItem():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_struct_MyDataItem()


def _fbthrift_metadata__struct_MyUnion():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_struct_MyUnion()


def _fbthrift_metadata__exception_MyException():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_exception_MyException()


def _fbthrift_metadata__exception_MyExceptionWithMessage():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_exception_MyExceptionWithMessage()


def _fbthrift_metadata__struct_ReservedKeyword():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_struct_ReservedKeyword()


def _fbthrift_metadata__struct_UnionToBeRenamed():
    return test.fixtures.basic.module.thrift_metadata.gen_metadata_struct_UnionToBeRenamed()


_fbthrift_all_structs = [
    MyStruct,
    Containers,
    MyDataItem,
    MyUnion,
    MyException,
    MyExceptionWithMessage,
    ReservedKeyword,
    UnionToBeRenamed,
]
_fbthrift_python_types.fill_specs(*_fbthrift_all_structs)


FLAG = True

OFFSET = -10

COUNT = 200

MASK = 16388846

E = float(2.718281828459)

DATE = "June 28, 2017"

AList = _fbthrift_python_types.List(_fbthrift_python_types.typeinfo_i32, (2, 3, 5, 7, ))

ASet = _fbthrift_python_types.Set(_fbthrift_python_types.typeinfo_string, ("foo", "bar", "baz", ))

AMap = _fbthrift_python_types.Map(_fbthrift_python_types.typeinfo_string, _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_i32), { "foo": _fbthrift_python_types.List(_fbthrift_python_types.typeinfo_i32, (1, 2, 3, 4, )), "bar": _fbthrift_python_types.List(_fbthrift_python_types.typeinfo_i32, (10, 32, 54, ))})

MyEnumAlias = MyEnum
MyDataItemAlias = MyDataItem



class _fbthrift_FooService_simple_rpc_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_FooService_simple_rpc_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )




class _fbthrift_FB303Service_simple_rpc_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "int_parameter",  # name
            "int_parameter",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i32,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            4, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_FB303Service_simple_rpc_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            lambda: _fbthrift_python_types.StructTypeInfo(ReservedKeyword),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )




class _fbthrift_MyService_ping_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_ping_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_getRandomData_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_getRandomData_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )


class _fbthrift_MyService_sink_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "sink",  # name
            "sink",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_MyService_sink_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_putDataById_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "id",  # name
            "id",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "data",  # name
            "data",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_MyService_putDataById_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_hasDataById_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "id",  # name
            "id",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_MyService_hasDataById_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            _fbthrift_python_types.typeinfo_bool,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )


class _fbthrift_MyService_getDataById_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "id",  # name
            "id",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_MyService_getDataById_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )


class _fbthrift_MyService_deleteDataById_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "id",  # name
            "id",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_MyService_deleteDataById_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_lobDataById_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "id",  # name
            "id",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
            True, # field type is primitive
            5, # IDL type (see BaseTypeEnum)
        ),
        _fbthrift_python_types.FieldInfo(
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "data",  # name
            "data",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_MyService_invalid_return_for_hack_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_invalid_return_for_hack_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_float),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )


class _fbthrift_MyService_rpc_skipped_codegen_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )


class _fbthrift_MyService_rpc_skipped_codegen_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )




class _fbthrift_DbMixedStackArguments_getDataByKey0_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "key",  # name
            "key",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_DbMixedStackArguments_getDataByKey0_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            _fbthrift_python_types.typeinfo_binary,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )


class _fbthrift_DbMixedStackArguments_getDataByKey1_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "key",  # name
            "key",  # python name (from @python.Name annotation)
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            8, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_DbMixedStackArguments_getDataByKey1_result(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            0,  # id
            _fbthrift_python_types.FieldQualifier.Optional, # qualifier
            "success",  # name
            "success", # name
            _fbthrift_python_types.typeinfo_binary,  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
        ),
    )



_fbthrift_python_types.fill_specs(
    _fbthrift_FooService_simple_rpc_args,
    _fbthrift_FooService_simple_rpc_result,
    _fbthrift_FB303Service_simple_rpc_args,
    _fbthrift_FB303Service_simple_rpc_result,
    _fbthrift_MyService_ping_args,
    _fbthrift_MyService_ping_result,
    _fbthrift_MyService_getRandomData_args,
    _fbthrift_MyService_getRandomData_result,
    _fbthrift_MyService_sink_args,
    _fbthrift_MyService_sink_result,
    _fbthrift_MyService_putDataById_args,
    _fbthrift_MyService_putDataById_result,
    _fbthrift_MyService_hasDataById_args,
    _fbthrift_MyService_hasDataById_result,
    _fbthrift_MyService_getDataById_args,
    _fbthrift_MyService_getDataById_result,
    _fbthrift_MyService_deleteDataById_args,
    _fbthrift_MyService_deleteDataById_result,
    _fbthrift_MyService_lobDataById_args,
    _fbthrift_MyService_invalid_return_for_hack_args,
    _fbthrift_MyService_invalid_return_for_hack_result,
    _fbthrift_MyService_rpc_skipped_codegen_args,
    _fbthrift_MyService_rpc_skipped_codegen_result,
    _fbthrift_DbMixedStackArguments_getDataByKey0_args,
    _fbthrift_DbMixedStackArguments_getDataByKey0_result,
    _fbthrift_DbMixedStackArguments_getDataByKey1_args,
    _fbthrift_DbMixedStackArguments_getDataByKey1_result,
)
