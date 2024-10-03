/**
 * Autogenerated by Thrift for thrift/annotation/cpp.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#pragma once

#include <functional>
#include <folly/Range.h>

#include "thrift/compiler/test/fixtures/mcpp2-compare/gen-cpp2/cpp_data.h"
#include "thrift/compiler/test/fixtures/mcpp2-compare/gen-cpp2/cpp_types.h"
#include "thrift/compiler/test/fixtures/mcpp2-compare/gen-cpp2/cpp_metadata.h"
namespace thrift {
namespace py3 {



template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Name>(
    ::facebook::thrift::annotation::cpp::Name& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.value_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Name>().value_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Type>(
    ::facebook::thrift::annotation::cpp::Type& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.name_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Type>().name_ref());
      return;
    case 1:
      obj.template__ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Type>().template__ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Ref>(
    ::facebook::thrift::annotation::cpp::Ref& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.type_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Ref>().type_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Lazy>(
    ::facebook::thrift::annotation::cpp::Lazy& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.ref_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Lazy>().ref_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::DisableLazyChecksum>(
    ::facebook::thrift::annotation::cpp::DisableLazyChecksum& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Adapter>(
    ::facebook::thrift::annotation::cpp::Adapter& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.name_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Adapter>().name_ref());
      return;
    case 1:
      obj.adaptedType_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Adapter>().adaptedType_ref());
      return;
    case 2:
      obj.underlyingName_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Adapter>().underlyingName_ref());
      return;
    case 3:
      obj.extraNamespace_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Adapter>().extraNamespace_ref());
      return;
    case 4:
      obj.moveOnly_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::Adapter>().moveOnly_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::PackIsset>(
    ::facebook::thrift::annotation::cpp::PackIsset& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.atomic_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::PackIsset>().atomic_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::MinimizePadding>(
    ::facebook::thrift::annotation::cpp::MinimizePadding& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::ScopedEnumAsUnionType>(
    ::facebook::thrift::annotation::cpp::ScopedEnumAsUnionType& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::FieldInterceptor>(
    ::facebook::thrift::annotation::cpp::FieldInterceptor& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.name_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::FieldInterceptor>().name_ref());
      return;
    case 1:
      obj.noinline_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::FieldInterceptor>().noinline_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::UseOpEncode>(
    ::facebook::thrift::annotation::cpp::UseOpEncode& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::EnumType>(
    ::facebook::thrift::annotation::cpp::EnumType& obj, uint16_t index) {
  switch (index) {
    case 0:
      obj.type_ref().copy_from(default_inst<::facebook::thrift::annotation::cpp::EnumType>().type_ref());
      return;
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Frozen2Exclude>(
    ::facebook::thrift::annotation::cpp::Frozen2Exclude& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::Frozen2RequiresCompleteContainerParams>(
    ::facebook::thrift::annotation::cpp::Frozen2RequiresCompleteContainerParams& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::ProcessInEbThreadUnsafe>(
    ::facebook::thrift::annotation::cpp::ProcessInEbThreadUnsafe& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::RuntimeAnnotation>(
    ::facebook::thrift::annotation::cpp::RuntimeAnnotation& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::UseCursorSerialization>(
    ::facebook::thrift::annotation::cpp::UseCursorSerialization& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline void reset_field<::facebook::thrift::annotation::cpp::GenerateDeprecatedHeaderClientMethods>(
    ::facebook::thrift::annotation::cpp::GenerateDeprecatedHeaderClientMethods& obj, uint16_t index) {
  switch (index) {
  }
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Name>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Type>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Ref>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Lazy>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::DisableLazyChecksum>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Adapter>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::PackIsset>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::MinimizePadding>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::ScopedEnumAsUnionType>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::FieldInterceptor>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::UseOpEncode>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::EnumType>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Frozen2Exclude>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::Frozen2RequiresCompleteContainerParams>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::ProcessInEbThreadUnsafe>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::RuntimeAnnotation>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::UseCursorSerialization>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}

template<>
inline const std::unordered_map<std::string_view, std::string_view>& PyStructTraits<
    ::facebook::thrift::annotation::cpp::GenerateDeprecatedHeaderClientMethods>::namesmap() {
  static const folly::Indestructible<NamesMap> map {
    {
    }
  };
  return *map;
}
} // namespace py3
} // namespace thrift
