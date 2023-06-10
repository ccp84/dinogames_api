# DRF API code repository for Dinosaur Games Library

## Concept

The Dinosaur Games Library operates to provide social events where members can come along and play library games with other members. The online library portal provides staff the ability to maintain an up to date list of the games available to be played at social nights, and keep members informed of the latest news and events for the group. Members are able to view and search the library, and review the games they have played providing a resource for other members and site visitors to look up new games they might want to play. All members and site visitors can also see the latest admin announcements for social events and news items about the library. 

This repository will hold the data and user accounts for the project and provide API endpoints allowing a front end application to connect to this data in a user friendly manner. The endpoints provided by this API are intended to be connected to programatically by a front end application and not directly accessed by the end user.

## Scope

* It will allow site visitors to view the game library to search for a game to play
* It will allow site visitors to create an annount and become a registered member
* It will allow registered members to edit their account details
* It should allow registered members to leave a review of games they have played for others to see
* It should allow registered members to edit the details of reviews they have written
* It could allow registered members to leave a thumbs up or thumbs down rating for games that they have played
* It will allow staff members to add new games to the library
* It will allow staff members to edit the library game details
* It should allow staff members to post news and events announcements
* It should allow site visitors to view news and events announcements that have been posted

Using MoSCoW prioritisation these functions have been prioritised as 'must have', 'should have', 'could have' and have been turned into user stories to create the [project board](https://github.com/users/ccp84/projects/5/views/1?reload=true). Any remaining features outside of this project's timeframe will be moved to 'won't have', and in production would become part of the next release or future features.

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
| profileicon | CharField | max_length 25, populated by ICON_CHOICES which are all related the their linked FontAwesome icon on the React front end, default=dice |
| is_staff | BooleanField | default=False |
| is_active | BooleanField | default=True |

The profilepic field from this model is no longer used by the front end app and was replaced in use by profileicon however has been left in for futureproofing of project development that may move back to a design that reinstates the use of profile images as well as / instead of icons. 

The Game Model

| Field Name | Field Type | Details |
| ---------- | ---------- | ------- |
| id | PrimaryKey | BigAuto Unique |
| title | CharField | max_length 100, unique |
| tags | TextField | blank - A searchable list of key words linked to the game genre or play style |
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

### Custom User Model

I have used a custom user model which replaces the standard Django User model. It was essential that this was the first step in the project before any migrations were made to avoid table conflicts.

The django documentation on customising the base user model is available [here](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model) as well as a full guide from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)

This custom user model negates the need for a separate Profile model to hold the rest of the user data and means one less linkage between models to account for when working with ForeignKeys.

### Dj-rest-auth

For this project I have used the latest version of dj-rest-auth to ensure forward compatibility of code and to allow me to set custom registration serializers as defined in the documentation. I have followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html) for this install process.

### Custom User Serializer

The initial registraion form does not suit my custom user model:

![rest auth register](/documentation/readme/rest_auth_initial_register.png)

