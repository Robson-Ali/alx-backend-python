#!/usr/bin/env python3
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''a function that gets the value from a
    dictionary using the key'''
    if key in dct:
        return dct[key]
    else:
        return
