#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/exceptions/src/module.thrift
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




cdef object get_types_reflection():
    import importlib
    return importlib.import_module(
        "module.types_reflection"
    )

@__cython.auto_pickle(False)
cdef class Fiery(thrift.py3.exceptions.GeneratedError):
    def __init__(Fiery self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cFiery]()
        self._fields_setter = _fbthrift_types_fields.__Fiery_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("Fiery", {
          "message": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).message_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cFiery] cpp_obj):
        __fbthrift_inst = <Fiery>Fiery.__new__(Fiery, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst

    cdef inline message_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).message_ref().value()).decode('UTF-8')

    @property
    def message(self):
        return self.message_impl()


    def __hash__(Fiery self):
        return super().__hash__()

    def __repr__(Fiery self):
        return super().__repr__()

    def __str__(Fiery self):
        field = self.message
        if field is None:
            return str(field)
        return field


    def __copy__(Fiery self):
        cdef shared_ptr[_module_cbindings.cFiery] cpp_obj = make_shared[_module_cbindings.cFiery](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Fiery._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cFiery](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<Fiery>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Fiery()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cFiery].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.Fiery"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cFiery](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 1

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(Fiery self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cFiery](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(Fiery self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cFiery]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cFiery](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.Fiery, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.Fiery, self)

@__cython.auto_pickle(False)
cdef class Serious(thrift.py3.exceptions.GeneratedError):
    def __init__(Serious self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cSerious]()
        self._fields_setter = _fbthrift_types_fields.__Serious_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("Serious", {
          "not_sonnet": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).not_sonnet_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cSerious] cpp_obj):
        __fbthrift_inst = <Serious>Serious.__new__(Serious, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst

    cdef inline not_sonnet_impl(self):
        if not deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).not_sonnet_ref().has_value():
            return None
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).not_sonnet_ref().value_unchecked()).decode('UTF-8')

    @property
    def not_sonnet(self):
        return self.not_sonnet_impl()


    def __hash__(Serious self):
        return super().__hash__()

    def __repr__(Serious self):
        return super().__repr__()

    def __str__(Serious self):
        field = self.not_sonnet
        if field is None:
            return str(field)
        return field


    def __copy__(Serious self):
        cdef shared_ptr[_module_cbindings.cSerious] cpp_obj = make_shared[_module_cbindings.cSerious](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Serious._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cSerious](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<Serious>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Serious()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cSerious].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.Serious"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cSerious](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 1

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(Serious self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cSerious](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(Serious self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cSerious]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cSerious](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.Serious, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.Serious, self)

@__cython.auto_pickle(False)
cdef class ComplexFieldNames(thrift.py3.exceptions.GeneratedError):
    def __init__(ComplexFieldNames self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cComplexFieldNames]()
        self._fields_setter = _fbthrift_types_fields.__ComplexFieldNames_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("ComplexFieldNames", {
          "error_message": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_message_ref().has_value(),
          "internal_error_message": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).internal_error_message_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cComplexFieldNames] cpp_obj):
        __fbthrift_inst = <ComplexFieldNames>ComplexFieldNames.__new__(ComplexFieldNames, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst

    cdef inline error_message_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_message_ref().value()).decode('UTF-8')

    @property
    def error_message(self):
        return self.error_message_impl()

    cdef inline internal_error_message_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).internal_error_message_ref().value()).decode('UTF-8')

    @property
    def internal_error_message(self):
        return self.internal_error_message_impl()


    def __hash__(ComplexFieldNames self):
        return super().__hash__()

    def __repr__(ComplexFieldNames self):
        return super().__repr__()

    def __str__(ComplexFieldNames self):
        field = self.internal_error_message
        if field is None:
            return str(field)
        return field


    def __copy__(ComplexFieldNames self):
        cdef shared_ptr[_module_cbindings.cComplexFieldNames] cpp_obj = make_shared[_module_cbindings.cComplexFieldNames](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return ComplexFieldNames._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cComplexFieldNames](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<ComplexFieldNames>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__ComplexFieldNames()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cComplexFieldNames].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.ComplexFieldNames"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cComplexFieldNames](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 2

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(ComplexFieldNames self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cComplexFieldNames](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(ComplexFieldNames self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cComplexFieldNames]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cComplexFieldNames](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.ComplexFieldNames, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.ComplexFieldNames, self)

