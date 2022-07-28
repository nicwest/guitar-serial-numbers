import pytest
from guitar_serial_numbers import gibson

"""
test serial numbers:

https://www.gibson.com/en-US/support/serial-number-search

70108276 means the instrument was produced on Jan. 10, 1978, in Kalamazoo and was the 276th instrument stamped that day.
82765501 means the instrument was produced on Oct. 3, 1985, in Nashville and was the 1st instrument stamped that day.

https://youtu.be/ez0JOBzZcBM?t=735

111490107 2019, 114 day of the year (24th april)


"""


class TestUSAAcousticMemphis1975toPresent:

    def test_takes_str(self):
        gibson.usa_acoustic_memphis_1975_present('70108276')

    def test_takes_int(self):
        gibson.usa_acoustic_memphis_1975_present(70108276)

    def test_derive_pre_2000_year(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('70008000')
        assert guitar.year == 1978

    def test_derive_post_2000_year(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('100090000')
        assert guitar.year == 2019

    def test_derive_day(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('91149000')
        assert guitar.day == 114

    def test_derive_day_with_zeros(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('90049000')
        assert guitar.day == 4

    def test_derive_rank(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('00009123')
        assert guitar.rank == 123

    def test_derive_rank_with_batch_numbers(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('000009123')
        assert guitar.rank == 123

    def test_derive_batch(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('000093900')
        assert guitar.batch == 3

    def test_derive_batch_pre_july_2005(self):
        guitar = gibson.usa_acoustic_memphis_1975_present('00009900')
        assert guitar.batch is None
