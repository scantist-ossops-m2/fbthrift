#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
import typing as _typing

import folly.iobuf as _fbthrift_iobuf
import thrift.py3.builder


import module.types as _module_types


_fbthrift_struct_type__MyStruct = _module_types.MyStruct
class MyStruct_Builder(thrift.py3.builder.StructBuilder):
    _struct_type = _fbthrift_struct_type__MyStruct

    def __init__(self):
        self.MyIntField: _typing.Optional[int] = None
        self.MyStringField: _typing.Optional[str] = None

    def __iter__(self):
        yield "MyIntField", self.MyIntField
        yield "MyStringField", self.MyStringField
