/**
 * Autogenerated by Thrift for src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#include "thrift/compiler/test/fixtures/encode/gen-cpp2/module_types.h"
#include "thrift/compiler/test/fixtures/encode/gen-cpp2/module_types.tcc"

#include <thrift/lib/cpp2/gen/module_types_cpp.h>

#include "thrift/compiler/test/fixtures/encode/gen-cpp2/module_data.h"


namespace apache { namespace thrift {

constexpr std::size_t const TEnumTraits<::facebook::thrift::test::Enum>::size;
folly::Range<::facebook::thrift::test::Enum const*> const TEnumTraits<::facebook::thrift::test::Enum>::values = folly::range(TEnumDataStorage<::facebook::thrift::test::Enum>::values);
folly::Range<folly::StringPiece const*> const TEnumTraits<::facebook::thrift::test::Enum>::names = folly::range(TEnumDataStorage<::facebook::thrift::test::Enum>::names);

bool TEnumTraits<::facebook::thrift::test::Enum>::findName(type value, folly::StringPiece* out) noexcept {
  return ::apache::thrift::detail::st::enum_find_name(value, out);
}

bool TEnumTraits<::facebook::thrift::test::Enum>::findValue(folly::StringPiece name, type* out) noexcept {
  return ::apache::thrift::detail::st::enum_find_value(name, out);
}

}} // apache::thrift

namespace facebook { namespace thrift { namespace test {
#ifndef ANDROID
FOLLY_PUSH_WARNING
FOLLY_GNU_DISABLE_WARNING("-Wdeprecated-declarations")
const _Enum_EnumMapFactory::ValuesToNamesMapType _Enum_VALUES_TO_NAMES = _Enum_EnumMapFactory::makeValuesToNamesMap();
const _Enum_EnumMapFactory::NamesToValuesMapType _Enum_NAMES_TO_VALUES = _Enum_EnumMapFactory::makeNamesToValuesMap();
FOLLY_POP_WARNING
#endif
}}} // facebook::thrift::test

namespace apache {
namespace thrift {
namespace detail {

void TccStructTraits<::facebook::thrift::test::Foo>::translateFieldName(
    folly::StringPiece _fname,
    int16_t& fid,
    apache::thrift::protocol::TType& _ftype) noexcept {
  using data = apache::thrift::TStructDataStorage<::facebook::thrift::test::Foo>;
  static const st::translate_field_name_table table{
      data::fields_size,
      data::fields_names.data(),
      data::fields_ids.data(),
      data::fields_types.data()};
  st::translate_field_name(_fname, fid, _ftype, table);
}

} // namespace detail
} // namespace thrift
} // namespace apache

namespace facebook { namespace thrift { namespace test {

const char* Foo::__fbthrift_thrift_uri() {
  return "facebook.com/thrift/test/Foo";
}

const folly::StringPiece Foo::__fbthrift_get_field_name(::apache::thrift::FieldOrdinal ord) {
  if (ord == ::apache::thrift::FieldOrdinal{0}) { return {}; }
  return apache::thrift::TStructDataStorage<Foo>::fields_names[folly::to_underlying(ord) - 1];
}


Foo::Foo(apache::thrift::FragileConstructor, ::std::int32_t field__arg) :
    __fbthrift_field_field(std::move(field__arg)) {
  __isset.set(folly::index_constant<0>(), true);
}


void Foo::__fbthrift_clear() {
  // clear all fields
  this->__fbthrift_field_field = ::std::int32_t();
  __isset = {};
}

void Foo::__fbthrift_clear_terse_fields() {
}

bool Foo::__fbthrift_is_empty() const {
  return false;
}

bool Foo::operator==(FOLLY_MAYBE_UNUSED const Foo& rhs) const {
  FOLLY_MAYBE_UNUSED auto& lhs = *this;
  if (!(lhs.field_ref() == rhs.field_ref())) {
    return false;
  }
  return true;
}

bool Foo::operator<(FOLLY_MAYBE_UNUSED const Foo& rhs) const {
  FOLLY_MAYBE_UNUSED auto& lhs = *this;
  if (!(lhs.field_ref() == rhs.field_ref())) {
    return lhs.field_ref() < rhs.field_ref();
  }
  return false;
}


void swap(FOLLY_MAYBE_UNUSED Foo& a, FOLLY_MAYBE_UNUSED Foo& b) {
  using ::std::swap;
  swap(a.__fbthrift_field_field, b.__fbthrift_field_field);
  swap(a.__isset, b.__isset);
}

template void Foo::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
template uint32_t Foo::write<>(apache::thrift::BinaryProtocolWriter*) const;
template uint32_t Foo::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
template uint32_t Foo::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
template void Foo::readNoXfer<>(apache::thrift::CompactProtocolReader*);
template uint32_t Foo::write<>(apache::thrift::CompactProtocolWriter*) const;
template uint32_t Foo::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
template uint32_t Foo::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;


}}} // facebook::thrift::test

namespace apache {
namespace thrift {
namespace detail {

void TccStructTraits<::facebook::thrift::test::Bar>::translateFieldName(
    folly::StringPiece _fname,
    int16_t& fid,
    apache::thrift::protocol::TType& _ftype) noexcept {
  using data = apache::thrift::TStructDataStorage<::facebook::thrift::test::Bar>;
  static const st::translate_field_name_table table{
      data::fields_size,
      data::fields_names.data(),
      data::fields_ids.data(),
      data::fields_types.data()};
  st::translate_field_name(_fname, fid, _ftype, table);
}

} // namespace detail
} // namespace thrift
} // namespace apache

namespace facebook { namespace thrift { namespace test {

const char* Bar::__fbthrift_thrift_uri() {
  return "facebook.com/thrift/test/Bar";
}

const folly::StringPiece Bar::__fbthrift_get_field_name(::apache::thrift::FieldOrdinal ord) {
  if (ord == ::apache::thrift::FieldOrdinal{0}) { return {}; }
  return apache::thrift::TStructDataStorage<Bar>::fields_names[folly::to_underlying(ord) - 1];
}

Bar::Bar(const Bar&) = default;
Bar& Bar::operator=(const Bar&) = default;
Bar::Bar(FOLLY_MAYBE_UNUSED Bar&& other) noexcept :
    __fbthrift_field_list_field(std::move(other.__fbthrift_field_list_field)),
    __isset(other.__isset) {
}

Bar& Bar::operator=(FOLLY_MAYBE_UNUSED Bar&& other) noexcept {
    this->__fbthrift_field_list_field = std::move(other.__fbthrift_field_list_field);
    __isset = other.__isset;
    return *this;
}


Bar::Bar(apache::thrift::FragileConstructor, ::std::vector<::facebook::thrift::test::AdaptedFoo> list_field__arg) :
    __fbthrift_field_list_field(std::move(list_field__arg)) {
  __isset.set(folly::index_constant<0>(), true);
}


void Bar::__fbthrift_clear() {
  // clear all fields
  this->__fbthrift_field_list_field.clear();
  __isset = {};
}

void Bar::__fbthrift_clear_terse_fields() {
}

bool Bar::__fbthrift_is_empty() const {
  return false;
}

bool Bar::operator==(FOLLY_MAYBE_UNUSED const Bar& rhs) const {
  FOLLY_MAYBE_UNUSED auto& lhs = *this;
  if (!(lhs.list_field_ref() == rhs.list_field_ref())) {
    return false;
  }
  return true;
}

bool Bar::operator<(FOLLY_MAYBE_UNUSED const Bar& rhs) const {
  FOLLY_MAYBE_UNUSED auto& lhs = *this;
  if (!(lhs.list_field_ref() == rhs.list_field_ref())) {
    return lhs.list_field_ref() < rhs.list_field_ref();
  }
  return false;
}

const ::std::vector<::facebook::thrift::test::AdaptedFoo>& Bar::get_list_field() const& {
  return __fbthrift_field_list_field;
}

::std::vector<::facebook::thrift::test::AdaptedFoo> Bar::get_list_field() && {
  return std::move(__fbthrift_field_list_field);
}


void swap(FOLLY_MAYBE_UNUSED Bar& a, FOLLY_MAYBE_UNUSED Bar& b) {
  using ::std::swap;
  swap(a.__fbthrift_field_list_field, b.__fbthrift_field_list_field);
  swap(a.__isset, b.__isset);
}

template void Bar::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
template uint32_t Bar::write<>(apache::thrift::BinaryProtocolWriter*) const;
template uint32_t Bar::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
template uint32_t Bar::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
template void Bar::readNoXfer<>(apache::thrift::CompactProtocolReader*);
template uint32_t Bar::write<>(apache::thrift::CompactProtocolWriter*) const;
template uint32_t Bar::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
template uint32_t Bar::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;


}}} // facebook::thrift::test

namespace apache {
namespace thrift {
namespace detail {

void TccStructTraits<::facebook::thrift::test::OpEncodeStruct>::translateFieldName(
    folly::StringPiece _fname,
    int16_t& fid,
    apache::thrift::protocol::TType& _ftype) noexcept {
  using data = apache::thrift::TStructDataStorage<::facebook::thrift::test::OpEncodeStruct>;
  static const st::translate_field_name_table table{
      data::fields_size,
      data::fields_names.data(),
      data::fields_ids.data(),
      data::fields_types.data()};
  st::translate_field_name(_fname, fid, _ftype, table);
}

} // namespace detail
} // namespace thrift
} // namespace apache

namespace facebook { namespace thrift { namespace test {

const char* OpEncodeStruct::__fbthrift_thrift_uri() {
  return "facebook.com/thrift/test/OpEncodeStruct";
}

const folly::StringPiece OpEncodeStruct::__fbthrift_get_field_name(::apache::thrift::FieldOrdinal ord) {
  if (ord == ::apache::thrift::FieldOrdinal{0}) { return {}; }
  return apache::thrift::TStructDataStorage<OpEncodeStruct>::fields_names[folly::to_underlying(ord) - 1];
}

OpEncodeStruct::OpEncodeStruct(const OpEncodeStruct& srcObj) :
    __fbthrift_field_int_field(srcObj.__fbthrift_field_int_field),
    __fbthrift_field_enum_field(srcObj.__fbthrift_field_enum_field),
    __fbthrift_field_foo_field(srcObj.__fbthrift_field_foo_field),
    __fbthrift_field_adapted_field(srcObj.__fbthrift_field_adapted_field),
    __fbthrift_field_list_field(srcObj.__fbthrift_field_list_field),
    __fbthrift_field_list_shared_ptr_field(srcObj.__fbthrift_field_list_shared_ptr_field),
    __fbthrift_field_list_cpp_type_field(srcObj.__fbthrift_field_list_cpp_type_field),
    __fbthrift_field_set_field(srcObj.__fbthrift_field_set_field),
    __fbthrift_field_map_field(srcObj.__fbthrift_field_map_field),
    __fbthrift_field_nested_field(srcObj.__fbthrift_field_nested_field),
    __fbthrift_field_bar_field(srcObj.__fbthrift_field_bar_field),
    __fbthrift_field_adapted_list_field(srcObj.__fbthrift_field_adapted_list_field),
    __isset(srcObj.__isset) {
  ::apache::thrift::adapt_detail::construct<::apache::thrift::test::TemplatedTestAdapter, 4>(__fbthrift_field_adapted_field, *this);
  ::apache::thrift::adapt_detail::construct<::FieldAdapter, 12>(__fbthrift_field_adapted_list_field, *this);
}

OpEncodeStruct& OpEncodeStruct::operator=(const OpEncodeStruct& other) {
  OpEncodeStruct tmp(other);
  swap(*this, tmp);
  return *this;
}

OpEncodeStruct::OpEncodeStruct() :
      __fbthrift_field_int_field(),
      __fbthrift_field_enum_field() {
  ::apache::thrift::adapt_detail::construct<::apache::thrift::test::TemplatedTestAdapter, 4>(__fbthrift_field_adapted_field, *this);
  ::apache::thrift::adapt_detail::construct<::FieldAdapter, 12>(__fbthrift_field_adapted_list_field, *this);
}


OpEncodeStruct::~OpEncodeStruct() {}

OpEncodeStruct::OpEncodeStruct(FOLLY_MAYBE_UNUSED OpEncodeStruct&& other) noexcept :
    __fbthrift_field_int_field(std::move(other.__fbthrift_field_int_field)),
    __fbthrift_field_enum_field(std::move(other.__fbthrift_field_enum_field)),
    __fbthrift_field_foo_field(std::move(other.__fbthrift_field_foo_field)),
    __fbthrift_field_adapted_field(std::move(other.__fbthrift_field_adapted_field)),
    __fbthrift_field_list_field(std::move(other.__fbthrift_field_list_field)),
    __fbthrift_field_list_shared_ptr_field(std::move(other.__fbthrift_field_list_shared_ptr_field)),
    __fbthrift_field_list_cpp_type_field(std::move(other.__fbthrift_field_list_cpp_type_field)),
    __fbthrift_field_set_field(std::move(other.__fbthrift_field_set_field)),
    __fbthrift_field_map_field(std::move(other.__fbthrift_field_map_field)),
    __fbthrift_field_nested_field(std::move(other.__fbthrift_field_nested_field)),
    __fbthrift_field_bar_field(std::move(other.__fbthrift_field_bar_field)),
    __fbthrift_field_adapted_list_field(std::move(other.__fbthrift_field_adapted_list_field)),
    __isset(other.__isset) {
  ::apache::thrift::adapt_detail::construct<::apache::thrift::test::TemplatedTestAdapter, 4>(__fbthrift_field_adapted_field, *this);
  ::apache::thrift::adapt_detail::construct<::FieldAdapter, 12>(__fbthrift_field_adapted_list_field, *this);
}

OpEncodeStruct& OpEncodeStruct::operator=(FOLLY_MAYBE_UNUSED OpEncodeStruct&& other) noexcept {
    this->__fbthrift_field_int_field = std::move(other.__fbthrift_field_int_field);
    this->__fbthrift_field_enum_field = std::move(other.__fbthrift_field_enum_field);
    this->__fbthrift_field_foo_field = std::move(other.__fbthrift_field_foo_field);
    this->__fbthrift_field_adapted_field = std::move(other.__fbthrift_field_adapted_field);
    this->__fbthrift_field_list_field = std::move(other.__fbthrift_field_list_field);
    this->__fbthrift_field_list_shared_ptr_field = std::move(other.__fbthrift_field_list_shared_ptr_field);
    this->__fbthrift_field_list_cpp_type_field = std::move(other.__fbthrift_field_list_cpp_type_field);
    this->__fbthrift_field_set_field = std::move(other.__fbthrift_field_set_field);
    this->__fbthrift_field_map_field = std::move(other.__fbthrift_field_map_field);
    this->__fbthrift_field_nested_field = std::move(other.__fbthrift_field_nested_field);
    this->__fbthrift_field_bar_field = std::move(other.__fbthrift_field_bar_field);
    this->__fbthrift_field_adapted_list_field = std::move(other.__fbthrift_field_adapted_list_field);
    __isset = other.__isset;
    return *this;
}


OpEncodeStruct::OpEncodeStruct(apache::thrift::FragileConstructor, ::std::int32_t int_field__arg, ::facebook::thrift::test::Enum enum_field__arg, ::facebook::thrift::test::Foo foo_field__arg, ::facebook::thrift::test::AdaptedFoo adapted_field__arg, ::std::vector<::facebook::thrift::test::AdaptedFoo> list_field__arg, ::std::shared_ptr<const ::std::vector<::facebook::thrift::test::AdaptedFoo>> list_shared_ptr_field__arg, ::std::vector<::facebook::thrift::test::AdaptedFoo> list_cpp_type_field__arg, ::std::set<::facebook::thrift::test::AdaptedFoo> set_field__arg, ::std::map<::facebook::thrift::test::AdaptedFoo, ::facebook::thrift::test::AdaptedFoo> map_field__arg, ::std::map<::std::int32_t, ::std::vector<::facebook::thrift::test::AdaptedFoo>> nested_field__arg, ::facebook::thrift::test::Bar bar_field__arg, ::apache::thrift::adapt_detail::adapted_field_t<::FieldAdapter, 12, ::std::vector<::facebook::thrift::test::AdaptedFoo>, OpEncodeStruct> adapted_list_field__arg) :
    __fbthrift_field_int_field(std::move(int_field__arg)),
    __fbthrift_field_enum_field(std::move(enum_field__arg)),
    __fbthrift_field_foo_field(std::move(foo_field__arg)),
    __fbthrift_field_adapted_field(std::move(adapted_field__arg)),
    __fbthrift_field_list_field(std::move(list_field__arg)),
    __fbthrift_field_list_shared_ptr_field(std::move(list_shared_ptr_field__arg)),
    __fbthrift_field_list_cpp_type_field(std::move(list_cpp_type_field__arg)),
    __fbthrift_field_set_field(std::move(set_field__arg)),
    __fbthrift_field_map_field(std::move(map_field__arg)),
    __fbthrift_field_nested_field(std::move(nested_field__arg)),
    __fbthrift_field_bar_field(std::move(bar_field__arg)),
    __fbthrift_field_adapted_list_field(std::move(adapted_list_field__arg)) {
  ::apache::thrift::adapt_detail::construct<::apache::thrift::test::TemplatedTestAdapter, 4>(__fbthrift_field_adapted_field, *this);
  ::apache::thrift::adapt_detail::construct<::FieldAdapter, 12>(__fbthrift_field_adapted_list_field, *this);
  __isset.set(folly::index_constant<0>(), true);
  __isset.set(folly::index_constant<1>(), true);
  __isset.set(folly::index_constant<2>(), true);
  __isset.set(folly::index_constant<3>(), true);
  __isset.set(folly::index_constant<4>(), true);
  __isset.set(folly::index_constant<5>(), true);
  __isset.set(folly::index_constant<6>(), true);
  __isset.set(folly::index_constant<7>(), true);
  __isset.set(folly::index_constant<8>(), true);
  __isset.set(folly::index_constant<9>(), true);
  __isset.set(folly::index_constant<10>(), true);
}


void OpEncodeStruct::__fbthrift_clear() {
  // clear all fields
  this->__fbthrift_field_int_field = ::std::int32_t();
  this->__fbthrift_field_enum_field = ::facebook::thrift::test::Enum();
  ::apache::thrift::clear(this->__fbthrift_field_foo_field);
  ::apache::thrift::adapt_detail::clear<::apache::thrift::test::TemplatedTestAdapter, 4>(__fbthrift_field_adapted_field, *this);
  this->__fbthrift_field_list_field.clear();
  this->__fbthrift_field_list_shared_ptr_field.reset();
  this->__fbthrift_field_list_cpp_type_field.clear();
  this->__fbthrift_field_set_field.clear();
  this->__fbthrift_field_map_field.clear();
  this->__fbthrift_field_nested_field.clear();
  ::apache::thrift::clear(this->__fbthrift_field_bar_field);
  ::apache::thrift::adapt_detail::clear<::FieldAdapter, 12>(__fbthrift_field_adapted_list_field, *this);
  __isset = {};
}

void OpEncodeStruct::__fbthrift_clear_terse_fields() {
}

bool OpEncodeStruct::__fbthrift_is_empty() const {
  return false;
}

bool OpEncodeStruct::operator==(FOLLY_MAYBE_UNUSED const OpEncodeStruct& rhs) const {
  FOLLY_MAYBE_UNUSED auto& lhs = *this;
  if (!(lhs.int_field_ref() == rhs.int_field_ref())) {
    return false;
  }
  if (!(lhs.enum_field_ref() == rhs.enum_field_ref())) {
    return false;
  }
  if (!(lhs.foo_field_ref() == rhs.foo_field_ref())) {
    return false;
  }
  if (::apache::thrift::adapt_detail::not_equal<::apache::thrift::test::TemplatedTestAdapter>(lhs.__fbthrift_field_adapted_field, rhs.__fbthrift_field_adapted_field)) {
    return false;
  }
  if (!(lhs.list_field_ref() == rhs.list_field_ref())) {
    return false;
  }
  if ((!::apache::thrift::detail::pointer_equal(lhs.list_shared_ptr_field_ref(), rhs.list_shared_ptr_field_ref()))) {
    return false;
  }
  if (!(lhs.list_cpp_type_field_ref() == rhs.list_cpp_type_field_ref())) {
    return false;
  }
  if (!(lhs.set_field_ref() == rhs.set_field_ref())) {
    return false;
  }
  if (!(lhs.map_field_ref() == rhs.map_field_ref())) {
    return false;
  }
  if (!(lhs.nested_field_ref() == rhs.nested_field_ref())) {
    return false;
  }
  if (!(lhs.bar_field_ref() == rhs.bar_field_ref())) {
    return false;
  }
  if (::apache::thrift::adapt_detail::not_equal<::FieldAdapter>(lhs.__fbthrift_field_adapted_list_field, rhs.__fbthrift_field_adapted_list_field)) {
    return false;
  }
  return true;
}

bool OpEncodeStruct::operator<(FOLLY_MAYBE_UNUSED const OpEncodeStruct& rhs) const {
  FOLLY_MAYBE_UNUSED auto& lhs = *this;
  if (!(lhs.int_field_ref() == rhs.int_field_ref())) {
    return lhs.int_field_ref() < rhs.int_field_ref();
  }
  if (!(lhs.enum_field_ref() == rhs.enum_field_ref())) {
    return lhs.enum_field_ref() < rhs.enum_field_ref();
  }
  if (!(lhs.foo_field_ref() == rhs.foo_field_ref())) {
    return lhs.foo_field_ref() < rhs.foo_field_ref();
  }
  if (::apache::thrift::adapt_detail::not_equal<::apache::thrift::test::TemplatedTestAdapter>(lhs.__fbthrift_field_adapted_field, rhs.__fbthrift_field_adapted_field)) {
    return ::apache::thrift::adapt_detail::less<::apache::thrift::test::TemplatedTestAdapter>(lhs.__fbthrift_field_adapted_field, rhs.__fbthrift_field_adapted_field);
  }
  if (!(lhs.list_field_ref() == rhs.list_field_ref())) {
    return lhs.list_field_ref() < rhs.list_field_ref();
  }
  if ((!::apache::thrift::detail::pointer_equal(lhs.list_shared_ptr_field_ref(), rhs.list_shared_ptr_field_ref()))) {
    return ::apache::thrift::detail::pointer_less(lhs.list_shared_ptr_field_ref(), rhs.list_shared_ptr_field_ref());
  }
  if (!(lhs.list_cpp_type_field_ref() == rhs.list_cpp_type_field_ref())) {
    return lhs.list_cpp_type_field_ref() < rhs.list_cpp_type_field_ref();
  }
  if (!(lhs.set_field_ref() == rhs.set_field_ref())) {
    return lhs.set_field_ref() < rhs.set_field_ref();
  }
  if (!(lhs.map_field_ref() == rhs.map_field_ref())) {
    return lhs.map_field_ref() < rhs.map_field_ref();
  }
  if (!(lhs.nested_field_ref() == rhs.nested_field_ref())) {
    return lhs.nested_field_ref() < rhs.nested_field_ref();
  }
  if (!(lhs.bar_field_ref() == rhs.bar_field_ref())) {
    return lhs.bar_field_ref() < rhs.bar_field_ref();
  }
  if (::apache::thrift::adapt_detail::not_equal<::FieldAdapter>(lhs.__fbthrift_field_adapted_list_field, rhs.__fbthrift_field_adapted_list_field)) {
    return ::apache::thrift::adapt_detail::less<::FieldAdapter>(lhs.__fbthrift_field_adapted_list_field, rhs.__fbthrift_field_adapted_list_field);
  }
  return false;
}

const ::facebook::thrift::test::Foo& OpEncodeStruct::get_foo_field() const& {
  return __fbthrift_field_foo_field;
}

::facebook::thrift::test::Foo OpEncodeStruct::get_foo_field() && {
  return std::move(__fbthrift_field_foo_field);
}

const ::std::vector<::facebook::thrift::test::AdaptedFoo>& OpEncodeStruct::get_list_field() const& {
  return __fbthrift_field_list_field;
}

::std::vector<::facebook::thrift::test::AdaptedFoo> OpEncodeStruct::get_list_field() && {
  return std::move(__fbthrift_field_list_field);
}

const ::std::vector<::facebook::thrift::test::AdaptedFoo>& OpEncodeStruct::get_list_cpp_type_field() const& {
  return __fbthrift_field_list_cpp_type_field;
}

::std::vector<::facebook::thrift::test::AdaptedFoo> OpEncodeStruct::get_list_cpp_type_field() && {
  return std::move(__fbthrift_field_list_cpp_type_field);
}

const ::std::set<::facebook::thrift::test::AdaptedFoo>& OpEncodeStruct::get_set_field() const& {
  return __fbthrift_field_set_field;
}

::std::set<::facebook::thrift::test::AdaptedFoo> OpEncodeStruct::get_set_field() && {
  return std::move(__fbthrift_field_set_field);
}

const ::std::map<::facebook::thrift::test::AdaptedFoo, ::facebook::thrift::test::AdaptedFoo>& OpEncodeStruct::get_map_field() const& {
  return __fbthrift_field_map_field;
}

::std::map<::facebook::thrift::test::AdaptedFoo, ::facebook::thrift::test::AdaptedFoo> OpEncodeStruct::get_map_field() && {
  return std::move(__fbthrift_field_map_field);
}

const ::std::map<::std::int32_t, ::std::vector<::facebook::thrift::test::AdaptedFoo>>& OpEncodeStruct::get_nested_field() const& {
  return __fbthrift_field_nested_field;
}

::std::map<::std::int32_t, ::std::vector<::facebook::thrift::test::AdaptedFoo>> OpEncodeStruct::get_nested_field() && {
  return std::move(__fbthrift_field_nested_field);
}

const ::facebook::thrift::test::Bar& OpEncodeStruct::get_bar_field() const& {
  return __fbthrift_field_bar_field;
}

::facebook::thrift::test::Bar OpEncodeStruct::get_bar_field() && {
  return std::move(__fbthrift_field_bar_field);
}


void swap(FOLLY_MAYBE_UNUSED OpEncodeStruct& a, FOLLY_MAYBE_UNUSED OpEncodeStruct& b) {
  using ::std::swap;
  swap(a.__fbthrift_field_int_field, b.__fbthrift_field_int_field);
  swap(a.__fbthrift_field_enum_field, b.__fbthrift_field_enum_field);
  swap(a.__fbthrift_field_foo_field, b.__fbthrift_field_foo_field);
  swap(a.__fbthrift_field_adapted_field, b.__fbthrift_field_adapted_field);
  swap(a.__fbthrift_field_list_field, b.__fbthrift_field_list_field);
  swap(a.__fbthrift_field_list_shared_ptr_field, b.__fbthrift_field_list_shared_ptr_field);
  swap(a.__fbthrift_field_list_cpp_type_field, b.__fbthrift_field_list_cpp_type_field);
  swap(a.__fbthrift_field_set_field, b.__fbthrift_field_set_field);
  swap(a.__fbthrift_field_map_field, b.__fbthrift_field_map_field);
  swap(a.__fbthrift_field_nested_field, b.__fbthrift_field_nested_field);
  swap(a.__fbthrift_field_bar_field, b.__fbthrift_field_bar_field);
  swap(a.__fbthrift_field_adapted_list_field, b.__fbthrift_field_adapted_list_field);
  swap(a.__isset, b.__isset);
}

template void OpEncodeStruct::readNoXfer<>(apache::thrift::BinaryProtocolReader*);
template uint32_t OpEncodeStruct::write<>(apache::thrift::BinaryProtocolWriter*) const;
template uint32_t OpEncodeStruct::serializedSize<>(apache::thrift::BinaryProtocolWriter const*) const;
template uint32_t OpEncodeStruct::serializedSizeZC<>(apache::thrift::BinaryProtocolWriter const*) const;
template void OpEncodeStruct::readNoXfer<>(apache::thrift::CompactProtocolReader*);
template uint32_t OpEncodeStruct::write<>(apache::thrift::CompactProtocolWriter*) const;
template uint32_t OpEncodeStruct::serializedSize<>(apache::thrift::CompactProtocolWriter const*) const;
template uint32_t OpEncodeStruct::serializedSizeZC<>(apache::thrift::CompactProtocolWriter const*) const;

static_assert(
    ::apache::thrift::detail::st::gen_check_json<
        OpEncodeStruct,
        ::apache::thrift::type_class::structure,
        ::facebook::thrift::test::Foo>,
    "inconsistent use of json option");
static_assert(
    ::apache::thrift::detail::st::gen_check_json<
        OpEncodeStruct,
        ::apache::thrift::type_class::structure,
        ::facebook::thrift::test::AdaptedFoo>,
    "inconsistent use of json option");
static_assert(
    ::apache::thrift::detail::st::gen_check_json<
        OpEncodeStruct,
        ::apache::thrift::type_class::structure,
        ::facebook::thrift::test::Bar>,
    "inconsistent use of json option");

}}} // facebook::thrift::test

namespace facebook { namespace thrift { namespace test { namespace {
FOLLY_MAYBE_UNUSED FOLLY_ERASE void validateAdapters() {
  ::apache::thrift::adapt_detail::validateFieldAdapter<::apache::thrift::test::TemplatedTestAdapter, 4, ::facebook::thrift::test::Foo, ::facebook::thrift::test::OpEncodeStruct>();
  ::apache::thrift::adapt_detail::validateFieldAdapter<::FieldAdapter, 12, ::std::vector<::facebook::thrift::test::Foo>, ::facebook::thrift::test::OpEncodeStruct>();
}
}}}} // facebook::thrift::test
