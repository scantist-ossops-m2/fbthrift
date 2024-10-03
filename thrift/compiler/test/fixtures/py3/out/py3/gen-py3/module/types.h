/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/py3/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#pragma once

#include <functional>
#include <folly/Range.h>

#include "thrift/compiler/test/fixtures/py3/gen-py3cpp/module_data.h"
#include "thrift/compiler/test/fixtures/py3/gen-py3cpp/module_types.h"
#include "thrift/compiler/test/fixtures/py3/gen-py3cpp/module_metadata.h"
namespace thrift {
namespace py3 {



template<>
inline void reset_field<::py3::simple::SimpleException>(
    ::py3::simple::SimpleException& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.err_code_ref().copy_from(default_inst<::py3::simple::SimpleException>().err_code_ref());
      return;
  }
}

template<>
inline void reset_field<::py3::simple::OptionalRefStruct>(
    ::py3::simple::OptionalRefStruct& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.optional_blob_ref()->reset();
      return;
  }
}

template<>
inline void reset_field<::py3::simple::SimpleStruct>(
    ::py3::simple::SimpleStruct& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.is_on_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().is_on_ref());
      return;
    case 1:
      obj.tiny_int_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().tiny_int_ref());
      return;
    case 2:
      obj.small_int_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().small_int_ref());
      return;
    case 3:
      obj.nice_sized_int_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().nice_sized_int_ref());
      return;
    case 4:
      obj.big_int_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().big_int_ref());
      return;
    case 5:
      obj.real_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().real_ref());
      return;
    case 6:
      obj.smaller_real_ref().copy_from(default_inst<::py3::simple::SimpleStruct>().smaller_real_ref());
      return;
  }
}

template<>
inline void reset_field<::py3::simple::HiddenTypeFieldsStruct>(
    ::py3::simple::HiddenTypeFieldsStruct& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::py3::simple::ComplexStruct>(
    ::py3::simple::ComplexStruct& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.structOne_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().structOne_ref());
      return;
    case 1:
      obj.structTwo_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().structTwo_ref());
      return;
    case 2:
      obj.an_integer_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().an_integer_ref());
      return;
    case 3:
      obj.name_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().name_ref());
      return;
    case 4:
      obj.an_enum_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().an_enum_ref());
      return;
    case 5:
      obj.some_bytes_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().some_bytes_ref());
      return;
    case 6:
      obj.from_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().from_ref());
      return;
    case 7:
      obj.cdef_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().cdef_ref());
      return;
    case 8:
      obj.bytes_with_cpp_type_ref().copy_from(default_inst<::py3::simple::ComplexStruct>().bytes_with_cpp_type_ref());
      return;
  }
}

template<>
inline void reset_field<::py3::simple::BinaryUnionStruct>(
    ::py3::simple::BinaryUnionStruct& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.u_ref().copy_from(default_inst<::py3::simple::BinaryUnionStruct>().u_ref());
      return;
  }
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::SimpleException>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::OptionalRefStruct>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::SimpleStruct>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::HiddenTypeFieldsStruct>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::ComplexStruct>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
      {"from", "sender"},
      {"cdef", "cdef_"},
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::BinaryUnion>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::py3::simple::BinaryUnionStruct>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}
} // namespace py3
} // namespace thrift
