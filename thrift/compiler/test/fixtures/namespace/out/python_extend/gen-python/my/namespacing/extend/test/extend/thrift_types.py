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


import python_module_root.my.namespacing.test.hsmodule.thrift_types
import python_module_root.my.namespacing.test.hsmodule.thrift_types as python_module_root__my__namespacing__test__hsmodule__thrift_types

# This unfortunately has to be down here to prevent circular imports
import python_module_root.my.namespacing.extend.test.extend.thrift_metadata
from python_module_root.my.namespacing.extend.test.extend.thrift_enums import *

_fbthrift_all_enums = [
]


_fbthrift_all_structs = [
]



class _fbthrift_ExtendTestService_check_args(metaclass=_fbthrift_python_types.StructMeta):
    _fbthrift_SPEC = (
        _fbthrift_python_types.FieldInfo(
            1,  # id
            _fbthrift_python_types.FieldQualifier.Unqualified, # qualifier
            "struct1",  # name
            "struct1",  # python name (from @python.Name annotation)
            lambda: _fbthrift_python_types.StructTypeInfo(python_module_root__my__namespacing__test__hsmodule__thrift_types.HsFoo),  # typeinfo
            None,  # default value
            None,  # adapter info
            False, # field type is primitive
            11, # IDL type (see BaseTypeEnum)
        ),
    )


class _fbthrift_ExtendTestService_check_result(metaclass=_fbthrift_python_types.StructMeta):
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



_fbthrift_python_types.fill_specs(
    _fbthrift_ExtendTestService_check_args,
    _fbthrift_ExtendTestService_check_result,
)
