// Autogenerated by Thrift for thrift/compiler/test/fixtures/enums/src/module.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package module

import (
    "maps"
    "sync"

    thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift/types"
    metadata "github.com/facebook/fbthrift/thrift/lib/thrift/metadata"
)

// (needed to ensure safety because of naive import list construction)
var _ = thrift.ZERO
var _ = maps.Copy[map[int]int, map[int]int]
var _ = metadata.GoUnusedProtection__

// Premade Thrift types
var (
    premadeThriftType_module_Metasyntactic *metadata.ThriftType = nil
    premadeThriftType_module_MyEnum1 *metadata.ThriftType = nil
    premadeThriftType_module_MyEnum2 *metadata.ThriftType = nil
    premadeThriftType_module_MyEnum3 *metadata.ThriftType = nil
    premadeThriftType_module_MyEnum4 *metadata.ThriftType = nil
    premadeThriftType_module_MyBitmaskEnum1 *metadata.ThriftType = nil
    premadeThriftType_module_MyBitmaskEnum2 *metadata.ThriftType = nil
    premadeThriftType_i32 *metadata.ThriftType = nil
    premadeThriftType_set_i32 *metadata.ThriftType = nil
    premadeThriftType_module_SomeStruct *metadata.ThriftType = nil
    premadeThriftType_module_MyStruct *metadata.ThriftType = nil
)

// Premade Thrift type initializer
var premadeThriftTypesInitOnce = sync.OnceFunc(func() {
    premadeThriftType_module_Metasyntactic = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.Metasyntactic"),
            )
    premadeThriftType_module_MyEnum1 = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.MyEnum1"),
            )
    premadeThriftType_module_MyEnum2 = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.MyEnum2"),
            )
    premadeThriftType_module_MyEnum3 = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.MyEnum3"),
            )
    premadeThriftType_module_MyEnum4 = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.MyEnum4"),
            )
    premadeThriftType_module_MyBitmaskEnum1 = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.MyBitmaskEnum1"),
            )
    premadeThriftType_module_MyBitmaskEnum2 = metadata.NewThriftType().SetTEnum(
        metadata.NewThriftEnumType().
            SetName("module.MyBitmaskEnum2"),
            )
    premadeThriftType_i32 = metadata.NewThriftType().SetTPrimitive(
        metadata.ThriftPrimitiveType_THRIFT_I32_TYPE.Ptr(),
            )
    premadeThriftType_set_i32 = metadata.NewThriftType().SetTSet(
        metadata.NewThriftSetType().
            SetValueType(premadeThriftType_i32),
            )
    premadeThriftType_module_SomeStruct = metadata.NewThriftType().SetTStruct(
        metadata.NewThriftStructType().
            SetName("module.SomeStruct"),
            )
    premadeThriftType_module_MyStruct = metadata.NewThriftType().SetTStruct(
        metadata.NewThriftStructType().
            SetName("module.MyStruct"),
            )
})

var premadeThriftTypesMapOnce = sync.OnceValue(
    func() map[string]*metadata.ThriftType {
        // Relies on premade Thrift types initialization
        premadeThriftTypesInitOnce()
        return map[string]*metadata.ThriftType{
            "module.Metasyntactic": premadeThriftType_module_Metasyntactic,
            "module.MyEnum1": premadeThriftType_module_MyEnum1,
            "module.MyEnum2": premadeThriftType_module_MyEnum2,
            "module.MyEnum3": premadeThriftType_module_MyEnum3,
            "module.MyEnum4": premadeThriftType_module_MyEnum4,
            "module.MyBitmaskEnum1": premadeThriftType_module_MyBitmaskEnum1,
            "module.MyBitmaskEnum2": premadeThriftType_module_MyBitmaskEnum2,
            "i32": premadeThriftType_i32,
            "module.SomeStruct": premadeThriftType_module_SomeStruct,
            "module.MyStruct": premadeThriftType_module_MyStruct,
        }
    },
)

var structMetadatasOnce = sync.OnceValue(
    func() []*metadata.ThriftStruct {
        // Relies on premade Thrift types initialization
        premadeThriftTypesInitOnce()
        return []*metadata.ThriftStruct{
            metadata.NewThriftStruct().
    SetName("module.SomeStruct").
    SetIsUnion(false).
    SetFields(
        []*metadata.ThriftField{
            metadata.NewThriftField().
    SetId(1).
    SetName("reasonable").
    SetIsOptional(false).
    SetType(premadeThriftType_module_Metasyntactic),
            metadata.NewThriftField().
    SetId(2).
    SetName("fine").
    SetIsOptional(false).
    SetType(premadeThriftType_module_Metasyntactic),
            metadata.NewThriftField().
    SetId(3).
    SetName("questionable").
    SetIsOptional(false).
    SetType(premadeThriftType_module_Metasyntactic),
            metadata.NewThriftField().
    SetId(4).
    SetName("tags").
    SetIsOptional(false).
    SetType(premadeThriftType_set_i32),
        },
    ),
            metadata.NewThriftStruct().
    SetName("module.MyStruct").
    SetIsUnion(false).
    SetFields(
        []*metadata.ThriftField{
            metadata.NewThriftField().
    SetId(1).
    SetName("me2_3").
    SetIsOptional(false).
    SetType(premadeThriftType_module_MyEnum2),
            metadata.NewThriftField().
    SetId(2).
    SetName("me3_n3").
    SetIsOptional(false).
    SetType(premadeThriftType_module_MyEnum3),
            metadata.NewThriftField().
    SetId(4).
    SetName("me1_t1").
    SetIsOptional(false).
    SetType(premadeThriftType_module_MyEnum1),
            metadata.NewThriftField().
    SetId(6).
    SetName("me1_t2").
    SetIsOptional(false).
    SetType(premadeThriftType_module_MyEnum1),
        },
    ),
        }
    },
)

