#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/params/src/module.thrift
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
    cSetOp as __cSetOp,
    richcmp as __richcmp,
    set_op as __set_op,
    setcmp as __setcmp,
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


from module.containers_FBTHRIFT_ONLY_DO_NOT_USE import (
    List__i32,
    List__Map__i32_i32,
    List__Set__i32,
    List__Map__i32_Map__i32_Set__i32,
    List__List__Map__i32_Map__i32_Set__i32,
)


cdef object get_types_reflection():
    import importlib
    return importlib.import_module(
        "module.types_reflection"
    )


cdef vector[cint32_t] List__i32__make_instance(object items) except *:
    cdef vector[cint32_t] c_inst
    if items is not None:
        for item in items:
            if not isinstance(item, int):
                raise TypeError(f"{item!r} is not of type int")
            item = <cint32_t> item
            c_inst.push_back(item)
    return cmove(c_inst)

cdef object List__i32__from_cpp(const vector[cint32_t]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(c_vec[idx])
    return List__i32(py_list, thrift.py3.types._fbthrift_list_private_ctor)

@__cython.auto_pickle(False)
@__cython.final
cdef class Map__i32_List__i32(thrift.py3.types.Map):
    def __init__(self, items=None):
        if isinstance(items, Map__i32_List__i32):
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = (<Map__i32_List__i32> items)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE
        else:
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = Map__i32_List__i32__make_instance(items)

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[cmap[cint32_t,vector[cint32_t]]] c_items):
        __fbthrift_inst = <Map__i32_List__i32>Map__i32_List__i32.__new__(Map__i32_List__i32)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(c_items)
        return __fbthrift_inst

    def __copy__(Map__i32_List__i32 self):
        cdef shared_ptr[cmap[cint32_t,vector[cint32_t]]] cpp_obj = make_shared[cmap[cint32_t,vector[cint32_t]]](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Map__i32_List__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

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
        cdef vector[cint32_t] citem
        __map_getitem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
        return List__i32__from_cpp(citem)

    def __iter__(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,vector[cint32_t]]] itr = __map_iter[cmap[cint32_t,vector[cint32_t]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
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
        cdef __map_iter[cmap[cint32_t,vector[cint32_t]]] itr = __map_iter[cmap[cint32_t,vector[cint32_t]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef vector[cint32_t] citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextValue(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield List__i32__from_cpp(citem)

    def items(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,vector[cint32_t]]] itr = __map_iter[cmap[cint32_t,vector[cint32_t]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t ckey = 0
        cdef vector[cint32_t] citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextItem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
            yield (ckey, List__i32__from_cpp(citem))

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Map__i32_List__i32()

Mapping.register(Map__i32_List__i32)

cdef shared_ptr[cmap[cint32_t,vector[cint32_t]]] Map__i32_List__i32__make_instance(object items) except *:
    cdef shared_ptr[cmap[cint32_t,vector[cint32_t]]] c_inst = make_shared[cmap[cint32_t,vector[cint32_t]]]()
    if items is not None:
        for key, item in items.items():
            if not isinstance(key, int):
                raise TypeError(f"{key!r} is not of type int")
            key = <cint32_t> key
            if item is None:
                raise TypeError("None is not of type _typing.Sequence[int]")
            if not isinstance(item, List__i32):
                item = List__i32(item)

            deref(c_inst)[key] = List__i32__make_instance(item)
    return cmove(c_inst)


@__cython.auto_pickle(False)
@__cython.final
cdef class Set__i32(thrift.py3.types.Set):
    def __init__(self, items=None):
        if isinstance(items, Set__i32):
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = (<Set__i32> items)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE
        else:
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = Set__i32__make_instance(items)

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[cset[cint32_t]] c_items):
        __fbthrift_inst = <Set__i32>Set__i32.__new__(Set__i32)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(c_items)
        return __fbthrift_inst

    def __copy__(Set__i32 self):
        cdef shared_ptr[cset[cint32_t]] cpp_obj = make_shared[cset[cint32_t]](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __len__(self):
        return deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()

    def __contains__(self, item):
        if not self or item is None:
            return False
        if not isinstance(item, int):
            return False
        return pbool(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).count(item))


    def __iter__(self):
        if not self:
            return
        cdef __set_iter[cset[cint32_t]] itr = __set_iter[cset[cint32_t]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t citem = 0
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNext(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield citem

    def __hash__(self):
        return super().__hash__()

    def __richcmp__(self, other, int op):
        if isinstance(other, Set__i32):
            # C level comparisons
            return __setcmp(
                self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
                (<Set__i32> other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
                op,
            )
        return self._fbthrift_py_richcmp(other, op)

    cdef _fbthrift_do_set_op(self, other, __cSetOp op):
        if not isinstance(other, Set__i32):
            other = Set__i32(other)
        cdef shared_ptr[cset[cint32_t]] result
        return Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(__set_op[cset[cint32_t]](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<Set__i32>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ))

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Set__i32()


Set.register(Set__i32)

cdef shared_ptr[cset[cint32_t]] Set__i32__make_instance(object items) except *:
    cdef shared_ptr[cset[cint32_t]] c_inst = make_shared[cset[cint32_t]]()
    if items is not None:
        for item in items:
            if not isinstance(item, int):
                raise TypeError(f"{item!r} is not of type int")
            item = <cint32_t> item
            deref(c_inst).insert(item)
    return cmove(c_inst)

cdef object Set__i32__from_cpp(const cset[cint32_t]& c_set) except *:
    cdef list py_items = []
    cdef __set_iter[cset[cint32_t]] iter = __set_iter[cset[cint32_t]](c_set)
    cdef cint32_t citem = 0
    for i in range(c_set.size()):
        iter.genNextItem(citem)
        py_items.append(citem)
    return Set__i32(frozenset(py_items), thrift.py3.types._fbthrift_set_private_ctor)

@__cython.auto_pickle(False)
@__cython.final
cdef class Map__i32_Set__i32(thrift.py3.types.Map):
    def __init__(self, items=None):
        if isinstance(items, Map__i32_Set__i32):
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = (<Map__i32_Set__i32> items)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE
        else:
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = Map__i32_Set__i32__make_instance(items)

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[cmap[cint32_t,cset[cint32_t]]] c_items):
        __fbthrift_inst = <Map__i32_Set__i32>Map__i32_Set__i32.__new__(Map__i32_Set__i32)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(c_items)
        return __fbthrift_inst

    def __copy__(Map__i32_Set__i32 self):
        cdef shared_ptr[cmap[cint32_t,cset[cint32_t]]] cpp_obj = make_shared[cmap[cint32_t,cset[cint32_t]]](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Map__i32_Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

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
        cdef shared_ptr[cset[cint32_t]] citem
        __map_getitem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
        return Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(citem)

    def __iter__(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,cset[cint32_t]]] itr = __map_iter[cmap[cint32_t,cset[cint32_t]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
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
        cdef __map_iter[cmap[cint32_t,cset[cint32_t]]] itr = __map_iter[cmap[cint32_t,cset[cint32_t]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef shared_ptr[cset[cint32_t]] citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextValue(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(citem)

    def items(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,cset[cint32_t]]] itr = __map_iter[cmap[cint32_t,cset[cint32_t]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t ckey = 0
        cdef shared_ptr[cset[cint32_t]] citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextItem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
            yield (ckey, Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(citem))

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Map__i32_Set__i32()

Mapping.register(Map__i32_Set__i32)

cdef shared_ptr[cmap[cint32_t,cset[cint32_t]]] Map__i32_Set__i32__make_instance(object items) except *:
    cdef shared_ptr[cmap[cint32_t,cset[cint32_t]]] c_inst = make_shared[cmap[cint32_t,cset[cint32_t]]]()
    if items is not None:
        for key, item in items.items():
            if not isinstance(key, int):
                raise TypeError(f"{key!r} is not of type int")
            key = <cint32_t> key
            if item is None:
                raise TypeError("None is not of type _typing.AbstractSet[int]")
            if not isinstance(item, Set__i32):
                item = Set__i32(item)

            deref(c_inst)[key] = deref((<Set__i32>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
    return cmove(c_inst)


@__cython.auto_pickle(False)
@__cython.final
cdef class Map__i32_i32(thrift.py3.types.Map):
    def __init__(self, items=None):
        if isinstance(items, Map__i32_i32):
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = (<Map__i32_i32> items)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE
        else:
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = Map__i32_i32__make_instance(items)

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[cmap[cint32_t,cint32_t]] c_items):
        __fbthrift_inst = <Map__i32_i32>Map__i32_i32.__new__(Map__i32_i32)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(c_items)
        return __fbthrift_inst

    def __copy__(Map__i32_i32 self):
        cdef shared_ptr[cmap[cint32_t,cint32_t]] cpp_obj = make_shared[cmap[cint32_t,cint32_t]](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Map__i32_i32._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

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
        cdef cint32_t citem = 0
        __map_getitem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
        return citem

    def __iter__(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,cint32_t]] itr = __map_iter[cmap[cint32_t,cint32_t]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
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
        cdef __map_iter[cmap[cint32_t,cint32_t]] itr = __map_iter[cmap[cint32_t,cint32_t]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t citem = 0
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextValue(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield citem

    def items(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,cint32_t]] itr = __map_iter[cmap[cint32_t,cint32_t]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t ckey = 0
        cdef cint32_t citem = 0
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextItem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
            yield (ckey, citem)

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Map__i32_i32()

Mapping.register(Map__i32_i32)

cdef shared_ptr[cmap[cint32_t,cint32_t]] Map__i32_i32__make_instance(object items) except *:
    cdef shared_ptr[cmap[cint32_t,cint32_t]] c_inst = make_shared[cmap[cint32_t,cint32_t]]()
    if items is not None:
        for key, item in items.items():
            if not isinstance(key, int):
                raise TypeError(f"{key!r} is not of type int")
            key = <cint32_t> key
            if not isinstance(item, int):
                raise TypeError(f"{item!r} is not of type int")
            item = <cint32_t> item

            deref(c_inst)[key] = item
    return cmove(c_inst)



cdef vector[cmap[cint32_t,cint32_t]] List__Map__i32_i32__make_instance(object items) except *:
    cdef vector[cmap[cint32_t,cint32_t]] c_inst
    if items is not None:
        for item in items:
            if item is None:
                raise TypeError("None is not of the type _typing.Mapping[int, int]")
            if not isinstance(item, Map__i32_i32):
                item = Map__i32_i32(item)
            c_inst.push_back(deref((<Map__i32_i32>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
    return cmove(c_inst)

cdef object List__Map__i32_i32__from_cpp(const vector[cmap[cint32_t,cint32_t]]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(Map__i32_i32._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[cmap[cint32_t,cint32_t]](c_vec[idx])))
    return List__Map__i32_i32(py_list, thrift.py3.types._fbthrift_list_private_ctor)


cdef vector[cset[cint32_t]] List__Set__i32__make_instance(object items) except *:
    cdef vector[cset[cint32_t]] c_inst
    if items is not None:
        for item in items:
            if item is None:
                raise TypeError("None is not of the type _typing.AbstractSet[int]")
            if not isinstance(item, Set__i32):
                item = Set__i32(item)
            c_inst.push_back(deref((<Set__i32>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
    return cmove(c_inst)

cdef object List__Set__i32__from_cpp(const vector[cset[cint32_t]]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[cset[cint32_t]](c_vec[idx])))
    return List__Set__i32(py_list, thrift.py3.types._fbthrift_list_private_ctor)

@__cython.auto_pickle(False)
@__cython.final
cdef class Map__i32_Map__i32_Set__i32(thrift.py3.types.Map):
    def __init__(self, items=None):
        if isinstance(items, Map__i32_Map__i32_Set__i32):
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = (<Map__i32_Map__i32_Set__i32> items)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE
        else:
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = Map__i32_Map__i32_Set__i32__make_instance(items)

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] c_items):
        __fbthrift_inst = <Map__i32_Map__i32_Set__i32>Map__i32_Map__i32_Set__i32.__new__(Map__i32_Map__i32_Set__i32)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(c_items)
        return __fbthrift_inst

    def __copy__(Map__i32_Map__i32_Set__i32 self):
        cdef shared_ptr[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] cpp_obj = make_shared[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Map__i32_Map__i32_Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

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
        cdef shared_ptr[cmap[cint32_t,cset[cint32_t]]] citem
        __map_getitem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
        return Map__i32_Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(citem)

    def __iter__(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] itr = __map_iter[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
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
        cdef __map_iter[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] itr = __map_iter[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef shared_ptr[cmap[cint32_t,cset[cint32_t]]] citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextValue(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, citem)
            yield Map__i32_Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(citem)

    def items(self):
        if not self:
            return
        cdef __map_iter[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] itr = __map_iter[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        cdef cint32_t ckey = 0
        cdef shared_ptr[cmap[cint32_t,cset[cint32_t]]] citem
        for i in range(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).size()):
            itr.genNextItem(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE, ckey, citem)
            yield (ckey, Map__i32_Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(citem))

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Map__i32_Map__i32_Set__i32()

Mapping.register(Map__i32_Map__i32_Set__i32)

cdef shared_ptr[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] Map__i32_Map__i32_Set__i32__make_instance(object items) except *:
    cdef shared_ptr[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] c_inst = make_shared[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]]()
    if items is not None:
        for key, item in items.items():
            if not isinstance(key, int):
                raise TypeError(f"{key!r} is not of type int")
            key = <cint32_t> key
            if item is None:
                raise TypeError("None is not of type _typing.Mapping[int, _typing.AbstractSet[int]]")
            if not isinstance(item, Map__i32_Set__i32):
                item = Map__i32_Set__i32(item)

            deref(c_inst)[key] = deref((<Map__i32_Set__i32>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
    return cmove(c_inst)



cdef vector[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] List__Map__i32_Map__i32_Set__i32__make_instance(object items) except *:
    cdef vector[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]] c_inst
    if items is not None:
        for item in items:
            if item is None:
                raise TypeError("None is not of the type _typing.Mapping[int, _typing.Mapping[int, _typing.AbstractSet[int]]]")
            if not isinstance(item, Map__i32_Map__i32_Set__i32):
                item = Map__i32_Map__i32_Set__i32(item)
            c_inst.push_back(deref((<Map__i32_Map__i32_Set__i32>item)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
    return cmove(c_inst)

cdef object List__Map__i32_Map__i32_Set__i32__from_cpp(const vector[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(Map__i32_Map__i32_Set__i32._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]](c_vec[idx])))
    return List__Map__i32_Map__i32_Set__i32(py_list, thrift.py3.types._fbthrift_list_private_ctor)


cdef vector[vector[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]]] List__List__Map__i32_Map__i32_Set__i32__make_instance(object items) except *:
    cdef vector[vector[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]]] c_inst
    if items is not None:
        for item in items:
            if item is None:
                raise TypeError("None is not of the type _typing.Sequence[_typing.Mapping[int, _typing.Mapping[int, _typing.AbstractSet[int]]]]")
            if not isinstance(item, List__Map__i32_Map__i32_Set__i32):
                item = List__Map__i32_Map__i32_Set__i32(item)
            c_inst.push_back(List__Map__i32_Map__i32_Set__i32__make_instance(item))
    return cmove(c_inst)

cdef object List__List__Map__i32_Map__i32_Set__i32__from_cpp(const vector[vector[cmap[cint32_t,cmap[cint32_t,cset[cint32_t]]]]]& c_vec) except *:
    cdef list py_list = []
    cdef int idx = 0
    for idx in range(c_vec.size()):
        py_list.append(List__Map__i32_Map__i32_Set__i32__from_cpp(c_vec[idx]))
    return List__List__Map__i32_Map__i32_Set__i32(py_list, thrift.py3.types._fbthrift_list_private_ctor)


