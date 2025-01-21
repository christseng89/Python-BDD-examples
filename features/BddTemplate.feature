Feature: [High-level description of functionality]
  A short description of the feature's purpose and its importance.

  Background:
    Given [Shared setup step 1]
    And [Shared setup step 2]
    # Add as many shared steps as needed.

  @Tag1 @Tag2
  Scenario: [Specific example illustrating the feature]
    Given [Initial condition]
    When [Action is performed]
    Then [Expected outcome]
    And [Additional checks or results]

  @Tag3
  Scenario Outline: [Specific example illustrating the feature with multiple data sets]
    Given [Initial condition with <parameter>]
    When [Action is performed with <parameter>]
    Then [Expected outcome for <parameter>]

    Examples:
      | parameter | additional_parameter |
      | value1    | value2               |
      | value3    | value4               |
