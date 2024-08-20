# FerretDB as MongoDB Alternative

[FerretDB](https://www.ferretdb.io/) is an open source alternative to MongoDB using PostgreSQL as a backing database. This repository is a copy of the[mongodb-express-rest-api-example](https://github.com/mongodb-developer/mongodb-express-rest-api-example), pre-configured to use FerretDB instead of MongoDB.

> [!NOTE]
>
> The aim is to demonstrate an open source alternative to MongoDB. Make sure you test your application with FerretDB as some feature may not be available yet.

## How To Run

1. Make sure you have [`docker`](https://docs.docker.com/engine/install) and [`docker compose`](https://docs.docker.com/compose/install) installed and configured.
2. Clone this repository.
3. Move into the `mongodb-express-rest-api-example` folder in your terminal.
4. Execute the `docker compose up` command.
5. Wait (watch the logs).

The system will download the necessary Docker images, execute `npm install` and run the development environment. After the system starts, you should be able to access the application at http://localhost:3000.

## Demo

https://github.com/DPGAlliance/dpg-resources/assets/178474/52c94e03-fbb2-4991-8244-cb0f654f6c1b

## License

Apache License 2.0