var exceptionMetadatasOnce = sync.OnceValue(
    func() []*metadata.ThriftException {
        // Relies on premade Thrift types initialization
        premadeThriftTypesInitOnce()
        return []*metadata.ThriftException{
        }
    },
)

var enumMetadatasOnce = sync.OnceValue(
    func() []*metadata.ThriftEnum {
        // Relies on premade Thrift types initialization
        premadeThriftTypesInitOnce()
        return []*metadata.ThriftEnum{
            metadata.NewThriftEnum().
    SetName("module.Metasyntactic").
    SetElements(
        map[int32]string{
            1: "FOO",
            2: "BAR",
            3: "BAZ",
            4: "BAX",
        },
    ),
            metadata.NewThriftEnum().
    SetName("module.MyEnum1").
    SetElements(
        map[int32]string{
            0: "ME1_0",
            1: "ME1_1",
            2: "ME1_2",
            3: "ME1_3",
            5: "ME1_5",
            6: "ME1_6",
        },
    ),
            metadata.NewThriftEnum().
    SetName("module.MyEnum2").
    SetElements(
        map[int32]string{
            0: "ME2_0",
            1: "ME2_1",
            2: "ME2_2",
        },
    ),
            metadata.NewThriftEnum().
    SetName("module.MyEnum3").
    SetElements(
        map[int32]string{
            0: "ME3_0",
            1: "ME3_1",
            -2: "ME3_N2",
            -1: "ME3_N1",
            9: "ME3_9",
            10: "ME3_10",
        },
    ),
            metadata.NewThriftEnum().
    SetName("module.MyEnum4").
    SetElements(
        map[int32]string{
            2147483645: "ME4_A",
            2147483646: "ME4_B",
            2147483647: "ME4_C",
            -2147483648: "ME4_D",
        },
    ),
            metadata.NewThriftEnum().
    SetName("module.MyBitmaskEnum1").
    SetElements(
        map[int32]string{
            1: "ONE",
            2: "TWO",
            4: "FOUR",
        },
    ),
            metadata.NewThriftEnum().
    SetName("module.MyBitmaskEnum2").
    SetElements(
        map[int32]string{
            1: "ONE",
            2: "TWO",
            4: "FOUR",
        },
    ),
        }
    },
)

var serviceMetadatasOnce = sync.OnceValue(
    func() []*metadata.ThriftService {
        // Relies on premade Thrift types initialization
        premadeThriftTypesInitOnce()
        return []*metadata.ThriftService{
        }
    },
)

// GetMetadataThriftType (INTERNAL USE ONLY).
// Returns metadata ThriftType for a given full type name.
func GetMetadataThriftType(fullName string) *metadata.ThriftType {
    return premadeThriftTypesMapOnce()[fullName]
}

// GetThriftMetadata returns complete Thrift metadata for current and imported packages.
func GetThriftMetadata() *metadata.ThriftMetadata {
    allEnumsMap := make(map[string]*metadata.ThriftEnum)
    allStructsMap := make(map[string]*metadata.ThriftStruct)
    allExceptionsMap := make(map[string]*metadata.ThriftException)
    allServicesMap := make(map[string]*metadata.ThriftService)

    // Add enum metadatas from the current program...
    for _, enumMetadata := range enumMetadatasOnce() {
        allEnumsMap[enumMetadata.GetName()] = enumMetadata
    }
    // Add struct metadatas from the current program...
    for _, structMetadata := range structMetadatasOnce() {
        allStructsMap[structMetadata.GetName()] = structMetadata
    }
    // Add exception metadatas from the current program...
    for _, exceptionMetadata := range exceptionMetadatasOnce() {
        allExceptionsMap[exceptionMetadata.GetName()] = exceptionMetadata
    }
    // Add service metadatas from the current program...
    for _, serviceMetadata := range serviceMetadatasOnce() {
        allServicesMap[serviceMetadata.GetName()] = serviceMetadata
    }

    // Obtain Thrift metadatas from recursively included programs...
    var recursiveThriftMetadatas []*metadata.ThriftMetadata

    // ...now merge metadatas from recursively included programs.
    for _, thriftMetadata := range recursiveThriftMetadatas {
        maps.Copy(allEnumsMap, thriftMetadata.GetEnums())
        maps.Copy(allStructsMap, thriftMetadata.GetStructs())
        maps.Copy(allExceptionsMap, thriftMetadata.GetExceptions())
        maps.Copy(allServicesMap, thriftMetadata.GetServices())
    }

    return metadata.NewThriftMetadata().
        SetEnums(allEnumsMap).
        SetStructs(allStructsMap).
        SetExceptions(allExceptionsMap).
        SetServices(allServicesMap)
}

// GetThriftMetadataForService returns Thrift metadata for the given service.
func GetThriftMetadataForService(scopedServiceName string) *metadata.ThriftMetadata {
    thriftMetadata := GetThriftMetadata()

    allServicesMap := thriftMetadata.GetServices()
    relevantServicesMap := make(map[string]*metadata.ThriftService)

    serviceMetadata := allServicesMap[scopedServiceName]
    // Visit and record all recursive parents of the target service.
    for serviceMetadata != nil {
        relevantServicesMap[serviceMetadata.GetName()] = serviceMetadata
        if serviceMetadata.IsSetParent() {
            serviceMetadata = allServicesMap[serviceMetadata.GetParent()]
        } else {
            serviceMetadata = nil
        }
    }

    thriftMetadata.SetServices(relevantServicesMap)

    return thriftMetadata
}
