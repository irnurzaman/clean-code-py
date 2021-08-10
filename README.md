# clean-code-py
This project is inspired by clean code architecture. Clean code architecture is the way we design our software with separation of concern in mind. The details about it is here https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html.

## Folder Structure
```sh
.
└── services
    ├── nasabah
    │   ├── api
    │   ├── app
    │   ├── entities
    │   ├── models
    │   ├── repository
    │   └── main.py
    └── rekening
        ├── api
        ├── app
        ├── entities
        ├── models
        ├── repository
        └── main.py
```
- `api` folder is place for our services API module. This module is responsible for receiving, validating, processing requests and parsing responses. The API could be REST API, gRPC, graphql, websocket, tcp or anything else.
- `app` folder is place for our service main logic. This module is responsible for main logic for our business process. This module doesn't know anything about how the data stored and how the data represented.
- `entites` folder is place for our service data models. This is module store the shape of our data.
- `models` folder is place for our service request/response models. This module store the shape of our requests and responses based on business processes
- `repository` folder is place for our service database driver. This module is responsible for storing and retrieving data. There is no business logic in here.
- `main.py` is our runner script. This script is responsible construct every dependencies and run the service. This is our service entrypoint.