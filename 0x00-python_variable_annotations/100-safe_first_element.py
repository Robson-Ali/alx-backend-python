# The types of the elements of the input are not know
from typing import Any, Union

def safe_first_element(lst: Union[list, tuple]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None
