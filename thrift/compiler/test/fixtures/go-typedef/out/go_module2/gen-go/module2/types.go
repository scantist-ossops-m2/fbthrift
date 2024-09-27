// Autogenerated by Thrift for thrift/compiler/test/fixtures/go-typedef/src/module2.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package module2

import (
    "fmt"
    "reflect"
    "strings"

    thrift "github.com/facebook/fbthrift/thrift/lib/go/thrift/types"
)

// (needed to ensure safety because of naive import list construction)
var _ = fmt.Printf
var _ = reflect.Ptr
var _ = strings.Split
var _ = thrift.ZERO


type Enum int32

const (
    Enum_A Enum = 0
    Enum_B Enum = 1
    Enum_C Enum = 2
)

// Enum value maps for Enum
var (
    EnumToName = map[Enum]string {
        Enum_A: "A",
        Enum_B: "B",
        Enum_C: "C",
    }

    EnumToValue = map[string]Enum {
        "A": Enum_A,
        "B": Enum_B,
        "C": Enum_C,
    }
)

func (x Enum) String() string {
    if v, ok := EnumToName[x]; ok {
        return v
    }
    return "<UNSET>"
}

func (x Enum) Ptr() *Enum {
    return &x
}

// Deprecated: Use EnumToValue instead (e.g. `x, ok := EnumToValue["name"]`).
func EnumFromString(s string) (Enum, error) {
    if v, ok := EnumToValue[s]; ok {
        return v, nil
    }
    return Enum(0), fmt.Errorf("not a valid Enum string")
}


