Feature:  Wikipedia

      @Home
      Scenario: Search for text
      Given App is lunched
      Then  I validate that Home page is displayed


      @Search
      Scenario Outline:  Search for Country
      Given App is lunched
      When  I send the text <country> to search
      Then  I validate Country <country> and description <description> corresponding expected

      Examples:
          | country | description                             |
          | Brazil  | Country in South America                |
          | Chicago | Largest city in Illinois, United States |


      @Articles
      Scenario: Show all top read articles
      Given App is lunched
      When  I click on All top read article link
      Then  I print all titles