Feature: GitHub API Validation
  # Enter feature description here

  @smoke
  Scenario: Token API Check
    Given I have GitHub token
    When I hit getRepo API of GitHub
    Then status code of response should be 200