Feature: Google\'s Search Functionality
    Scenario: can find search results
        When visit url google
        When search for testingbot
        Then title becomes TestingBot
