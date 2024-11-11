#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/enums/src/module.thrift
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

from test.fixtures.enums.module.types_impl_FBTHRIFT_ONLY_DO_NOT_USE import (
    Metasyntactic,
    MyEnum1,
    MyEnum2,
    MyEnum3,
    MyEnum4,
    MyBitmaskEnum1,
    MyBitmaskEnum2,
)

from test.fixtures.enums.module.containers_FBTHRIFT_ONLY_DO_NOT_USE import (
    Set__i32,
)


cdef object get_types_reflection():
    import importlib
    return importlib.import_module(
        "test.fixtures.enums.module.types_reflection"
    )

@__cython.auto_pickle(False)
cdef class SomeStruct(thrift.py3.types.Struct):
    def __init__(SomeStruct self, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enums_module_cbindings.cSomeStruct]()
        self._fields_setter = _fbthrift_types_fields.__SomeStruct_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__(**kwargs)

    def __call__(SomeStruct self, **kwargs):
        if not kwargs:
            return self
        cdef SomeStruct __fbthrift_inst = SomeStruct.__new__(SomeStruct)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enums_module_cbindings.cSomeStruct](deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
        __fbthrift_inst._fields_setter = _fbthrift_types_fields.__SomeStruct_FieldsSetter._fbthrift_create(__fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        for __fbthrift_name, _fbthrift_value in kwargs.items():
            __fbthrift_inst._fbthrift_set_field(__fbthrift_name, _fbthrift_value)
        return __fbthrift_inst

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("SomeStruct", {
          "reasonable": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).reasonable_ref().has_value(),
          "fine": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).fine_ref().has_value(),
          "questionable": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).questionable_ref().has_value(),
          "tags": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).tags_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_test_fixtures_enums_module_cbindings.cSomeStruct] cpp_obj):
        __fbthrift_inst = <SomeStruct>SomeStruct.__new__(SomeStruct)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        return __fbthrift_inst

    cdef inline reasonable_impl(self):
        if self.__fbthrift_cached_reasonable is None:
            self.__fbthrift_cached_reasonable = translate_cpp_enum_to_python(Metasyntactic, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).reasonable_ref().value()))
        return self.__fbthrift_cached_reasonable

    @property
    def reasonable(self):
        return self.reasonable_impl()

    cdef inline fine_impl(self):
        if self.__fbthrift_cached_fine is None:
            self.__fbthrift_cached_fine = translate_cpp_enum_to_python(Metasyntactic, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).fine_ref().value()))
        return self.__fbthrift_cached_fine

    @property
    def fine(self):
        return self.fine_impl()

    cdef inline questionable_impl(self):
        if self.__fbthrift_cached_questionable is None:
            self.__fbthrift_cached_questionable = translate_cpp_enum_to_python(Metasyntactic, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).questionable_ref().value()))
        return self.__fbthrift_cached_questionable

    @property
    def questionable(self):
        return self.questionable_impl()

    cdef inline tags_impl(self):
        if self.__fbthrift_cached_tags is None:
            self.__fbthrift_cached_tags = Set__i32__from_cpp(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).tags_ref().ref())
        return self.__fbthrift_cached_tags

    @property
    def tags(self):
        return self.tags_impl()


    def __hash__(SomeStruct self):
        return super().__hash__()

    def __repr__(SomeStruct self):
        return super().__repr__()

    def __str__(SomeStruct self):
        return super().__str__()


    def __copy__(SomeStruct self):
        cdef shared_ptr[_test_fixtures_enums_module_cbindings.cSomeStruct] cpp_obj = make_shared[_test_fixtures_enums_module_cbindings.cSomeStruct](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return SomeStruct._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_test_fixtures_enums_module_cbindings.cSomeStruct](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<SomeStruct>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__SomeStruct()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _test_fixtures_enums_module_cbindings.StructMetadata[_test_fixtures_enums_module_cbindings.cSomeStruct].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.SomeStruct"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_test_fixtures_enums_module_cbindings.cSomeStruct](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 4

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(SomeStruct self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_test_fixtures_enums_module_cbindings.cSomeStruct](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(SomeStruct self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enums_module_cbindings.cSomeStruct]()
        with nogil:
            needed = serializer.cdeserialize[_test_fixtures_enums_module_cbindings.cSomeStruct](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.SomeStruct, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.SomeStruct, self)

@__cython.auto_pickle(False)
cdef class MyStruct(thrift.py3.types.Struct):
    def __init__(MyStruct self, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enums_module_cbindings.cMyStruct]()
        self._fields_setter = _fbthrift_types_fields.__MyStruct_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__(**kwargs)

    def __call__(MyStruct self, **kwargs):
        if not kwargs:
            return self
        cdef MyStruct __fbthrift_inst = MyStruct.__new__(MyStruct)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enums_module_cbindings.cMyStruct](deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE))
        __fbthrift_inst._fields_setter = _fbthrift_types_fields.__MyStruct_FieldsSetter._fbthrift_create(__fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        for __fbthrift_name, _fbthrift_value in kwargs.items():
            __fbthrift_inst._fbthrift_set_field(__fbthrift_name, _fbthrift_value)
        return __fbthrift_inst

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("MyStruct", {
          "me2_3": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me2_3_ref().has_value(),
          "me3_n3": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me3_n3_ref().has_value(),
          "me1_t1": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me1_t1_ref().has_value(),
          "me1_t2": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me1_t2_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_test_fixtures_enums_module_cbindings.cMyStruct] cpp_obj):
        __fbthrift_inst = <MyStruct>MyStruct.__new__(MyStruct)
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        return __fbthrift_inst

    cdef inline me2_3_impl(self):
        if self.__fbthrift_cached_me2_3 is None:
            self.__fbthrift_cached_me2_3 = translate_cpp_enum_to_python(MyEnum2, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me2_3_ref().value()))
        return self.__fbthrift_cached_me2_3

    @property
    def me2_3(self):
        return self.me2_3_impl()

    cdef inline me3_n3_impl(self):
        if self.__fbthrift_cached_me3_n3 is None:
            self.__fbthrift_cached_me3_n3 = translate_cpp_enum_to_python(MyEnum3, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me3_n3_ref().value()))
        return self.__fbthrift_cached_me3_n3

    @property
    def me3_n3(self):
        return self.me3_n3_impl()

    cdef inline me1_t1_impl(self):
        if self.__fbthrift_cached_me1_t1 is None:
            self.__fbthrift_cached_me1_t1 = translate_cpp_enum_to_python(MyEnum1, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me1_t1_ref().value()))
        return self.__fbthrift_cached_me1_t1

    @property
    def me1_t1(self):
        return self.me1_t1_impl()

    cdef inline me1_t2_impl(self):
        if self.__fbthrift_cached_me1_t2 is None:
            self.__fbthrift_cached_me1_t2 = translate_cpp_enum_to_python(MyEnum1, <int>(deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).me1_t2_ref().value()))
        return self.__fbthrift_cached_me1_t2

    @property
    def me1_t2(self):
        return self.me1_t2_impl()


    def __hash__(MyStruct self):
        return super().__hash__()

    def __repr__(MyStruct self):
        return super().__repr__()

    def __str__(MyStruct self):
        return super().__str__()


    def __copy__(MyStruct self):
        cdef shared_ptr[_test_fixtures_enums_module_cbindings.cMyStruct] cpp_obj = make_shared[_test_fixtures_enums_module_cbindings.cMyStruct](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return MyStruct._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_test_fixtures_enums_module_cbindings.cMyStruct](
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
        _test_fixtures_enums_module_cbindings.StructMetadata[_test_fixtures_enums_module_cbindings.cMyStruct].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.MyStruct"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_test_fixtures_enums_module_cbindings.cMyStruct](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 4

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(MyStruct self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_test_fixtures_enums_module_cbindings.cMyStruct](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(MyStruct self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_test_fixtures_enums_module_cbindings.cMyStruct]()
        with nogil:
            needed = serializer.cdeserialize[_test_fixtures_enums_module_cbindings.cMyStruct](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "test.fixtures.enums.module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.MyStruct, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.MyStruct, self)


cdef cset[cint32_t] Set__i32__make_instance(object items) except *:
    cdef cset[cint32_t] c_inst
    if items is not None:
        for item in items:
            if not isinstance(item, int):
                raise TypeError(f"{item!r} is not of type int")
            item = <cint32_t> item
            c_inst.insert(item)
    return cmove(c_inst)

cdef object Set__i32__from_cpp(const cset[cint32_t]& c_set) except *:
    cdef list py_items = []
    cdef __set_iter[cset[cint32_t]] iter = __set_iter[cset[cint32_t]](c_set)
    cdef cint32_t citem = 0
    for i in range(c_set.size()):
        iter.genNextItem(citem)
        py_items.append(citem)
    return Set__i32(frozenset(py_items), thrift.py3.types._fbthrift_set_private_ctor)


