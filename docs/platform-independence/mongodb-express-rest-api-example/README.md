# MongoDB Alternatives

This repository is a copy of the
[mongodb-express-rest-api-example](https://github.com/mongodb-developer/mongodb-express-rest-api-example),
pre-configured to use FerretDB or DocumentDB instead of MongoDB.

* [FerretDB](https://www.ferretdb.io/) is an open source alternative to MongoDB using PostgreSQL as a backing database.
* [DocumentDB](https://documentdb.io/) an  open source and MIT licensed, with native BSON, advanced indexing, and vector
  search on PostgreSQL.

> [!NOTE]
>
> The aim is to demonstrate an open source alternative to MongoDB. Make sure you test your application as some feature
> may not be available yet.

## How To Run

1. Make sure you have [`docker`](https://docs.docker.com/engine/install) and [`docker
   compose`](https://docs.docker.com/compose/install) installed and configured.
2. Clone this repository.
3. Move into the `mongodb-express-rest-api-example` folder in your terminal.
4. Execute the `docker compose up` command.
5. Wait (watch the logs).

The system will download the necessary Docker images, execute `npm install` and run the development environment. After
the system starts, you should be able to access the application at http://localhost:3000.

## Using DocumentDB Instead of FerretDB

[DocumentDB](https://github.com/documentdb/documentdb) is an open source (MIT license) MongoDB compatible document
database built on PostgreSQL. The `docker-compose.documentdb.yml` file runs the same application against DocumentDB, no
application code changes are needed, only configuration.

Follow the same steps as above, but start the system with:

```bash
docker compose -f docker-compose.documentdb.yml up
```

Differences compared to the FerretDB setup:

- A single `documentdb-local` container (PostgreSQL + DocumentDB extensions + gateway) replaces the `postgres` and
  `ferretdb` containers.
- The gateway listens on port `10260` and serves TLS with a self-signed certificate, so the connection string uses
  `tls=true&tlsAllowInvalidCertificates=true`.
- Authentication uses `SCRAM-SHA-256` (FerretDB 1.x used `PLAIN`). The user is created on first start from the
  `USERNAME` and `PASSWORD` environment variables.

```
mongodb://username:password@documentdb:10260/?tls=true&tlsAllowInvalidCertificates=true&authMechanism=SCRAM-SHA-256
```

The image includes `mongosh`, so you can inspect the data with:

```bash
docker compose -f docker-compose.documentdb.yml exec documentdb mongosh --tls --tlsAllowInvalidCertificates -u username -p password mongodb://localhost:10260/
```

> [!NOTE]
>
> Tested with DocumentDB `v0.117-0` (`ghcr.io/documentdb/documentdb/documentdb-local:pg17-0.117.0`). Credentials are hardcoded for demo purposes only, do not use them in production.

## Demo

https://github.com/DPGAlliance/dpg-resources/assets/178474/52c94e03-fbb2-4991-8244-cb0f654f6c1b

## License

Apache License 2.0
