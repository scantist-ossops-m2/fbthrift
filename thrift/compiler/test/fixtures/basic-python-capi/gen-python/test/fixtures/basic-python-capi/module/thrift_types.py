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
        (
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyIntField",  # name
            _fbthrift_python_types.typeinfo_i64,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyStringField",  # name
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "MyDataField",  # name
            lambda: _fbthrift_python_types.StructTypeInfo(MyDataItem),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myEnum",  # name
            lambda: _fbthrift_python_types.EnumTypeInfo(MyEnum),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            5,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "oneway",  # name
            _fbthrift_python_types.typeinfo_bool,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            6,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "floatList",  # name
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_float),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            7,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "strMap",  # name
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_binary, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            8,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "floatSet",  # name
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_i32),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyStruct"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/MyStruct"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_MyStruct()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyStruct, self)

    def _to_py_deprecated(self):
        import importlib
        py_deprecated_types = importlib.import_module("module.ttypes")
        import thrift.util.converter
        return thrift.util.converter.to_py_struct(py_deprecated_types.MyStruct, self)


class MyDataItem(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyDataItem"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/MyDataItem"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_MyDataItem()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyDataItem, self)

    def _to_py_deprecated(self):
        import importlib
        py_deprecated_types = importlib.import_module("module.ttypes")
        import thrift.util.converter
        return thrift.util.converter.to_py_struct(py_deprecated_types.MyDataItem, self)


class TransitiveDoubler(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.TransitiveDoubler"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/TransitiveDoubler"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_TransitiveDoubler()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.TransitiveDoubler, self)

    def _to_py_deprecated(self):
        import importlib
        py_deprecated_types = importlib.import_module("module.ttypes")
        import thrift.util.converter
        return thrift.util.converter.to_py_struct(py_deprecated_types.TransitiveDoubler, self)


class DoubledPair(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        (
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "s",  # name
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "x",  # name
            _fbthrift_python_types.typeinfo_i32,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.DoubledPair"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/DoubledPair"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_DoubledPair()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.DoubledPair, self)

    def _to_py_deprecated(self):
        import importlib
        py_deprecated_types = importlib.import_module("module.ttypes")
        import thrift.util.converter
        return thrift.util.converter.to_py_struct(py_deprecated_types.DoubledPair, self)


class StringPair(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        (
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "normal",  # name
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "doubled",  # name
            _fbthrift_python_types.typeinfo_string,  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.StringPair"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/StringPair"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_StringPair()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.StringPair, self)

    def _to_py_deprecated(self):
        import importlib
        py_deprecated_types = importlib.import_module("module.ttypes")
        import thrift.util.converter
        return thrift.util.converter.to_py_struct(py_deprecated_types.StringPair, self)


class MyUnion(metaclass=_fbthrift_python_types.UnionMeta):
    _fbthrift_SPEC = (
        (
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myEnum",  # name
            lambda: _fbthrift_python_types.EnumTypeInfo(MyEnum),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            2,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myStruct",  # name
            lambda: _fbthrift_python_types.StructTypeInfo(MyStruct),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            3,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "myDataItem",  # name
            lambda: _fbthrift_python_types.StructTypeInfo(MyDataItem),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            4,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "doubleSet",  # name
            lambda: _fbthrift_python_types.SetTypeInfo(_fbthrift_python_types.typeinfo_i64),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            5,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "doubleList",  # name
            lambda: _fbthrift_python_types.ListTypeInfo(_fbthrift_python_types.typeinfo_double),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
        (
            6,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "strMap",  # name
            lambda: _fbthrift_python_types.MapTypeInfo(_fbthrift_python_types.typeinfo_binary, _fbthrift_python_types.typeinfo_string),  # typeinfo
            None,  # default value
            None,  # adapter info
        ),
    )

    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyUnion"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/MyUnion"

    @staticmethod
    def __get_metadata__():
        return _fbthrift_metadata__struct_MyUnion()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        import thrift.py3.converter
        return thrift.py3.converter.to_py3_struct(py3_types.MyUnion, self)

    def _to_py_deprecated(self):
        import importlib
        py_deprecated_types = importlib.import_module("module.ttypes")
        import thrift.util.converter
        return thrift.util.converter.to_py_struct(py_deprecated_types.MyUnion, self)

# This unfortunately has to be down here to prevent circular imports
import test.fixtures.basic-python-capi.module.thrift_metadata

class MyEnum(_fbthrift_python_types.Enum, int):
    MyValue1 = 0
    MyValue2 = 1
    @staticmethod
    def __get_thrift_name__() -> str:
        return "module.MyEnum"

    @staticmethod
    def __get_thrift_uri__():
        return "test.dev/fixtures/basic-python-capi/MyEnum"

    @staticmethod
    def __get_metadata__():
        return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_enum_MyEnum()

    def _to_python(self):
        return self

    def _to_py3(self):
        import importlib
        py3_types = importlib.import_module("test.fixtures.basic-python-capi.module.types")
        return py3_types.MyEnum(self.value)

    def _to_py_deprecated(self):
        return self.value

_fbthrift_all_enums = [
    MyEnum,
]

def _fbthrift_metadata__struct_MyStruct():
    return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_struct_MyStruct()
def _fbthrift_metadata__struct_MyDataItem():
    return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_struct_MyDataItem()
def _fbthrift_metadata__struct_TransitiveDoubler():
    return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_struct_TransitiveDoubler()
def _fbthrift_metadata__struct_DoubledPair():
    return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_struct_DoubledPair()
def _fbthrift_metadata__struct_StringPair():
    return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_struct_StringPair()
def _fbthrift_metadata__struct_MyUnion():
    return test.fixtures.basic-python-capi.module.thrift_metadata.gen_metadata_struct_MyUnion()

_fbthrift_all_structs = [
    MyStruct,
    MyDataItem,
    TransitiveDoubler,
    DoubledPair,
    StringPair,
    MyUnion,
]
_fbthrift_python_types.fill_specs(*_fbthrift_all_structs)
