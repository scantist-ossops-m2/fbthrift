/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/basic-python-capi/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#pragma once

#include "thrift/compiler/test/fixtures/basic-python-capi/gen-cpp2/module_metadata.h"
#include <thrift/lib/cpp2/visitation/visit_union.h>

namespace apache {
namespace thrift {
namespace detail {

template <>
struct VisitUnion<::test::fixtures::basic-python-capi::MyUnion> {

  template <typename F, typename T>
  decltype(auto) operator()(FOLLY_MAYBE_UNUSED F&& f, T&& t) const {
    using Union = std::remove_reference_t<T>;
    switch (t.getType()) {
    case Union::Type::myEnum:
      return f(0, *static_cast<T&&>(t).myEnum_ref());
    case Union::Type::myStruct:
      return f(1, *static_cast<T&&>(t).myStruct_ref());
    case Union::Type::myDataItem:
      return f(2, *static_cast<T&&>(t).myDataItem_ref());
    case Union::Type::doubleSet:
      return f(3, *static_cast<T&&>(t).doubleSet_ref());
    case Union::Type::doubleList:
      return f(4, *static_cast<T&&>(t).doubleList_ref());
    case Union::Type::strMap:
      return f(5, *static_cast<T&&>(t).strMap_ref());
    case Union::Type::__EMPTY__:
      return decltype(f(0, *static_cast<T&&>(t).myEnum_ref()))();
    }
  }
};
} // namespace detail
} // namespace thrift
} // namespace apache
