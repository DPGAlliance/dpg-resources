# DPG Assessment: Impact and Breadth Framework

*How the DPGA evaluates whether a solution is eligible for DPG certification*

---

## Table of Contents:
- [Purpose](#purpose)
- [The Two Dimensions](#the-two-dimensions)
  - [Impact](#impact)
  - [Breadth](#breadth)
- [The Four Quadrants](#the-four-quadrants)
  - [Quadrant 1 — Direct Impact, Low Breadth (Eligible)](#quadrant-1--direct-impact-low-breadth--eligible)
  - [Quadrant 2 — Indirect Impact, High Breadth (Eligible)](#quadrant-2--indirect-impact-high-breadth--eligible)
  - [Quadrant 3 — Low Impact, Low Breadth (Not Eligible)](#quadrant-3--low-impact-low-breadth--not-eligible)
  - [Quadrant 4 — Low Impact, High Breadth (Eligible with Justification)](#quadrant-4--low-impact-high-breadth--eligible-with-justification)
- [Summary Table](#summary-table)
- [What Applicants Should Address](#what-applicants-should-address)

---

## Purpose

This framework guides the assessment of submitted solutions for DPG eligibility along two dimensions: **Impact** (direct contribution to the UN SDGs) and **Breadth** (reach across diverse users or beneficiaries).

> [!NOTE]
> A solution must demonstrate meaningful standing on **at least one** of these dimensions to be eligible. A solution that scores low on both is not eligible.

---

## The Two Dimensions

### Impact

This refers to the degree to which a solution directly contributes to one or more UN SDG targets.

**Direct Impact** solutions:
- Are clearly and demonstrably linked to one or more SDG targets.
- Serve users or beneficiaries who are directly affected by SDG-linked outcomes — such as citizens, public-sector actors, community organisations, health workers, educators, or researchers working on SDG-relevant problems.
- Have a primary use case in areas like public health, education, governance, climate action, financial inclusion, or social protection.

**Indirect Impact** solutions:
- Have only indirect relevance to SDGs — for example, the connection runs through several downstream steps.
- Are primarily designed for software engineering, infrastructure, or technical performance without a clear societal application.
- Cannot identify a specific SDG target that the solution supports.

> [!NOTE]
> The line between direct and indirect impact requires reviewer judgment and is assessed case by case. As a general guide, you should ask: *Is the solution's primary output something that an SDG-affected beneficiary uses, or is it something a technical intermediary uses to potentially build something else?* Examples in each quadrant below illustrate how this distinction is applied in practice.

---

### Breadth

This refers to the range and diversity of end-users or beneficiaries who can directly use the solution and derive SDG-linked value from it.

**High Breadth** solutions:
- Are useful across multiple sectors, communities, or user groups.
- Can be meaningfully used by non-technical users, or serve large public-sector, civil society, or citizen audiences.
- Are not constrained to super-specialised technical disciplines.

**Low Breadth** solutions:
- Primarily serve a niche technical audience (e.g., software developers, data scientists, specialised researchers)
- Have outputs that serve software development or technical infrastructure rather than public-facing services
- Include: developer libraries, SDKs, plugins, compilers, programming languages, and frameworks used mainly in engineering workflows

> [!NOTE]
> Low Breadth alone does not disqualify a solution — it can still be eligible if Impact is high (see Quadrant 1 below). Equally, Indirect Impact alone does not disqualify a solution if Breadth is high and societal relevance is well-justified (see Quadrant 4 below).

---

## The Four Quadrants

The framework places solutions into one of four quadrants. Solutions in **Quadrants 1, 2, and 4** are generally eligible. Solutions in **Quadrant 3** are not.

![](https://github.com/DPGAlliance/dpg-resources/raw/main/docs/assets/dpg-IB-framework.jpg?raw=true)

---

### Quadrant 1 — Direct Impact, Low Breadth (✅ Eligible)

**Characteristics:**
- Strong and direct SDG relevance.
- Serves specialised or technical users, but the outputs of those users have clear societal value.
- The tool is a means to an SDG-relevant end, used by technical specialists who produce insights or outcomes that benefit the public.

**Typical Examples:**
- Diagnostic or analytical tools used by data scientists or researchers to produce SDG-relevant outputs (e.g., urban access metrics, public health risk mapping, climate modelling).
- AI safety or audit tools that protect patients or ensure institutional integrity in SDG-linked systems.

**Illustrative Archetypes:**

| Archetype | Description |
|---|---|
| SDG-linked research tool | A specialised platform used by researchers to analyse disease patterns and inform public health decisions. Users are technical, but the downstream impact is directly on SDG 3 outcomes. |
| Urban analytics tool | A data tool used by city planners and data scientists to model access to transport, housing, or services in underserved areas — directly informing SDG 11 targets. |

---

### Quadrant 2 — Indirect Impact, High Breadth (✅ Eligible)

**Characteristics:**
- Direct and demonstrable SDG impact.
- Broad usability across large, diverse, and non-technical user groups.
- Strong public-facing or service-delivery functionality.

**Typical Examples:**
- Citizen-facing health, education, or social protection platforms.
- Open-source systems used by governments or NGOs to deliver services at scale.
- Tools enabling public participation, transparency, or widespread service accessibility.

**Illustrative Archetypes:**

| Archetype | Description |
|---|---|
| National health information system | Used by health managers, facility staff, disease surveillance teams, and policymakers to track and respond to public health outcomes at scale. Directly linked to SDG 3 targets. |
| Open knowledge platform | Used by students, teachers, researchers, journalists, and the general public to access and contribute to freely available knowledge. Linked to SDG 4 (education) and SDG 10 (reduced inequalities). |

---

### Quadrant 3 — Low Impact, Low Breadth (❌ Not Eligible)

**Characteristics:**
- No meaningful or demonstrable SDG contribution.
- Primarily serves a niche technical audience.
- Limited applicability to public, institutional, or service-oriented contexts.

**Typical Examples:**
- Developer libraries, SDKs, and plugins.
- Compilers, interpreters, and programming languages.
- General-purpose engineering frameworks without SDG linkage.
- Internal tooling with no public-facing application.

**Illustrative Archetypes:**

| Archetype | Description |
|---|---|
| Developer utility | A general-purpose code testing library used by software engineers. No SDG linkage; no public beneficiary. |
| Internal automation tool | A workflow automation script for engineering teams. Provides productivity value but no societal or SDG-linked output. |

> [!NOTE]
> Solutions in this quadrant are typically screened out early in the review process. They may provide genuine technical value, but that value does not meet the threshold for a Digital Public Good.

---

### Quadrant 4 — Low Impact, High Breadth (✅ Eligible with justification)

**Characteristics:**
- Broad applicability across many user groups, including non-technical users.
- Indirect SDG impact, but the solution underpins or enables SDG-aligned ecosystems at scale.
- Applicants must make a clear case for societal relevance — this quadrant is not self-evidently eligible and requires justification.

**Typical Examples:**
- Broadly adopted open platforms that support civic access, information equity, or open knowledge ecosystems.
- General-purpose tools that underpin critical SDG-related operations for governments, NGOs, or civil society at scale.
- Operating systems or content management systems with documented, substantial adoption in public-interest sectors.

**Illustrative Archetypes:**

| Archetype | Description |
|---|---|
| Open web platform | A widely used open-source content management system adopted by government digital services, civil society organisations, and NGOs globally. While not SDG-specific, its breadth of adoption in public-interest contexts supports SDG 17 (partnerships) and SDG 10 (inclusion) goals. Justification required. |
| Open operating system | A freely available OS used by students, researchers, public institutions, and civil society organisations in low-resource environments. Contributes to digital access goals (SDG 9, SDG 17) by enabling open infrastructure at scale. Justification required. |

> [!NOTE]
> For solutions in this quadrant, reviewers should ask: *Does this tool, by virtue of its widespread adoption and open nature, meaningfully contribute to the conditions under which SDG outcomes are achieved — even if that contribution is indirect?* High-breadth solutions with only weak or speculative societal relevance should not qualify on breadth alone.

---

## Summary Table

| Quadrant | Impact | Breadth | Eligible? | Notes |
|---|---|---|---|---|
| **Q1** | Direct | Low | ✅ Yes | Technical users, but SDG-linked outputs. |
| **Q2** | Direct | High | ✅ Yes | The clearest case for eligibility. |
| **Q3** | Indirect | Low | ❌ No | Screened out; no SDG linkage, no breadth. |
| **Q4** | Indirect | High | ✅ With justification | Applicant must make societal relevance case. |

---

## What Applicants Should Address

Regardless of quadrant, applicants should clearly articulate:

1. **Which SDG targets does the solution support, and how?**: Be specific about the target, not just the SDG number. Explain whether the link is direct or indirect.
2. **Who are the end users or direct beneficiaries?**: Describe who uses the solution and how they benefit — distinguishing between technical users who operate it and the populations who benefit from its outputs.
3. **What is the scale or potential reach?**: Describe the current user base and the realistic population the solution is designed to serve.
4. **Is the solution primarily technical (Q1 or Q4 candidate)?:** Explain specifically how the outputs of your solution contribute to SDG-relevant outcomes, and provide evidence or examples where possible.

---

*Digital Public Goods Alliance · [digitalpublicgoods.net](https://digitalpublicgoods.net)*
