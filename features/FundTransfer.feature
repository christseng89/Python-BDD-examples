# Created by nehaucahr at 01/10/2024
Feature: Fund Transfer
  # As a customer, user wants to transfer funds from one account to another.

  Background: Application login
    Given user has valid credentials to login

  @valid @smoke @regression @positive
  Scenario Outline: Valid: Fund transfer with valid details
    When user clicks on Transfer Funds
    When user selects the "<FromAccount>" as "From" account
    And user selects the "<ToAccount>" as "To" account
    And user enters the amount to be transferred as "<Amount>"
    And user clicks on confirmation button
    Then user should see the message as "<Message>"
    And user clicks on Account Overview to check account balance
    And FROM account balance should be "<FromBalance>" for "<FromAccount>"
    And TO account balance should "<ToBalance>" for "<ToAccount>"
#    And the checking account balance should be "<CheckingBalance>"
#    And the savings account balance should be "<SavingBalance>"
##
    Examples:
      | FromAccount | ToAccount | Amount | Message              | CheckingBalance | SavingBalance |
      | 15231       | 15453     | 100    | "Transfer Complete!" | 415.50          | 100           |
      | 15453       | 15231     | 100    | "Transfer Complete!" | 515.50          | 0             |

  @invalid @regression @negative
  Scenario Outline: Invalid: Fund transfer with invalid details
    When user clicks on Transfer Funds
    When user selects the "<FromAccount>" as "From" account
    And user selects the "<ToAccount>" as "To" account
    And user enters the amount to be transferred as "<Amount>"
    And user clicks on confirmation button
    Then user should see the message as "<Message>"
    And user clicks on Account Overview to check account balance
    And FROM account balance should be "<FromBalance>" for "<FromAccount>"
    And TO account balance should "<ToBalance>" for "<ToAccount>"
#    And the checking account balance should be "<CheckingBalance>"
#    And the savings account balance should be "<SavingBalance>"

#    Ctrl + Alt + L to Reformat the Examples
#  Examples:
    | FromAccount | ToAccount | Amount | Message                             | CheckingBalance | SavingBalance | AdditionalStep                    |
    | Checking    | Savings   | 0      | "Invalid amount entered"            | 0               | 0             |                                   |
    | Checking    | Savings   | 10000  | "Insufficient funds"                | 0               | 0             |                                   |
    | Checking    | Checking  | 100    | "Invalid account selection"         | 0               | 0             |                                   |
    | Checking    | Savings   | 100    | "User session timeout"              | 0               | 0             | User session timeout              |
    | Checking    | Savings   | 100    | "User account is blocked or closed" | 0               | 0             | User account is blocked or closed |

#  Scenario: Successful fund transfer from checking to savings account
#    Given user has valid credentials to login
#    And user wants to transfer funds from checking account to savings account
#    And user enter the amount that needs to be transferred
#    And user clicks on confirmation button
#    Then user should see the confirmation message as "Successful fund transfer"

# Review comments
# 1. Transfer spelling is incorrect.
# 2. No When Statement
# 3. at line 7 we have 2 actions taking place at the same time.
# 4. No amount mentioned in this scenarios.
# 5. verify if funds has been successfully transferred to saving account.

#  Scenario: Successful fund transfer from checking to savings account
#    When user selects the "Checking" as "From" account
#    And user selects the "Savings" as "To" account
#    And user enters the amount to be transferred as "$100"
#    And user clicks on confirmation button
#    Then user should see the confirmation message as "Successful fund transfer"
#    And the checking account balance should be reduced by "$100"
#    And the savings account balance should be increased by "$100"

#  Scenario: Transaction rejected due to invalid amount.
#    When user selects the "Checking" as "From" account
#    And user selects the "Savings" as "To" account
#    And user enters the amount to be transferred as "$0"
#    And user clicks on confirmation button
#    Then user should see the error message as "Invalid amount entered"
#    And the checking account balance should remain the same
#    And the savings account balance should remain the same
#
#  Scenario: Transaction rejected due to insufficient funds.
#    When user selects the "Checking" as "From" account
#    And user selects the "Savings" as "To" account
#    And user enters the amount to be transferred as "$1000"
#    And user clicks on confirmation button
#    Then user should see the error message as "Insufficient funds"
#    And the checking account balance should remain the same
#    And the savings account balance should remain the same
#
#  Scenario: Incomplete transaction due to session timeout.
#    When user selects the "Checking" as "From" account
#    And user selects the "Savings" as "To" account
#    And user enters the amount to be transferred as "$100"
#    And user clicks on confirmation button
#    And user session times out
#    Then user should see the error message as "Session timeout"
#    And the checking account balance should remain the same
#    And the savings account balance should remain the same

#  Scenario: Transaction rejected due to invalid account selection.
#    When user selects the "Checking" as "From" account
#    And user selects the "Checking" as "To" account
#    And user enters the amount to be transferred as "$100"
#    And user clicks on confirmation button
#    Then user should see the error message as "Invalid account selection"
#    And the checking account balance should remain the same
#    And the savings account balance should remain the same
#
#  Scenario: Transaction failure due to blocked or closed account.
#    When user selects the "Checking" as "From" account
#    And user selects the "Savings" as "To" account
#    And user enters the amount to be transferred as "$100"
#    And user clicks on confirmation button
#    And user account is blocked or closed
#    Then user should see the error message as "Account blocked or closed"
#    And the checking account balance should remain the same
#    And the savings account balance should remain the same
