Feature: payment service contract test

Background:
* url 'http://localhost:8080/api/movies'

Scenario: create, get, update, list and delete payments
    Given request { name: 'Godfather' }
    When method post
    Then status 201
    And match response == { ID: '#number', name: 'Godfather' }
    And def id = response.ID

    Given path id
    When method get
    Then status 200
    And match response == { ID: '#(id)', name: 'Godfather' }

    Given path id
    And request { ID: '#(id)', name: 'Godfather II' }
    When method put
    Then status 200
    And match response == { ID: '#(id)', name: 'Godfather II' }

    When method get
    Then status 200
    And match response contains { ID: '#(id)', name: 'Godfather II' }

    Given path id
    When method delete
    Then status 204

    When method get
    Then status 200
    And match response !contains { ID: '#(id)', name: '#string' }
