#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/refs/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#


import thrift.py3.types
import module.thrift_metadata

_fbthrift__module_name__ = "module.types"



class MyEnum(thrift.py3.types.CompiledEnum):
    Zero = 0
    One = 1

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return module.thrift_metadata.gen_metadata_enum_MyEnum()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnum"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return python_types.MyEnum(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class TypedEnum(thrift.py3.types.CompiledEnum):
    VAL1 = 0
    VAL2 = 1

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return module.thrift_metadata.gen_metadata_enum_TypedEnum()

    @staticmethod
    def __get_thrift_name__():
        return "module.TypedEnum"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return python_types.TypedEnum(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value





class __MyUnionType(thrift.py3.types.CompiledEnum):
    anInteger = 1
    aString = 2
    EMPTY = 0

    __module__ = _fbthrift__module_name__
    __slots__ = ()


class __NonTriviallyDestructibleUnionType(thrift.py3.types.CompiledEnum):
    int_field = 1
    EMPTY = 0

    __module__ = _fbthrift__module_name__
    __slots__ = ()

