/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/types/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#pragma once

#include "thrift/compiler/test/fixtures/types/gen-cpp2/module_types.h"
#include "thrift/compiler/test/fixtures/types/gen-cpp2/module_fatal.h"

#include <fatal/type/enum.h>

#include <type_traits>

namespace apache::thrift::detail {
template <>
struct ExtraEnumTraits<::apache::thrift::fixtures::types::has_bitwise_ops> {
  static inline constexpr std::string_view name = "has_bitwise_ops";
  using module = ::apache::thrift::fixtures::types::module_tags::module;
};
template<>
inline constexpr bool kHasExtraEnumTraits<::apache::thrift::fixtures::types::has_bitwise_ops> = true;
template <>
struct ExtraEnumTraits<::apache::thrift::fixtures::types::is_unscoped> {
  static inline constexpr std::string_view name = "is_unscoped";
  using module = ::apache::thrift::fixtures::types::module_tags::module;
};
template<>
inline constexpr bool kHasExtraEnumTraits<::apache::thrift::fixtures::types::is_unscoped> = true;
template <>
struct ExtraEnumTraits<::apache::thrift::fixtures::types::MyForwardRefEnum> {
  static inline constexpr std::string_view name = "MyForwardRefEnum";
  using module = ::apache::thrift::fixtures::types::module_tags::module;
};
template<>
inline constexpr bool kHasExtraEnumTraits<::apache::thrift::fixtures::types::MyForwardRefEnum> = true;
}
