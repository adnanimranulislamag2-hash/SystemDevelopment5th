"""
Test suite for the Calculator class.
"""

import pytest
from src.calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    """Create a calculator instance for tests."""
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_at_boundary_values(self, calc):
        """Test adding at boundary values does not raise exception."""
        # Arrange
        a = 1000000  # At MAX_VALUE
        b = -1000000  # At MIN_VALUE
        expected = 0

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_input_outside_range_raises_exception(self, calc):
        """Test that adding inputs outside valid range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_input_below_range_raises_exception(self, calc):
        """Test that adding inputs below valid range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_first_input_outside_range_raises_exception(self, calc):
        """Test that adding with first input outside range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_second_input_outside_range_raises_exception(self, calc):
        """Test that adding with second input outside range raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001  # Outside MAX_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_first_input_below_range_raises_exception(self, calc):
        """Test that adding with first input below range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_second_input_below_range_raises_exception(self, calc):
        """Test that adding with second input below range raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001  # Below MIN_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.add(a, b)

    def test_add_invalid_input_exception_message(self, calc):
        """Test that InvalidInputException has proper message for out of range values."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(a, b)
        assert "1000001" in str(exc_info.value)
        assert "outside valid range" in str(exc_info.value).lower()


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self, calc):
        """Test subtracting negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self, calc):
        """Test subtracting positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self, calc):
        """Test subtracting negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_with_zero(self, calc):
        """Test subtracting with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero_from_number(self, calc):
        """Test subtracting number from zero."""
        # Arrange
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_floats(self, calc):
        """Test subtracting floating point numbers."""
        # Arrange
        a = 5.7
        b = 2.3
        expected = 3.4

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_at_boundary_values(self, calc):
        """Test subtracting at boundary values does not raise exception."""
        # Arrange
        a = 1000000  # At MAX_VALUE
        b = -1000000  # At MIN_VALUE
        expected = 2000000

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_input_outside_range_raises_exception(self, calc):
        """Test that subtracting inputs outside valid range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_input_below_range_raises_exception(self, calc):
        """Test that subtracting inputs below valid range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_first_input_outside_range_raises_exception(self, calc):
        """Test that subtracting with first input outside range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_second_input_outside_range_raises_exception(self, calc):
        """Test that subtracting with second input outside range raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001  # Outside MAX_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_first_input_below_range_raises_exception(self, calc):
        """Test that subtracting with first input below range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_second_input_below_range_raises_exception(self, calc):
        """Test that subtracting with second input below range raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001  # Below MIN_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.subtract(a, b)

    def test_subtract_invalid_input_exception_message(self, calc):
        """Test that InvalidInputException has proper message for out of range values."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.subtract(a, b)
        assert "1000001" in str(exc_info.value)
        assert "outside valid range" in str(exc_info.value).lower()


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self, calc):
        """Test multiplying negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative(self, calc):
        """Test multiplying positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = -15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_with_zero(self, calc):
        """Test multiplying with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_floats(self, calc):
        """Test multiplying floating point numbers."""
        # Arrange
        a = 2.5
        b = 4.0
        expected = 10.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_at_boundary_values(self, calc):
        """Test multiplying at boundary values does not raise exception."""
        # Arrange
        a = 1000000  # At MAX_VALUE
        b = 1  # Simple value
        expected = 1000000

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_input_outside_range_raises_exception(self, calc):
        """Test that multiplying inputs outside valid range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_input_below_range_raises_exception(self, calc):
        """Test that multiplying inputs below valid range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_first_input_outside_range_raises_exception(self, calc):
        """Test that multiplying with first input outside range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_second_input_outside_range_raises_exception(self, calc):
        """Test that multiplying with second input outside range raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001  # Outside MAX_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_first_input_below_range_raises_exception(self, calc):
        """Test that multiplying with first input below range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_second_input_below_range_raises_exception(self, calc):
        """Test that multiplying with second input below range raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001  # Below MIN_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.multiply(a, b)

    def test_multiply_invalid_input_exception_message(self, calc):
        """Test that InvalidInputException has proper message for out of range values."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.multiply(a, b)
        assert "1000001" in str(exc_info.value)
        assert "outside valid range" in str(exc_info.value).lower()


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 10
        b = 2
        expected = 5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self, calc):
        """Test dividing negative numbers."""
        # Arrange
        a = -10
        b = -2
        expected = 5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_and_negative(self, calc):
        """Test dividing positive and negative numbers."""
        # Arrange
        a = 10
        b = -2
        expected = -5.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_with_zero_numerator(self, calc):
        """Test dividing zero by a number."""
        # Arrange
        a = 0
        b = 5
        expected = 0.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_zero_raises_value_error_with_correct_message(self, calc):
        """Test that dividing by zero raises ValueError with correct message."""
        # Arrange
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            calc.divide(a, b)
        assert "Cannot divide by zero" == str(exc_info.value)

    def test_divide_by_zero_raises_value_error(self, calc):
        """Test that dividing by zero raises ValueError."""
        # Arrange
        a = 5
        b = 0

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)

    def test_divide_floats(self, calc):
        """Test dividing floating point numbers."""
        # Arrange
        a = 7.5
        b = 2.5
        expected = 3.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_at_boundary_values(self, calc):
        """Test dividing at boundary values does not raise exception."""
        # Arrange
        a = 1000000  # At MAX_VALUE
        b = 1  # Simple value
        expected = 1000000.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_input_outside_range_raises_exception(self, calc):
        """Test that dividing inputs outside valid range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_input_below_range_raises_exception(self, calc):
        """Test that dividing inputs below valid range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_first_input_outside_range_raises_exception(self, calc):
        """Test that dividing with first input outside range raises InvalidInputException."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_second_input_outside_range_raises_exception(self, calc):
        """Test that dividing with second input outside range raises InvalidInputException."""
        # Arrange
        a = 5
        b = 1000001  # Outside MAX_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_first_input_below_range_raises_exception(self, calc):
        """Test that dividing with first input below range raises InvalidInputException."""
        # Arrange
        a = -1000001  # Below MIN_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_second_input_below_range_raises_exception(self, calc):
        """Test that dividing with second input below range raises InvalidInputException."""
        # Arrange
        a = 5
        b = -1000001  # Below MIN_VALUE

        # Act & Assert
        with pytest.raises(InvalidInputException):
            calc.divide(a, b)

    def test_divide_by_zero_with_valid_inputs(self, calc):
        """Test that dividing by zero raises ValueError even with valid inputs otherwise."""
        # Arrange
        a = 1000000  # Valid input at boundary
        b = 0  # Zero denominator

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)

    def test_divide_by_zero_with_both_valid_inputs(self, calc):
        """Test that dividing by zero raises ValueError regardless of other input validity."""
        # Arrange
        a = -1000000  # Valid input at boundary
        b = 0  # Zero denominator

        # Act & Assert
        with pytest.raises(ValueError):
            calc.divide(a, b)

    def test_divide_edge_case_both_inputs_at_boundaries(self, calc):
        """Test dividing with both inputs at boundary values."""
        # Arrange
        a = 1000000  # At MAX_VALUE
        b = -1000000  # At MIN_VALUE
        expected = -1.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_invalid_input_exception_message(self, calc):
        """Test that InvalidInputException has proper message for out of range values."""
        # Arrange
        a = 1000001  # Outside MAX_VALUE
        b = 5

        # Act & Assert
        with pytest.raises(InvalidInputException) as exc_info:
            calc.divide(a, b)
        assert "1000001" in str(exc_info.value)
        assert "outside valid range" in str(exc_info.value).lower()
