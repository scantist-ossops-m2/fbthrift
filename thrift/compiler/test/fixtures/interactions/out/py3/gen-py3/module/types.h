/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/interactions/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#pragma once

#include <functional>
#include <folly/Range.h>

#include "thrift/compiler/test/fixtures/interactions/gen-cpp2/module_data.h"
#include "thrift/compiler/test/fixtures/interactions/gen-cpp2/module_types.h"
#include "thrift/compiler/test/fixtures/interactions/gen-cpp2/module_metadata.h"
namespace thrift {
namespace py3 {



template<>
inline void reset_field<::cpp2::CustomException>(
    ::cpp2::CustomException& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.message_ref().copy_from(default_inst<::cpp2::CustomException>().message_ref());
      return;
  }
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::cpp2::CustomException>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}
} // namespace py3
} // namespace thrift
