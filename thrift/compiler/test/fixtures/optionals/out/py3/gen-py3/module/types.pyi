#
# Autogenerated by Thrift for thrift/compiler/test/fixtures/optionals/src/module.thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

import enum as _python_std_enum
import folly.iobuf as _fbthrift_iobuf
import thrift.py3.types
import thrift.py3.exceptions
import typing as _typing

import sys
import itertools


class Animal(thrift.py3.types.Enum):
    DOG: Animal = ...
    CAT: Animal = ...
    TARANTULA: Animal = ...
    def _to_python(self) -> "module.thrift_types.Animal": ...   # type: ignore
    def _to_py3(self) -> Animal: ...
    def _to_py_deprecated(self) -> int: ...


class Color(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        red: bool
        green: bool
        blue: bool
        alpha: bool
        pass

    red: _typing.Final[float] = ...
    green: _typing.Final[float] = ...
    blue: _typing.Final[float] = ...
    alpha: _typing.Final[float] = ...

    def __init__(
        self, *,
        red: _typing.Optional[float]=None,
        green: _typing.Optional[float]=None,
        blue: _typing.Optional[float]=None,
        alpha: _typing.Optional[float]=None
    ) -> None: ...

    def __call__(
        self, *,
        red: _typing.Union[float, None]=None,
        green: _typing.Union[float, None]=None,
        blue: _typing.Union[float, None]=None,
        alpha: _typing.Union[float, None]=None
    ) -> Color: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['Color'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'Color') -> bool: ...
    def __gt__(self, other: 'Color') -> bool: ...
    def __le__(self, other: 'Color') -> bool: ...
    def __ge__(self, other: 'Color') -> bool: ...

    def _to_python(self) -> "module.thrift_types.Color": ...   # type: ignore
    def _to_py3(self) -> Color: ...
    def _to_py_deprecated(self) -> "module.ttypes.Color": ...   # type: ignore

class Vehicle(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        color: bool
        licensePlate: bool
        description: bool
        name: bool
        hasAC: bool
        pass

    color: _typing.Final[Color] = ...
    licensePlate: _typing.Final[_typing.Optional[str]] = ...
    description: _typing.Final[_typing.Optional[str]] = ...
    name: _typing.Final[_typing.Optional[str]] = ...
    hasAC: _typing.Final[bool] = ...

    def __init__(
        self, *,
        color: _typing.Optional[Color]=None,
        licensePlate: _typing.Optional[str]=None,
        description: _typing.Optional[str]=None,
        name: _typing.Optional[str]=None,
        hasAC: _typing.Optional[bool]=None
    ) -> None: ...

    def __call__(
        self, *,
        color: _typing.Union[Color, None]=None,
        licensePlate: _typing.Union[str, None]=None,
        description: _typing.Union[str, None]=None,
        name: _typing.Union[str, None]=None,
        hasAC: _typing.Union[bool, None]=None
    ) -> Vehicle: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['Vehicle'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'Vehicle') -> bool: ...
    def __gt__(self, other: 'Vehicle') -> bool: ...
    def __le__(self, other: 'Vehicle') -> bool: ...
    def __ge__(self, other: 'Vehicle') -> bool: ...

    def _to_python(self) -> "module.thrift_types.Vehicle": ...   # type: ignore
    def _to_py3(self) -> Vehicle: ...
    def _to_py_deprecated(self) -> "module.ttypes.Vehicle": ...   # type: ignore

class Person(thrift.py3.types.Struct, _typing.Hashable):
    class __fbthrift_IsSet:
        id: bool
        name: bool
        age: bool
        address: bool
        favoriteColor: bool
        friends: bool
        bestFriend: bool
        petNames: bool
        afraidOfAnimal: bool
        vehicles: bool
        pass

    id: _typing.Final[int] = ...
    name: _typing.Final[str] = ...
    age: _typing.Final[_typing.Optional[int]] = ...
    address: _typing.Final[_typing.Optional[str]] = ...
    favoriteColor: _typing.Final[_typing.Optional[Color]] = ...
    friends: _typing.Final[_typing.Optional[_typing.AbstractSet[int]]] = ...
    bestFriend: _typing.Final[_typing.Optional[int]] = ...
    petNames: _typing.Final[_typing.Optional[_typing.Mapping[Animal, str]]] = ...
    afraidOfAnimal: _typing.Final[_typing.Optional[Animal]] = ...
    vehicles: _typing.Final[_typing.Optional[_typing.Sequence[Vehicle]]] = ...

    def __init__(
        self, *,
        id: _typing.Optional[int]=None,
        name: _typing.Optional[str]=None,
        age: _typing.Optional[int]=None,
        address: _typing.Optional[str]=None,
        favoriteColor: _typing.Optional[Color]=None,
        friends: _typing.Optional[_typing.AbstractSet[int]]=None,
        bestFriend: _typing.Optional[int]=None,
        petNames: _typing.Optional[_typing.Mapping[Animal, str]]=None,
        afraidOfAnimal: _typing.Optional[Animal]=None,
        vehicles: _typing.Optional[_typing.Sequence[Vehicle]]=None
    ) -> None: ...

    def __call__(
        self, *,
        id: _typing.Union[int, None]=None,
        name: _typing.Union[str, None]=None,
        age: _typing.Union[int, None]=None,
        address: _typing.Union[str, None]=None,
        favoriteColor: _typing.Union[Color, None]=None,
        friends: _typing.Union[_typing.AbstractSet[int], None]=None,
        bestFriend: _typing.Union[int, None]=None,
        petNames: _typing.Union[_typing.Mapping[Animal, str], None]=None,
        afraidOfAnimal: _typing.Union[Animal, None]=None,
        vehicles: _typing.Union[_typing.Sequence[Vehicle], None]=None
    ) -> Person: ...

    def __reduce__(self) -> _typing.Tuple[_typing.Callable, _typing.Tuple[_typing.Type['Person'], bytes]]: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __lt__(self, other: 'Person') -> bool: ...
    def __gt__(self, other: 'Person') -> bool: ...
    def __le__(self, other: 'Person') -> bool: ...
    def __ge__(self, other: 'Person') -> bool: ...

    def _to_python(self) -> "module.thrift_types.Person": ...   # type: ignore
    def _to_py3(self) -> Person: ...
    def _to_py_deprecated(self) -> "module.ttypes.Person": ...   # type: ignore

class Set__i64(_typing.AbstractSet[int], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.AbstractSet[int]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.AbstractSet[int]: ...
    def __contains__(self, x: object) -> bool: ...
    def union(self, other: _typing.AbstractSet[int]) -> 'Set__i64': ...
    def intersection(self, other: _typing.AbstractSet[int]) -> 'Set__i64': ...
    def difference(self, other: _typing.AbstractSet[int]) -> 'Set__i64': ...
    def symmetric_difference(self, other: _typing.AbstractSet[int]) -> 'Set__i64': ...
    def issubset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def issuperset(self, other: _typing.AbstractSet[int]) -> bool: ...
    def __iter__(self) -> _typing.Iterator[int]: ...


class Map__Animal_string(_typing.Mapping[Animal, str], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Mapping[Animal, str]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Mapping[Animal, str]: ...
    def __getitem__(self, key: Animal) -> str: ...
    def __iter__(self) -> _typing.Iterator[Animal]: ...


_List__VehicleT = _typing.TypeVar('_List__VehicleT', bound=_typing.Sequence[Vehicle])


class List__Vehicle(_typing.Sequence[Vehicle], _typing.Hashable):
    def __init__(self, items: _typing.Optional[_typing.Sequence[Vehicle]]=None) -> None: ...
    def __len__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __copy__(self) -> _typing.Sequence[Vehicle]: ...
    @_typing.overload
    def __getitem__(self, i: int) -> Vehicle: ...
    @_typing.overload
    def __getitem__(self, s: slice) -> _typing.Sequence[Vehicle]: ...
    def __add__(self, other: _typing.Sequence[Vehicle]) -> 'List__Vehicle': ...
    def __radd__(self, other: _List__VehicleT) -> _List__VehicleT: ...
    def __reversed__(self) -> _typing.Iterator[Vehicle]: ...
    def __iter__(self) -> _typing.Iterator[Vehicle]: ...


PersonID = int
