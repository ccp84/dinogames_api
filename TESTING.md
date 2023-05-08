# Testing

## Postman Checking Availability of Endpoints

| Endpoint          | Expected Result                                                          |                                                                     |
| ----------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| User Registration | 201_Created. Returns user details added to the system                    | ![screenshot](/documentation/testing/postman_testingregister.png)   |
| Login             | 200 OK. Returns access token and user profile details                    | ![screenshot](/documentation/testing/postman_testinglogin.png)      |
| Logout            | 200 OK. Removes access and refresh tokens from cookie, no data returned. | ![screenshot](/documentation/testing/postman_testinglogout.png)     |
| User detail       | 200 OK. Returns user profile detail for id given.                        | ![screenshot](/documentation/testing/postman_testinguserdetail.png) |
