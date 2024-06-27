<?hh
/**
 * Autogenerated by Thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

/**
 * Original thrift service:-
 * Factories
 */
interface FactoriesAsyncIf extends \IThriftAsyncIf {
  /**
   * Original thrift definition:-
   * void
   *   foo();
   */
  public function foo(): Awaitable<void>;

  /**
   * Original thrift definition:-
   * void
   *   interact(1: i32 arg);
   */
  public function interact(int $arg): Awaitable<void>;

  /**
   * Original thrift definition:-
   * i32
   *   interactFast();
   */
  public function interactFast(): Awaitable<int>;
}

/**
 * Original thrift service:-
 * Factories
 */
interface FactoriesIf extends \IThriftSyncIf {
  /**
   * Original thrift definition:-
   * void
   *   foo();
   */
  public function foo(): void;

  /**
   * Original thrift definition:-
   * void
   *   interact(1: i32 arg);
   */
  public function interact(int $arg): void;

  /**
   * Original thrift definition:-
   * i32
   *   interactFast();
   */
  public function interactFast(): int;
}

/**
 * Original thrift service:-
 * Factories
 */
interface FactoriesAsyncClientIf extends FactoriesAsyncIf {
  /**
   * Original thrift definition:-
   * i32, stream<i32>
   *   serialize();
   */
  public function serialize(): Awaitable<\ResponseAndStream<int, int>>;
}

/**
 * Original thrift service:-
 * Factories
 */
interface FactoriesClientIf extends \IThriftSyncIf {
  /**
   * Original thrift definition:-
   * void
   *   foo();
   */
  public function foo(): Awaitable<void>;

  /**
   * Original thrift definition:-
   * void
   *   interact(1: i32 arg);
   */
  public function interact(int $arg): Awaitable<void>;

  /**
   * Original thrift definition:-
   * i32
   *   interactFast();
   */
  public function interactFast(): Awaitable<int>;

  /**
   * Original thrift definition:-
   * i32, stream<i32>
   *   serialize();
   */
  public function serialize(): Awaitable<\ResponseAndStream<int, int>>;
}

/**
 * Original thrift service:-
 * Factories
 */
trait FactoriesClientBase {
  require extends \ThriftClientBase;

}

class FactoriesAsyncClient extends \ThriftClientBase implements FactoriesAsyncClientIf {
  use FactoriesClientBase;

  /**
   * Original thrift definition:-
   * void
   *   foo();
   */
  public async function foo(): Awaitable<void> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_foo_args::withDefaultValues();
    await $this->asyncHandler_->genBefore("Factories", "foo", $args);
    $currentseqid = $this->sendImplHelper($args, "foo", false);
    await $this->genAwaitResponse(Factories_foo_result::class, "foo", true, $currentseqid, $rpc_options);
  }

  /**
   * Original thrift definition:-
   * void
   *   interact(1: i32 arg);
   */
  public async function interact(int $arg): Awaitable<void> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_interact_args::fromShape(shape(
      'arg' => $arg,
    ));
    await $this->asyncHandler_->genBefore("Factories", "interact", $args);
    $currentseqid = $this->sendImplHelper($args, "interact", false);
    await $this->genAwaitResponse(Factories_interact_result::class, "interact", true, $currentseqid, $rpc_options);
  }

  /**
   * Original thrift definition:-
   * i32
   *   interactFast();
   */
  public async function interactFast(): Awaitable<int> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_interactFast_args::withDefaultValues();
    await $this->asyncHandler_->genBefore("Factories", "interactFast", $args);
    $currentseqid = $this->sendImplHelper($args, "interactFast", false);
    return await $this->genAwaitResponse(Factories_interactFast_result::class, "interactFast", false, $currentseqid, $rpc_options);
  }

  /**
   * Original thrift definition:-
   * i32, stream<i32>
   *   serialize();
   */
  public async function serialize(): Awaitable<\ResponseAndStream<int, int>> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_serialize_args::withDefaultValues();
    await $this->asyncHandler_->genBefore("Factories", "serialize", $args);
    $currentseqid = $this->sendImplHelper($args, "serialize", false);
    return await $this->genAwaitStreamResponse(Factories_serialize_FirstResponse::class, Factories_serialize_StreamResponse::class, "serialize", false, $currentseqid, $rpc_options);
  }

}

class FactoriesClient extends \ThriftClientBase implements FactoriesClientIf {
  use FactoriesClientBase;