I have followed the [rest-auth documentation](https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#) for adding a customised registration serializer. The base of my serializer is built on source code from the dj-rest-auth github repository file [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)

![rest auth custom serializer](/documentation/readme/rest_auth_custom_register.png)

Also included is a serializer for returning user details to the admin only view. 

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

### The Game Model

This model will hold all library game instances. In a change from the planned ERD to make number of players more searchable I have used 2 separate fields for min and max players. To help with slimlining the vast range of game play times that could possibly be returned, the `playtime` field is linked to choices for less than 5 minutes, 5-10, 10-20, 20-40, 40-90 and then anything over an hour and a half. Again these fields will make the games library easier to search and filter for members. 

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

This serializer method checks the id of the currently logged in user and searches the list of ratings for the game for that users id. If there is a rating for that user, it returns the id linked to the rating that user left for that game, if no rating found then it returns a null value. 
* The code for this method is based on the `likes` component of the CI Moments walkthrough. 

`get_rating_value`

Similarly to `get_rating_id` this serializer method checks for a rating listed for the currently logged in user. It returns the value of the rating, either True - thumbs up or False - thumbs down. 
* The code for this method is based on the `likes` component of the CI Moments walkthrough.

`get_playtime_value`

This serializer method returns the human readable value of the `GAME_LENGTH_CHOICES` tuple used to populate `playtime` and is included specifically for the React frontend to use for display purposes. 
* The solution to this display issue was found in the [StackOverflow thread here](https://stackoverflow.com/questions/49414773/returning-the-human-readable-element-of-a-choice-field-in-drf-serializer)


### Game Library Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| games/ | GameList | List | Read only view available to all site visitors for viewing the library. Added onto the queryset are counts for the number of thumbs up and thumbs down ratings for each game. Searching is available on title and tags fields. Sort by id, title, max/min players and playtime. |
| games/<int:pk> | GameDetail | Retrieve | A read only view for all site visitors to view a full game individually. Added onto the queryset are counts for the number of thumbs up and thumbs down ratings for each game. |
| games/create | GameCreate | ListCreate | An admin only read write view for adding new game listings to the library. |
| games/edit/<int:pk> | GameEdit | RetrieveUpdateDestroy | An admin only read edit delete view for making changes to games in the library and deleting listings. |

## Milestone 3 - Player Reviews

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Review model and serializer. * Add view for listing all reviews. * Add endpoint to create new reviews. * Add update and destroy endpoint for review owner. * Filter review list by member | ![sprint3](/documentation/readme/sprint3.png) |

### The Review Model

The Review model holds all reviews written by authorised members of the library. Each review has an author linked to the CustomUser model, game being reviewed linked to the Game model, content of the review and the date and time it was last updated. 

### Review Serializers

The review serializer returned fields:
```python
fields = [
        'id', 'author', 'is_author', 'profileicon',
        'game', 'game_title', 'content', 'lastupdated'
        ]
```

Read only fields : author - author.username, profileicon - author.profileicon

Serializer method fields being used:

`get_is_author`

This method checks if the currently logged in user matches the review author field and returns the result. 

`get_lastupdated`

This method formats `lastupdated` from a string into a readable version of date and time. 

The Review Detail Serializer

This extends everything from the Review serializer, but makes game a read only field so that it cannot be overwritten when editing an instance. 

### Review Component Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| reviews/ | ReviewList | ListCreate | Read endpoint for all site visitors, write endpoint for authenticated members. Includes a save method to add the currently logged in user as the author. Filtering provided by Django Filter Backends, filterable on author and game fields. |
| reviews/author | AuthorList | List | Read endpoint with the queryset filtered by the currently logged in user. Provided as a cleaner access point to a full list of all reviews written by one member than the additional filtering. |
| reviews/<int:pk> | ReviewDetail | RetrieveUpdateDestroy | A read write destroy endpoint for the review author to maintain their reviews. Utilises the custom permission class `IsOwnerOrReadOnly` to manage put and delete actions.  |

### Custom Permission Class

The standard permission classes don't cover specifically granting access only to the author or a resource and so for this purpose a custom permission class was needed. Using the example in the CI Moments walkthrough, and reading further in the DRF documentation [here](https://www.django-rest-framework.org/api-guide/permissions/#examples) I added the permission class `IsOwnerOrReadOnly`.

## Milestone 4 - Announcements

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Announcement model and serializer. * Create Category model. * Add view for listing all announcements. * Add admin only endpoint to create new announcements. * Add update and destroy endpoint for admin users. | ![sprint4](/documentation/readme/sprint4.png) |

### The Announcement Model

The Announcement model holds all admin posts about news and events. Each instance has a category linked to the Category model, title of the article, content of the article, the date and time it was last updated and the author linked to CustomUser.

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

Read only fields : author - returns the username of the user that posted the announcement, profileicon - returns the icon linked to the account of the author, category_title - returns the title of the category the announcement has been tagged with.

Serializer method fields being used:

`get_lastupdated`

This method formats `lastupdated` from a string into a readable version of date and time. 

### Announcement Component Endpoints

| URL | View | View Class | Details |
| --- | ---- | ---------- | ------- |
| announcement/ | AnnouncementList | List | Read only endpoint for site visitors to be able to view all announcements  |
| announcement/admin | AnnouncementCreate | ListCreate | Read write endpoint accessible to admin users only. includes a save method so that the currently logged in user is automatically added as the post author. |
| announcement/admin/<int:pk> | AnnouncementDetail | RetrieveUpdateDestroy | Read write delete endpoint for admin users only to edit and delete announcement instances. Includes a save method so that the currently logged in user is added as the post author incase a different member of staff to the original author edits the announcement. |

## Milestone 5 - Ratings

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Ratings model and serializer. * Add authenticated view for creating ratings. * Link Game component to view ratings. * Add update view for author of rating. | ![sprint5](/documentation/readme/sprint5.png) |

### The Ratings model

The ratings model has an author linked to CustomUser, game being rated linked to the Game model, and a boolean rating for thumbs up or thumbs down. It also has a unique requirement for one author only being able to rate a game once. 

In order for this component to work, additional fields have also been added to the Game component above.

### Ratings Serializer

Fields returned by the serializer:
```python
fields = [
        'id', 'author', 'game', 'game_title', 'rating'
        ]
```

Read only fields : author - author.username, game_title - game.title

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
| ratings/<int:pk> | RatingDetail | RetrieveUpdateDestroy | Read edit delete endpoint for instance owner to edit and remove the ratings they have left. |

## Future Features

## Testing

## Deployment

## Technologies Used

## Credits

### Documentation and additonal tutorials

* I Followed the DRF documentation [here](https://www.django-rest-framework.org/tutorial/quickstart/#project-setup) as a reminder of the steps needed to start the project.
* To create the custom user model and user management I used both the [django documentation](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example) as well as tutorials from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)
* For use of dj-rest-auth I followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
* Serializing date time field https://www.django-rest-framework.org/api-guide/fields/#datetimefield
* To return a filtered list of reviews specific to the logged in user I followed the [DRF guide to using backend filters here](https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend)
* To add the extra fields to the Game queryset for calculating and returning numbers of thumbs up and thumbs down ratings, I read the topics listed in the documentation [here as an overview of aggregation](https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#cheat-sheet) and also [this part of the documentation](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#std-fieldlookup-exact) for producing the correct SQL query string. 

### Code used from other sources

* Custom serializer built from the base code of the rest-auth repository [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)
* Custom permission class `IsOwnerOrReadOnly` taken from the DRF documentation [here](https://www.django-rest-framework.org/api-guide/permissions/#examples)

### Media and images

### Honourable mentions
