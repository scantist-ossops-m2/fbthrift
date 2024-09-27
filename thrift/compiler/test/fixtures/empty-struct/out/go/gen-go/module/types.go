// Autogenerated by Thrift for thrift/compiler/test/fixtures/empty-struct/src/module.thrift
//
// DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
//  @generated

package module

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


type Empty struct {
}
// Compile time interface enforcer
var _ thrift.Struct = (*Empty)(nil)

func NewEmpty() *Empty {
    return (&Empty{}).setDefaults()
}



func (x *Empty) Write(p thrift.Encoder) error {
    if err := p.WriteStructBegin("Empty"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }


    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *Empty) Read(p thrift.Decoder) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, wireType, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if wireType == thrift.STOP {
            break;
        }

        var fieldReadErr error
        switch {
        default:
            fieldReadErr = p.Skip(wireType)
        }

        if fieldReadErr != nil {
            return fieldReadErr
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}

func (x *Empty) String() string {
    if x == nil {
        return "<nil>"
    }

    var sb strings.Builder

    sb.WriteString("Empty({")
    sb.WriteString("})")

    return sb.String()
}
func (x *Empty) setDefaults() *Empty {
    return x
}


type Nada struct {
}
// Compile time interface enforcer
var _ thrift.Struct = (*Nada)(nil)

func NewNada() *Nada {
    return (&Nada{}).setDefaults()
}

func (x *Nada) countSetFields() int {
    count := int(0)
    return count
}

func (x *Nada) CountSetFieldsNada() int {
    return x.countSetFields()
}



func (x *Nada) Write(p thrift.Encoder) error {
    if countSet := x.countSetFields(); countSet > 1 {
        return fmt.Errorf("%T write union: no more than one field must be set (%d set).", x, countSet)
    }
    if err := p.WriteStructBegin("Nada"); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct begin error: ", x), err)
    }


    if err := p.WriteFieldStop(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write field stop error: ", x), err)
    }

    if err := p.WriteStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T write struct end error: ", x), err)
    }
    return nil
}

func (x *Nada) Read(p thrift.Decoder) error {
    if _, err := p.ReadStructBegin(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read error: ", x), err)
    }

    for {
        _, wireType, id, err := p.ReadFieldBegin()
        if err != nil {
            return thrift.PrependError(fmt.Sprintf("%T field %d read error: ", x, id), err)
        }

        if wireType == thrift.STOP {
            break;
        }

        var fieldReadErr error
        switch {
        default:
            fieldReadErr = p.Skip(wireType)
        }

        if fieldReadErr != nil {
            return fieldReadErr
        }

        if err := p.ReadFieldEnd(); err != nil {
            return err
        }
    }

    if err := p.ReadStructEnd(); err != nil {
        return thrift.PrependError(fmt.Sprintf("%T read struct end error: ", x), err)
    }

    return nil
}

func (x *Nada) String() string {
    if x == nil {
        return "<nil>"
    }

    var sb strings.Builder

    sb.WriteString("Nada({")
    sb.WriteString("})")

    return sb.String()
}
func (x *Nada) setDefaults() *Nada {
    return x
}


// RegisterTypes registers types found in this file that have a thrift_uri with the passed in registry.
func RegisterTypes(registry interface {
  RegisterType(name string, initializer func() any)
}) {

}
