#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from thrift.py3.reflection cimport (
  MethodSpec as __MethodSpec,
  ArgumentSpec as __ArgumentSpec,
  NumberType as __NumberType,
)

import folly.iobuf as _fbthrift_iobuf


cimport test.fixtures.interactions.module.types as _test_fixtures_interactions_module_types


cdef __InterfaceSpec get_reflection__MyService(bint for_clients):
    cdef __InterfaceSpec spec = __InterfaceSpec._fbthrift_create(
        name="MyService",
        annotations={
        },
    )
    spec.add_method(
        __MethodSpec._fbthrift_create(
            name="foo",
            arguments=(
            ),
            result=None,
            result_kind=__NumberType.NOT_A_NUMBER,
            exceptions=(
            ),
            annotations={
            },
        )
    )
    spec.add_method(
        __MethodSpec._fbthrift_create(
            name="interact",
            arguments=(
                __ArgumentSpec._fbthrift_create(
                    name="arg",
                    type=int,
                    kind=__NumberType.I32,
                    annotations={
                    },
                ),
            ),
            result=None,
            result_kind=__NumberType.NOT_A_NUMBER,
            exceptions=(
            ),
            annotations={
            },
        )
    )
    spec.add_method(
        __MethodSpec._fbthrift_create(
            name="interactFast",
            arguments=(
            ),
            result=int,
            result_kind=__NumberType.I32,
            exceptions=(
            ),
            annotations={
            },
        )
    )
    spec.add_method(
        __MethodSpec._fbthrift_create(
            name="serialize",
            arguments=(
            ),
            result=_test_fixtures_interactions_module_types.ResponseAndClientBufferedStream__i32_i32 if for_clients else _test_fixtures_interactions_module_types.ResponseAndServerStream__i32_i32,
            result_kind=__NumberType.NOT_A_NUMBER,
            exceptions=(
            ),
            annotations={
            },
        )
    )
    return spec