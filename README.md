
## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and install these requirements 

```console
pip i pymongo fastapi uvicorn python-dotenv


```
2. Add .env file in to the project

 ```console

CONNECTION_STRING = mongodb+srv://username:password@cluster0.zvyixqc.mongodb.net/InvizLabsAssignment-backend?retryWrites=true&w=majority


```
2. Start the application:

```console
python -m uvicorn index:app --reload
```

