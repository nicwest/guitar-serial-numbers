from typing import Union, Optional
from dataclasses import dataclass


# https://www.gibson.com/en-US/support/serial-number-search
@dataclass
class Guitar:
    year: int
    day: int
    rank: int
    factory: str
    batch: Optional[int] = None


def usa_acoustic_memphis_1975_present(number: Union[str, int]):
    number = str(number)
    year = int(number[0] + number[4])
    # someone will need to deal with this in 2075
    if year < 75:
        year += 2000
    else:
        year += 1900
    day = int(number[1:4])
    rank = int(number[-3:])
    batch = int(number[5])
    if len(number) != 9:
        batch = None
    factory = 'pewpew'
    return Guitar(year=year, day=day, batch=batch, rank=rank, factory=factory)
