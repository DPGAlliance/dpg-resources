# Platform independence

> 💡 Resources & FAQs about platform independence requirements for digital public goods.
> 
### Frequently Asked Questions (FAQs)

**What does platform independence mean for a DPG?**

When digital public goods have mandatory dependencies that create more restrictions than the original license (the license of your product), proving independence from any closed-source or proprietary component(s) and demonstrating the existence of functional, open alternatives that can be used without significant changes to the core product <span style="text-decoration:underline;">is required</span>.

_*Mandatory dependencies are those required for the software to run properly._

**Why is platform independence important for DPGs?**

This <span style="text-decoration:underline;">ensures digital public goods are accessible</span> to a wide range of users, adopters, and implementers under clear and open terms, giving choice, freedom, and control to use the solution (both as a whole and its individual components) without any further restrictions that go against the [open source definition](https://opensource.org/osd/) and addressing possible concerns for vendor lock-in, transparency of security risks and other considerations.

**What could undermine the platform independence of a DPG?**

Any <span style="text-decoration:underline;">closed-source or proprietary dependencies</span> and components that the solution relies on to function properly and that are not available under an [OSI-approved license](https://opensource.org/licenses/). This includes:

* Programming languages and frameworks, 
* Third-party software modules and libraries, 
* Database management systems,
* External APIs or data sources,
* Operating systems and runtime environments,
* Other services and utilities.

_* Deployment, testing, validation, CI/CD, containerization, and similar tools are not considered or required to be open source for platform independence._

**If the solution relies on services or components with a free tier or version, is this enough to comply with platform independence?**

<span style="text-decoration:underline;">No</span>. Platform independence is not about cost, is about the freedom and legal terms on which the different dependencies and components are available.

### Evidence of Platform Independence

**How to comply with the platform independence requirement?**

The straightforward answer is only to use open-source components, but we understand that in many cases this might not be the best available option or there is a specific reason to use a certain technology stack. In this sense, the use of closed or proprietary components is allowed as long as there are <span style="text-decoration:underline;">open alternatives that can be easily used/ swapped</span> and the feasibility of their implementation is demonstrated. 

It is required that solutions technically demonstrate that someone could use the open alternative(s) without any <span style="text-decoration:underline;">significant</span> refactoring or modification to the source code. Or in the case it is needed, comprehensive instructions on how to migrate to an open alternative.

The solution can take one of the following paths:

1. <span style="text-decoration:underline;">**Replace the proprietary dependency**</span> (all that are required) for an open alternative with an OSI-approved license. _This is the best option when there are open-source alternatives that provide the same functionality or features._
2. <span style="text-decoration:underline;">**Create an abstraction layer**</span> for the features and logic that use the proprietary dependencies and allow implementers to choose between this and other open alternatives, removing any platform-specific intricacies. _This is the best option when the available open alternatives do not provide the same level of functionality or have other limitations. Or you want to provide choice to implementers._
3. <span style="text-decoration:underline;">**Create a patch/ migration instructions**</span> that technically demonstrate the possibility of using or swapping the proprietary dependency for an open alternative, and that is publicly available in the source code repository. This must include comprehensive instructions (code + documentation) that allow a developer to easily implement or use an open alternative. _This is the best option when it is not desired to change the main tech stack into production or final versions of the solution, but it still provides a way for implementers to use the open alternative if they choose to do so._

### Examples of Common Dependencies

Here you can find some examples of common dependencies that are closed-source or [source-available](https://en.wikipedia.org/wiki/Source-available_software#:~:text=Source%2Davailable%20software%20is%20software,to%20be%20called%20open%2Dsource.), but not under an approved OSI license.

**MongoDB**

All versions released after October 16, 2018, including patch fixes for prior versions, use a [Server Side Public License](https://www.mongodb.com/licensing/server-side-public-license) (SSPL), which is not approved or compatible with [OSI's definition](https://opensource.org/osd/) of open source.

If the solution depends directly on MongoDB, in order to comply with platform independence, please provide an open alternative to this dependency. For example;  FerretDB (Apache License 2.0), PostgreSQL (PostgreSQL License), CouchDB (Apache License 2.0), and others.

We recommend looking at [FerretDB](https://www.ferretdb.io/) and its migration tools for simpler databases that do not require advanced features offered by MongoDB, as it is compatible with MongoDB drivers and popular MongoDB tools.

_* Please note that older versions of MongoDB under AGPL 3.0 license are not actively supported and may present real security concerns, so this option is not recommended and could potentially fail indicators 8 “Adherence to Best Practices” and 9A “Data Privacy & Security” of the DPG Standard._

**ElasticSearch and Kibana**

As of version 7.11, Elasticsearch and Kibana have moved from an Apache 2.0 license to a [dual license](https://www.elastic.co/pricing/faq/licensing) under the Elastic License and Server Side Public License (SSPL), which are not approved or compatible with [OSI's definition](https://opensource.org/osd/) of open source.

If the solution depends directly on ElasticSearch, in order to comply with platform independence, please provide an open alternative to this dependency. For example; OpenSearch (Apache License 2.0), Apache Solr (Apache License 2.0), InfluxDB (MIT license).

**Firebase**

While some components of Firebase are open source, the majority of its services and features are proprietary and offered as part of Google's cloud offerings. The open-source components of Firebase are typically related to client-side libraries and SDKs. Core infrastructure and many of the backend services provided by Firebase, such as Firestore, Firebase Authentication, Cloud Messaging (FCM), and Cloud Storage, are not open-source and remain under Google's proprietary control.

[Supabase](https://supabase.com/) is an Apache-2.0 license open-source Firebase alternative.
