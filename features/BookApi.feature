Feature: Verify if Book are added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added

    Scenario Outline: Verify AddBook API functionality
      Given the Book details with <isbn> and <aisle>
      When we execute the AddBook PostAPI method
      Then book is successfully added
      Examples:
        |isbn   |aisle |
        |abcdef  | 621 |
        |abcdef  | 622 |
        |abcdef  | 623  |