import math
from unittest.mock import patch, Mock

import pytest
import requests

from project import PlaneAssist, get_float_input, manage_data, check_internet_connection


def test_wing_area_func():
    plane = PlaneAssist(1000)  # Altitude 1000 meters
    inputs = {
        "cl_max": 1.5,  # dimensionless
        "mass": 1500,  # kilograms
        "velocity": 50,  # meters/second
    }
    expected_wing_area = round(
        ((1500 * plane.gravity) / (0.5 * plane.density * (50 * 2) * 1.5)),
        2,
    )
    assert plane.wing_area_func(inputs) == expected_wing_area


def test_stall_speed_func():
    plane = PlaneAssist(1000)  # Altitude 1000 meters
    inputs = {
        "cl_max": 1.5,  # dimensionless
        "mass": 1500,  # kilograms
        "area": 30,  # square meters
    }
    expected_stall_speed = round(
        math.sqrt((2 * (1500 * plane.gravity) / plane.density * 1.5 * 30)),
        2,
    )
    assert plane.stall_speed_func(inputs) == expected_stall_speed


def test_thrust_func():
    plane = PlaneAssist(1000)  # Altitude 1000 meters
    inputs = {
        "cd": 0.05,  # dimensionless
        "velocity": 50,  # meters/second
        "area": 30,  # square meters
    }
    expected_thrust = round(
        (0.5 * 0.05 * plane.density * 50**2 * 30),
        2,
    )
    assert plane.thrust_func(inputs) == expected_thrust


def test_flight_time_func():
    inputs = {
        "capacity": 5000,  # mAh
        "capacity_used": 80,  # percent
        "cruise_current_draw": 30,  # Ampere
        "wattage_payload": 50,  # Watts
        "battery_voltage": 11.1,  # Voltage
    }
    expected_flight_time = round(
        ((5000 / 1000) * 80 * 0.01) / (30 + (50 / 11.1)) * 60, 2
    )
    assert PlaneAssist.flight_time_func(inputs) == expected_flight_time


def test_range_func():
    inputs = {
        "flight_time": 60,  # minutes
        "true_airspeed": 50,  # meters/second
        "wind_speed": 10,  # meters/second
        "wind_origin": 0,  # degree
        "course": 0,  # degree
    }
    wind_corr_angle = 0

    expected_ground_speed = math.sqrt(
        inputs["true_airspeed"] ** 2
        + inputs["wind_speed"] ** 2
        - (
            2
            * inputs["true_airspeed"]
            * inputs["wind_speed"]
            * math.cos(inputs["course"])
            - inputs["wind_origin"]
            + wind_corr_angle
        )
    )
    expected_range = round(inputs["flight_time"] * 60 * expected_ground_speed / 1000, 2)
    assert PlaneAssist.range_func(inputs) == expected_range


def test_all_in_one():
    plane = PlaneAssist(altitude=0)  # Altitude 0 meters

    inputs = {
        "true_airspeed": 20.0,
        "wind_speed": 5.0,
        "course": 45.0,
        "wind_origin": 180.0,
        "mass": 500.0,
        "cl_max": 1.5,
        "velocity_min": 15.0,
        "cd": 0.02,
        "capacity": 10000.0,
        "capacity_used": 80.0,
        "cruise_current_draw": 2.0,
        "battery_voltage": 12.0,
        "wattage_p": 50.0,
    }

    result = plane.all_in_one(inputs)

    expected_wing_area = 177.9
    expected_stall_speed = 1461.62
    expected_thrust = 490.0
    expected_flight_time = 77.84
    expected_aircraft_range = 104.43

    assert result[0] == expected_wing_area
    assert result[1] == expected_stall_speed
    assert result[2] == expected_thrust
    assert result[3] == expected_flight_time
    assert result[4] == expected_aircraft_range
    assert result[5]["wing_area"] == expected_wing_area
    assert result[5]["stall_speed"] == expected_stall_speed
    assert result[5]["thrust"] == expected_thrust
    assert result[5]["flight_time"] == expected_flight_time
    assert result[5]["aircraft_range"] == expected_aircraft_range


def test_get_float_input():
    # Test case for valid input
    with patch("builtins.input", return_value="10.5"):
        assert get_float_input() == 10.5

    # Test case for invalid input followed by valid input
    with patch("builtins.input", side_effect=["not_a_float", "15.7"]):
        assert get_float_input() == 15.7


def test_manage_data():
    # Mocking the get_float_input function
    with patch("project.get_float_input", side_effect=[10.5, 20.7, 30.9]):

        prompt_messages = {
            "key1": "Message 1: ",
            "key2": "Message 2: ",
            "key3": "Message 3: ",
        }
        result = manage_data(prompt_messages)
        assert result == {"key1": 10.5, "key2": 20.7, "key3": 30.9}


@patch("project.requests.head")
def test_check_internet_connection(mock_head):
    # Mock the requests.head to return a successful response
    mock_head.return_value = Mock(status_code=200)
    assert check_internet_connection() == True

    # Mock the requests.head to raise a ConnectionError
    mock_head.side_effect = requests.ConnectionError
    assert check_internet_connection() == False


if __name__ == "__main__":
    pytest.main()
