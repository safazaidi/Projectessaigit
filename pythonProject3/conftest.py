# conftest.py
import pytest

@pytest.fixture
def sample_booking_data():
    """Provide common test data for bookings."""
    return {
        "night": 3,
        "price_per_night": 80.0,
        "discount_percent": 10.0,
    }
