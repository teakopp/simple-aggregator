import pytest
from simple_aggregator.modules.utils import format_date

def test_accepts_default_datetimes():
    formatted_date = format_date("2021-03-03 18:54:12.411+00")
    assert formatted_date == "2021-03-03 18:54"

def test_accepts_shorter_datetimes():
    formatted_date = format_date("2021-03-03 18:54")
    assert formatted_date == "2021-03-03 18:54"

def test_accepts_z_format():
    formatted_date = format_date("2022-03-01T03:01:00Z")
    assert formatted_date == "2022-03-01 03:01"

def test_value_error_if_incorrect():
    with pytest.raises(ValueError):
       format_date("2021-03-03 18:")


