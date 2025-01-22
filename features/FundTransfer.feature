# Created by nehaucahr at 01/10/2024
Feature: Fund Transfer
  # As a customer, user wants to transfer funds from one account to another.

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

  Scenario: Successful fund transfer from checking to savings account
    Given user has valid credentials to login
    When user selects the "Checking" as "From" account
    And user selects the "Savings" as "To" account
    And user enters the amount to be transferred as "$100"
    And user clicks on confirmation button
    Then user should see the confirmation message as "Successful fund transfer"
    And the checking account balance should be reduced by "$100"
    And the savings account balance should be increased by "$100"
