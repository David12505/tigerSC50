# TigerCS50
An interactive yearbook where a user can interact with other user's profile.

- The User can login.
- The User can only view/edit and delete their own profile.
- The User can see an index page of ALL users in the yearbook.
- The User can Search for a Friend by [ name, ..., ect ]
- The User can view another user's profile.
- The User can comment on a friend's profile.
- The User can private message a friend.

## Models:
### User
- id
- email
- username
- password
- first_name
- last_name
- profile_photo
- preferences (comma separated)
- quote

### Comment
- id
- poster_id
- reciever_id
- comment

### Like
- id
- comment_id
- user_id

## Optional Model:
### Message
- id
- messenger_id
- reciever_id
- message

<<<<<<< HEAD
### David:
Hello Everyone


### David:
I added 2 file for the sign_in/sign_up page, also added a master file.
=======
>>>>>>> d08d390407fc17d7119ad8e9867d0528c4b69330
