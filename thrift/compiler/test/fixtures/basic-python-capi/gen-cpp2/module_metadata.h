/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/basic-python-capi/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#pragma once

#include <vector>

#include <thrift/lib/cpp2/gen/module_metadata_h.h>
#include "thrift/compiler/test/fixtures/basic-python-capi/gen-cpp2/module_types.h"


namespace apache {
namespace thrift {
namespace detail {
namespace md {

template <>
class EnumMetadata<::test::fixtures::basic-python-capi::MyEnum> {
 public:
  static void gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic-python-capi::MyStruct> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic-python-capi::MyDataItem> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
template <>
class StructMetadata<::test::fixtures::basic-python-capi::MyUnion> {
 public:
  static const ::apache::thrift::metadata::ThriftStruct& gen(ThriftMetadata& metadata);
};
} // namespace md
} // namespace detail
} // namespace thrift
} // namespace apache
