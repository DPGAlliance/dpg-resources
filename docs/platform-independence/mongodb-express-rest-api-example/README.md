# FerretDB as MongoDB alternative

[FerretDB](https://www.ferretdb.io/) is an open source alternative to MongoDB using PostgreSQL as backing database.

This repository is a copy of [mongodb-express-rest-api-example](https://github.com/mongodb-developer/mongodb-express-rest-api-example), pre-configured to use FerretDB instead of MongoDB.

NOTE: The aim is to demostrate an open source alternative to MongoDB. Make sure you test your application with FerretDB as some feature may not be available yet.

## Dependencies

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## How To Run

1. Make sure you have `docker` and `docker compose` installed and configured
2. Clone the repository
3. Move to the `mongodb-express-rest-api-example` folder
4. Execute: `docker compose up`
5. Wait (watch logs)

The system will download the necessary Docker images, execute `npm install` and run the development environment.

After the system start, you should be able to access the application at: http://localhost:3000/

## Demo

https://github.com/DPGAlliance/dpg-resources/assets/178474/52c94e03-fbb2-4991-8244-cb0f654f6c1b

## License

Apache License 2.0
