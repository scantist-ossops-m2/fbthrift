#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/transitive-deps/src/a.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
    uint16_t as cuint16_t,
    uint32_t as cuint32_t,
)
from libcpp.string cimport string
from libcpp cimport bool as cbool, nullptr, nullptr_t
from cpython cimport bool as pbool
from libcpp.memory cimport shared_ptr, unique_ptr
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap, pair as cpair
from libcpp.unordered_map cimport unordered_map as cumap
cimport folly.iobuf as _fbthrift_iobuf
from thrift.python.exceptions cimport cTException
from thrift.py3.types cimport (
    bstring,
    field_ref as __field_ref,
    optional_field_ref as __optional_field_ref,
    required_field_ref as __required_field_ref,
    terse_field_ref as __terse_field_ref,
    union_field_ref as __union_field_ref,
    get_union_field_value as __get_union_field_value,
)
from thrift.python.common cimport cThriftMetadata as __fbthrift_cThriftMetadata

cimport b.cbindings as _b_cbindings
cimport c.cbindings as _c_cbindings


cdef extern from "thrift/compiler/test/fixtures/transitive-deps/gen-cpp2/a_metadata.h" namespace "apache::thrift::detail::md":
    cdef cppclass ExceptionMetadata[T]:
        @staticmethod
        void gen(__fbthrift_cThriftMetadata &metadata)
cdef extern from "thrift/compiler/test/fixtures/transitive-deps/gen-cpp2/a_metadata.h" namespace "apache::thrift::detail::md":
    cdef cppclass StructMetadata[T]:
        @staticmethod
        void gen(__fbthrift_cThriftMetadata &metadata)
cdef extern from "thrift/compiler/test/fixtures/transitive-deps/gen-cpp2/a_types_custom_protocol.h" namespace "::cpp2":

    cdef cppclass cA "::cpp2::A":
        cA() except +
        cA(const cA&) except +
        bint operator==(cA&)
        bint operator!=(cA&)
        bint operator<(cA&)
        bint operator>(cA&)
        bint operator<=(cA&)
        bint operator>=(cA&)
        __field_ref[vector[vector[_c_cbindings.cC]]] b_ref "b_ref" ()
        __field_ref[vector[_c_cbindings.cC]] other_ref "other_ref" ()

