#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/mcpp2-compare/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#


import thrift.py3.types
import module.thrift_metadata

_fbthrift__module_name__ = "module.types"



class MyEnumA(thrift.py3.types.CompiledEnum):
    fieldA = 1
    fieldB = 2
    fieldC = 4

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return module.thrift_metadata.gen_metadata_enum_MyEnumA()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnumA"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return python_types.MyEnumA(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class AnnotatedEnum(thrift.py3.types.CompiledEnum):
    FIELDA = 2
    FIELDB = 4
    FIELDC = 9

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return module.thrift_metadata.gen_metadata_enum_AnnotatedEnum()

    @staticmethod
    def __get_thrift_name__():
        return "module.AnnotatedEnum"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return python_types.AnnotatedEnum(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class AnnotatedEnum2(thrift.py3.types.CompiledEnum):
    FIELDA = 2
    FIELDB = 4
    FIELDC = 9

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return module.thrift_metadata.gen_metadata_enum_AnnotatedEnum2()

    @staticmethod
    def __get_thrift_name__():
        return "module.AnnotatedEnum2"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return python_types.AnnotatedEnum2(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyEnumB(thrift.py3.types.CompiledEnum):
    AField = 0

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return module.thrift_metadata.gen_metadata_enum_MyEnumB()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnumB"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return python_types.MyEnumB(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value





class __SimpleUnionType(thrift.py3.types.CompiledEnum):
    intValue = 7
    stringValue = 2
    EMPTY = 0

    __module__ = _fbthrift__module_name__
    __slots__ = ()


class __ComplexUnionType(thrift.py3.types.CompiledEnum):
    intValue = 1
    opt_intValue = 201
    stringValue = 3
    opt_stringValue = 203
    intValue2 = 4
    intValue3 = 6
    doubelValue = 7
    boolValue = 8
    union_list = 9
    union_set = 10
    union_map = 11
    opt_union_map = 211
    enum_field = 12
    enum_container = 13
    a_struct = 14
    a_set_struct = 15
    a_union = 16
    opt_a_union = 216
    a_union_list = 17
    a_union_typedef = 18
    a_union_typedef_list = 19
    MyBinaryField = 20
    MyBinaryField2 = 21
    MyBinaryListField4 = 23
    ref_field = 24
    ref_field2 = 25
    excp_field = 26
    MyCustomField = 27
    EMPTY = 0

    __module__ = _fbthrift__module_name__
    __slots__ = ()


class __FloatUnionType(thrift.py3.types.CompiledEnum):
    floatSide = 1
    doubleSide = 2
    EMPTY = 0

    __module__ = _fbthrift__module_name__
    __slots__ = ()

