# DRF API code repository for Dinosaur Games Library

## Concept

The Dinosaur Games Library operates to provide social events where members can come along and play library games with other members. The online library portal provides staff with the ability to maintain an up-to-date list of the games available to be played at social nights and keep members informed of the latest news and events for the group. Members can view and search the library, and review the games they have played providing a resource for other members and site visitors to look up new games they might want to play. All members and site visitors can also see the latest admin announcements for social events and news items about the library. 

This repository will hold the data and user accounts for the project and provide API endpoints allowing a front-end application to connect to this data in a user-friendly manner. The endpoints provided by this API are intended to be connected to programmatically by a front-end application and not directly accessed by the end user. For the React frontend repository please look [here](https://github.com/ccp84/dinogames_react/).

The deployed API can be viewed [here](https://dinogames-api.herokuapp.com/) 

## Scope

* It will allow site visitors to view the game library to search for a game to play
* It will allow site visitors to create an account and become a registered member
* It will allow registered members to edit their account details
* It should allow registered members to leave a review of games they have played for others to see
* It should allow registered members to edit the details of reviews they have written
* It could allow registered members to leave a thumbs up or thumbs down rating for games that they have played
* It will allow staff members to add new games to the library
* It will allow staff members to edit the library game details
* It should allow staff members to post news and events announcements
* It should allow site visitors to view news and events announcements that have been posted
* It could allow staff members to post detailed social event invitations
* It could allow registered members to list the games they would like to be available to play at social events

Using MoSCoW prioritisation these functions have been prioritised as 'must have', 'should have', and 'could have' and have been turned into user stories to create the [project board](https://github.com/users/ccp84/projects/5/views/1). 

Estimated story points have been added to each User Story and Task as [Xsp] to aid time considerations in each sprint.

Any remaining features outside of this project's timeframe will be moved to 'won't have', and in production would become part of the next release or future features.

## Data Model

The ERD outline provided here gives an overview of the project vision. The models represent different components of the project and so will be worked through progressively adding to the functionality as each milestone is achieved. 

![ERD](/documentation/readme/ERD.png)

### Database Schema 

The CustomUser Model

| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| username | CharField | max_length 100, unique |
| email | EmailField | required |
| firstname | CharField | max_length 100, required |
| lastname | CharField | max_length 100, required |
| profileicon | CharField | max_length 25, populated by ICON_CHOICES which are all related to their linked FontAwesome icon on the React front end, default=dice |
| is_staff | BooleanField | default=False |
| is_active | BooleanField | default=True |

The profilepic field from this model is no longer used by the front-end app and was replaced in use by profileicon however has been left in for futureproofing of project development that may move back to a design that reinstates the use of profile images as well as / instead of icons. 

The Game Model

| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| title | CharField | max_length 100, unique |
| tags | TextField | blank - A searchable list of keywords linked to the game genre or play style |
| overview | TextField | blank - More detailed description of the game | 
| minplayers | IntegerField | default=1 |
| maxplayers | IntegerField | default=4 |
| playtime | IntegerField | populated by GAME_LENGTH_CHOICES to give a set number of game playtime results for search and filter purposes, default=0 "0-5 minutes" |

The Review Model

| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| author | ForeignKey | Link to CustomUser, the user account linked to the author of the review |
| game | ForeignKey | Link to Game, the game that is being reviewed |
| content | TextField |  |
| lastupdated | DateTimeField | auto_now, tracking when the review was last modified | 

The Announcement Model

| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| category | ForeignKey | Link to Category, default=1 (News), defines the type of announcement currently News or Events |
| title | CharField | max_length 100 |
| content | TextField |  |
| lastupdated | DateTimeField | auto_now, tracking of when the article was last modified | 
| author | ForeignKey | link to CustomUser, protect on delete | 

The Category Model

| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| title | CharField | max_length 50, holds announcements categories as this is easier to update in the future than a choice list for adding further categories | 

The Rating Model
| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| author | ForeignKey | link to CustomUser, the user account of the member who created the rating |
| game | ForeignKey | link to Game, the game the user is leaving a rating for | 
| rating | BooleanField | blank = not yet rated, True = thumbs up, False = thumbs down |

## Project Development

## Milestone 1 - User Accounts

| Tasks This Sprint | Sprint Overview|
| ----------------- | -------------- |
| Project Setup, Create Custom user model and serializers, make signup endpoint available to all users, set up JWT, make login endpoint available to all users, make token refresh endpoint available to authenticated users, make logout endpoint available to deny further token refreshes | ![sprint 1 screenshot](/documentation/readme/sprint1.png) |

| User Stories This Milestone | Backend Acceptance Criteria |
| --------------------------- | --------------------------- |
| As a visitor to the site I want to be able to create an account so that I can access the full membership features | Custom user model is created in DRF, API endpoint for account creation is exposed and accessible to all site visitors |
| As a member I want to be able to log into my account so that I can access the full features of the library. | Login endpoint is available to connect to at the API, JWT exchange is set up at the API to allow for stateless authentication |
| As a member I want to be able to log out of my account to keep my data secure. | Logout endpoint is reachable to send requests to |

### Custom User Model

I have used a custom user model which replaces the standard Django User model. This needed to be the first step in the project before any migrations were made to avoid table conflicts.

The Django documentation on customising the base user model is available [here](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model) as well as a full guide from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)

This custom user model negates the need for a separate Profile model to hold the rest of the user data and means one less linkage between models to account for when working with foreign keys.

### Dj-rest-auth

For this project, I have used the latest version of DJ-rest-auth to ensure forward compatibility of code and to allow me to set custom registration serializers as defined in the documentation. I have followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html) for this installation process.

### Custom User Serializer

The initial registration form does not suit my custom user model:

![rest auth register](/documentation/readme/rest_auth_initial_register.png)

I have followed the [rest-auth documentation](https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#) for adding a customised registration serializer. The base of my serializer is built on source code from the DJ-rest-auth GitHub repository file [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)

![rest auth custom serializer](/documentation/readme/rest_auth_custom_register.png)

Also included is a serializer for returning user details to the admin-only view. 

### User Account Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| dj-rest-auth/ |  |  |  Standard dj-rest-auth url includes from the library |
| dj-rest-auth/registration/ |  |  |  Standard registration urls from the allauth library | 
| user/<int:pk> | UserDetail | RetrieveUpdate | Admin only permission to view and update all user accounts |


## Milestone 2 - Game Library

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| Create Game model and serializers. Add CreateList, RetrieveUpdateDestroy endpoints for admin and Listview endpoint for all. | ![sprint2](/documentation/readme/sprint2.png) |

| User Stories This Milestone | Backend Acceptance Criteria |
| --------------------------- | --------------------------- |
| As a member of staff I want to be able to add games to the library so that site visitors can see what games are available to play | Game model is created in DRF backend, Create game endpoint available and accepts authenticated data requests and saves to the game table, POST endpoint is available and rejects connections without authentication headers, Created games are listed in the games library |
| As a member of staff I want to be able to edit listed games so that the details are always accurate and up to date | Detailed View is available from the API, PUT endpoint is accessible and accepts requests from the admin users |
| As a member of staff I want to be able to delete a game from the library so that any old games no longer available are removed from the list | Delete endpoint is accessible to admin accounts, and the Game instance is successfully deleted from the library |
| As a member I want to be able to see all of the games available in the library so that I can read the reviews and look for games I might like | The API returns a full list of games available from the Game table |
| As a member I want to be able to search the library by game feature so that I can pick out the games most suited to my interests | Search and filter set up on the API endpoint |

### The Game Model

This model will hold all library game instances. In a change from the planned ERD to make the number of players more searchable I have used 2 separate fields for min and max players. To help with slim lining the vast range of gameplay times that could be returned, the `playtime` field is linked to choices for less than 5 minutes, 5-10, 10-20, 20-40, 40-90 and then anything over an hour and a half. Again these fields will make the games library easier to search and filter for members. 

### Game Serializer

Fields returned from the serializer:
```python
fields = [
    'id', 'title', 'tags', 'minplayers', 'maxplayers',
    'playtime', 'playtime_name', 'overview', 'rating_id',
    'rating_value', 'thumbsup', 'thumbsdown',
    ]
```

Additional serializer methods being used:

`get_rating_id`

This serializer method checks the id of the currently logged-in user and searches the list of ratings for the game for that user's id. If there is a rating for that user, it returns the id linked to the rating that the user left for that game, if no rating is found then it returns a null value. 
* The code for this method is based on the `likes` component of the CI Moments walkthrough. 

`get_rating_value`

Similarly to `get_rating_id` this serializer method checks for a rating listed for the currently logged-in user. It returns the value of the rating, either True - thumbs up or False - thumbs down. 
* The code for this method is based on the `likes` component of the CI Moments walkthrough.

`get_playtime_value`

This serializer method returns the human readable value of the `GAME_LENGTH_CHOICES` tuple used to populate `playtime` and is included specifically for the React frontend to use for display purposes. 
* The solution to this display issue was found in the [StackOverflow thread here](https://stackoverflow.com/questions/49414773/returning-the-human-readable-element-of-a-choice-field-in-drf-serializer)


### Game Library Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| games/ | GameList | List | Read-only view available to all site visitors for viewing the library. Added onto the queryset are counts for the number of thumbs up and thumbs down ratings for each game. Searching is available on title and tags fields. Sort by id, title, max/min players and playtime. |
| games/<int:pk> | GameDetail | Retrieve | A read-only view for all site visitors to view a full game individually. Added onto the queryset are counts for the number of thumbs up and thumbs down ratings for each game. |
| games/create | GameCreate | ListCreate | An admin-only read-write view for adding new game listings to the library. |
| games/edit/<int:pk> | GameEdit | RetrieveUpdateDestroy | An admin-only read edit delete view for making changes to games in the library and deleting listings. |

## Milestone 3 - Player Reviews

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Review model and serializer. * Add view for listing all reviews. * Add endpoint to create new reviews. * Add update and destroy endpoint for review owner. * Filter review list by member | ![sprint3](/documentation/readme/sprint3.png) |

| User Stories This Milestone | Backend Acceptance Criteria |
| --------------------------- | --------------------------- |
| As a library member I want to be able to review games that I have played so that other members can find out if they might want to play that game | Reviews model created, POST endpoint created and accessible to authenticated users |
| As a library member I want to be able to edit the reviews I have left so that I can change any errors or update my opinion at a later date | PUT endpoint accepts requests from instance owner only, Data is successfully updated |
| As a library member I want to be able to delete reviews that I have made so that I can start again if there are too many edits to make or remove opinions I no longer hold. | Destroy endpoint accepts requests from resource owner only |
| As a member I want to be able to see a list of reviews that I have written so that I can remember what I have already reviewed and check they are still relevant | Filtered list endpoint available for reviews written by the logged-in user |
| As a site visitor I want to be able to read reviews of games by people that have already played them so that I can decide if I might want to play that game | API list endpoint available for all with read access |

### The Review Model

The Review model holds all reviews written by authorised members of the library. Each review has an author linked to the CustomUser model, the game being reviewed linked to the Game model, the content of the review and the date and time it was last updated. 

### Review Serializers

The review serializer returned fields:
```python
fields = [
        'id', 'author', 'is_author', 'profileicon',
        'game', 'game_title', 'content', 'lastupdated'
        ]
```

Read-only fields: author - author.username, profileicon - author.profileicon

Serializer method fields being used:

`get_is_author`

This method checks if the currently logged-in user matches the review author field and returns the result. 

`get_lastupdated`

This method formats `lastupdated` from a string into a readable version of the date and time. 

The Review Detail Serializer

This extends everything from the Review serializer but makes game a read-only field so that it cannot be overwritten when editing an instance. 

### Review Component Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| reviews/ | ReviewList | ListCreate | Read endpoint for all site visitors, write endpoint for authenticated members. Includes a save method to add the currently logged-in user as the author. Filtering provided by Django Filter Backends, filterable on author and game fields. |
| reviews/author | AuthorList | List | Read endpoint with the queryset filtered by the currently logged-in user. Provided as a cleaner access point to a full list of all reviews written by one member than the additional filtering. |
| reviews/<int:pk> | ReviewDetail | RetrieveUpdateDestroy | A read-write destroy endpoint for the review author to maintain their reviews. Utilises the custom permission class `IsOwnerOrReadOnly` to manage put and delete actions.  |

### Custom Permission Class

The standard permission classes don't cover specifically granting access only to the author or a resource and so for this purpose, a custom permission class was needed. Using the example in the CI Moments walkthrough, and reading further in the DRF documentation [here](https://www.django-rest-framework.org/api-guide/permissions/#examples) I added the permission class `IsOwnerOrReadOnly`.

## Milestone 4 - Announcements

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Announcement model and serializer. * Create Category model. * Add view for listing all announcements. * Add admin-only endpoint to create new announcements. * Add update and destroy endpoint for admin users. | ![sprint4](/documentation/readme/sprint4.png) |

| User Stories This Milestone | Backend Acceptance Criteria |
| --------------------------- | --------------------------- |
| As an admin user I want to create announcements so that I can update site visitors about events happening in the library | News model is created in DRF, Category model is created in DRF, A CreateAPI view is available that is accessible to admin-only |
| As an admin user I want to be able to edit existing announcements so that they will always be up to date if the details change | PUT endpoint accessible to admin users only, Edits are successfully saved |
| As an admin user I want to be able to delete announcements so that events and updates that are no longer relevant can be removed | Destroy endpoint accessible to admin users only |
| As a visitor to the site I want to be able to read all of the latest announcements so that I can find out about events that are happening in the library | ListAPI endpoint is available for read-only access to all site visitors, Announcements are listed in reverse chronological order |

### The Announcement Model

The Announcement model holds all admin posts about news and events. Each instance has a category linked to the Category model, the title of the article, the content of the article, the date and time it was last updated and the author linked to CustomUser.

### The Category Model

The Category model very simply has a title. This is the category for the announcement being posted and has been developed this way as it is easier to extend the available categories for announcement posts via a linked table than it is to extend a choice field and tuple list. Future project development could allow new categories to be added from the front end. 

### Announcement Serializer

Fields returned by the serializer:
```python
fields = [
        'id', 'category', 'category_title', 'title',
        'content', 'lastupdated', 'author', 'profileicon'
        ]
```

Read-only fields: author - returns the username of the user that posted the announcement, profileicon - returns the icon linked to the account of the author, category_title - returns the title of the category the announcement has been tagged with.

Serializer method fields being used:

`get_lastupdated`

This method formats `lastupdated` from a string into a readable version of the date and time. 

### Announcement Component Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| announcement/ | AnnouncementList | List | Read-only endpoint for site visitors to be able to view all announcements  |
| announcement/admin | AnnouncementCreate | ListCreate | Read write endpoint accessible to admin users only. includes a save method so that the currently logged-in user is automatically added as the post author. |
| announcement/admin/<int:pk> | AnnouncementDetail | RetrieveUpdateDestroy | Read write delete endpoint for admin users only to edit and delete announcement instances. Includes a save method so that the currently logged-in user is added as the post author in case a different member of staff to the original author edits the announcement. |

## Milestone 5 - Ratings

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Ratings model and serializer. * Add authenticated view for creating ratings. * Link the Game component to view ratings. * Add an update view for the author of the rating. | ![sprint5](/documentation/readme/sprint5.png) |

| User Stories This Milestone | Backend Acceptance Criteria |
| --------------------------- | --------------------------- |
| As a member I want to be able to add a thumbs up or thumbs down rating so that other users can see if they might want to play the game. | Ratings model created in DRF backend, POST endpoint available to all authenticated members |
| As a user I want to be able to edit the rating I have left so that I can update my opinion if I change my mind. | PUT endpoint available to the author of the rating |
| As a member I want to see the games I have rated so that I can pick out games I have already enjoyed playing to play again. | Retrieve endpoint available that filters ratings by the member that made them |
|As a site visitor I want to be able to see ratings left by other people so that I know if I might want to play that game or not. | GET endpoint filtered by game available to return a list of all ratings |

### The Ratings model

The ratings model has an author linked to CustomUser, the game being rated linked to the Game model, and a boolean rating for thumbs up or thumbs down. It also has a unique requirement for one author only being able to rate a game once. 

For this component to work, additional fields have also been added to the Game component above.

### Ratings Serializer

Fields returned by the serializer:
```python
fields = [
        'id', 'author', 'game', 'game_title', 'rating'
        ]
```

Read-only fields: author - author.username, game_title - game.title

Additional methods being used:

Return an error message instead of a standard server 500 message if a user tried to create more than one rating instance.
```python
try:
    return super().create(validated_data)
except IntegrityError:
    raise serializers.ValidationError({
        'detail': 'You can only rate a game once'
})
```
* Code based on the CI Moments Walkthrough project

### Ratings Component Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| ratings/ | RatingList | ListCreate | Read endpoint for all site visitors, write endpoint for authenticated members to add thumbs up/down ratings to games. Makes use of Django Filter Backend to filter by game, rating and author. Sorting by ratings. |
| ratings/<int:pk> | RatingDetail | RetrieveUpdateDestroy | Read edit delete endpoint for the instance owner to edit and remove the ratings they have left. |

## Future Features

* The Requests component - allowing members to request new games to be added to the library. This feature would utilise the thumbs up/down ratings component to allow other members to upvote requests to the top of the list to vote for the next new game to be added. 
* Adding a swagger or similar landing page to the API for developers to be able to navigate the endpoints easily so that the developer in charge of updating front-end connections can understand the data flow. 

## Testing

Link to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://dinogames-api.herokuapp.com).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: c25k).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online because Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | user's own value |

Heroku needs two additional files to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
        - `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "user's own value")
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/ccp84/dinogames_api) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
        - `git clone https://github.com/ccp84/dinogames_api.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ccp84/dinogames_api)

Please note that to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ccp84/dinogames_api)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


## Technologies Used  
### This project is built on the following languages and frameworks

* Python
* Django
* DRF

### Libraries included in this project

* cloudinary
* coverage
* dj-database-url
* dj-rest-auth
* django-allauth
* django-cloudinary-storage
* django-cors-headers
* django-filter
* djangorestframework-simplejwt
* gunicorn
* Pillow
* psycopg2

### Other tools used as a developer

* Git - Version control and project flow management
* GitHub - Cloud hosting of project files
* Heroku - Cloud hosting of deployed project
* Cloudinary - Cloud storage for static files
* SQlite - Development and testing SQL server
* Elephant Sql - Live hosted Postgresql project database
* Lucid - Used to create ERD
* paint.net - Used for image manipulation
* CI Python Linter - Used to validate my Python code.

## Credits

### Documentation and additional tutorials

* I Followed the DRF documentation [here](https://www.django-rest-framework.org/tutorial/quickstart/#project-setup) as a reminder of the steps needed to start the project.
* To create the custom user model and user management I used both the [django documentation](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example) as well as tutorials from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)
* For use of DJ-rest-auth I followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
* Serializing date time field https://www.django-rest-framework.org/api-guide/fields/#datetimefield
* To return a filtered list of reviews specific to the logged-in user I followed the [DRF guide to using backend filters here](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend)
* To add the extra fields to the Game queryset for calculating and returning numbers of thumbs up and thumbs down ratings, I read the topics listed in the documentation [here as an overview of aggregation](https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#cheat-sheet) and also [this part of the documentation](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#std-fieldlookup-exact) for producing the correct SQL query string. 

### Code used from other sources

* Custom serializer built from the base code of the rest-auth repository [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)
* Custom permission class `IsOwnerOrReadOnly` taken from the DRF documentation [here](https://www.django-rest-framework.org/api-guide/permissions/#examples)

### Honourable mentions
* With thanks to my mentor Lauren Popich for her advice and guidance throughout this project
* My fellow June '22 cohort students for their ongoing support
