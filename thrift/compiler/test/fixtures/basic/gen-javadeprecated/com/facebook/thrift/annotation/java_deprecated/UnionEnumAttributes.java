/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
package com.facebook.thrift.annotation.java_deprecated;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;
import java.util.BitSet;
import java.util.Arrays;
import com.facebook.thrift.*;
import com.facebook.thrift.annotations.*;
import com.facebook.thrift.async.*;
import com.facebook.thrift.meta_data.*;
import com.facebook.thrift.server.*;
import com.facebook.thrift.transport.*;
import com.facebook.thrift.protocol.*;

@SuppressWarnings({ "unused", "serial" })
public class UnionEnumAttributes implements TBase, java.io.Serializable, Cloneable, Comparable<UnionEnumAttributes> {
  private static final TStruct STRUCT_DESC = new TStruct("UnionEnumAttributes");
  private static final TField ATTRIBUTES_FIELD_DESC = new TField("attributes", TType.LIST, (short)1);

  public List<String> attributes;
  public static final int ATTRIBUTES = 1;

  // isset id assignments

  public static final Map<Integer, FieldMetaData> metaDataMap;

  static {
    Map<Integer, FieldMetaData> tmpMetaDataMap = new HashMap<Integer, FieldMetaData>();
    tmpMetaDataMap.put(ATTRIBUTES, new FieldMetaData("attributes", TFieldRequirementType.DEFAULT, 
        new ListMetaData(TType.LIST, 
            new FieldValueMetaData(TType.STRING))));
    metaDataMap = Collections.unmodifiableMap(tmpMetaDataMap);
  }

  static {
    FieldMetaData.addStructMetaDataMap(UnionEnumAttributes.class, metaDataMap);
  }

  public UnionEnumAttributes() {
  }

  public UnionEnumAttributes(
      List<String> attributes) {
    this();
    this.attributes = attributes;
  }

  public static class Builder {
    private List<String> attributes;

    public Builder() {
    }

    public Builder setAttributes(final List<String> attributes) {
      this.attributes = attributes;
      return this;
    }

    public UnionEnumAttributes build() {
      UnionEnumAttributes result = new UnionEnumAttributes();
      result.setAttributes(this.attributes);
      return result;
    }
  }

  public static Builder builder() {
    return new Builder();
  }

  /**
   * Performs a deep copy on <i>other</i>.
   */
  public UnionEnumAttributes(UnionEnumAttributes other) {
    if (other.isSetAttributes()) {
      this.attributes = TBaseHelper.deepCopy(other.attributes);
    }
  }

  public UnionEnumAttributes deepCopy() {
    return new UnionEnumAttributes(this);
  }

  public List<String> getAttributes() {
    return this.attributes;
  }

  public UnionEnumAttributes setAttributes(List<String> attributes) {
    this.attributes = attributes;
    return this;
  }

  public void unsetAttributes() {
    this.attributes = null;
  }

  // Returns true if field attributes is set (has been assigned a value) and false otherwise
  public boolean isSetAttributes() {
    return this.attributes != null;
  }

  public void setAttributesIsSet(boolean __value) {
    if (!__value) {
      this.attributes = null;
    }
  }

  @SuppressWarnings("unchecked")
  public void setFieldValue(int fieldID, Object __value) {
    switch (fieldID) {
    case ATTRIBUTES:
      if (__value == null) {
        unsetAttributes();
      } else {
        setAttributes((List<String>)__value);
      }
      break;

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  public Object getFieldValue(int fieldID) {
    switch (fieldID) {
    case ATTRIBUTES:
      return getAttributes();

    default:
      throw new IllegalArgumentException("Field " + fieldID + " doesn't exist!");
    }
  }

  @Override
  public boolean equals(Object _that) {
    if (_that == null)
      return false;
    if (this == _that)
      return true;
    if (!(_that instanceof UnionEnumAttributes))
      return false;
    UnionEnumAttributes that = (UnionEnumAttributes)_that;

    if (!TBaseHelper.equalsNobinary(this.isSetAttributes(), that.isSetAttributes(), this.attributes, that.attributes)) { return false; }

    return true;
  }

  @Override
  public int hashCode() {
    return Arrays.deepHashCode(new Object[] {attributes});
  }

  @Override
  public int compareTo(UnionEnumAttributes other) {
    if (other == null) {
      // See java.lang.Comparable docs
      throw new NullPointerException();
    }

    if (other == this) {
      return 0;
    }
    int lastComparison = 0;

    lastComparison = Boolean.valueOf(isSetAttributes()).compareTo(other.isSetAttributes());
    if (lastComparison != 0) {
      return lastComparison;
    }
    lastComparison = TBaseHelper.compareTo(attributes, other.attributes);
    if (lastComparison != 0) { 
      return lastComparison;
    }
    return 0;
  }

  public void read(TProtocol iprot) throws TException {
    TField __field;
    iprot.readStructBegin(metaDataMap);
    while (true)
    {
      __field = iprot.readFieldBegin();
      if (__field.type == TType.STOP) {
        break;
      }
      switch (__field.id)
      {
        case ATTRIBUTES:
          if (__field.type == TType.LIST) {
            {
              TList _list0 = iprot.readListBegin();
              this.attributes = new ArrayList<String>(Math.max(0, _list0.size));
              for (int _i1 = 0; 
                   (_list0.size < 0) ? iprot.peekList() : (_i1 < _list0.size); 
                   ++_i1)
              {
                String _elem2;
                _elem2 = iprot.readString();
                this.attributes.add(_elem2);
              }
              iprot.readListEnd();
            }
          } else {
            TProtocolUtil.skip(iprot, __field.type);
          }
          break;
        default:
          TProtocolUtil.skip(iprot, __field.type);
          break;
      }
      iprot.readFieldEnd();
    }
    iprot.readStructEnd();


    // check for required fields of primitive type, which can't be checked in the validate method
    validate();
  }

  public void write(TProtocol oprot) throws TException {
    validate();

    oprot.writeStructBegin(STRUCT_DESC);
    if (this.attributes != null) {
      oprot.writeFieldBegin(ATTRIBUTES_FIELD_DESC);
      {
        oprot.writeListBegin(new TList(TType.STRING, this.attributes.size()));
        for (String _iter3 : this.attributes)        {
          oprot.writeString(_iter3);
        }
        oprot.writeListEnd();
      }
      oprot.writeFieldEnd();
    }
    oprot.writeFieldStop();
    oprot.writeStructEnd();
  }

  @Override
  public String toString() {
    return toString(1, true);
  }

  @Override
  public String toString(int indent, boolean prettyPrint) {
    String indentStr = prettyPrint ? TBaseHelper.getIndentedString(indent) : "";
    String newLine = prettyPrint ? "\n" : "";
    String space = prettyPrint ? " " : "";
    StringBuilder sb = new StringBuilder("UnionEnumAttributes");
    sb.append(space);
    sb.append("(");
    sb.append(newLine);
    boolean first = true;

    sb.append(indentStr);
    sb.append("attributes");
    sb.append(space);
    sb.append(":").append(space);
    if (this.getAttributes() == null) {
      sb.append("null");
    } else {
      sb.append(TBaseHelper.toString(this.getAttributes(), indent + 1, prettyPrint));
    }
    first = false;
    sb.append(newLine + TBaseHelper.reduceIndent(indentStr));
    sb.append(")");
    return sb.toString();
  }

  public void validate() throws TException {
    // check for required fields
  }

}

