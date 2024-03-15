/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/types/src/module.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated @nocommit
 */
#pragma once

#include <thrift/lib/cpp2/reflection/reflection.h>

#include <fatal/type/list.h>
#include <fatal/type/pair.h>
#include <fatal/type/sequence.h>

#include "thrift/compiler/test/fixtures/types/gen-cpp2/module_types.h"
namespace apache { namespace thrift { namespace fixtures { namespace types {

namespace __fbthrift_refl {

struct __fbthrift_strings_module {
  using AdaptedList = ::fatal::sequence<char, 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't'>;
  using AdaptedListDep = ::fatal::sequence<char, 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using AllocatorAware = ::fatal::sequence<char, 'A', 'l', 'l', 'o', 'c', 'a', 't', 'o', 'r', 'A', 'w', 'a', 'r', 'e'>;
  using AllocatorAware2 = ::fatal::sequence<char, 'A', 'l', 'l', 'o', 'c', 'a', 't', 'o', 'r', 'A', 'w', 'a', 'r', 'e', '2'>;
  using AnnotatedTypes = ::fatal::sequence<char, 'A', 'n', 'n', 'o', 't', 'a', 't', 'e', 'd', 'T', 'y', 'p', 'e', 's'>;
  using CompleteList = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't'>;
  using CompleteListDep = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using CompleteMap = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p'>;
  using CompleteMapDep = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p', 'D', 'e', 'p'>;
  using ComplexNestedWithDefault = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 'x', 'N', 'e', 's', 't', 'e', 'd', 'W', 'i', 't', 'h', 'D', 'e', 'f', 'a', 'u', 'l', 't'>;
  using ComplexString = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 'x', 'S', 't', 'r', 'i', 'n', 'g'>;
  using ContainerStruct = ::fatal::sequence<char, 'C', 'o', 'n', 't', 'a', 'i', 'n', 'e', 'r', 'S', 't', 'r', 'u', 'c', 't'>;
  using CppTypeStruct = ::fatal::sequence<char, 'C', 'p', 'p', 'T', 'y', 'p', 'e', 'S', 't', 'r', 'u', 'c', 't'>;
  using DependentAdaptedList = ::fatal::sequence<char, 'D', 'e', 'p', 'e', 'n', 'd', 'e', 'n', 't', 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't'>;
  using DependentAdaptedListDep = ::fatal::sequence<char, 'D', 'e', 'p', 'e', 'n', 'd', 'e', 'n', 't', 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using ForwardUsageByRef = ::fatal::sequence<char, 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'U', 's', 'a', 'g', 'e', 'B', 'y', 'R', 'e', 'f'>;
  using ForwardUsageRoot = ::fatal::sequence<char, 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'U', 's', 'a', 'g', 'e', 'R', 'o', 'o', 't'>;
  using ForwardUsageStruct = ::fatal::sequence<char, 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'U', 's', 'a', 'g', 'e', 'S', 't', 'r', 'u', 'c', 't'>;
  using IncompleteList = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't'>;
  using IncompleteListDep = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using IncompleteMap = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p'>;
  using IncompleteMapDep = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p', 'D', 'e', 'p'>;
  using IntTypedef_field = ::fatal::sequence<char, 'I', 'n', 't', 'T', 'y', 'p', 'e', 'd', 'e', 'f', '_', 'f', 'i', 'e', 'l', 'd'>;
  using MinPadding = ::fatal::sequence<char, 'M', 'i', 'n', 'P', 'a', 'd', 'd', 'i', 'n', 'g'>;
  using MinPaddingWithCustomType = ::fatal::sequence<char, 'M', 'i', 'n', 'P', 'a', 'd', 'd', 'i', 'n', 'g', 'W', 'i', 't', 'h', 'C', 'u', 's', 't', 'o', 'm', 'T', 'y', 'p', 'e'>;
  using MyDataItem = ::fatal::sequence<char, 'M', 'y', 'D', 'a', 't', 'a', 'I', 't', 'e', 'm'>;
  using MyForwardRefEnum = ::fatal::sequence<char, 'M', 'y', 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'R', 'e', 'f', 'E', 'n', 'u', 'm'>;
  using MyIntField = ::fatal::sequence<char, 'M', 'y', 'I', 'n', 't', 'F', 'i', 'e', 'l', 'd'>;
  using MyStringField = ::fatal::sequence<char, 'M', 'y', 'S', 't', 'r', 'i', 'n', 'g', 'F', 'i', 'e', 'l', 'd'>;
  using MyStruct = ::fatal::sequence<char, 'M', 'y', 'S', 't', 'r', 'u', 'c', 't'>;
  using MyStructWithForwardRefEnum = ::fatal::sequence<char, 'M', 'y', 'S', 't', 'r', 'u', 'c', 't', 'W', 'i', 't', 'h', 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'R', 'e', 'f', 'E', 'n', 'u', 'm'>;
  using NONZERO = ::fatal::sequence<char, 'N', 'O', 'N', 'Z', 'E', 'R', 'O'>;
  using Renamed = ::fatal::sequence<char, 'R', 'e', 'n', 'a', 'm', 'i', 'n', 'g'>;
  using SomeService = ::fatal::sequence<char, 'S', 'o', 'm', 'e', 'S', 'e', 'r', 'v', 'i', 'c', 'e'>;
  using StructWithDoubleUnderscores = ::fatal::sequence<char, 'S', 't', 'r', 'u', 'c', 't', 'W', 'i', 't', 'h', 'D', 'o', 'u', 'b', 'l', 'e', 'U', 'n', 'd', 'e', 'r', 's', 'c', 'o', 'r', 'e', 's'>;
  using TrivialNestedWithDefault = ::fatal::sequence<char, 'T', 'r', 'i', 'v', 'i', 'a', 'l', 'N', 'e', 's', 't', 'e', 'd', 'W', 'i', 't', 'h', 'D', 'e', 'f', 'a', 'u', 'l', 't'>;
  using TrivialNumeric = ::fatal::sequence<char, 'T', 'r', 'i', 'v', 'i', 'a', 'l', 'N', 'u', 'm', 'e', 'r', 'i', 'c'>;
  using TypedefStruct = ::fatal::sequence<char, 'T', 'y', 'p', 'e', 'd', 'e', 'f', 'S', 't', 'r', 'u', 'c', 't'>;
  using UintTypedef_field = ::fatal::sequence<char, 'U', 'i', 'n', 't', 'T', 'y', 'p', 'e', 'd', 'e', 'f', '_', 'f', 'i', 'e', 'l', 'd'>;
  using VirtualStruct = ::fatal::sequence<char, 'V', 'i', 'r', 't', 'u', 'a', 'l', 'S', 't', 'r', 'u', 'c', 't'>;
  using ZERO = ::fatal::sequence<char, 'Z', 'E', 'R', 'O'>;
  using __fbthrift_hash_0c4818643f9621274104ab52168631abaacc615446cc2ec90f0aa906bbfd1c81 = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p', 'D', 'e', 'p'>;
  using __fbthrift_hash_140bedbf9c3f6d56a9846d2ba7088798683f4da0c248231336e6a05679e4fdfe = ::fatal::sequence<char, 'n', 'o', 'n', 'e'>;
  using __fbthrift_hash_19a44da6ac03b8c8144c3a99a91ac0d0734415ad3c06fc30cee8a5a9121b9d5f = ::fatal::sequence<char, 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'U', 's', 'a', 'g', 'e', 'B', 'y', 'R', 'e', 'f'>;
  using __fbthrift_hash_1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9 = ::fatal::sequence<char, 'n'>;
  using __fbthrift_hash_1f1ad1f18e5a6c83567d19384346b4b81dd70d9734dbf296dc088223fa90cfb5 = ::fatal::sequence<char, 'V', 'i', 'r', 't', 'u', 'a', 'l', 'S', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_226f9104cf99aade86761476f3732bed796cc56da511d333b7a8fb62593f7c0c = ::fatal::sequence<char, 'M', 'y', 'S', 't', 'r', 'u', 'c', 't', 'W', 'i', 't', 'h', 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'R', 'e', 'f', 'E', 'n', 'u', 'm'>;
  using __fbthrift_hash_27bd877418cee5d4df04485498d0b38607647eaa2466d8f9559314f9b4dcc56d = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 'x', 'S', 't', 'r', 'i', 'n', 'g'>;
  using __fbthrift_hash_2a21fe6d592a19b7de898b50eb53c429608de1a66f3e9f62da19714a770553d1 = ::fatal::sequence<char, 'b', 'i', 'g'>;
  using __fbthrift_hash_2b4b338c3cd2d947a8ffb1f8f9597044d5353556e9d0cfc4b2e084604a7c60da = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using __fbthrift_hash_2bf193b40158e8c527d83d622099b9e835d4eb8350c9fb51344aef93d5068fb4 = ::fatal::sequence<char, 'Z', 'E', 'R', 'O'>;
  using __fbthrift_hash_2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae = ::fatal::sequence<char, 'f', 'o', 'o'>;
  using __fbthrift_hash_2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 = ::fatal::sequence<char, 'h', 'e', 'l', 'l', 'o'>;
  using __fbthrift_hash_3057376b8e4caae0679dad516a162bab52247e7d3487e78b24d7324cf7d1f223 = ::fatal::sequence<char, 'M', 'i', 'n', 'P', 'a', 'd', 'd', 'i', 'n', 'g', 'W', 'i', 't', 'h', 'C', 'u', 's', 't', 'o', 'm', 'T', 'y', 'p', 'e'>;
  using __fbthrift_hash_3a6eb0790f39ac87c94f3856b2dd2c5d110e6811602261a9a923d3bb23adc8b7 = ::fatal::sequence<char, 'd', 'a', 't', 'a'>;
  using __fbthrift_hash_3b88d9bd5cbf2a4ba8d2bb23cfb27676df2fdf0eaa2f9e147f4e5b71fe43b04a = ::fatal::sequence<char, 'T', 'r', 'i', 'v', 'i', 'a', 'l', 'N', 'e', 's', 't', 'e', 'd', 'W', 'i', 't', 'h', 'D', 'e', 'f', 'a', 'u', 'l', 't'>;
  using __fbthrift_hash_3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d = ::fatal::sequence<char, 'b'>;
  using __fbthrift_hash_3ec6adc2b7c7f64e5c960005c7b5674432ca24503d7ee390347118ca9171f2d1 = ::fatal::sequence<char, 'd', 'e', 'c', 'o', 'r', 'a', 't', 'e', 'd', '_', 's', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_3fc4ccfe745870e2c0d99f71f30ff0656c8dedd41cc1d7d3d376b0dbe685e2f3 = ::fatal::sequence<char, 't', 'w', 'o'>;
  using __fbthrift_hash_405d3717ce9f1e8652b3e6e9085270dd58ac3bb5fb05edc5a3136caf353ae1b3 = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p'>;
  using __fbthrift_hash_448d27c6db38f6f3798a038a9deae3f1b8527fc5b225886028d06c6d9ffa877c = ::fatal::sequence<char, 'M', 'y', 'D', 'a', 't', 'a', 'I', 't', 'e', 'm'>;
  using __fbthrift_hash_463a2e2458322db48dcc738e6792afe31f8fb1883cd29f0ecae7719e93de0818 = ::fatal::sequence<char, 'i', '3', '2', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_46a2d9d4323d5f1afec65c915a165277a03e43b6c68d742cf7011e3e53165010 = ::fatal::sequence<char, 'M', 'y', 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'R', 'e', 'f', 'E', 'n', 'u', 'm'>;
  using __fbthrift_hash_474c671a4588b9e32ce6beafdd372558d874086a8038790710c33186afccf69a = ::fatal::sequence<char, 'e', 'm', 'p', 't', 'y', '_', 's', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_486ea46224d1bb4fb680f34f7c9ad96a8f24ec88be73ea8e5a6c65260e9cb8a7 = ::fatal::sequence<char, 'w', 'o', 'r', 'l', 'd'>;
  using __fbthrift_hash_4b52fb402e58543eb406111961ce4b6760c045edd3af4068b93a1ff7ac4ccfc1 = ::fatal::sequence<char, 'a', 'a', '_', 'm', 'a', 'p'>;
  using __fbthrift_hash_4c4f1be7384da0ab8e9483a59b7018f4671e228da38fa30ee8eabe777bc24cda = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'G'>;
  using __fbthrift_hash_4c6cfb1e13d0a9cd8b94c25edb9c79091017483a687257e50b7698994ce6ed97 = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't'>;
  using __fbthrift_hash_53940ac400998db00c671404e5a93276d9bcd94cf10d533bc9a3c72712e1ca76 = ::fatal::sequence<char, 'M', 'y', 'S', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_55c08bd2971fde106159fb69085c6e57b77b291d5ac214f1479c0b4f41107cf1 = ::fatal::sequence<char, 'a', 'a', '_', 'u', 'n', 'i', 'q', 'u', 'e'>;
  using __fbthrift_hash_594e519ae499312b29433b7dd8a97ff068defcba9755b6d5d00e84c524d67b06 = ::fatal::sequence<char, 'z'>;
  using __fbthrift_hash_5ab816af8034a41718cabc63bd821ab7283b905d4770d0a2952ce8e00bb38520 = ::fatal::sequence<char, 'U', 'i', 'n', 't', 'T', 'y', 'p', 'e', 'd', 'e', 'f', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_65bba66356177eb17443bb2709f871192d0e181f094944d7f4da6a4ce2ec3aca = ::fatal::sequence<char, 'A', 'l', 'l', 'o', 'c', 'a', 't', 'o', 'r', 'A', 'w', 'a', 'r', 'e'>;
  using __fbthrift_hash_68f4d40289380c5c6536b552d834e0a1e0df88fddcd39d4a6d7f3a0b1cf22012 = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'F'>;
  using __fbthrift_hash_6d4b9ee50b6b0430209f88e2ce0c8ffca5a1b4372666061653e53e2278e74300 = ::fatal::sequence<char, 'I', 'n', 't', 'T', 'y', 'p', 'e', 'd', 'e', 'f', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_7692c3ad3540bb803c020b3aee66cd8887123234ea0c6e7143c0add73ff431ed = ::fatal::sequence<char, 'o', 'n', 'e'>;
  using __fbthrift_hash_79e4897b515e7d37977a04ed0e467ea2f4c4e220207f77f3b8060ada31502e8d = ::fatal::sequence<char, 'm', 'a', 'j', 'o', 'r', 'V', 'e', 'r'>;
  using __fbthrift_hash_7a60aa9f6a5416b61206a441ce84695a835326c0edc0c9b86b92b618f29eb9ed = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'C'>;
  using __fbthrift_hash_7af8f5c4c7c52a8a8bd7151e1a20e8003de8a0f5b4c08676355b69772b2ae1d7 = ::fatal::sequence<char, 'b', 'i', 'g', 'g', 'i', 's', 'h'>;
  using __fbthrift_hash_7e2428b843e9d6724a9fa32f00a42ac06e8207b9bfba3984a09216c291b96032 = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p', 'D', 'e', 'p'>;
  using __fbthrift_hash_807dd0d279451e184de30a99fcae80861ff87a2813b2385f94c7e8f232034fb0 = ::fatal::sequence<char, 'I', 'n', 'c', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'M', 'a', 'p'>;
  using __fbthrift_hash_81db8ebbbbc69c6c6ad4a6aa92b76e0c08af547da236b9e2c9dbe1d8285a8130 = ::fatal::sequence<char, 's', 'm', 'a', 'l', 'l'>;
  using __fbthrift_hash_8237ba3a74a56d4dd93ccd4eb20f1fe6172b74cd9f227e053a7147ad88c73379 = ::fatal::sequence<char, 'C', 'p', 'p', 'T', 'y', 'p', 'e', 'S', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_880a35405ed995030f9d4b4939e636855aa93e6e6173fe61bd40adec636dec29 = ::fatal::sequence<char, 'a', 'a', '_', 'l', 'i', 's', 't'>;
  using __fbthrift_hash_8841d05aac4c5bad0b39a0f488a8cb61c0d273515073afde4b80ba3b758e687c = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'H'>;
  using __fbthrift_hash_8950abfda7b727630760dd35bcf5c3daa7631aff223a90f7728c0d2521dde10c = ::fatal::sequence<char, 't', 'i', 'n', 'y'>;
  using __fbthrift_hash_8a7fe0db5af3fa9a49c63f9c602f11a2d5463fd3a3390a101182571af7ef2b7b = ::fatal::sequence<char, 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'U', 's', 'a', 'g', 'e', 'S', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_8b5b9db0c13db24256c829aa364aa90c6d2eba318b9232a4ab9313b954d3555f = ::fatal::sequence<char, 't', 'h', 'r', 'e', 'e'>;
  using __fbthrift_hash_90c1d00182627507e06a35eaa3ecf459d2f3330efa432d5fd7d0d2b223b18f5a = ::fatal::sequence<char, 'F', 'o', 'r', 'w', 'a', 'r', 'd', 'U', 's', 'a', 'g', 'e', 'R', 'o', 'o', 't'>;
  using __fbthrift_hash_9214968c06bb1e32a700a6643f8e199c162564b738a53905630d1254e847be19 = ::fatal::sequence<char, 'A', 'l', 'l', 'o', 'c', 'a', 't', 'o', 'r', 'A', 'w', 'a', 'r', 'e', '2'>;
  using __fbthrift_hash_92b5f04ab4f35860f8e017dac31b28085b633f3d5f287e09764244f834381326 = ::fatal::sequence<char, 'A', 'n', 'n', 'o', 't', 'a', 't', 'e', 'd', 'T', 'y', 'p', 'e', 's'>;
  using __fbthrift_hash_94209cfdf96688afebe74f85d1cd7a90dfe7ee35666cd21d9d0b1d3d18b7764b = ::fatal::sequence<char, 'D', 'e', 'p', 'e', 'n', 'd', 'e', 'n', 't', 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't'>;
  using __fbthrift_hash_9a7302ee3e51eaab2318d59da3f22a350369afc13cc8435dd325610e17811647 = ::fatal::sequence<char, 'D', 'e', 'p', 'e', 'n', 'd', 'e', 'n', 't', 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using __fbthrift_hash_a003c1938a10c7729197e235918bdad7bc795ec24b19f24c66e4f24374526ad8 = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'A'>;
  using __fbthrift_hash_a1cdc34d520653dc2c8afd403ec6a3a1541ce66b6511e8cd5450aa25c7586db8 = ::fatal::sequence<char, '_', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_a3d53ffeeecb838901452e3279a13dcce02e91865d83cb64d8f3e5ed8c18bf03 = ::fatal::sequence<char, 'b', 'i', 'n', 'a', 'r', 'y', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_a73c4974ccb5981437f75c22da908dd553c1389729210c7d554a65e1b0f4045a = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'D'>;
  using __fbthrift_hash_b2a30733d38d491ca5f3dcb7fd435cd0774f957f27f886d82bd5018c558abb72 = ::fatal::sequence<char, 'M', 'y', 'S', 't', 'r', 'i', 'n', 'g', 'F', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_b3d13ad22fdfe53e99c368c9c7072081947fb407b6cdbe7f1d3555f02b84dd42 = ::fatal::sequence<char, 'T', 'y', 'p', 'e', 'd', 'e', 'f', 'S', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_b8df6be2c45d108344f608d16c9ccc59da495e9f547c5277fbc265f9ec699bea = ::fatal::sequence<char, 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't'>;
  using __fbthrift_hash_b94ffb2aa613f7327b42b6b06bb4997cca951e0db1dca0a84889e524bfe841ef = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 'x', 'N', 'e', 's', 't', 'e', 'd', 'W', 'i', 't', 'h', 'D', 'e', 'f', 'a', 'u', 'l', 't'>;
  using __fbthrift_hash_ba2a88de7258832d40bb04e70c8d37d66141754f3561ecfa366dc9496c9a7704 = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'E'>;
  using __fbthrift_hash_ba6aeb3608b7a761e88a18f5bfe84b5977d241c78c0739b58f2802a58589d1ab = ::fatal::sequence<char, 'R', 'e', 'n', 'a', 'm', 'i', 'n', 'g'>;
  using __fbthrift_hash_bce941ba2bb38745b37f096fe3e00e1315d800eb63a3ea9f1ae532dd34f658f0 = ::fatal::sequence<char, 'A', 'd', 'a', 'p', 't', 'e', 'd', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using __fbthrift_hash_be755881b879f256d3e3140f805d0bdd328c171304324350ef5ca9fd16f7721d = ::fatal::sequence<char, 'T', 'r', 'i', 'v', 'i', 'a', 'l', 'N', 'u', 'm', 'e', 'r', 'i', 'c'>;
  using __fbthrift_hash_bfaf0acc93bb6b488b6a5a8d0bcc12a66bdac79da50021adc4da36e22a6af810 = ::fatal::sequence<char, 'a', 'a', '_', 's', 'e', 't'>;
  using __fbthrift_hash_c082456a7766e23a18db084cd34b6ff510baef506548b897cc80e9b7d3e121c8 = ::fatal::sequence<char, 'm', 'e', 'd', 'i', 'u', 'm'>;
  using __fbthrift_hash_c0d2856b74d0df05b9d4456b177950351bd88e98b77f12574dfb7a911acee0d0 = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_c0e365354b208682f10159aaccdbed810e6899c482258b02f13b3d9913b1f8ea = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't'>;
  using __fbthrift_hash_c7e10d053d5c1a0a0743c1dfc0a38c439cd181cc30829f18cc684e286d0baf27 = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'B'>;
  using __fbthrift_hash_c9fa85c7498e0de702c747ccbfa86a6946006c87e0d3a64b9156945848027d08 = ::fatal::sequence<char, 'a', 'a', '_', 's', 'h', 'a', 'r', 'e', 'd'>;
  using __fbthrift_hash_ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb = ::fatal::sequence<char, 'a'>;
  using __fbthrift_hash_cd2d91d50cdc4fe7150ace032c028ef161c83c70624416f93ad9c2d39738630f = ::fatal::sequence<char, 'C', 'o', 'm', 'p', 'l', 'e', 't', 'e', 'L', 'i', 's', 't', 'D', 'e', 'p'>;
  using __fbthrift_hash_ce341f28cce92dd4aef1789ba556e94d03c552eb381fa789efc112a2a7b95913 = ::fatal::sequence<char, 'N', 'O', 'N', 'Z', 'E', 'R', 'O'>;
  using __fbthrift_hash_ddbb5f5c6cda27e9cba90a7892f91c2724176d74b0d802d42c5b950bd8719a47 = ::fatal::sequence<char, 'M', 'i', 'n', 'P', 'a', 'd', 'd', 'i', 'n', 'g'>;
  using __fbthrift_hash_e3a3d7b658f4a9d27441f151b296f2d70d43f430bf424f52c4cfb58409d82bf3 = ::fatal::sequence<char, 'i', 's', '_', 'u', 'n', 's', 'c', 'o', 'p', 'e', 'd'>;
  using __fbthrift_hash_ea7bd83abd8b7b855031fc7f4e0e961fe4c408203a46f5126d609632ddf0c641 = ::fatal::sequence<char, 'l', 'i', 's', 't', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_eb09df30c303344c1e4a4ebda8428a9b865358242230e1d1917b533b8e65c014 = ::fatal::sequence<char, 'b', 'o', 'x', '_', 'f', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_efda3b7db6b44fe655cfcf36ce339c894e64337d7f192d6ad81a95d5c98a2359 = ::fatal::sequence<char, 'M', 'y', 'I', 'n', 't', 'F', 'i', 'e', 'l', 'd'>;
  using __fbthrift_hash_f119bbf23aedae2e52bbe52603d5596f495df52e77522ef10e4e47e6cef18e97 = ::fatal::sequence<char, 'a', 'a', '_', 's', 't', 'r', 'i', 'n', 'g'>;
  using __fbthrift_hash_f6db24d8a8de900ae31838bf4f66ecfa5ce280df4954ad1d3da4a0baef6450fc = ::fatal::sequence<char, 'n', 'o', 't', '_', 'a', '_', 'c', 'o', 'n', 't', 'a', 'i', 'n', 'e', 'r'>;
  using __fbthrift_hash_f73ff478b4a9b34d4eff05cdf698cc686afde247b71802a7cc7efb170de26cac = ::fatal::sequence<char, 'h', 'a', 's', '_', 'b', 'i', 't', 'w', 'i', 's', 'e', '_', 'o', 'p', 's'>;
  using __fbthrift_hash_f9194e73f9e9459e3450ea10a179cdf77aafa695beecd3b9344a98d111622243 = ::fatal::sequence<char, 'z', 'e', 'r', 'o'>;
  using __fbthrift_hash_fc98093c3066e94bd61bba0613ffb2fb75cada3ebe2e43741f035d4bfb3fe716 = ::fatal::sequence<char, 'C', 'o', 'n', 't', 'a', 'i', 'n', 'e', 'r', 'S', 't', 'r', 'u', 'c', 't'>;
  using __fbthrift_hash_ff465de32ce1b76e4c62975cf13d3a1c2797b864292cf204ab54800bab38ea2d = ::fatal::sequence<char, 'S', 't', 'r', 'u', 'c', 't', 'W', 'i', 't', 'h', 'D', 'o', 'u', 'b', 'l', 'e', 'U', 'n', 'd', 'e', 'r', 's', 'c', 'o', 'r', 'e', 's'>;
  using __field = ::fatal::sequence<char, '_', '_', 'f', 'i', 'e', 'l', 'd'>;
  using a = ::fatal::sequence<char, 'a'>;
  using aa_list = ::fatal::sequence<char, 'a', 'a', '_', 'l', 'i', 's', 't'>;
  using aa_map = ::fatal::sequence<char, 'a', 'a', '_', 'm', 'a', 'p'>;
  using aa_set = ::fatal::sequence<char, 'a', 'a', '_', 's', 'e', 't'>;
  using aa_shared = ::fatal::sequence<char, 'a', 'a', '_', 's', 'h', 'a', 'r', 'e', 'd'>;
  using aa_string = ::fatal::sequence<char, 'a', 'a', '_', 's', 't', 'r', 'i', 'n', 'g'>;
  using aa_unique = ::fatal::sequence<char, 'a', 'a', '_', 'u', 'n', 'i', 'q', 'u', 'e'>;
  using b = ::fatal::sequence<char, 'b'>;
  using bar = ::fatal::sequence<char, 'f', 'o', 'o'>;
  using big = ::fatal::sequence<char, 'b', 'i', 'g'>;
  using biggish = ::fatal::sequence<char, 'b', 'i', 'g', 'g', 'i', 's', 'h'>;
  using binary_field = ::fatal::sequence<char, 'b', 'i', 'n', 'a', 'r', 'y', '_', 'f', 'i', 'e', 'l', 'd'>;
  using binary_keyed_map = ::fatal::sequence<char, 'b', 'i', 'n', 'a', 'r', 'y', '_', 'k', 'e', 'y', 'e', 'd', '_', 'm', 'a', 'p'>;
  using bounce_map = ::fatal::sequence<char, 'b', 'o', 'u', 'n', 'c', 'e', '_', 'm', 'a', 'p'>;
  using box_field = ::fatal::sequence<char, 'b', 'o', 'x', '_', 'f', 'i', 'e', 'l', 'd'>;
  using cpp_allocator = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'a', 'l', 'l', 'o', 'c', 'a', 't', 'o', 'r'>;
  using cpp_declare_bitwise_ops = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'd', 'e', 'c', 'l', 'a', 'r', 'e', '_', 'b', 'i', 't', 'w', 'i', 's', 'e', '_', 'o', 'p', 's'>;
  using cpp_declare_equal_to = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'd', 'e', 'c', 'l', 'a', 'r', 'e', '_', 'e', 'q', 'u', 'a', 'l', '_', 't', 'o'>;
  using cpp_declare_hash = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'd', 'e', 'c', 'l', 'a', 'r', 'e', '_', 'h', 'a', 's', 'h'>;
  using cpp_deprecated_enum_unscoped = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'd', 'e', 'p', 'r', 'e', 'c', 'a', 't', 'e', 'd', '_', 'e', 'n', 'u', 'm', '_', 'u', 'n', 's', 'c', 'o', 'p', 'e', 'd'>;
  using cpp_noncomparable = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'n', 'o', 'n', 'c', 'o', 'm', 'p', 'a', 'r', 'a', 'b', 'l', 'e'>;
  using cpp_virtual = ::fatal::sequence<char, 'c', 'p', 'p', '.', 'v', 'i', 'r', 't', 'u', 'a', 'l'>;
  using data = ::fatal::sequence<char, 'd', 'a', 't', 'a'>;
  using decorated_struct = ::fatal::sequence<char, 'd', 'e', 'c', 'o', 'r', 'a', 't', 'e', 'd', '_', 's', 't', 'r', 'u', 'c', 't'>;
  using empty_struct = ::fatal::sequence<char, 'e', 'm', 'p', 't', 'y', '_', 's', 't', 'r', 'u', 'c', 't'>;
  using field = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd'>;
  using fieldA = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'A'>;
  using fieldB = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'B'>;
  using fieldC = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'C'>;
  using fieldD = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'D'>;
  using fieldE = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'E'>;
  using fieldF = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'F'>;
  using fieldG = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'G'>;
  using fieldH = ::fatal::sequence<char, 'f', 'i', 'e', 'l', 'd', 'H'>;
  using foo = ::fatal::sequence<char, 'f', 'o', 'o'>;
  using has_bitwise_ops = ::fatal::sequence<char, 'h', 'a', 's', '_', 'b', 'i', 't', 'w', 'i', 's', 'e', '_', 'o', 'p', 's'>;
  using hello = ::fatal::sequence<char, 'h', 'e', 'l', 'l', 'o'>;
  using i32_field = ::fatal::sequence<char, 'i', '3', '2', '_', 'f', 'i', 'e', 'l', 'd'>;
  using is_unscoped = ::fatal::sequence<char, 'i', 's', '_', 'u', 'n', 's', 'c', 'o', 'p', 'e', 'd'>;
  using list_field = ::fatal::sequence<char, 'l', 'i', 's', 't', '_', 'f', 'i', 'e', 'l', 'd'>;
  using m = ::fatal::sequence<char, 'm'>;
  using majorVer = ::fatal::sequence<char, 'm', 'a', 'j', 'o', 'r', 'V', 'e', 'r'>;
  using medium = ::fatal::sequence<char, 'm', 'e', 'd', 'i', 'u', 'm'>;
  using module = ::fatal::sequence<char, 'm', 'o', 'd', 'u', 'l', 'e'>;
  using n = ::fatal::sequence<char, 'n'>;
  using none = ::fatal::sequence<char, 'n', 'o', 'n', 'e'>;
  using not_a_container = ::fatal::sequence<char, 'n', 'o', 't', '_', 'a', '_', 'c', 'o', 'n', 't', 'a', 'i', 'n', 'e', 'r'>;
  using one = ::fatal::sequence<char, 'o', 'n', 'e'>;
  using r = ::fatal::sequence<char, 'r'>;
  using small = ::fatal::sequence<char, 's', 'm', 'a', 'l', 'l'>;
  using three = ::fatal::sequence<char, 't', 'h', 'r', 'e', 'e'>;
  using tiny = ::fatal::sequence<char, 't', 'i', 'n', 'y'>;
  using two = ::fatal::sequence<char, 't', 'w', 'o'>;
  using world = ::fatal::sequence<char, 'w', 'o', 'r', 'l', 'd'>;
  using z = ::fatal::sequence<char, 'z'>;
  using zero = ::fatal::sequence<char, 'z', 'e', 'r', 'o'>;
};

struct module_module_traits {
  using strings = __fbthrift_strings_module;
  using name = strings::module;
  using namespaces = ::fatal::list<
  >;
  using enums = ::fatal::list<
      ::fatal::pair<::apache::thrift::fixtures::types::has_bitwise_ops, strings::has_bitwise_ops>,
      ::fatal::pair<::apache::thrift::fixtures::types::is_unscoped, strings::is_unscoped>,
      ::fatal::pair<::apache::thrift::fixtures::types::MyForwardRefEnum, strings::MyForwardRefEnum>
  >;
  using unions = ::fatal::list<
  >;
  using structs = ::fatal::list<
      ::fatal::pair<::apache::thrift::fixtures::types::empty_struct, strings::empty_struct>,
      ::fatal::pair<::apache::thrift::fixtures::types::decorated_struct, strings::decorated_struct>,
      ::fatal::pair<::apache::thrift::fixtures::types::ContainerStruct, strings::ContainerStruct>,
      ::fatal::pair<::apache::thrift::fixtures::types::CppTypeStruct, strings::CppTypeStruct>,
      ::fatal::pair<::apache::thrift::fixtures::types::VirtualStruct, strings::VirtualStruct>,
      ::fatal::pair<::apache::thrift::fixtures::types::MyStructWithForwardRefEnum, strings::MyStructWithForwardRefEnum>,
      ::fatal::pair<::apache::thrift::fixtures::types::TrivialNumeric, strings::TrivialNumeric>,
      ::fatal::pair<::apache::thrift::fixtures::types::TrivialNestedWithDefault, strings::TrivialNestedWithDefault>,
      ::fatal::pair<::apache::thrift::fixtures::types::ComplexString, strings::ComplexString>,
      ::fatal::pair<::apache::thrift::fixtures::types::ComplexNestedWithDefault, strings::ComplexNestedWithDefault>,
      ::fatal::pair<::apache::thrift::fixtures::types::MinPadding, strings::MinPadding>,
      ::fatal::pair<::apache::thrift::fixtures::types::MinPaddingWithCustomType, strings::MinPaddingWithCustomType>,
      ::fatal::pair<::apache::thrift::fixtures::types::MyStruct, strings::MyStruct>,
      ::fatal::pair<::apache::thrift::fixtures::types::MyDataItem, strings::MyDataItem>,
      ::fatal::pair<::apache::thrift::fixtures::types::Renamed, strings::Renamed>,
      ::fatal::pair<::apache::thrift::fixtures::types::AnnotatedTypes, strings::AnnotatedTypes>,
      ::fatal::pair<::apache::thrift::fixtures::types::ForwardUsageRoot, strings::ForwardUsageRoot>,
      ::fatal::pair<::apache::thrift::fixtures::types::ForwardUsageStruct, strings::ForwardUsageStruct>,
      ::fatal::pair<::apache::thrift::fixtures::types::ForwardUsageByRef, strings::ForwardUsageByRef>,
      ::fatal::pair<::apache::thrift::fixtures::types::IncompleteMap, strings::IncompleteMap>,
      ::fatal::pair<::apache::thrift::fixtures::types::IncompleteMapDep, strings::IncompleteMapDep>,
      ::fatal::pair<::apache::thrift::fixtures::types::CompleteMap, strings::CompleteMap>,
      ::fatal::pair<::apache::thrift::fixtures::types::CompleteMapDep, strings::CompleteMapDep>,
      ::fatal::pair<::apache::thrift::fixtures::types::IncompleteList, strings::IncompleteList>,
      ::fatal::pair<::apache::thrift::fixtures::types::IncompleteListDep, strings::IncompleteListDep>,
      ::fatal::pair<::apache::thrift::fixtures::types::CompleteList, strings::CompleteList>,
      ::fatal::pair<::apache::thrift::fixtures::types::CompleteListDep, strings::CompleteListDep>,
      ::fatal::pair<::apache::thrift::fixtures::types::AdaptedList, strings::AdaptedList>,
      ::fatal::pair<::apache::thrift::fixtures::types::DependentAdaptedList, strings::DependentAdaptedList>,
      ::fatal::pair<::apache::thrift::fixtures::types::AllocatorAware, strings::AllocatorAware>,
      ::fatal::pair<::apache::thrift::fixtures::types::AllocatorAware2, strings::AllocatorAware2>,
      ::fatal::pair<::apache::thrift::fixtures::types::TypedefStruct, strings::TypedefStruct>,
      ::fatal::pair<::apache::thrift::fixtures::types::StructWithDoubleUnderscores, strings::StructWithDoubleUnderscores>
  >;
  using constants = ::fatal::list<
  >;
  using services = ::fatal::list<
      strings::SomeService
  >;
};

} // __fbthrift_refl

class module_tags {
  using __fbthrift_strings = __fbthrift_refl::__fbthrift_strings_module;
  struct __fbthrift_languages {
  };
  struct __fbthrift_enums {
    using has_bitwise_ops = __fbthrift_strings::has_bitwise_ops;
    using is_unscoped = __fbthrift_strings::is_unscoped;
    using MyForwardRefEnum = __fbthrift_strings::MyForwardRefEnum;
  };
  struct __fbthrift_unions {
  };
  struct __fbthrift_structs {
    using empty_struct = __fbthrift_strings::empty_struct;
    using decorated_struct = __fbthrift_strings::decorated_struct;
    using ContainerStruct = __fbthrift_strings::ContainerStruct;
    using CppTypeStruct = __fbthrift_strings::CppTypeStruct;
    using VirtualStruct = __fbthrift_strings::VirtualStruct;
    using MyStructWithForwardRefEnum = __fbthrift_strings::MyStructWithForwardRefEnum;
    using TrivialNumeric = __fbthrift_strings::TrivialNumeric;
    using TrivialNestedWithDefault = __fbthrift_strings::TrivialNestedWithDefault;
    using ComplexString = __fbthrift_strings::ComplexString;
    using ComplexNestedWithDefault = __fbthrift_strings::ComplexNestedWithDefault;
    using MinPadding = __fbthrift_strings::MinPadding;
    using MinPaddingWithCustomType = __fbthrift_strings::MinPaddingWithCustomType;
    using MyStruct = __fbthrift_strings::MyStruct;
    using MyDataItem = __fbthrift_strings::MyDataItem;
    using Renamed = __fbthrift_strings::Renamed;
    using AnnotatedTypes = __fbthrift_strings::AnnotatedTypes;
    using ForwardUsageRoot = __fbthrift_strings::ForwardUsageRoot;
    using ForwardUsageStruct = __fbthrift_strings::ForwardUsageStruct;
    using ForwardUsageByRef = __fbthrift_strings::ForwardUsageByRef;
    using IncompleteMap = __fbthrift_strings::IncompleteMap;
    using IncompleteMapDep = __fbthrift_strings::IncompleteMapDep;
    using CompleteMap = __fbthrift_strings::CompleteMap;
    using CompleteMapDep = __fbthrift_strings::CompleteMapDep;
    using IncompleteList = __fbthrift_strings::IncompleteList;
    using IncompleteListDep = __fbthrift_strings::IncompleteListDep;
    using CompleteList = __fbthrift_strings::CompleteList;
    using CompleteListDep = __fbthrift_strings::CompleteListDep;
    using AdaptedList = __fbthrift_strings::AdaptedList;
    using DependentAdaptedList = __fbthrift_strings::DependentAdaptedList;
    using AllocatorAware = __fbthrift_strings::AllocatorAware;
    using AllocatorAware2 = __fbthrift_strings::AllocatorAware2;
    using TypedefStruct = __fbthrift_strings::TypedefStruct;
    using StructWithDoubleUnderscores = __fbthrift_strings::StructWithDoubleUnderscores;
  };
  struct __fbthrift_constants {
  };
  struct __fbthrift_services {
    using SomeService = __fbthrift_strings::SomeService;
  };
 public:
  struct module {};

  using strings = __fbthrift_strings;
  using languages = __fbthrift_languages;
  using enums = __fbthrift_enums;
  using unions = __fbthrift_unions;
  using structs = __fbthrift_structs;
  using constants = __fbthrift_constants;
  using services = __fbthrift_services;
};

THRIFT_REGISTER_REFLECTION_METADATA(module_tags::module, __fbthrift_refl::module_module_traits);

}}}} // apache::thrift::fixtures::types