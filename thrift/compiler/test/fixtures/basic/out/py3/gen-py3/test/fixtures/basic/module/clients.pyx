#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/basic/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#
from libc.stdint cimport (
    int8_t as cint8_t,
    int16_t as cint16_t,
    int32_t as cint32_t,
    int64_t as cint64_t,
)
from libcpp.memory cimport shared_ptr, make_shared, unique_ptr
from libcpp.string cimport string
from libcpp cimport bool as cbool
from cpython cimport bool as pbool
from libcpp.vector cimport vector
from libcpp.set cimport set as cset
from libcpp.map cimport map as cmap
from libcpp.utility cimport move as cmove
from cython.operator cimport dereference as deref, typeid
from cpython.ref cimport PyObject
from thrift.py3.client cimport cRequestChannel_ptr, makeClientWrapper, cClientWrapper
from thrift.py3.exceptions cimport try_make_shared_exception
from thrift.python.exceptions cimport create_py_exception
from folly cimport cFollyTry, cFollyUnit, c_unit
from folly.cast cimport down_cast_ptr
from libcpp.typeinfo cimport type_info
import thrift.py3.types
cimport thrift.py3.types
from thrift.py3.types cimport make_unique
import thrift.py3.client
cimport thrift.py3.client
from thrift.python.common cimport (
    RpcOptions as __RpcOptions,
    cThriftServiceMetadataResponse as __fbthrift_cThriftServiceMetadataResponse,
    ServiceMetadata,
    MetadataBox as __MetadataBox,
)

from folly.futures cimport bridgeFutureWith
from folly.executor cimport get_executor
cimport folly.iobuf as _fbthrift_iobuf
import folly.iobuf as _fbthrift_iobuf
from folly.iobuf cimport move as move_iobuf
cimport cython

import sys
import types as _py_types
from asyncio import get_event_loop as asyncio_get_event_loop, shield as asyncio_shield, InvalidStateError as asyncio_InvalidStateError

cimport test.fixtures.basic.module.types as _test_fixtures_basic_module_types
cimport test.fixtures.basic.module.cbindings as _test_fixtures_basic_module_cbindings
import test.fixtures.basic.module.types as _test_fixtures_basic_module_types

import test.fixtures.basic.module.services_reflection as _services_reflection
cimport test.fixtures.basic.module.services_reflection as _services_reflection

from test.fixtures.basic.module.clients_wrapper cimport cFooServiceAsyncClient, cFooServiceClientWrapper
from test.fixtures.basic.module.clients_wrapper cimport cFB303ServiceAsyncClient, cFB303ServiceClientWrapper
from test.fixtures.basic.module.clients_wrapper cimport cMyServiceAsyncClient, cMyServiceClientWrapper
from test.fixtures.basic.module.clients_wrapper cimport cDbMixedStackArgumentsAsyncClient, cDbMixedStackArgumentsClientWrapper


