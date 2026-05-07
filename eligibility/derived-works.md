# Evaluating Derived Works as Digital Public Goods

*A framework for forks, distributions, and related projects*

---

## Purpose

The DPG Registry lists solutions that provide genuine public value. As the ecosystem grows, we receive increasing applications from projects that are derived from — or built on top of — existing DPGs or open-source software. This framework explains how we evaluate those projects.

Our goal is to keep the registry useful and discoverable, while recognizing that meaningful innovations often build on existing foundations.

---

## Who This Applies To

This framework applies to applications where the project is:

- A **fork** — a project that diverges from a parent project's codebase (whether permanently or partially)
- A **distribution** — a curated bundle, configuration, or packaging of an existing project (e.g., a Linux distribution, a CMS distribution)
- A **vertical build** — a specialized implementation of a broader platform tailored to a specific sector or geography

It does not apply to projects that merely reference or integrate with other DPGs as dependencies.

---

## The Central Question

> **Does this project provide meaningful public value that the parent project cannot already provide in its default state?**

If the answer is clearly yes — the project stands on its own. If the answer is unclear or marginal, reviewers will assess it against the three pillars below. If the answer is no, applicants are encouraged to contribute their work upstream and be recognized as contributors to the existing DPG.

---

## Three Pillars of Distinction

A derived project should demonstrate meaningful distinction in at least one of the following areas. These pillars are equal — a strong case in any one of them is sufficient.

| Pillar | What It Means | Illustrative Examples |
|---|---|---|
| **1. Functional Innovation** | The project adds substantial features, APIs, or capabilities not present in the parent project. UI reskins, rebranding, and minor configuration changes do not qualify. | Offline-first data collection mode; integrated national ID verification layer; novel API for cross-sector interoperability |
| **2. Distinct SDG Impact** | The project fundamentally redirects the solution toward an underserved sector, regulatory context, or specific SDG targets that the parent project does not address. | A health records system adapted for refugee camps; a financial inclusion platform designed for informal workers in a specific regulatory environment |
| **3. Operational Independence** | The project has its own clear governance, maintainership, and active community. Close ties to a parent project are acceptable, so long as there are clear lines of accountability and an independent roadmap. | Separate technical steering committee; independent release cycle; distinct community of contributors and implementers |

---

## How We Categorize Derived Projects

Based on our review, derived project applications fall into three categories:

| Category | Description | Outcome |
|---|---|---|
| **Not Eligible** | The project provides little or no distinction from its parent. This includes compatibility rebuilds (projects whose primary goal is replicating another project's releases without modification), rebrands, simple configurations, and deployments that add only local branding or minor policy settings. These projects may represent real value in specific contexts, but they do not meet the threshold for a standalone registry listing. | Not listed |
| **Requires Review** | The project shows some distinction but it is not immediately clear whether it meets the threshold. This typically includes specialized distributions with sector-specific configuration or packaging that goes beyond cosmetic changes, but where the functional or SDG delta needs to be articulated more clearly by the applicant. | Reviewer assessment |
| **Eligible** | The project demonstrates clear, meaningful distinction in at least one of the three pillars. It provides unique value to users and the broader ecosystem that is not already captured by the parent DPG. | Listed |

---

## A Note on Deployments and Digital Sovereignty

We recognize that many governments and institutions create localized deployments of open-source platforms — adding local language packs, security policies, national branding, or procurement configurations. This practice is valuable and represents exactly the kind of digital sovereignty the DPG ecosystem aims to enable.

However, a deployment of a DPG is not the same as a new Digital Public Good. If a government agency configures an existing DPG for local use, we encourage them to:

- Document and share their configuration openly so others can replicate it
- Contribute improvements back to the parent project
- Be listed as an **implementer** of the existing DPG, rather than as a standalone entry

If a local deployment introduces innovations substantial enough to meet the criteria above, it may qualify as a distinct DPG in its own right.

---

## What Applicants Should Provide

If you are applying as a derived project, your application should clearly address the following:

### Relationship to the Parent Project

- What is the upstream or parent project your solution is based on?
- Is this a hard fork (permanent divergence), a maintained fork (tracks upstream with additions), or a distribution/bundle?
- Is your project recognized or endorsed by the parent community?

### Your Meaningful Distinction

- What specific problem does your project solve that the parent project cannot solve in its default state?
- What significant features, configurations, or integrations are unique to your version?
- Which SDGs or development contexts does your project specifically address — and how do these differ from the parent project?

### Governance and Sustainability

- Does your project have its own governance structure, maintainers, and community?
- How do you manage security updates and patches from the parent project?
- Do you contribute improvements back to the upstream project?

---

## Illustrative Archetypes

The following archetypes illustrate how the framework applies. These are generalized examples, not references to specific projects.

| Archetype | Description | Likely Outcome |
|---|---|---|
| **Compatibility Rebuild** | A project whose stated goal is binary or bug-for-bug compatibility with another project — recompiling sources, tracking releases, without independently authoring core logic or configuration. While this provides important access value, the registry should list the root project where integration decisions are made. | Not Eligible |
| **Government Deployment** | A public agency takes an existing DPG and adds local branding, a national language pack, and security policies. The deployment is valuable but is best understood as an implementation of the existing DPG. | Not Eligible (encouraged to be listed as implementer) |
| **Sector-Specific Distribution** | A civil society organization packages an existing platform with substantial domain-specific data models, workflows, and integrations designed for a specific underserved sector. The packaging work itself represents meaningful intellectual property and SDG alignment. | Requires Review → Likely Eligible |
| **Innovating Fork** | A project that started from an existing codebase but has developed independent features, a distinct SDG focus, and its own active governance over time. The functional and mission delta from the parent is clear and substantial. | Eligible |

---

## Our Commitment to Applicants

We understand that the line between a "deployment" and a "distinct DPG" is sometimes genuinely unclear. If your project falls in a gray area, we encourage you to:

- Describe your project's distinction as specifically as possible in your application
- Reach out to the DPGA team for a pre-application conversation
- Consider whether contributing to or co-listing under an existing DPG entry might better serve your goals

Our aim is not to be restrictive but to ensure the registry remains a high-quality resource that genuinely serves those looking for solutions. Projects that do not qualify as standalone DPGs may still be listed as implementations, contributors, or deployments within an existing entry — ensuring your work is visible and credited.

---

*Digital Public Goods Alliance · [digitalpublicgoods.net](https://digitalpublicgoods.net)*
