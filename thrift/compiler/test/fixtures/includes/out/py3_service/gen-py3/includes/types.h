/**
 * Autogenerated by Thrift for includes.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#pragma once

#include <functional>
#include <folly/Range.h>

#include "thrift/compiler/test/fixtures/includes/gen-cpp2/includes_data.h"
#include "thrift/compiler/test/fixtures/includes/gen-cpp2/includes_types.h"
#include "thrift/compiler/test/fixtures/includes/gen-cpp2/includes_metadata.h"
namespace thrift {
namespace py3 {



template<>
inline void reset_field<::cpp2::Included>(
    ::cpp2::Included& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.MyIntField_ref().copy_from(default_inst<::cpp2::Included>().MyIntField_ref());
      return;
    case 1:
      obj.MyTransitiveField_ref().copy_from(default_inst<::cpp2::Included>().MyTransitiveField_ref());
      return;
  }
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::cpp2::Included>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}
} // namespace py3
} // namespace thrift
