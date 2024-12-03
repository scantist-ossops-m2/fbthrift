#
# Autogenerated by Thrift for b.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
cimport cython as __cython
from cpython.object cimport PyTypeObject
from libcpp.memory cimport shared_ptr, make_shared, unique_ptr
from libcpp.optional cimport optional as __optional
from libcpp.string cimport string
from libcpp cimport bool as cbool
from libcpp.iterator cimport inserter as cinserter
from libcpp.utility cimport move as cmove
from cpython cimport bool as pbool
from cython.operator cimport dereference as deref, preincrement as inc, address as ptr_address
import thrift.py3.types
from thrift.py3.types import _IsSet as _fbthrift_IsSet
from thrift.py3.types cimport make_unique
cimport thrift.py3.types
cimport thrift.py3.exceptions
cimport thrift.python.exceptions
import thrift.python.converter
from thrift.python.types import EnumMeta as __EnumMeta
from thrift.python.std_libcpp cimport sv_to_str as __sv_to_str, string_view as __cstring_view
from thrift.python.types cimport BadEnum as __BadEnum
from thrift.py3.types cimport (
    richcmp as __richcmp,
    init_unicode_from_cpp as __init_unicode_from_cpp,
    set_iter as __set_iter,
    map_iter as __map_iter,
    reference_shared_ptr as __reference_shared_ptr,
    get_field_name_by_index as __get_field_name_by_index,
    reset_field as __reset_field,
    translate_cpp_enum_to_python,
    const_pointer_cast,
    make_const_shared,
    constant_shared_ptr,
)
cimport thrift.py3.serializer as serializer
from thrift.python.protocol cimport Protocol as __Protocol
import folly.iobuf as _fbthrift_iobuf
from folly.optional cimport cOptional
from folly.memory cimport to_shared_ptr as __to_shared_ptr
from folly.range cimport Range as __cRange

import sys
from collections.abc import Sequence, Set, Mapping, Iterable
import weakref as __weakref
import builtins as _builtins
import importlib
cimport c.types as _c_types
import c.types as _c_types

import b.thrift_types as _fbthrift_python_types

from b.containers_FBTHRIFT_ONLY_DO_NOT_USE import (
    List__c_C,
)


cdef object get_types_reflection():
    return importlib.import_module(
        "b.types_reflection"
    )

cdef vector[_c_cbindings.cC] List__c_C__make_instance(object items) except *:
    cdef vector[_c_cbindings.cC] c_inst
    if items is None:
        return cmove(c_inst)
    for item in items:
        if not isinstance(item, _c_types.C):
            raise TypeError(f"{item!r} is not of type _c_types.C")
        c_inst.push_back(deref((<_c_types.C>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
    return cmove(c_inst)

cdef object List__c_C__from_cpp(const vector[_c_cbindings.cC]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(_c_types.C._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[_c_cbindings.cC](c_vec[idx])))
    return List__c_C(py_list, thrift.py3.types._fbthrift_list_private_ctor)


B = List__c_C
E = _c_types.E
