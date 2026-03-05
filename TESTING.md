# Testing Strategy

This document describes the testing strategy used for the Quick-Calc application.

## What Was Tested

The following components were tested:

- Core calculator logic (addition, subtraction, multiplication, division)
- Error handling for division by zero
- Edge cases such as negative numbers, decimal numbers, and large numbers
- Integration between user input and calculator operations

## What Was Not Tested

The project does not include performance testing, security testing, or graphical interface testing.  
These were excluded because the application focuses only on arithmetic logic and testing methodology.

---

## Testing Pyramid

The project follows the **Testing Pyramid** principle:

- **Unit Tests (8 tests)** verify individual calculation functions.
- **Integration Tests (2 tests)** verify that components interact correctly.

This reflects the pyramid structure where most tests exist at the unit level.

---

## Black-box vs White-box Testing

Unit tests mainly use **white-box testing** because they verify internal functions directly.

Integration tests follow **black-box testing**, simulating user interactions without inspecting internal implementation.

---

## Functional vs Non-Functional Testing

The tests focus on **functional testing**, verifying that the calculator operations produce correct results.

Non-functional aspects such as performance or scalability were not tested because they are outside the scope of this assignment.

---

## Regression Testing

The test suite also acts as **regression testing**.  
If a previously working feature fails, the test suite will immediately detect the regression before deployment or release.

---

## Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_addition | Unit | Pass |
| test_subtraction | Unit | Pass |
| test_multiplication | Unit | Pass |
| test_division | Unit | Pass |
| test_division_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_full_addition_flow | Integration | Pass |
| test_clear_after_operation | Integration | Pass |

All tests pass successfully in version **v1.0.0**.