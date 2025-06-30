Feature: Flask API Endpoints
  As an API user
  I want to access different endpoints
  So that I can get appropriate responses

  Scenario: Access root endpoint
    When I make a GET request to "/"
    Then the response status code should be 200
    And the response body should be "Hello"

  Scenario: Access non-existent endpoint
    When I make a GET request to "/non-existent"
    Then the response status code should be 404
    And the response body should be "Not Found"
