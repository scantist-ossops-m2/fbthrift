#
# Autogenerated by Thrift for includes.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#


import thrift.py3.types
import includes.thrift_metadata

_fbthrift__module_name__ = "includes.types"



class AnEnum(thrift.py3.types.CompiledEnum):
    FIELDA = 2
    FIELDB = 4

    __module__ = _fbthrift__module_name__
    __slots__ = ()

    @staticmethod
    def __get_metadata__():
        return includes.thrift_metadata.gen_metadata_enum_AnEnum()

    @staticmethod
    def __get_thrift_name__():
        return "includes.AnEnum"

    def _to_python(self):
        import importlib
        python_types = importlib.import_module(
            "includes.thrift_types"
        )
        return python_types.AnEnum(self.value)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        return self.value




