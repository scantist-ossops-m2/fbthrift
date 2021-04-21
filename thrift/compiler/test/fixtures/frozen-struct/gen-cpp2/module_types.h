/**
 * Autogenerated by Thrift for src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#pragma once

#include <thrift/lib/cpp2/gen/module_types_h.h>


#include "thrift/compiler/test/fixtures/frozen-struct/gen-cpp2/include1_types.h"
#include "thrift/compiler/test/fixtures/frozen-struct/gen-cpp2/include2_types.h"

namespace apache {
namespace thrift {
namespace tag {
struct i32Field;
struct strField;
struct listField;
struct mapField;
struct inclAField;
struct inclBField;
struct i32Field;
struct inclEnumB;
} // namespace tag
namespace detail {
#ifndef APACHE_THRIFT_ACCESSOR_i32Field
#define APACHE_THRIFT_ACCESSOR_i32Field
APACHE_THRIFT_DEFINE_ACCESSOR(i32Field);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_strField
#define APACHE_THRIFT_ACCESSOR_strField
APACHE_THRIFT_DEFINE_ACCESSOR(strField);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_listField
#define APACHE_THRIFT_ACCESSOR_listField
APACHE_THRIFT_DEFINE_ACCESSOR(listField);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_mapField
#define APACHE_THRIFT_ACCESSOR_mapField
APACHE_THRIFT_DEFINE_ACCESSOR(mapField);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_inclAField
#define APACHE_THRIFT_ACCESSOR_inclAField
APACHE_THRIFT_DEFINE_ACCESSOR(inclAField);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_inclBField
#define APACHE_THRIFT_ACCESSOR_inclBField
APACHE_THRIFT_DEFINE_ACCESSOR(inclBField);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_i32Field
#define APACHE_THRIFT_ACCESSOR_i32Field
APACHE_THRIFT_DEFINE_ACCESSOR(i32Field);
#endif
#ifndef APACHE_THRIFT_ACCESSOR_inclEnumB
#define APACHE_THRIFT_ACCESSOR_inclEnumB
APACHE_THRIFT_DEFINE_ACCESSOR(inclEnumB);
#endif
} // namespace detail
} // namespace thrift
} // namespace apache

// BEGIN declare_enums
namespace some { namespace ns {

enum class EnumB {
  EMPTY = 1,
};




}} // some::ns

namespace std {
template<> struct hash<::some::ns::EnumB> :
  ::apache::thrift::detail::enum_hash<::some::ns::EnumB> {};
} // std

namespace apache { namespace thrift {


template <> struct TEnumDataStorage<::some::ns::EnumB>;

template <> struct TEnumTraits<::some::ns::EnumB> {
  using type = ::some::ns::EnumB;

  static constexpr std::size_t const size = 1;
  static folly::Range<type const*> const values;
  static folly::Range<folly::StringPiece const*> const names;

  static char const* findName(type value);
  static bool findValue(char const* name, type* out);

  static constexpr type min() { return type::EMPTY; }
  static constexpr type max() { return type::EMPTY; }
};


}} // apache::thrift

namespace some { namespace ns {

using _EnumB_EnumMapFactory = apache::thrift::detail::TEnumMapFactory<EnumB>;
[[deprecated("use apache::thrift::util::enumNameSafe, apache::thrift::util::enumName, or apache::thrift::TEnumTraits")]]
extern const _EnumB_EnumMapFactory::ValuesToNamesMapType _EnumB_VALUES_TO_NAMES;
[[deprecated("use apache::thrift::TEnumTraits")]]
extern const _EnumB_EnumMapFactory::NamesToValuesMapType _EnumB_NAMES_TO_VALUES;

}} // some::ns

// END declare_enums
// BEGIN forward_declare
namespace some { namespace ns {
class ModuleA;
class ModuleB;
}} // some::ns
// END forward_declare
// BEGIN typedefs

// END typedefs
// BEGIN hash_and_equal_to
// END hash_and_equal_to
THRIFT_IGNORE_ISSET_USE_WARNING_BEGIN
namespace some { namespace ns {
#ifndef SWIG
using ::apache::thrift::detail::operator!=;
using ::apache::thrift::detail::operator>;
using ::apache::thrift::detail::operator<=;
using ::apache::thrift::detail::operator>=;
#endif

class ModuleA final  {
 private:
  friend struct ::apache::thrift::detail::st::struct_private_access;

  //  used by a static_assert in the corresponding source
  static constexpr bool __fbthrift_cpp2_gen_json = false;
  static constexpr bool __fbthrift_cpp2_gen_nimble = false;
  static constexpr bool __fbthrift_cpp2_gen_has_thrift_uri = false;

 public:
  using __fbthrift_cpp2_type = ModuleA;
  static constexpr bool __fbthrift_cpp2_is_union =
    false;


 public:

  ModuleA();

  // FragileConstructor for use in initialization lists only.
  [[deprecated("This constructor is deprecated")]]
  ModuleA(apache::thrift::FragileConstructor, ::std::int32_t i32Field__arg, ::std::string strField__arg, ::std::vector<::std::int16_t> listField__arg, ::std::map<::std::string, ::std::int32_t> mapField__arg, ::some::ns::IncludedA inclAField__arg, ::some::ns::IncludedB inclBField__arg);

  ModuleA(ModuleA&&) noexcept;

  ModuleA(const ModuleA&) = default;


  ModuleA& operator=(ModuleA&&) noexcept;

  ModuleA& operator=(const ModuleA&) = default;
  void __clear();

  ~ModuleA();

 private:
  ::std::int32_t i32Field;
 private:
  ::std::string strField;
 private:
  ::std::vector<::std::int16_t> listField;
 private:
  ::std::map<::std::string, ::std::int32_t> mapField;
 private:
  ::some::ns::IncludedA inclAField;
 private:
  ::some::ns::IncludedB inclBField;

 public:
  [[deprecated("__isset field is deprecated in Thrift struct. Use _ref() accessors instead.")]]
  struct __isset {
    bool i32Field;
    bool strField;
    bool listField;
    bool mapField;
    bool inclAField;
    bool inclBField;
  } __isset = {};

  bool operator==(const ModuleA&) const;
  bool operator<(const ModuleA&) const;

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> i32Field_ref() const& {
    return {this->i32Field, __isset.i32Field};
  }

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> i32Field_ref() const&& {
    return {std::move(this->i32Field), __isset.i32Field};
  }

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> i32Field_ref() & {
    return {this->i32Field, __isset.i32Field};
  }

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> i32Field_ref() && {
    return {std::move(this->i32Field), __isset.i32Field};
  }

  template <typename..., typename T = ::std::string>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> strField_ref() const& {
    return {this->strField, __isset.strField};
  }

  template <typename..., typename T = ::std::string>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> strField_ref() const&& {
    return {std::move(this->strField), __isset.strField};
  }

  template <typename..., typename T = ::std::string>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> strField_ref() & {
    return {this->strField, __isset.strField};
  }

  template <typename..., typename T = ::std::string>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> strField_ref() && {
    return {std::move(this->strField), __isset.strField};
  }

  template <typename..., typename T = ::std::vector<::std::int16_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> listField_ref() const& {
    return {this->listField, __isset.listField};
  }

  template <typename..., typename T = ::std::vector<::std::int16_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> listField_ref() const&& {
    return {std::move(this->listField), __isset.listField};
  }

  template <typename..., typename T = ::std::vector<::std::int16_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> listField_ref() & {
    return {this->listField, __isset.listField};
  }

  template <typename..., typename T = ::std::vector<::std::int16_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> listField_ref() && {
    return {std::move(this->listField), __isset.listField};
  }

  template <typename..., typename T = ::std::map<::std::string, ::std::int32_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> mapField_ref() const& {
    return {this->mapField, __isset.mapField};
  }

  template <typename..., typename T = ::std::map<::std::string, ::std::int32_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> mapField_ref() const&& {
    return {std::move(this->mapField), __isset.mapField};
  }

  template <typename..., typename T = ::std::map<::std::string, ::std::int32_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> mapField_ref() & {
    return {this->mapField, __isset.mapField};
  }

  template <typename..., typename T = ::std::map<::std::string, ::std::int32_t>>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> mapField_ref() && {
    return {std::move(this->mapField), __isset.mapField};
  }

  template <typename..., typename T = ::some::ns::IncludedA>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> inclAField_ref() const& {
    return {this->inclAField, __isset.inclAField};
  }

  template <typename..., typename T = ::some::ns::IncludedA>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> inclAField_ref() const&& {
    return {std::move(this->inclAField), __isset.inclAField};
  }

  template <typename..., typename T = ::some::ns::IncludedA>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> inclAField_ref() & {
    return {this->inclAField, __isset.inclAField};
  }

  template <typename..., typename T = ::some::ns::IncludedA>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> inclAField_ref() && {
    return {std::move(this->inclAField), __isset.inclAField};
  }

  template <typename..., typename T = ::some::ns::IncludedB>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> inclBField_ref() const& {
    return {this->inclBField, __isset.inclBField};
  }

  template <typename..., typename T = ::some::ns::IncludedB>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> inclBField_ref() const&& {
    return {std::move(this->inclBField), __isset.inclBField};
  }

  template <typename..., typename T = ::some::ns::IncludedB>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> inclBField_ref() & {
    return {this->inclBField, __isset.inclBField};
  }

  template <typename..., typename T = ::some::ns::IncludedB>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> inclBField_ref() && {
    return {std::move(this->inclBField), __isset.inclBField};
  }

  ::std::int32_t get_i32Field() const {
    return i32Field;
  }

  ::std::int32_t& set_i32Field(::std::int32_t i32Field_) {
    i32Field = i32Field_;
    __isset.i32Field = true;
    return i32Field;
  }

  const ::std::string& get_strField() const& {
    return strField;
  }

  ::std::string get_strField() && {
    return std::move(strField);
  }

  template <typename T_ModuleA_strField_struct_setter = ::std::string>
  ::std::string& set_strField(T_ModuleA_strField_struct_setter&& strField_) {
    strField = std::forward<T_ModuleA_strField_struct_setter>(strField_);
    __isset.strField = true;
    return strField;
  }
  const ::std::vector<::std::int16_t>& get_listField() const&;
  ::std::vector<::std::int16_t> get_listField() &&;

  template <typename T_ModuleA_listField_struct_setter = ::std::vector<::std::int16_t>>
  ::std::vector<::std::int16_t>& set_listField(T_ModuleA_listField_struct_setter&& listField_) {
    listField = std::forward<T_ModuleA_listField_struct_setter>(listField_);
    __isset.listField = true;
    return listField;
  }
  const ::std::map<::std::string, ::std::int32_t>& get_mapField() const&;
  ::std::map<::std::string, ::std::int32_t> get_mapField() &&;

  template <typename T_ModuleA_mapField_struct_setter = ::std::map<::std::string, ::std::int32_t>>
  ::std::map<::std::string, ::std::int32_t>& set_mapField(T_ModuleA_mapField_struct_setter&& mapField_) {
    mapField = std::forward<T_ModuleA_mapField_struct_setter>(mapField_);
    __isset.mapField = true;
    return mapField;
  }
  const ::some::ns::IncludedA& get_inclAField() const&;
  ::some::ns::IncludedA get_inclAField() &&;

  template <typename T_ModuleA_inclAField_struct_setter = ::some::ns::IncludedA>
  ::some::ns::IncludedA& set_inclAField(T_ModuleA_inclAField_struct_setter&& inclAField_) {
    inclAField = std::forward<T_ModuleA_inclAField_struct_setter>(inclAField_);
    __isset.inclAField = true;
    return inclAField;
  }
  const ::some::ns::IncludedB& get_inclBField() const&;
  ::some::ns::IncludedB get_inclBField() &&;

  template <typename T_ModuleA_inclBField_struct_setter = ::some::ns::IncludedB>
  ::some::ns::IncludedB& set_inclBField(T_ModuleA_inclBField_struct_setter&& inclBField_) {
    inclBField = std::forward<T_ModuleA_inclBField_struct_setter>(inclBField_);
    __isset.inclBField = true;
    return inclBField;
  }

  template <class Protocol_>
  uint32_t read(Protocol_* iprot);
  template <class Protocol_>
  uint32_t serializedSize(Protocol_ const* prot_) const;
  template <class Protocol_>
  uint32_t serializedSizeZC(Protocol_ const* prot_) const;
  template <class Protocol_>
  uint32_t write(Protocol_* prot_) const;

 private:
  template <class Protocol_>
  void readNoXfer(Protocol_* iprot);

  friend class ::apache::thrift::Cpp2Ops<ModuleA>;
  friend void swap(ModuleA& a, ModuleA& b);
};

template <class Protocol_>
uint32_t ModuleA::read(Protocol_* iprot) {
  auto _xferStart = iprot->getCursorPosition();
  readNoXfer(iprot);
  return iprot->getCursorPosition() - _xferStart;
}

}} // some::ns
namespace some { namespace ns {
#ifndef SWIG
using ::apache::thrift::detail::operator!=;
using ::apache::thrift::detail::operator>;
using ::apache::thrift::detail::operator<=;
using ::apache::thrift::detail::operator>=;
#endif

class ModuleB final  {
 private:
  friend struct ::apache::thrift::detail::st::struct_private_access;

  //  used by a static_assert in the corresponding source
  static constexpr bool __fbthrift_cpp2_gen_json = false;
  static constexpr bool __fbthrift_cpp2_gen_nimble = false;
  static constexpr bool __fbthrift_cpp2_gen_has_thrift_uri = false;

 public:
  using __fbthrift_cpp2_type = ModuleB;
  static constexpr bool __fbthrift_cpp2_is_union =
    false;


 public:

  ModuleB() :
      i32Field(0),
      inclEnumB(static_cast< ::some::ns::EnumB>(0)) {}
  // FragileConstructor for use in initialization lists only.
  [[deprecated("This constructor is deprecated")]]
  ModuleB(apache::thrift::FragileConstructor, ::std::int32_t i32Field__arg, ::some::ns::EnumB inclEnumB__arg);

  ModuleB(ModuleB&&) = default;

  ModuleB(const ModuleB&) = default;


  ModuleB& operator=(ModuleB&&) = default;

  ModuleB& operator=(const ModuleB&) = default;
  void __clear();
 private:
  ::std::int32_t i32Field;
 private:
  ::some::ns::EnumB inclEnumB;

 public:
  [[deprecated("__isset field is deprecated in Thrift struct. Use _ref() accessors instead.")]]
  struct __isset {
    bool i32Field;
    bool inclEnumB;
  } __isset = {};

  bool operator==(const ModuleB&) const;
  bool operator<(const ModuleB&) const;

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> i32Field_ref() const& {
    return {this->i32Field, __isset.i32Field};
  }

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> i32Field_ref() const&& {
    return {std::move(this->i32Field), __isset.i32Field};
  }

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> i32Field_ref() & {
    return {this->i32Field, __isset.i32Field};
  }

  template <typename..., typename T = ::std::int32_t>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> i32Field_ref() && {
    return {std::move(this->i32Field), __isset.i32Field};
  }

  template <typename..., typename T = ::some::ns::EnumB>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&> inclEnumB_ref() const& {
    return {this->inclEnumB, __isset.inclEnumB};
  }

  template <typename..., typename T = ::some::ns::EnumB>
  FOLLY_ERASE ::apache::thrift::field_ref<const T&&> inclEnumB_ref() const&& {
    return {std::move(this->inclEnumB), __isset.inclEnumB};
  }

  template <typename..., typename T = ::some::ns::EnumB>
  FOLLY_ERASE ::apache::thrift::field_ref<T&> inclEnumB_ref() & {
    return {this->inclEnumB, __isset.inclEnumB};
  }

  template <typename..., typename T = ::some::ns::EnumB>
  FOLLY_ERASE ::apache::thrift::field_ref<T&&> inclEnumB_ref() && {
    return {std::move(this->inclEnumB), __isset.inclEnumB};
  }

  ::std::int32_t get_i32Field() const {
    return i32Field;
  }

  ::std::int32_t& set_i32Field(::std::int32_t i32Field_) {
    i32Field = i32Field_;
    __isset.i32Field = true;
    return i32Field;
  }

  ::some::ns::EnumB get_inclEnumB() const {
    return inclEnumB;
  }

  ::some::ns::EnumB& set_inclEnumB(::some::ns::EnumB inclEnumB_) {
    inclEnumB = inclEnumB_;
    __isset.inclEnumB = true;
    return inclEnumB;
  }

  template <class Protocol_>
  uint32_t read(Protocol_* iprot);
  template <class Protocol_>
  uint32_t serializedSize(Protocol_ const* prot_) const;
  template <class Protocol_>
  uint32_t serializedSizeZC(Protocol_ const* prot_) const;
  template <class Protocol_>
  uint32_t write(Protocol_* prot_) const;

 private:
  template <class Protocol_>
  void readNoXfer(Protocol_* iprot);

  friend class ::apache::thrift::Cpp2Ops<ModuleB>;
  friend void swap(ModuleB& a, ModuleB& b);
};

template <class Protocol_>
uint32_t ModuleB::read(Protocol_* iprot) {
  auto _xferStart = iprot->getCursorPosition();
  readNoXfer(iprot);
  return iprot->getCursorPosition() - _xferStart;
}

}} // some::ns
THRIFT_IGNORE_ISSET_USE_WARNING_END
