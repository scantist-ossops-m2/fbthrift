// @generated by Thrift for thrift/compiler/test/fixtures/basic-enum/src/module.thrift
// This file is probably not the place you want to edit!

//! Thrift constant definitions for `module`.

pub const kOne: crate::types::MyEnum = crate::types::MyEnum::ONE;

pub static enumNames: ::once_cell::sync::Lazy<::std::collections::BTreeMap<crate::types::MyEnum, ::std::string::String>> = ::once_cell::sync::Lazy::new(|| {
            let mut map = ::std::collections::BTreeMap::new();
            {
                #[inline(never)]
                fn __do_insert(map: &mut ::std::collections::BTreeMap<crate::types::MyEnum, ::std::string::String>) {
                    map.insert(crate::types::MyEnum::ONE, "one".to_owned());
                }
                __do_insert(&mut map);
            }
            {
                #[inline(never)]
                fn __do_insert(map: &mut ::std::collections::BTreeMap<crate::types::MyEnum, ::std::string::String>) {
                    map.insert(crate::types::MyEnum::TWO, "two".to_owned());
                }
                __do_insert(&mut map);
            }
            map
        });

