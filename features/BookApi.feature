Feature: Verify if Book are added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddBook API functionality
    Given The Book details which needs to be added to Library
    When We execute the AddBook PostAPI method
    Then Book is successfully added
