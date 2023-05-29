# DRF API code repository for Dinosaur Games Library

## Concept

The Dinosaur Games Library operates to provide social events where members can come along and play library games with other members. The online library portal provides staff the ability to maintain an up to date list of the games available to be played at social nights, and keep members informed of the latest news and events for the group. Members are able to view and search the library, and review the games they have played providing a resource for other members and site visitors to look up new games they might want to play. All members and site visitors can also see the latest admin announcements for social events and news items about the library. 

## Scope

This repository will hold the data and user accounts for the project and provide API endpoints allowing a front end application to connect to this data in a user friendly manner. The endpoints provided by this API are intended to be connected to programatically by a front end application and not directly accessed by the end user.

## Data Model

The ERD provided here gives an overview of the full project vision, this has been broken down with MoSCoW prioritisation and so will be worked through progressively adding to the functionality as each milestone is achieved.

![ERD](/documentation/readme/ERD.png)

## Project Development

## Milestone 1 - User Accounts

| Tasks This Sprint | Sprint Overview|
| ----------------- | -------------- |
| Project Setup, Create Custom user model and serializers, make signup endpoint available to all users, set up JWT, make login endpoint available to all users, make token refresh endpoint available to authenticated users, make logout endpoint available to deny further token refreshes | ![sprint 1 screenshot](/documentation/readme/sprint1.png) |

### Custom User Model

I have used a custom user model which replaces the standard Django User model. It was essential that this was the first step in the project before any migrations were made to avoid table conflicts.

The django documentation on customising the base user model is available [here](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model) as well as a full guide from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)

This custom user model negates the need for a separate Profile model and means one less linkage between models to account for when working with ForeignKeys.

### Dj-rest-auth

For this project I have used the latest version of dj-rest-auth to ensure forward compatibility of code and to allow me to set custom registration serializers as defined in the documentation. I have followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html) for this install process.

The initial registraion form does not suit my custom user model:

![rest auth register](/documentation/readme/rest_auth_initial_register.png)

So I have followed the [rest-auth documentation](https://dj-rest-auth.readthedocs.io/en/latest/configuration.html#) for adding a customised registration serializer. The base of my serializer is built on code from the dj-rest-auth github repository file [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)

![rest auth custom serializer](/documentation/readme/rest_auth_custom_register.png)

## Milestone 2 - Game Library

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| Create Game model and serializers. Add CreateList, RetrieveUpdateDestroy endpoints for admin and Listview endpoint for all. | ![sprint2](/documentation/readme/sprint2.png) |

### The Game Model

This model will hold all member game instances. In a change from the planned ERD to make number of players more searchable I have used 2 separate fields for min and max players. To help with slimlining the vast range of game play times that could possibly be returned, this field is linked to choices for less than 5 minutes, 5-10, 10-20, 20-40, 40-90 and then anything over an hour and a half. Again these fields will make the games library easier to search and filter for members. 

### Viewing the library

All visitors will be able to view but make no changes to the full list of games in the library, authenticated members are able to add to the current list of games. For this a single endpoint can be created using the generic `List` view with the permission class of `IsAuthenticatedOrReadOnly`. 
The serializer extends the standard model serializer class and imports the Game model and all model fields for serialization.

### Detailed view of games

This `Retrieve` endpoint can be accessed by all viewing the library to view a single record from the game table. The permission class of `IsAuthenticatedOrReadOnly` is redundant really as this is a read only endpoint. 

### Editing and deleting a game as an administrator

Deletion of incorrectly added, duplicate and out of print games will be restricted to admin only. This `RetrieveUpdateDestroy` endpoint utilises the more robust permission class of `IsAdminUser` to ensure delete permissions are tightly controlled. 

### Filtering the games library

Sorting:
from rest_framework import generics, filters
filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'id',
        'title',
        'maxplayers',
        'minplayers',
        'playtime',
    ]

searching:
/games/?search=board
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'title',
        'tags',
    ]

## Milestone 3 - Player Reviews

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Review model and serializer. * Add view for listing all reviews. * Add endpoint to create new reviews. * Add update and destroy endpoint for review owner. * Filter review list by member | ![sprint3](/documentation/readme/sprint3.png) |

### The Review Model

### Creating a review

### Editing a review

### Deleting a review

### Listing all reviews for a game
https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
### Listing all reviews for a member
https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend

## Milestone 4 - Announcements

| Tasks this sprint | Sprint Overview |
| ----------------- | --------------- |
| * Create Announcement model and serializer. * Create Category model. * Add view for listing all announcements. * Add admin only endpoint to create new announcements. * Add update and destroy endpoint for admin users. | ![sprint4](/documentation/readme/sprint4.png) |

### The Announcement Model

### The Category Model

### Creating an announcement

### Linking to a category

### Viewing announcements

### Filtering by category

### Editing and deleting announcements

## Credits

### Documentation and additonal tutorials

* I Followed the DRF documentation [here](https://www.django-rest-framework.org/tutorial/quickstart/#project-setup) as a reminder of the steps needed to start the project.
* To create the custom user model and user management I used both the [django documentation](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example) as well as tutorials from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)
* For use of dj-rest-auth I followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)
* Serializing date time field https://www.django-rest-framework.org/api-guide/fields/#datetimefield

### Code used from other sources

* Custom serializer built from the base code of the rest-auth repository [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)
* Custom permission class `IsOwnerOrReadOnly` taken from DRF documentation [here](https://www.django-rest-framework.org/api-guide/permissions/#examples)

### Media and images

### Honourable mentions