cdef void FooService_simple_rpc_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void FB303Service_simple_rpc_callback(
    cFollyTry[_test_fixtures_basic_module_cbindings.cReservedKeyword]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_test_fixtures_basic_module_types.ReservedKeyword._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[_test_fixtures_basic_module_cbindings.cReservedKeyword](cmove(result.value()))))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_ping_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_getRandomData_callback(
    cFollyTry[string]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(result.value().data().decode('UTF-8'))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_sink_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_putDataById_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_hasDataById_callback(
    cFollyTry[cbool]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(<bint>result.value())
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_getDataById_callback(
    cFollyTry[string]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(result.value().data().decode('UTF-8'))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_deleteDataById_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_lobDataById_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_invalid_return_for_hack_callback(
    cFollyTry[cset[float]]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(_test_fixtures_basic_module_types.Set__float._create_FBTHRIFT_ONLY_DO_NOT_USE(make_shared[cset[float]](cmove(result.value()))))
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void MyService_rpc_skipped_codegen_callback(
    cFollyTry[cFollyUnit]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(None)
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void DbMixedStackArguments_getDataByKey0_callback(
    cFollyTry[string]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(result.value())
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))

cdef void DbMixedStackArguments_getDataByKey1_callback(
    cFollyTry[string]&& result,
    PyObject* userdata
) noexcept:
    client, pyfuture, options = <object> userdata  
    if result.hasException():
        pyfuture.set_exception(create_py_exception(result.exception(), <__RpcOptions>options))
    else:
        try:
            pyfuture.set_result(result.value())
        except Exception as ex:
            pyfuture.set_exception(ex.with_traceback(None))


cdef object _FooService_annotations = _py_types.MappingProxyType({
})


@cython.auto_pickle(False)
cdef class FooService(thrift.py3.client.Client):
    annotations = _FooService_annotations

    cdef const type_info* _typeid(FooService self):
        return &typeid(cFooServiceAsyncClient)

    cdef bind_client(FooService self, cRequestChannel_ptr&& channel):
        self._client = makeClientWrapper[cFooServiceAsyncClient, cFooServiceClientWrapper](
            cmove(channel)
        )

    @cython.always_allow_keywords(True)
    def simple_rpc(
            FooService self,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cFooServiceClientWrapper, cClientWrapper](self._client.get()).simple_rpc(rpc_options._cpp_obj, 
            ),
            FooService_simple_rpc_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)


    @classmethod
    def __get_reflection__(cls):
        return _services_reflection.get_reflection__FooService(for_clients=True)

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftServiceMetadataResponse response
        ServiceMetadata[_services_reflection.cFooServiceSvIf].gen(response)
        return __MetadataBox.box(cmove(deref(response.metadata_ref())))

    @staticmethod
    def __get_thrift_name__():
        return "module.FooService"

cdef object _FB303Service_annotations = _py_types.MappingProxyType({
})


@cython.auto_pickle(False)
cdef class FB303Service(thrift.py3.client.Client):
    annotations = _FB303Service_annotations

    cdef const type_info* _typeid(FB303Service self):
        return &typeid(cFB303ServiceAsyncClient)

    cdef bind_client(FB303Service self, cRequestChannel_ptr&& channel):
        self._client = makeClientWrapper[cFB303ServiceAsyncClient, cFB303ServiceClientWrapper](
            cmove(channel)
        )

    @cython.always_allow_keywords(True)
    def simple_rpc(
            FB303Service self,
            int_parameter not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(int_parameter, int):
            raise TypeError(f'int_parameter is not a {int !r}.')
        else:
            int_parameter = <cint32_t> int_parameter
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[_test_fixtures_basic_module_cbindings.cReservedKeyword](
            self._executor,
            down_cast_ptr[cFB303ServiceClientWrapper, cClientWrapper](self._client.get()).simple_rpc(rpc_options._cpp_obj, 
                int_parameter,
            ),
            FB303Service_simple_rpc_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)


    @classmethod
    def __get_reflection__(cls):
        return _services_reflection.get_reflection__FB303Service(for_clients=True)

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftServiceMetadataResponse response
        ServiceMetadata[_services_reflection.cFB303ServiceSvIf].gen(response)
        return __MetadataBox.box(cmove(deref(response.metadata_ref())))

    @staticmethod
    def __get_thrift_name__():
        return "module.FB303Service"

cdef object _MyService_annotations = _py_types.MappingProxyType({
})


@cython.auto_pickle(False)
cdef class MyService(thrift.py3.client.Client):
    annotations = _MyService_annotations

    cdef const type_info* _typeid(MyService self):
        return &typeid(cMyServiceAsyncClient)

    cdef bind_client(MyService self, cRequestChannel_ptr&& channel):
        self._client = makeClientWrapper[cMyServiceAsyncClient, cMyServiceClientWrapper](
            cmove(channel)
        )

    @cython.always_allow_keywords(True)
    def ping(
            MyService self,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).ping(rpc_options._cpp_obj, 
            ),
            MyService_ping_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def getRandomData(
            MyService self,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[string](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).getRandomData(rpc_options._cpp_obj, 
            ),
            MyService_getRandomData_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def sink(
            MyService self,
            sink not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(sink, int):
            raise TypeError(f'sink is not a {int !r}.')
        else:
            sink = <cint64_t> sink
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).sink(rpc_options._cpp_obj, 
                sink,
            ),
            MyService_sink_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def putDataById(
            MyService self,
            id not None,
            str data not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(id, int):
            raise TypeError(f'id is not a {int !r}.')
        else:
            id = <cint64_t> id
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).putDataById(rpc_options._cpp_obj, 
                id,
                data.encode('UTF-8'),
            ),
            MyService_putDataById_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def hasDataById(
            MyService self,
            id not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(id, int):
            raise TypeError(f'id is not a {int !r}.')
        else:
            id = <cint64_t> id
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cbool](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).hasDataById(rpc_options._cpp_obj, 
                id,
            ),
            MyService_hasDataById_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def getDataById(
            MyService self,
            id not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(id, int):
            raise TypeError(f'id is not a {int !r}.')
        else:
            id = <cint64_t> id
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[string](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).getDataById(rpc_options._cpp_obj, 
                id,
            ),
            MyService_getDataById_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def deleteDataById(
            MyService self,
            id not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(id, int):
            raise TypeError(f'id is not a {int !r}.')
        else:
            id = <cint64_t> id
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).deleteDataById(rpc_options._cpp_obj, 
                id,
            ),
            MyService_deleteDataById_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def lobDataById(
            MyService self,
            id not None,
            str data not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        if not isinstance(id, int):
            raise TypeError(f'id is not a {int !r}.')
        else:
            id = <cint64_t> id
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).lobDataById(rpc_options._cpp_obj, 
                id,
                data.encode('UTF-8'),
            ),
            MyService_lobDataById_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def invalid_return_for_hack(
            MyService self,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cset[float]](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).invalid_return_for_hack(rpc_options._cpp_obj, 
            ),
            MyService_invalid_return_for_hack_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def rpc_skipped_codegen(
            MyService self,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[cFollyUnit](
            self._executor,
            down_cast_ptr[cMyServiceClientWrapper, cClientWrapper](self._client.get()).rpc_skipped_codegen(rpc_options._cpp_obj, 
            ),
            MyService_rpc_skipped_codegen_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)


    @classmethod
    def __get_reflection__(cls):
        return _services_reflection.get_reflection__MyService(for_clients=True)

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftServiceMetadataResponse response
        ServiceMetadata[_services_reflection.cMyServiceSvIf].gen(response)
        return __MetadataBox.box(cmove(deref(response.metadata_ref())))

    @staticmethod
    def __get_thrift_name__():
        return "module.MyService"

cdef object _DbMixedStackArguments_annotations = _py_types.MappingProxyType({
})


@cython.auto_pickle(False)
cdef class DbMixedStackArguments(thrift.py3.client.Client):
    annotations = _DbMixedStackArguments_annotations

    cdef const type_info* _typeid(DbMixedStackArguments self):
        return &typeid(cDbMixedStackArgumentsAsyncClient)

    cdef bind_client(DbMixedStackArguments self, cRequestChannel_ptr&& channel):
        self._client = makeClientWrapper[cDbMixedStackArgumentsAsyncClient, cDbMixedStackArgumentsClientWrapper](
            cmove(channel)
        )

    @cython.always_allow_keywords(True)
    def getDataByKey0(
            DbMixedStackArguments self,
            str key not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[string](
            self._executor,
            down_cast_ptr[cDbMixedStackArgumentsClientWrapper, cClientWrapper](self._client.get()).getDataByKey0(rpc_options._cpp_obj, 
                key.encode('UTF-8'),
            ),
            DbMixedStackArguments_getDataByKey0_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)

    @cython.always_allow_keywords(True)
    def getDataByKey1(
            DbMixedStackArguments self,
            str key not None,
            __RpcOptions rpc_options=None
    ):
        if rpc_options is None:
            rpc_options = <__RpcOptions>__RpcOptions.__new__(__RpcOptions)
        self._check_connect_future()
        __loop = asyncio_get_event_loop()
        __future = __loop.create_future()
        __userdata = (self, __future, rpc_options)
        bridgeFutureWith[string](
            self._executor,
            down_cast_ptr[cDbMixedStackArgumentsClientWrapper, cClientWrapper](self._client.get()).getDataByKey1(rpc_options._cpp_obj, 
                key.encode('UTF-8'),
            ),
            DbMixedStackArguments_getDataByKey1_callback,
            <PyObject *> __userdata
        )
        return asyncio_shield(__future)


    @classmethod
    def __get_reflection__(cls):
        return _services_reflection.get_reflection__DbMixedStackArguments(for_clients=True)

    @staticmethod
    def __get_metadata__():
        cdef __fbthrift_cThriftServiceMetadataResponse response
        ServiceMetadata[_services_reflection.cDbMixedStackArgumentsSvIf].gen(response)
        return __MetadataBox.box(cmove(deref(response.metadata_ref())))

    @staticmethod
    def __get_thrift_name__():
        return "module.DbMixedStackArguments"

