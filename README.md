# **Ebook Management**
This is a small project for _Ebook management_ using **REST API** with **Django** and **SQLite**
This Ebook management includes 2 models
- User model
- Ebook model

for **User** Model we user the default django user model and created one **Ebook** model
The Ebook model has the following fields
- Title (text)
- Author (text)
- Genre (list of Fantasy, Literary, Mystery, Non-Fiction, Science Fiction, and Thriller)
- Review (1-5 stars)
- Favorite? (boolean)

## project
to use the restapi in your project you need to intall the restframework package first
**pip install djangorestframework**
then we need to include that in your installed apps list
after that we created the **ModelSerializer** in **serializers.py** file.
then we import that serializers to the views
we use the **class based views** to create the api's.
we can save and retrive datas to and from the model using the get and post method.Here i use the postman platform to perform the operations
after run the server using the below urls to perform the operations
- 127.0.0.1:8000/ap/ -to add new Ebook

the filter operation is performed on the basics of review rate do we need to use the url
- 127.0.0.1:8000/ap/all/?search=5 - will return all the Ebook having rating 5
## Token Authentication
In this project we Token authentication to authenticate the user. when ever a user is created using username and password a new token will generate and password will be saving as hashpassword 