  /**
   * Original thrift definition:-
   * void
   *   foo();
   */
  public async function foo(): Awaitable<void> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_foo_args::withDefaultValues();
    await $this->asyncHandler_->genBefore("Factories", "foo", $args);
    $currentseqid = $this->sendImplHelper($args, "foo", false);
    await $this->genAwaitResponse(Factories_foo_result::class, "foo", true, $currentseqid, $rpc_options);
  }

  /**
   * Original thrift definition:-
   * void
   *   interact(1: i32 arg);
   */
  public async function interact(int $arg): Awaitable<void> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_interact_args::fromShape(shape(
      'arg' => $arg,
    ));
    await $this->asyncHandler_->genBefore("Factories", "interact", $args);
    $currentseqid = $this->sendImplHelper($args, "interact", false);
    await $this->genAwaitResponse(Factories_interact_result::class, "interact", true, $currentseqid, $rpc_options);
  }

  /**
   * Original thrift definition:-
   * i32
   *   interactFast();
   */
  public async function interactFast(): Awaitable<int> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_interactFast_args::withDefaultValues();
    await $this->asyncHandler_->genBefore("Factories", "interactFast", $args);
    $currentseqid = $this->sendImplHelper($args, "interactFast", false);
    return await $this->genAwaitResponse(Factories_interactFast_result::class, "interactFast", false, $currentseqid, $rpc_options);
  }

  /**
   * Original thrift definition:-
   * i32, stream<i32>
   *   serialize();
   */
  public async function serialize(): Awaitable<\ResponseAndStream<int, int>> {
    $hh_frame_metadata = $this->getHHFrameMetadata();
    if ($hh_frame_metadata !== null) {
      \HH\set_frame_metadata($hh_frame_metadata);
    }
    $rpc_options = $this->getAndResetOptions() ?? \ThriftClientBase::defaultOptions();
    $args = Factories_serialize_args::withDefaultValues();
    await $this->asyncHandler_->genBefore("Factories", "serialize", $args);
    $currentseqid = $this->sendImplHelper($args, "serialize", false);
    return await $this->genAwaitStreamResponse(Factories_serialize_FirstResponse::class, Factories_serialize_StreamResponse::class, "serialize", false, $currentseqid, $rpc_options);
  }

  /* send and recv functions */
  public function send_foo(): int {
    $args = Factories_foo_args::withDefaultValues();
    return $this->sendImplHelper($args, "foo", false);
  }
  public function recv_foo(?int $expectedsequenceid = null): void {
    $this->recvImplHelper(Factories_foo_result::class, "foo", true, $expectedsequenceid);
  }
  public function send_interact(int $arg): int {
    $args = Factories_interact_args::fromShape(shape(
      'arg' => $arg,
    ));
    return $this->sendImplHelper($args, "interact", false);
  }
  public function recv_interact(?int $expectedsequenceid = null): void {
    $this->recvImplHelper(Factories_interact_result::class, "interact", true, $expectedsequenceid);
  }
  public function send_interactFast(): int {
    $args = Factories_interactFast_args::withDefaultValues();
    return $this->sendImplHelper($args, "interactFast", false);
  }
  public function recv_interactFast(?int $expectedsequenceid = null): int {
    return $this->recvImplHelper(Factories_interactFast_result::class, "interactFast", false, $expectedsequenceid);
  }
}

// HELPER FUNCTIONS AND STRUCTURES

