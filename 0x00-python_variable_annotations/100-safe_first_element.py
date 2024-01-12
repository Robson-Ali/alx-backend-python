from typing import List, Optional

def safe_first_element(lst: List[Optional[int]]) -> Optional[int]:
    if lst:
        return lst[0]
    else:
        return None
