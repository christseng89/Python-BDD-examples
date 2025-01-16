Feature: Loan Application Management
  # Enter feature description here

  @smoke
  Scenario: Validate the existence of the loan application file
    Given the file path exists utilities/loan_app.csv
    When I read the file
    Then Sam in records