class Factories_foo_args implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Factories_foo_args';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.foo_args",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_foo_result extends \ThriftSyncStructWithoutResult implements \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Factories_foo_result';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.Factories_foo_result",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_interact_args implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
    1 => shape(
      'var' => 'arg',
      'type' => \TType::I32,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'arg' => 1,
  ];

  const type TConstructorShape = shape(
    ?'arg' => ?int,
  );

  const int STRUCTURAL_ID = 6449802475022035959;
  public int $arg;

  public function __construct(?int $arg = null)[] {
    $this->arg = $arg ?? 0;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'arg'),
    );
  }

  public function getName()[]: string {
    return 'Factories_interact_args';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.interact_args",
        "fields" => vec[
          tmeta_ThriftField::fromShape(
            shape(
              "id" => 1,
              "type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                )
              ),
              "name" => "arg",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_interact_result extends \ThriftSyncStructWithoutResult implements \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Factories_interact_result';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.Factories_interact_result",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_interactFast_args implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Factories_interactFast_args';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.interactFast_args",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_interactFast_result extends \ThriftSyncStructWithResult implements \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const type TResult = int;

  const \ThriftStructTypes::TSpec SPEC = dict[
    0 => shape(
      'var' => 'success',
      'type' => \TType::I32,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'success' => 0,
  ];

  const type TConstructorShape = shape(
    ?'success' => ?this::TResult,
  );

  const int STRUCTURAL_ID = 3865318819874171525;
  public ?this::TResult $success;

  public function __construct(?this::TResult $success = null)[] {
    $this->success = $success;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'success'),
    );
  }

  public function getName()[]: string {
    return 'Factories_interactFast_result';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.Factories_interactFast_result",
        "fields" => vec[
          tmeta_ThriftField::fromShape(
            shape(
              "id" => 0,
              "type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                )
              ),
              "name" => "success",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_serialize_args implements \IThriftSyncStruct, \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const \ThriftStructTypes::TSpec SPEC = dict[
  ];
  const dict<string, int> FIELDMAP = dict[
  ];

  const type TConstructorShape = shape(
  );

  const int STRUCTURAL_ID = 957977401221134810;

  public function __construct()[] {
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
    );
  }

  public function getName()[]: string {
    return 'Factories_serialize_args';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.serialize_args",
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_serialize_StreamResponse extends \ThriftSyncStructWithResult implements \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const type TResult = int;

  const \ThriftStructTypes::TSpec SPEC = dict[
    0 => shape(
      'var' => 'success',
      'type' => \TType::I32,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'success' => 0,
  ];

  const type TConstructorShape = shape(
    ?'success' => ?this::TResult,
  );

  const int STRUCTURAL_ID = 3865318819874171525;
  public ?this::TResult $success;

  public function __construct(?this::TResult $success = null)[] {
    $this->success = $success;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'success'),
    );
  }

  public function getName()[]: string {
    return 'Factories_serialize_StreamResponse';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.Factories_serialize_StreamResponse",
        "fields" => vec[
          tmeta_ThriftField::fromShape(
            shape(
              "id" => 0,
              "type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                )
              ),
              "name" => "success",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class Factories_serialize_FirstResponse extends \ThriftSyncStructWithResult implements \IThriftStructMetadata {
  use \ThriftSerializationTrait;

  const type TResult = int;

  const \ThriftStructTypes::TSpec SPEC = dict[
    0 => shape(
      'var' => 'success',
      'type' => \TType::I32,
    ),
  ];
  const dict<string, int> FIELDMAP = dict[
    'success' => 0,
  ];

  const type TConstructorShape = shape(
    ?'success' => ?this::TResult,
  );

  const int STRUCTURAL_ID = 3865318819874171525;
  public ?this::TResult $success;

  public function __construct(?this::TResult $success = null)[] {
    $this->success = $success;
  }

  public static function withDefaultValues()[]: this {
    return new static();
  }

  public static function fromShape(self::TConstructorShape $shape)[]: this {
    return new static(
      Shapes::idx($shape, 'success'),
    );
  }

  public function getName()[]: string {
    return 'Factories_serialize_FirstResponse';
  }

  public static function getStructMetadata()[]: \tmeta_ThriftStruct {
    return tmeta_ThriftStruct::fromShape(
      shape(
        "name" => "module.Factories_serialize_FirstResponse",
        "fields" => vec[
          tmeta_ThriftField::fromShape(
            shape(
              "id" => 0,
              "type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                )
              ),
              "name" => "success",
            )
          ),
        ],
        "is_union" => false,
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TStructAnnotations {
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

class FactoriesStaticMetadata implements \IThriftServiceStaticMetadata {
  public static function getServiceMetadata()[]: \tmeta_ThriftService {
    return tmeta_ThriftService::fromShape(
      shape(
        "name" => "module.Factories",
        "functions" => vec[
          tmeta_ThriftFunction::fromShape(
            shape(
              "name" => "foo",
              "return_type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_VOID_TYPE,
                )
              ),
            )
          ),
          tmeta_ThriftFunction::fromShape(
            shape(
              "name" => "interact",
              "return_type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_VOID_TYPE,
                )
              ),
              "arguments" => vec[
                tmeta_ThriftField::fromShape(
                  shape(
                    "id" => 1,
                    "type" => tmeta_ThriftType::fromShape(
                      shape(
                        "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                      )
                    ),
                    "name" => "arg",
                  )
                ),
              ],
            )
          ),
          tmeta_ThriftFunction::fromShape(
            shape(
              "name" => "interactFast",
              "return_type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                )
              ),
            )
          ),
          tmeta_ThriftFunction::fromShape(
            shape(
              "name" => "serialize",
              "return_type" => tmeta_ThriftType::fromShape(
                shape(
                  "t_stream" => tmeta_ThriftStreamType::fromShape(
                    shape(
                      "elemType" => tmeta_ThriftType::fromShape(
                        shape(
                          "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                        )
                      ),
                      "initialResponseType" => tmeta_ThriftType::fromShape(
                        shape(
                          "t_primitive" => tmeta_ThriftPrimitiveType::THRIFT_I32_TYPE,
                        )
                      ),
                    )
                  ),
                )
              ),
            )
          ),
        ],
      )
    );
  }

  public static function getServiceMetadataResponse()[]: \tmeta_ThriftServiceMetadataResponse {
    return \tmeta_ThriftServiceMetadataResponse::fromShape(
      shape(
        'context' => \tmeta_ThriftServiceContext::fromShape(
          shape(
            'service_info' => self::getServiceMetadata(),
            'module' => \tmeta_ThriftModuleContext::fromShape(
              shape(
                'name' => 'module',
              )
            ),
          )
        ),
        'metadata' => \tmeta_ThriftMetadata::fromShape(
          shape(
            'enums' => dict[
            ],
            'structs' => dict[
            ],
            'exceptions' => dict[
            ],
            'services' => dict[
            ],
          )
        ),
      )
    );
  }

  public static function getAllStructuredAnnotations()[write_props]: \TServiceAnnotations {
    return shape(
      'service' => dict[],
      'functions' => dict[
      ],
    );
  }
}

