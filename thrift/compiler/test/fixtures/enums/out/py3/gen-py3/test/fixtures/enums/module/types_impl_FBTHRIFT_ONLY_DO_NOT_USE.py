#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/enums/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#


import thrift.py3.types
import test.fixtures.enums.module.thrift_metadata

_fbthrift__module_name__ = "test.fixtures.enums.module.types"



class Metasyntactic(thrift.py3.types.CompiledEnum):
    FOO = 1
    BAR = 2
    BAZ = 3
    BAX = 4

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_Metasyntactic()

    @staticmethod
    def __get_thrift_name__():
        return "module.Metasyntactic"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.Metasyntactic(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyEnum1(thrift.py3.types.CompiledEnum):
    ME1_0 = 0
    ME1_1 = 1
    ME1_2 = 2
    ME1_3 = 3
    ME1_5 = 5
    ME1_6 = 6

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_MyEnum1()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnum1"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.MyEnum1(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyEnum2(thrift.py3.types.CompiledEnum):
    ME2_0 = 0
    ME2_1 = 1
    ME2_2 = 2

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_MyEnum2()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnum2"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.MyEnum2(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyEnum3(thrift.py3.types.CompiledEnum):
    ME3_0 = 0
    ME3_1 = 1
    ME3_N2 = -2
    ME3_N1 = -1
    ME3_9 = 9
    ME3_10 = 10

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_MyEnum3()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnum3"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.MyEnum3(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyEnum4(thrift.py3.types.CompiledEnum):
    ME4_A = 2147483645
    ME4_B = 2147483646
    ME4_C = 2147483647
    ME4_D = -2147483648

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_MyEnum4()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyEnum4"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.MyEnum4(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyBitmaskEnum1(thrift.py3.types.CompiledEnum):
    ONE = 1
    TWO = 2
    FOUR = 4

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_MyBitmaskEnum1()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyBitmaskEnum1"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.MyBitmaskEnum1(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




class MyBitmaskEnum2(thrift.py3.types.CompiledEnum):
    ONE = 1
    TWO = 2
    FOUR = 4

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return test.fixtures.enums.module.thrift_metadata.gen_metadata_enum_MyBitmaskEnum2()

    @staticmethod
    def __get_thrift_name__():
        return "module.MyBitmaskEnum2"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return python_types.MyBitmaskEnum2(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




