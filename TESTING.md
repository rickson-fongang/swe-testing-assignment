# Testing Strategy — Quick-Calc

## 1. Overview

The testing strategy for Quick-Calc follows a layered approach aligned with best practices in software engineering. The objective was to verify functional correctness of arithmetic logic while demonstrating understanding of structured testing principles discussed in Lecture 3.

---

## 2. What Was Tested

### Unit Tests
Unit tests target the `Calculator` class directly. Each arithmetic operation is tested independently in isolation.

Covered:
- Addition
- Subtraction
- Multiplication
- Division
- Division by zero (exception handling)
- Negative numbers
- Decimal numbers
- Large numbers

### Integration Tests
Integration tests verify interaction between the CLI/input layer (`cli.py`) and the underlying calculation logic (`calculator.py`).

Covered:
- Full calculation flow (e.g., 5 + 3 = 8)
- Clear/reset functionality after calculation

---

## 3. What Was Not Tested

- Performance testing (not required for scope)
- Security testing (no external input exposure)
- Usability testing (CLI-based minimal interface)
- Load testing (application complexity does not justify it)

These were intentionally excluded to maintain scope alignment with assignment objectives.

---

## 4. Testing Pyramid

The test suite reflects the Testing Pyramid structure:

- Majority: Unit Tests (fast, isolated, logic-level verification)
- Few: Integration Tests (component interaction validation)
- No end-to-end tests (not required for this scale)

This structure ensures fast feedback cycles and high reliability at the logic layer.

---

## 5. Black-Box vs White-Box Testing

### Unit Tests — White-Box Approach
Unit tests were written with full knowledge of the internal implementation of the Calculator class. Edge cases such as division by zero were explicitly tested.

### Integration Tests — Black-Box Approach
Integration tests focus on behavior and output rather than internal structure. They simulate user-level interaction with the system.

---

## 6. Functional vs Non-Functional Testing

### Functional Testing
All arithmetic correctness and error handling behavior were tested.

### Non-Functional Testing
Not covered:
- Performance benchmarks
- Scalability
- Reliability under stress

These were outside the assignment scope.

---

## 7. Regression Testing

The implemented test suite can be used as a regression safety net. Any future changes to the arithmetic logic or input layer can be validated by running:
