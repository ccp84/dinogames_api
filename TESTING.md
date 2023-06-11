# Testing

Return to the [README.md](README.md) file.

## Code Validation
### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Dinogames main component |  |  |  |
| settings.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/dinogames/settings.py) | ![screenshot](documentation/testing/py_validation_settings.png) | None |
| permissions.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/dinogames/permissions.py) | ![screenshot](documentation/testing/py_validation_permissions.png) | None |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/dinogames/urls.py) | ![screenshot](documentation/testing/py_validation_dinogames_urls.png) | None |
| Announcements component |  |  |  |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/announcements/admin.py) | ![screenshot](documentation/testing/py_validation_announcements_admin.png) | None |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/announcements/models.py) | ![screenshot](documentation/testing/py_validation_announcements_models.png) | None |
| serializers.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/announcements/serializers.py) | ![screenshot](documentation/testing/py_validation_announcements_serializer.png) | None |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/announcements/urls.py) | ![screenshot](documentation/testing/py_validation_announcements_urls.png) | None |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/announcements/views.py) | ![screenshot](documentation/testing/py_validation_announcements_views.png) | None |
| Games component |  |  |  |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/games/admin.py) | ![screenshot](documentation/testing/py_validation_games_admin.png) | None |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/games/models.py) | ![screenshot](documentation/testing/py_validation_games_models.png) | None |
| serializers.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/games/serializers.py) | ![screenshot](documentation/testing/py_validation_games_serializer.png) | None |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/games/urls.py) | ![screenshot](documentation/testing/py_validation_games_urls.png) | None |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/games/views.py) | ![screenshot](documentation/testing/py_validation_games_views.png) | None |
| Ratings component |  |  |  |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/ratings/admin.py) | ![screenshot](documentation/testing/py_validation_ratings_admin.png) | None |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/ratings/models.py) | ![screenshot](documentation/testing/py_validation_ratings_models.png) | None |
| serializers.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/ratings/serializers.py) | ![screenshot](documentation/testing/py_validation_ratings_serializer.png) | None |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/ratings/urls.py) | ![screenshot](documentation/testing/py_validation_ratings_urls.png) | None |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/ratings/views.py) | ![screenshot](documentation/testing/py_validation_ratings_views.png) | None |
| Reviews component |  |  |  |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/reviews/admin.py) | ![screenshot](documentation/testing/py_validation_reviews_admin.png) | None |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/reviews/models.py) | ![screenshot](documentation/testing/py_validation_reviews_models.png) | None |
| serializers.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/reviews/serializers.py) | ![screenshot](documentation/testing/py_validation_reviews_serializer.png) | None |
| urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/reviews/urls.py) | ![screenshot](documentation/testing/py_validation_reviews_urls.png) | None |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/ccp84/dinogames_api/main/reviews/views.py) | ![screenshot](documentation/testing/py_validation_reviews_views.png) | None |

## Defensive Programming

Defensive programming was manually tested using Postman to check the responses of all endpoints as follows:

| Endpoint| Expected Result |         |
| ------- | --------------- | ------- |
| User Registration | 201_Created. Returns user details added to the system| ![screenshot](/documentation/testing/postman_testingregister.png)|
| Login | 200 OK. Returns access token and user profile details| ![screenshot](/documentation/testing/postman_testinglogin.png)|
| Logout | 200 OK. Removes access and refresh tokens from cookie, no data returned.| ![screenshot](/documentation/testing/postman_testinglogout.png)|
| User detail | 200 OK. Returns user profile detail for id given.| ![screenshot](/documentation/testing/postman_testinguserdetail.png)|
| Token refresh | 200 OK Returns new access token| ![screenshot](/documentation/testing/postman_testing_tokenrefresh.png)|
| Game List | Logged out - 403 Not Authenticated| ![screenshot](/documentation/testing/postman_testinggamelist_loggedout.png)|
| Game List | Logged in - 200 OK| ![screenshot](/documentation/testing/postman_testinggamelist_loggedin.png)|
| Game Create | Logged out - 403 Not Authenticated| ![screenshot](/documentation/testing/postman_testinggamecreate_loggedout.png)|
| Game Create | Logged in - 201 Created| ![screenshot](/documentation/testing/postman_testinggamecreate_loggedin.png)|


## User Story Testing

| User Story | Screenshot |
| --- | --- |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test register `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the tests that I have created:

| File | Coverage | Screenshot |
| --- | --- | --- |

#### Unit Test Issues

Return to the [README.md](README.md) file.