from typing import List, Optional, TypeVar

def safely_get_value(dct: dict, key: str, default: Optional[int] = None) -> Optional[int]:
    if key in dct:
        return dct[key]
    else:
        return default
