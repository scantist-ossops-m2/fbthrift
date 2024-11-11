#
# Autogenerated by Thrift for included.thrift
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
from thrift.python.types import EnumMeta as __EnumMeta
from thrift.python.std_libcpp cimport sv_to_str as __sv_to_str, string_view as __cstring_view
from thrift.python.types cimport(
    BadEnum as __BadEnum,
)
from thrift.py3.types cimport (
    richcmp as __richcmp,
    init_unicode_from_cpp as __init_unicode_from_cpp,
    set_iter as __set_iter,
    map_iter as __map_iter,
    map_contains as __map_contains,
    map_getitem as __map_getitem,
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


from apache.thrift.fixtures.types.included.containers_FBTHRIFT_ONLY_DO_NOT_USE import (
    List__std_unordered_map__Map__i32_string,
)


cdef object get_types_reflection():
    import importlib
    return importlib.import_module(
        "apache.thrift.fixtures.types.included.types_reflection"
    )

@__cython.auto_pickle(False)
@__cython.final
cdef class std_unordered_map__Map__i32_string(thrift.py3.types.Map):
    def __init__(self, items=None):
        if isinstance(items, std_unordered_map__Map__i32_string):
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = (<std_unordered_map__Map__i32_string> items)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE
        else:
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = std_unordered_map__Map__i32_string__make_instance(items)

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] c_items):
        __fbthrift_inst = <std_unordered_map__Map__i32_string>std_unordered_map__Map__i32_string.__new__(std_unordered_map__Map__i32_string)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(c_items)
        return __fbthrift_inst

    def __copy__(std_unordered_map__Map__i32_string self):
        cdef shared_ptr[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] cpp_obj = make_shared[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return std_unordered_map__Map__i32_string._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __len__(self):
        return deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()

    cdef _check_key_type(self, key):
        if not self or key is None:
            return
        if isinstance(key, int):
            return key

    def __getitem__(self, key):
        err = KeyError(f'{key}')
        key = self._check_key_type(key)
        if key is None:
            raise err
        cdef cint32_t ckey = key
        if not __map_contains(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey):
            raise err
        cdef string citem
        __map_getitem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
        return bytes(citem).decode('UTF-8')

    def __iter__(self):
        if not self:
            return
        cdef __map_iter[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] itr = __map_iter[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t citem = 0
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextKey(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield citem

    def __contains__(self, key):
        key = self._check_key_type(key)
        if key is None:
            return False
        cdef cint32_t ckey = key
        return __map_contains(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey)

    def values(self):
        if not self:
            return
        cdef __map_iter[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] itr = __map_iter[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef string citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextValue(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield bytes(citem).decode('UTF-8')

    def items(self):
        if not self:
            return
        cdef __map_iter[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] itr = __map_iter[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t ckey = 0
        cdef string citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextItem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
            yield (ckey, bytes(citem).decode('UTF-8'))

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__std_unordered_map__Map__i32_string()

Mapping.register(std_unordered_map__Map__i32_string)

cdef shared_ptr[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] std_unordered_map__Map__i32_string__make_instance(object items) except *:
    cdef shared_ptr[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] c_inst = make_shared[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]]()
    if items is not None:
        for key, item in items.items():
            if not isinstance(key, int):
                raise TypeError(f"{key!r} is not of type int")
            key = <cint32_t> key
            if not isinstance(item, str):
                raise TypeError(f"{item!r} is not of type str")

            deref(c_inst)[key] = item.encode('UTF-8')
    return cmove(c_inst)



cdef vector[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] List__std_unordered_map__Map__i32_string__make_instance(object items) except *:
    cdef vector[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]] c_inst
    if items is not None:
        for item in items:
            if item is None:
                raise TypeError("None is not of the type _typing.Mapping[int, str]")
            if not isinstance(item, std_unordered_map__Map__i32_string):
                item = std_unordered_map__Map__i32_string(item)
            c_inst.push_back(deref((<std_unordered_map__Map__i32_string>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
    return cmove(c_inst)

cdef object List__std_unordered_map__Map__i32_string__from_cpp(const vector[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(std_unordered_map__Map__i32_string._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[_apache_thrift_fixtures_types_included_cbindings.std_unordered_map[cint32_t,string]](c_vec[idx])))
    return List__std_unordered_map__Map__i32_string(py_list, thrift.py3.types._fbthrift_list_private_ctor)


SomeMap = std_unordered_map__Map__i32_string
SomeListOfTypeMap = List__std_unordered_map__Map__i32_string
