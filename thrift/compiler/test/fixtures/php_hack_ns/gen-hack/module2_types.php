<?hh
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

namespace hack_ns2;

/**
 * Original thrift enum:-
 * Status
 */
enum Status: int {
  Unknown = 0;
}

class Status_TEnumStaticMetadata implements \IThriftEnumStaticMetadata {
  public static function getEnumMetadata()[]: \tmeta_ThriftEnum {
    return \tmeta_ThriftEnum::fromShape(
      shape(
        "name" => "module2.Status",
        "elements" => dict[
          0 => "Unknown",
        ],
      )
    );
  }

  public static function getAllStructuredAnnotations()[]: \TEnumAnnotations {
    return shape(
      'enum' => dict[],
      'constants' => dict[
      ],
    );
  }
}

/**
 * Original thrift struct:-
 * FBStruct
 */
class FBStruct implements \IThriftSyncStruct {
  use \ThriftSerializationTrait;

  const dict<int, this::TFieldSpec> SPEC = dict[
    1 => shape(
      'var' => 'str_value',
      'type' => \TType::STRING,
    ),
    2 => shape(
      'var' => 'enum_value',
      'type' => \TType::I32,
      'enum' => \foo_php_ns_Status::class,
    ),
    3 => shape(
      'var' => 'struct_value',
      'type' => \TType::STRUCT,
      'class' => \foo_php_ns_TestStruct::class,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'str_value' => 1,
    'enum_value' => 2,
    'struct_value' => 3,
  ];

  const type TConstructorShape = shape(
    ?'str_value' => ?string,
    ?'enum_value' => ?\foo_php_ns_Status,
    ?'struct_value' => ?\foo_php_ns_TestStruct,
  );

  const int STRUCTURAL_ID = 3033845145268312663;
  /**
   * Original thrift field:-
   * 1: string str_value
   */
  public string $str_value;
  /**
   * Original thrift field:-
   * 2: enum module.Status enum_value
   */
  public ?\foo_php_ns_Status $enum_value;
  /**
   * Original thrift field:-
   * 3: struct module.TestStruct struct_value
   */
  public ?\foo_php_ns_TestStruct $struct_value;

  public function __construct(?string $str_value = null, ?\foo_php_ns_Status $enum_value = null, ?\foo_php_ns_TestStruct $struct_value = null  )[] {
    $this->str_value = $str_value ?? '';
    $this->enum_value = $enum_value;
    $this->struct_value = $struct_value;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'str_value'),
      Shapes::idx($shape, 'enum_value'),
      Shapes::idx($shape, 'struct_value'),
    );
  }

  public function getName()[]: string {
    return 'FBStruct';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return \tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module2.FBStruct",
        "fields" => vec[
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => \tmeta_ThriftPrimitiveType::THRIFT_STRING_TYPE,
                )
              ),
              "name" => "str_value",
            )
          ),
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 2,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_enum" => \tmeta_ThriftEnumType::fromShape(
                    shape(
                      "name" => "module.Status",
                    )
                  ),
                )
              ),
              "name" => "enum_value",
            )
          ),
          \tmeta_ThriftField::fromShape(
            shape(
              "id" => 3,
              "type" => \tmeta_ThriftType::fromShape(
                shape(
                  "t_struct" => \tmeta_ThriftStructType::fromShape(
                    shape(
                      "name" => "module.TestStruct",
                    )
                  ),
                )
              ),
              "name" => "struct_value",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[]: \TStructAnnotations {
    return shape(
      'struct' => dict[],
      'fields' => dict[
      ],
    );
  }

  public function getInstanceKey()[write_props]: string {
    return \TCompactSerializer::serialize($this);
  }

}

