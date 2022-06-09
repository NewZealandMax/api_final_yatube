# api-yatube
## _Introduction_
Yatube API provides simple interface for apllications to get information about groups, publications, comments and follows in social network. It also allows to publish and edit posts with commentaries and follow users.
Edit and delete actions are available only for authors.

## _Authentication_
1. To get JWT-token send POST to
```
api/v1/jwt/create/
```
using fields "username" and "password":
```
{
    "username": "ElonMusk",
    "password": "LetsgotoMars!!!111"
}
```
Response samples:
```
{
    "refresh": "string",
    "access": "string"
}
```
2. To refresh JWT-token send POST to
```
api/v1/jwt/refresh/
```
using field "refresh":
```
{
    "refresh": "string",
}
```
Response samples:
```
{
    "access": "string"
}
```
3. To verify JWT-token send POST to
```
api/v1/jwt/verify/
```
using field "token":
```
{
    "token": "string",
}
```

## _Endpoints_
### 1. Groups
1.1. Retrieving list with information about all groups (GET):
```
api/v1/groups/
```
Response example:
```
[
    {
        "id": 1,
        "title": "Группа котиков",
        "slug": "cats",
        "description": "Это группа котиков"
    },
    {
        "id": 2,
        "title": "Группа пёсиков",
        "slug": "dogs",
        "description": "Это группа пёсиков"
    }
]
```
1.2. Retrieving group detail (GET):
```
api/v1/groups/{group_id}/
```
Response example:
```
{
    "id": 1,
    "title": "Группа котиков",
    "slug": "cats",
    "description": "Это группа котиков"
}
```
### 2. Posts
2.1. Retrieving list with information about all posts (GET):
```
api/v1/posts/
```
Pagination is implemented.
Parameters:
- "limit" (posts per page)
- "offset" (offset of pages)
Response example:
```
[
    {
        "id": 2,
        "text": "Пост для котиков",
        "pub_date": "2022-05-29T07:20:56.174825Z",
        "author": "NewZealand",
        "image": null,
        "group": 1
    },
    {
        "id": 3,
        "text": "Пост для пёсиков",
        "pub_date": "2022-05-30T16:01:40.452363Z",
        "author": "admin",
        "image": null,
        "group": 2
    }
]
```
2.2. Publishing post (POST). Anonimous access denied.
```
api/v1/posts/
```
Fields:
- "text": "some text"
- "group": group_id (not nessesary)

Request samples:
```
{
    "text": "My text post",
    "group": 1
}
```
Response samples:
```
{
    "id": 4,
    "text": "My text post",
    "pub_date": "2022-05-30T16:14:44.248441Z",
    "author": "admin",
    "image": null,
    "group": 1
}
```
2.3. Post detail information and actions (GET, PUT, PATCH, DELETE):
```
api/v1/posts/{post_id}/
```
GET requests are available for all authenticated users and other are only for content's author.
Fields (PUT, PATCH):
- "text": "some text"
- "group": group_id

### 3. Commentaries
3.1. Retrieving list with all comments of particular post (GET):
```
api/v1/posts/{post_id}/comments/
```
Response example for api/v1/posts/2/comments/:
```
[
    {
        "id": 1,
        "author": "NewZealand",
        "post": 2,
        "text": "Комментарий для котиков",
        "created": "2022-05-29T09:17:45.580914Z"
    },
    {
        "id": 2,
        "author": "NewZealand",
        "post": 2,
        "text": "Комментарий для котиков метод put",
        "created": "2022-05-29T09:23:18.681353Z"
    }
]
```
3.2. Add comment (POST). Anonimous access denied.
```
api/v1/posts/{post_id}/comments/
```
Fields:
- "text": "some text"

POST request to api/v1/posts/3/comments/:
```
{
    "text": "My commentary"
}
```
Correspondent response:
```
{
    "id": 4,
    "author": "admin",
    "post": 3,
    "text": "My commentary",
    "created": "2022-05-30T16:22:53.088396Z"
}
```
3.3. Commentary detail information and actions (GET, PUT, PATCH, DELETE):
```
api/v1/posts/{post_id}/comments/{comment_id}/
```
GET requests are available for all authenticated users and other are only for content's author.
Fields (PUT, PATCH):
- "text": "some text"

### 4. Followings
4.1. Retrieving all followings of user (GET). Anonimous access denied.
```
api/v1/follow/
```
Searching by "following" field is enabled.
Response samples:
```
[
    {
        "user": "string",
        "following1": "string"
    },
    {
        "user": "string",
        "following2": "string"
    }
]
```
4.2. Follow the author (POST). Anonimous access denied.
```
api/v1/follow/
```
Request samples:
```
{
    "following": "string"
}
```
Response samples:
```
{
    "user": "string",
    "following": "string"
}
```

**_Developed by Max Stepanov.
Powered by Python._**
