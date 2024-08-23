#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/stream/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
cimport cython as __cython
from cython.operator cimport dereference as deref
from libcpp.utility cimport move as cmove
from thrift.py3.types cimport (
    assign_unique_ptr,
    assign_shared_ptr,
    assign_shared_const_ptr,
    bytes_to_string,
    make_unique,
    make_shared,
    make_const_shared,
)
cimport thrift.py3.types
from thrift.py3.types cimport (
    reset_field as __reset_field,
    StructFieldsSetter as __StructFieldsSetter
)

from thrift.py3.types cimport const_pointer_cast
from thrift.python.types cimport BadEnum as _fbthrift_BadEnum


@__cython.auto_pickle(False)
cdef class __FooStreamEx_FieldsSetter(__StructFieldsSetter):

    @staticmethod
    cdef __FooStreamEx_FieldsSetter _fbthrift_create(_module_types.cFooStreamEx* struct_cpp_obj):
        cdef __FooStreamEx_FieldsSetter __fbthrift_inst = __FooStreamEx_FieldsSetter.__new__(__FooStreamEx_FieldsSetter)
        __fbthrift_inst._struct_cpp_obj = struct_cpp_obj
        return __fbthrift_inst

    cdef void set_field(__FooStreamEx_FieldsSetter self, const char* name, object value) except *:
        cdef __cstring_view cname = __cstring_view(name)
        cdef cumap[__cstring_view, __FooStreamEx_FieldsSetterFunc].iterator found = self._setters.find(cname)
        if found == self._setters.end():
            raise TypeError(f"invalid field name {name.decode('utf-8')}")
        deref(found).second(self, value)


@__cython.auto_pickle(False)
cdef class __FooEx_FieldsSetter(__StructFieldsSetter):

    @staticmethod
    cdef __FooEx_FieldsSetter _fbthrift_create(_module_types.cFooEx* struct_cpp_obj):
        cdef __FooEx_FieldsSetter __fbthrift_inst = __FooEx_FieldsSetter.__new__(__FooEx_FieldsSetter)
        __fbthrift_inst._struct_cpp_obj = struct_cpp_obj
        return __fbthrift_inst

    cdef void set_field(__FooEx_FieldsSetter self, const char* name, object value) except *:
        cdef __cstring_view cname = __cstring_view(name)
        cdef cumap[__cstring_view, __FooEx_FieldsSetterFunc].iterator found = self._setters.find(cname)
        if found == self._setters.end():
            raise TypeError(f"invalid field name {name.decode('utf-8')}")
        deref(found).second(self, value)


@__cython.auto_pickle(False)
cdef class __FooEx2_FieldsSetter(__StructFieldsSetter):

    @staticmethod
    cdef __FooEx2_FieldsSetter _fbthrift_create(_module_types.cFooEx2* struct_cpp_obj):
        cdef __FooEx2_FieldsSetter __fbthrift_inst = __FooEx2_FieldsSetter.__new__(__FooEx2_FieldsSetter)
        __fbthrift_inst._struct_cpp_obj = struct_cpp_obj
        return __fbthrift_inst

    cdef void set_field(__FooEx2_FieldsSetter self, const char* name, object value) except *:
        cdef __cstring_view cname = __cstring_view(name)
        cdef cumap[__cstring_view, __FooEx2_FieldsSetterFunc].iterator found = self._setters.find(cname)
        if found == self._setters.end():
            raise TypeError(f"invalid field name {name.decode('utf-8')}")
        deref(found).second(self, value)

