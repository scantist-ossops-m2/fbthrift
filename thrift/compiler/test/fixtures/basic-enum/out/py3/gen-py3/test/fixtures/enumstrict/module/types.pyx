#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/basic-enum/src/module.thrift
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

import test.fixtures.enumstrict.module.thrift_types as _fbthrift_python_types
from test.fixtures.enumstrict.module.types_impl_FBTHRIFT_ONLY_DO_NOT_USE import (
    EmptyEnum,
    MyEnum,
    MyUseIntrinsicDefaultEnum,
    MyBigEnum,
)

from test.fixtures.enumstrict.module.containers_FBTHRIFT_ONLY_DO_NOT_USE import (
    Map__MyEnum_string,
)


cdef object get_types_reflection():
    return importlib.import_module(
        "test.fixtures.enumstrict.module.types_reflection"
    )

@__cython.auto_pickle(False)
cdef class MyStruct(thrift.py3.types.Struct):
    def __init__(MyStruct self, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enumstrict_module_cbindings.cMyStruct]()
        self._fields_setter = _fbthrift_types_fields.__MyStruct_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__(**kwargs)

    def __call__(MyStruct self, **kwargs):
        if not kwargs:
            return self
        cdef MyStruct __fbthrift_inst = MyStruct.__new__(MyStruct)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enumstrict_module_cbindings.cMyStruct](deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
        __fbthrift_inst._fields_setter = _fbthrift_types_fields.__MyStruct_FieldsSetter._fbthrift_create(__fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        for __fbthrift_name, _fbthrift_value in kwargs.items():
            __fbthrift_inst._fbthrift_set_field(__fbthrift_name, _fbthrift_value)
        return __fbthrift_inst

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("MyStruct", {
          "myEnum": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).myEnum_ref().has_value(),
          "myBigEnum": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).myBigEnum_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_test_fixtures_enumstrict_module_cbindings.cMyStruct] cpp_obj):
        __fbthrift_inst = <MyStruct>MyStruct.__new__(MyStruct)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        return __fbthrift_inst

    cdef inline myEnum_impl(self):
        if self.__fbthrift_cached_myEnum is None:
            self.__fbthrift_cached_myEnum = translate_cpp_enum_to_python(MyEnum, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).myEnum_ref().value()))
        return self.__fbthrift_cached_myEnum

    @property
    def myEnum(self):
        return self.myEnum_impl()

    cdef inline myBigEnum_impl(self):
        if self.__fbthrift_cached_myBigEnum is None:
            self.__fbthrift_cached_myBigEnum = translate_cpp_enum_to_python(MyBigEnum, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).myBigEnum_ref().value()))
        return self.__fbthrift_cached_myBigEnum

    @property
    def myBigEnum(self):
        return self.myBigEnum_impl()


    def __hash__(MyStruct self):
        return super().__hash__()

    def __repr__(MyStruct self):
        return super().__repr__()

    def __str__(MyStruct self):
        return super().__str__()


    def __copy__(MyStruct self):
        cdef shared_ptr[_test_fixtures_enumstrict_module_cbindings.cMyStruct] cpp_obj = make_shared[_test_fixtures_enumstrict_module_cbindings.cMyStruct](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return MyStruct._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_test_fixtures_enumstrict_module_cbindings.cMyStruct](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<MyStruct>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__MyStruct()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _test_fixtures_enumstrict_module_cbindings.StructMetadata[_test_fixtures_enumstrict_module_cbindings.cMyStruct].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.MyStruct"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_test_fixtures_enumstrict_module_cbindings.cMyStruct](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 2

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(MyStruct self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_test_fixtures_enumstrict_module_cbindings.cMyStruct](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(MyStruct self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enumstrict_module_cbindings.cMyStruct]()
        with nogil:
            needed = serializer.cdeserialize[_test_fixtures_enumstrict_module_cbindings.cMyStruct](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        return thrift.python.converter.to_python_struct(
            _fbthrift_python_types.MyStruct,
            self,
        )

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.MyStruct, self)

cdef cmap[_test_fixtures_enumstrict_module_cbindings.cMyEnum,string] Map__MyEnum_string__make_instance(object items) except *:
    cdef cmap[_test_fixtures_enumstrict_module_cbindings.cMyEnum,string] c_inst
    if items is None:
        return cmove(c_inst)
    for key, item in items.items():
        if not isinstance(key, MyEnum):
            raise TypeError(f"{key!r} is not of type MyEnum")
        if not isinstance(item, str):
            raise TypeError(f"{item!r} is not of type str")

        c_inst[<_test_fixtures_enumstrict_module_cbindings.cMyEnum><int>key] = item.encode('UTF-8')
    return cmove(c_inst)

cdef object Map__MyEnum_string__from_cpp(const cmap[_test_fixtures_enumstrict_module_cbindings.cMyEnum,string]& c_map) except *:
    cdef dict py_items = {}
    cdef __map_iter[cmap[_test_fixtures_enumstrict_module_cbindings.cMyEnum,string]] iter = __map_iter[cmap[_test_fixtures_enumstrict_module_cbindings.cMyEnum,string]](c_map)
    cdef _test_fixtures_enumstrict_module_cbindings.cMyEnum ckey
    cdef string cval
    for i in range(c_map.size()):
        iter.genNextKeyVal(ckey, cval)
        py_items[translate_cpp_enum_to_python(MyEnum, <int> ckey)] = __init_unicode_from_cpp(cval)
    return Map__MyEnum_string(py_items, private_ctor_token=thrift.py3.types._fbthrift_map_private_ctor)


kOne = MyEnum(<int> (_test_fixtures_enumstrict_module_cbindings.ckOne()))
enumNames = Map__MyEnum_string__from_cpp(_test_fixtures_enumstrict_module_cbindings.cenumNames())
