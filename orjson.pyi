from typing import Any, Callable, Optional, Union

__version__ = str

def dumps(
    __obj: Any,
    default: Optional[Callable[[Any], Any]] = ...,
    option: Optional[int] = ...,
    max_default_recursion: int = 5,
) -> bytes: ...
def loads(__obj: Union[bytes, bytearray, str]) -> Any: ...

class JSONDecodeError(ValueError): ...
class JSONEncodeError(TypeError): ...

OPT_SERIALIZE_DATACLASS: int
OPT_NAIVE_UTC: int
OPT_OMIT_MICROSECONDS: int
OPT_STRICT_INTEGER: int
OPT_UTC_Z: int
