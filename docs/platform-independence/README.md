# Platform Independence Guide

This guide contains more resources and frequently asked questions about the [Platform Independence](https://github.com/DPGAlliance/dpg-resources/wiki/4.-Platform-Independence) requirement for digital public goods.

---

## FAQs

<details>
<summary><b>What does platform independence mean for a DPG?</b></summary>

<br />

When digital public goods have mandatory dependencies (dependencies required for the software to run properly) that create more restrictions than the original license (the license of your product), proving independence from any closed-source or proprietary component(s) and demonstrating the existence of functional, open alternatives that can be used without significant changes to the core product **is required**.
</details>

<details>
<summary><b>Why is platform independence important for DPGs?</b></summary>

<br />

This **ensures digital public goods are accessible** to a wide range of users, adopters, and implementers under clear and open terms, giving choice, freedom, and control to use the solution (both as a whole and its individual components) without any further restrictions that go against the [open source definition](https://opensource.org/osd) and addressing possible concerns for vendor lock-in, transparency of security risks, and other considerations.
</details>

<details>
<summary><b>What could undermine the platform independence of a DPG?</b></summary>

<br />

Any **closed-source or proprietary dependencies** and components that the solution relies on to function properly and that are not available under an [OSI-approved license](https://opensource.org/licenses/). This includes:

- Programming languages and frameworks. 
- Third-party software modules and libraries.
- Database management systems.
- External APIs or data sources.
- Operating systems and runtime environments.
- Other services and utilities.

*_Deployment, testing, validation, CI/CD, containerization, and similar tools are not considered or required to be open source for platform independence._
</details>

<details>
<summary><b>If the solution relies on services or components with a free tier or version, is this enough to comply with platform independence?</b></summary>

<br />

**No**. Platform independence is not about cost, is about the freedom and legal terms on which the different dependencies and components are available.
</details>

## Evidence of Platform Independence

**How can I comply with the platform independence requirement?**

The straightforward answer is only to use open-source components, but we understand that in many cases this might not be the best available option or there is a specific reason to use a certain technology stack. In this sense, the use of closed or proprietary components is allowed as long as there are **open alternatives that can be easily used/swapped** and the feasibility of their implementation is demonstrated. 

It is required that solutions technically demonstrate that someone could use the open alternative(s) without any **significant** refactoring or modification to the source code. In the case it is needed, comprehensive instructions on how to migrate to an open alternative are required.

The solution can take one of the following paths:

1. **Replace the proprietary dependency** (all that are required) for an open alternative with an OSI-approved license. _This is the best option when there are open-source alternatives that provide the same functionality or features._
2. **Create an abstraction layer** for the features and logic that use the proprietary dependencies and allow implementers to choose between this and other open alternatives, removing any platform-specific intricacies. _This is the best option when the available open alternatives do not provide the same level of functionality or have other limitations or you want to provide choices to implementers_.
3. **Create patch/migration instructions** that technically demonstrate the possibility of using or swapping the proprietary dependency for an open alternative, that is publicly available in the source code repository. This must include comprehensive instructions (code + documentation) that allow a developer to easily implement or use an open alternative. _This is the best option when it is not desired to change the main tech stack into production or final versions of the solution, but it still provides a way for implementers to use the open alternative if they choose to do so._

### Examples of Common Dependencies

Here you can find some examples of common dependencies that are closed-source or [source-available](https://en.wikipedia.org/wiki/Source-available_software), but not under an approved OSI license.

<details>
<summary><b>MongoDB</b></summary>
<br />

All versions released after October 16, 2018, including patch fixes for prior versions, use a [Server Side Public License](https://spdx.org/licenses/SSPL-1.0.html) (SSPL), which is not approved or compatible with [OSI's definition](https://opensource.org/osd/) of open source.

If your solution depends directly on MongoDB, to comply with platform independence, please provide an open alternative to this dependency (e.g., FerretDB [Apache License 2.0], PostgreSQL [PostgreSQL License], CouchDB [Apache License 2.0], etc.).

We recommend looking at [FerretDB](https://ferretdb.io) and its migration tools for simpler databases that do not require advanced features offered by MongoDB, as it is compatible with MongoDB drivers and popular MongoDB tools. We have an [example code](./mongodb-express-rest-api-example/) for this migration you can take a look at too.

_Please note that older versions of MongoDB under AGPL 3.0 license are not actively supported and may present real security concerns, so this option is not recommended and could potentially fail indicators 8 "Adherence to Best Practices" and 9A "Data Privacy & Security" of the DPG Standard._
</details>

<details>
<summary><b>ElasticSearch and Kibana</b></summary>
<br />

Starting from version 7.11, Elasticsearch and Kibana have moved from an Apache 2.0 license to a [dual license](https://elastic.co/pricing/faq/licensing) under the [Elastic License](https://spdx.org/licenses/Elastic-2.0.html) and [Server Side Public License](https://spdx.org/licenses/SSPL-1.0.html) (SSPL), which are not approved or compatible with [OSI's definition](https://opensource.org/osd) of open source.

If your solution depends directly on ElasticSearch, to comply with platform independence, please provide an open alternative to this dependency (e.g., OpenSearch [Apache License 2.0], Apache Solr [Apache License 2.0], InfluxDB [MIT License], etc.).
</details>

<details>
<summary><b>Firebase</b></summary>
<br />

While some components of Firebase are open source, the majority of its services and features are proprietary and offered as part of Google's cloud offerings. The open-source components of Firebase are typically related to client-side libraries and SDKs. Core infrastructure and many of the backend services provided by Firebase, such as Firestore, Firebase Authentication, Cloud Messaging (FCM), and Cloud Storage, are not open-source and remain under Google's proprietary control.

If your solution depends directly on Firebase, to comply with platform independence, please provide an open alternative to this dependency (e.g., Supabase [Apache License 2.0], Appwrite [BSD 3-Clause], etc.).
</details>

<details>
<summary><b>Redis</b></summary>
<br />

Starting from Redis v7.4 and all future releases, Redis is moving away from the BSD 3-Clause License to a [dual-license](https://redis.io/blog/redis-adopts-dual-source-available-licensing) model, offering developers the choice between the [Redis Source Available License](https://redis.com/legal/rsalv2-agreement/) version 2 (RSALv2) or the [Server-Side Public License](https://spdx.org/licenses/SSPL-1.0.html) version 1 (SSPLv1), which is not approved or compatible with [OSI's definition](https://opensource.org/osd/) of open source.

If your solution depends directly on Redis, to comply with platform independence, please provide an open alternative to this dependency (e.g., Redict [LGPL-3.0-only], Valkey [BSD 3-Clause], etc.).
</details>


