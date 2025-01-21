# Created by nehaucahr at 01/10/2024
Feature: Fund Transfer
  # As a customer, user wants to transfer funds from one account to another.

  Scenario: Successful fund transfer from checking to savings account
    Given user has valid credentials to login
    And user wants to transfer funds from checking account to savings account
    And user enter the amount that needs to be transferred
    And user clicks on confirmation button
    Then user should see the confirmation message as "Successful fund transfer"