@__cython.auto_pickle(False)
cdef class CustomFieldNames(thrift.py3.exceptions.GeneratedError):
    def __init__(CustomFieldNames self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cCustomFieldNames]()
        self._fields_setter = _fbthrift_types_fields.__CustomFieldNames_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("CustomFieldNames", {
          "error_message": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_message_ref().has_value(),
          "internal_error_message": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).internal_error_message_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cCustomFieldNames] cpp_obj):
        __fbthrift_inst = <CustomFieldNames>CustomFieldNames.__new__(CustomFieldNames, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst

    cdef inline error_message_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_message_ref().value()).decode('UTF-8')

    @property
    def error_message(self):
        return self.error_message_impl()

    cdef inline internal_error_message_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).internal_error_message_ref().value()).decode('UTF-8')

    @property
    def internal_error_message(self):
        return self.internal_error_message_impl()


    def __hash__(CustomFieldNames self):
        return super().__hash__()

    def __repr__(CustomFieldNames self):
        return super().__repr__()

    def __str__(CustomFieldNames self):
        field = self.internal_error_message
        if field is None:
            return str(field)
        return field


    def __copy__(CustomFieldNames self):
        cdef shared_ptr[_module_cbindings.cCustomFieldNames] cpp_obj = make_shared[_module_cbindings.cCustomFieldNames](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return CustomFieldNames._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cCustomFieldNames](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<CustomFieldNames>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__CustomFieldNames()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cCustomFieldNames].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.CustomFieldNames"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cCustomFieldNames](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 2

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(CustomFieldNames self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cCustomFieldNames](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(CustomFieldNames self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cCustomFieldNames]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cCustomFieldNames](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.CustomFieldNames, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.CustomFieldNames, self)

@__cython.auto_pickle(False)
cdef class ExceptionWithPrimitiveField(thrift.py3.exceptions.GeneratedError):
    def __init__(ExceptionWithPrimitiveField self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cExceptionWithPrimitiveField]()
        self._fields_setter = _fbthrift_types_fields.__ExceptionWithPrimitiveField_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("ExceptionWithPrimitiveField", {
          "message": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).message_ref().has_value(),
          "error_code": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_code_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cExceptionWithPrimitiveField] cpp_obj):
        __fbthrift_inst = <ExceptionWithPrimitiveField>ExceptionWithPrimitiveField.__new__(ExceptionWithPrimitiveField, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst

    cdef inline message_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).message_ref().value()).decode('UTF-8')

    @property
    def message(self):
        return self.message_impl()

    cdef inline error_code_impl(self):
        return deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_code_ref().value()

    @property
    def error_code(self):
        return self.error_code_impl()


    def __hash__(ExceptionWithPrimitiveField self):
        return super().__hash__()

    def __repr__(ExceptionWithPrimitiveField self):
        return super().__repr__()

    def __str__(ExceptionWithPrimitiveField self):
        field = self.message
        if field is None:
            return str(field)
        return field


    def __copy__(ExceptionWithPrimitiveField self):
        cdef shared_ptr[_module_cbindings.cExceptionWithPrimitiveField] cpp_obj = make_shared[_module_cbindings.cExceptionWithPrimitiveField](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return ExceptionWithPrimitiveField._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cExceptionWithPrimitiveField](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<ExceptionWithPrimitiveField>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__ExceptionWithPrimitiveField()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cExceptionWithPrimitiveField].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.ExceptionWithPrimitiveField"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cExceptionWithPrimitiveField](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 2

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(ExceptionWithPrimitiveField self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cExceptionWithPrimitiveField](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(ExceptionWithPrimitiveField self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cExceptionWithPrimitiveField]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cExceptionWithPrimitiveField](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.ExceptionWithPrimitiveField, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.ExceptionWithPrimitiveField, self)

@__cython.auto_pickle(False)
cdef class ExceptionWithStructuredAnnotation(thrift.py3.exceptions.GeneratedError):
    def __init__(ExceptionWithStructuredAnnotation self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cExceptionWithStructuredAnnotation]()
        self._fields_setter = _fbthrift_types_fields.__ExceptionWithStructuredAnnotation_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("ExceptionWithStructuredAnnotation", {
          "message_field": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).message_field_ref().has_value(),
          "error_code": deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_code_ref().has_value(),
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cExceptionWithStructuredAnnotation] cpp_obj):
        __fbthrift_inst = <ExceptionWithStructuredAnnotation>ExceptionWithStructuredAnnotation.__new__(ExceptionWithStructuredAnnotation, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst

    cdef inline message_field_impl(self):
        return (<bytes>deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).message_field_ref().value()).decode('UTF-8')

    @property
    def message_field(self):
        return self.message_field_impl()

    cdef inline error_code_impl(self):
        return deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE).error_code_ref().value()

    @property
    def error_code(self):
        return self.error_code_impl()


    def __hash__(ExceptionWithStructuredAnnotation self):
        return super().__hash__()

    def __repr__(ExceptionWithStructuredAnnotation self):
        return super().__repr__()

    def __str__(ExceptionWithStructuredAnnotation self):
        field = self.message_field
        if field is None:
            return str(field)
        return field


    def __copy__(ExceptionWithStructuredAnnotation self):
        cdef shared_ptr[_module_cbindings.cExceptionWithStructuredAnnotation] cpp_obj = make_shared[_module_cbindings.cExceptionWithStructuredAnnotation](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return ExceptionWithStructuredAnnotation._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cExceptionWithStructuredAnnotation](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<ExceptionWithStructuredAnnotation>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__ExceptionWithStructuredAnnotation()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cExceptionWithStructuredAnnotation].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.ExceptionWithStructuredAnnotation"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cExceptionWithStructuredAnnotation](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 2

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(ExceptionWithStructuredAnnotation self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cExceptionWithStructuredAnnotation](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(ExceptionWithStructuredAnnotation self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cExceptionWithStructuredAnnotation]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cExceptionWithStructuredAnnotation](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.ExceptionWithStructuredAnnotation, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.ExceptionWithStructuredAnnotation, self)

