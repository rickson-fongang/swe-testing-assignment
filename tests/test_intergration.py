from quick_calc.cli import calculate_expression, clear_display

def test_full_addition_flow():
    result = calculate_expression(5, "+", 3)
    assert result == 8

def test_clear_after_operation():
    _ = calculate_expression(5, "+", 3)
    result = clear_display()
    assert result == 0