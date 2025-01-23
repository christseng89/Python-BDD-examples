Feature: Verify if Book are added and deleted using Library API
  # Enter feature description here

  @smoke
  @book
  Scenario: Verify AddBook API
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 200

    @regression
    @book
    Scenario Outline: Verify AddBook API Outline
      Given the Book details with <isbn> and <aisle>
      When we execute the AddBook PostAPI method
      Then book is successfully added
      Examples:
        | isbn   | aisle |
        | abcdef | 621   |
        | abcdef | 622   |
        | abcdef | 623   |