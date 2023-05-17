# DRF API code repository for Dinosaur Games Library

## Concept

My local boardgames group meet each week with members bringing along their own games to share with the group. This can lead to sometimes a limited selection of games on offer, or not knowing which games other members have that the group would like to play. The Dinosaur Games Library app provides a solution to this by allowing members of the group to list the games that they own and are happy to share in an online library available for other members to view and search. Requests could then be made ahead of social events for particular games that the group would like to play to be brought along that week. Additional features of the app would allow admin users to advertise the group to visitors to the site and publicise social events to gain a wider membership, add important group updates to the front page as these can sometimes be missed in the Facebook group, and allow for an 'add to social' button for games to be automatically requested via the app at a particular social event.

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
| Create Game model and serializers. Add views for create, update, delete, listview and detailed view. Create permissions for post owner. Expose endpoints for create, edit and delete game. Add search and filter for game features. | ![sprint2](/documentation/readme/sprint2.png) |

### The Game Model

This model will hold all member game instances. In a change from the planned ERD to make number of players more searchable I have used 2 separate fields for min and max players. To help with slimlining the vast range of game play times that could possibly be returned, this field is linked to choices for less than 5 minutes, 5-10, 10-20, 20-40, 40-90 and then anything over an hour and a half. Again these fields will make the games library easier to search and filter for members. 

### Viewing the library and creating a listing

All authenticated members will be able to view the full list of games in the library as well as add their own. For this a single endpoint can be created using the generic `ListCreate` view with the permission class of `IsAuthenticated`. 
The serializer extends the standard model serializer class and imports the Game model and all model fields for serialization. 

### Listing games owned by a member

A second list view is included in the urls to filter owned games only. This endpoint uses a filtered queryset.
```python
    def get_queryset(self):
        """
        Override the standard query set and filter
        """
        user = self.request.user
        return Game.objects.filter(owner=user)
```

### Editing and deleting a game listing

This endpoint is restricted to the owner of a game. A custom permission class was needed as DRF doesnt include this level of detail - I have used the example provided in the DRF documentation as a robust and working [example](https://www.django-rest-framework.org/api-guide/permissions/#examples)
It makes use of the generic `RetrieveUpdateDestroyAPIView`. Filtering the query set is not necessary as authenticated members are able to view game details already. The custom permission class ensures that only the game owner can make any changes to the listing and so there is no need to make this view any more complicated. 

### Filtering the games library

## The Reviews Model


## Credits

### Documentation and additonal tutorials

* I Followed the DRF documentation [here](https://www.django-rest-framework.org/tutorial/quickstart/#project-setup) as a reminder of the steps needed to start the project.
* To create the custom user model and user management I used both the [django documentation](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#a-full-example) as well as tutorials from [Very Academy](https://www.youtube.com/watch?v=Ae7nc1EGv-A)
* For use of dj-rest-auth I followed the documentation [here](https://dj-rest-auth.readthedocs.io/en/latest/installation.html)


### Code used from other sources

* Custom serializer built from the base code of the rest-auth repository [here](https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/serializers.py)
* Custom permission class `IsOwnerOrReadOnly` taken from DRF documentation [here](https://www.django-rest-framework.org/api-guide/permissions/#examples)

### Media and images

### Honourable mentions
