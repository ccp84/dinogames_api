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

## Postman Checking Availability of Endpoints

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
