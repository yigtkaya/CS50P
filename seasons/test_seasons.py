from seasons import Age
import pytest

def test_Age():

    assert Age("1999-01-01") == "Twelve million, three hundred eighty-eight thousand, three hundred twenty minutes"
    assert Age("2001-01-01") == "Eleven million, three hundred thirty-five thousand, six hundred eighty minutes"
    assert Age("1995-01-01") == "Fourteen million, four hundred ninety-two thousand, one hundred sixty minutes"
    assert Age("2020-06-01") ==  "One million, one hundred twenty-four thousand, six hundred forty minutes"
    assert Age("1998-06-20") ==  "Twelve million, six hundred sixty-nine thousand, one hundred twenty minutes"