@__cython.auto_pickle(False)
cdef class Banal(thrift.py3.exceptions.GeneratedError):
    def __init__(Banal self, *args, **kwargs):
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cBanal]()
        self._fields_setter = _fbthrift_types_fields.__Banal_FieldsSetter._fbthrift_create(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get())
        super().__init__( *args, **kwargs)

    cdef void _fbthrift_set_field(self, str name, object value) except *:
        self._fields_setter.set_field(name.encode("utf-8"), value)

    cdef object _fbthrift_isset(self):
        return _fbthrift_IsSet("Banal", {
        })

    @staticmethod
    cdef _create_FBTHRIFT_ONLY_DO_NOT_USE(shared_ptr[_module_cbindings.cBanal] cpp_obj):
        __fbthrift_inst = <Banal>Banal.__new__(Banal, (<bytes>deref(cpp_obj).what()).decode('utf-8'))
        __fbthrift_inst._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = cmove(cpp_obj)
        _builtins.Exception.__init__(__fbthrift_inst, *(v for _, v in __fbthrift_inst))
        return __fbthrift_inst


    def __hash__(Banal self):
        return super().__hash__()

    def __repr__(Banal self):
        return super().__repr__()

    def __str__(Banal self):
        return super().__str__()


    def __copy__(Banal self):
        cdef shared_ptr[_module_cbindings.cBanal] cpp_obj = make_shared[_module_cbindings.cBanal](
            deref(self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE)
        )
        return Banal._create_FBTHRIFT_ONLY_DO_NOT_USE(cmove(cpp_obj))

    def __richcmp__(self, other, int op):
        r = self._fbthrift_cmp_sametype(other, op)
        return __richcmp[_module_cbindings.cBanal](
            self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            (<Banal>other)._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE,
            op,
        ) if r is None else r

    @staticmethod
    def __get_reflection__():
        return get_types_reflection().get_reflection__Banal()

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftMetadata meta
        _module_cbindings.ExceptionMetadata[_module_cbindings.cBanal].gen(meta)
        return __MetadataBox.box(cmove(meta))

    @staticmethod
    def __get_thrift_name__():
        return "module.Banal"

    @classmethod
    def _fbthrift_get_field_name_by_index(cls, idx):
        return __sv_to_str(__get_field_name_by_index[_module_cbindings.cBanal](idx))

    @classmethod
    def _fbthrift_get_struct_size(cls):
        return 0

    cdef _fbthrift_iobuf.IOBuf _fbthrift_serialize(Banal self, __Protocol proto):
        cdef unique_ptr[_fbthrift_iobuf.cIOBuf] data
        with nogil:
            data = cmove(serializer.cserialize[_module_cbindings.cBanal](self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto))
        return _fbthrift_iobuf.from_unique_ptr(cmove(data))

    cdef cuint32_t _fbthrift_deserialize(Banal self, const _fbthrift_iobuf.cIOBuf* buf, __Protocol proto) except? 0:
        cdef cuint32_t needed
        self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE = make_shared[_module_cbindings.cBanal]()
        with nogil:
            needed = serializer.cdeserialize[_module_cbindings.cBanal](buf, self._cpp_obj_FBTHRIFT_ONLY_DO_NOT_USE.get(), proto)
        return needed


    def _to_python(self):
        import importlib
        import thrift.python.converter
        python_types = importlib.import_module(
            "module.thrift_types"
        )
        return thrift.python.converter.to_python_struct(python_types.Banal, self)

    def _to_py3(self):
        return self

    def _to_py_deprecated(self):
        import importlib
        import thrift.util.converter
        py_deprecated_types = importlib.import_module("module.ttypes")
        return thrift.util.converter.to_py_struct(py_deprecated_types.Banal, self)


