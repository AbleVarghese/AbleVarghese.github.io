# README evidence excerpt — ory/kratos

**Source:** https://github.com/ory/kratos/blob/master/README.md

<h1 align="center">
  <img src="https://raw.githubusercontent.com/ory/meta/master/static/banners/kratos.svg" alt="Ory Kratos - Cloud native identity and user management">
</h1>
<h4 align="center">
  <a href="https://www.ory.com/chat">Chat</a> ·
  <a href="https://github.com/ory/kratos/discussions">Discussions</a> ·
  <a href="https://www.ory.com/l/sign-up-newsletter">Newsletter</a> ·
  <a href="https://www.ory.com/docs/">Docs</a> ·
  <a href="https://console.ory.sh/">Try Ory Network</a> ·
  <a href="https://www.ory.com/jobs/">Jobs</a>
</h4>
Ory Kratos is an API first identity and user management system for cloud native
applications. It centralizes login, registration, recovery, verification, and
profile management flows so your services consume them instead of reimplementing
them.
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of contents**
- [What is Ory Kratos?](#what-is-ory-kratos)
  - [Why Ory Kratos](#why-ory-kratos)
- [Migrating from Auth0, Okta, and similar providers](#migrating-from-auth0-okta-and-similar-providers)
- [Deployment options](#deployment-options)
  - [Use Ory Kratos on the Ory Network](#use-ory-kratos-on-the-ory-network)
  - [Self-host Ory Kratos](#self-host-ory-kratos)
- [Quickstart](#quickstart)
  - [Who is using it?](#who-is-using-it)
<!-- END doctoc generated TOC please keep comment here to allow auto update -->
## What is Ory Kratos?
Ory Kratos is an API first identity and user management system that follows
[cloud architecture best practices](https://www.ory.com/docs/ecosystem/software-architecture-philosophy).
It focuses on core identity workflows that almost every application needs:
- Self service login and registration
- Account verification and recovery
- Multi factor authentication
- Profile and account management
- Identity schemas and traits
- Admin APIs for lifecycle management
We recommend starting with the
[Ory Kratos introduction docs](https://www.ory.com/kratos/docs/) to learn more
about its architecture, feature set, and how it compares to other systems.
### Why Ory Kratos
Ory Kratos is designed to:
- Remove identity logic from your application code and expose it over HTTP APIs
- Work well with any UI framework through browser based and native app flows
- Scale to large numbers of identities and devices
- Integrate with the rest of the Ory stack for OAuth2, OpenID Connect, and
  access control
- Fit into modern cloud native environments such as Kubernetes and managed
  platforms
## Migrating from Auth0, Okta, and similar providers
If you are migrating from Auth0, Okta, or another identity provider that uses
OAuth2 / OpenID Connect based login, consider using **Ory Hydra + Ory Kratos**
together:
- **Ory Hydra** acts as the OAuth2 and OpenID Connect provider and can replace
  most authorization server and token issuing capabilities of your existing IdP.
- **Ory Kratos** provides identity, credentials, and user-facing flows (login,
  registration, recovery, verification, profile management).
This combination is often a drop-in replacement for OAuth2 and OpenID Connect
capabilities at the protocol level. In practice, you update client configuration
and endpoints to point to Hydra, migrate identities into Kratos, and keep your
applications speaking the same OAuth2 / OIDC protocols they already use.
## Deployment options
You can run Ory Kratos in two main ways:
- As a managed service on the Ory Network
- As a self hosted service under your own control, with or without the Ory
  Enterprise License
### Use Ory Kratos on the Ory Network
The [Ory Network](https://www.ory.com/cloud) is the fastest way to use Ory
services in production. **Ory Identities** is powered by the open source Ory
Kratos server and is API compatible.
The Ory Network provides:
- Identity and credential management that scales to billions of users and
  devices
- Registration, login, and account management flows for passkeys, biometrics,
  social login, SSO, and multi factor authentication
- Prebuilt login, registration, and account management pages and components
- OAuth2 and OpenID Connect for single sign on, API access, and machine to
  machine authorization
- Low latency permission checks based on the Zanzibar model with the Ory
  Permission Language
- GDPR friendly storage with data locality and compliance in mind
- Web based Ory Console and Ory CLI for administration and operations
- Cloud native APIs compatible with the open source servers
- Fair, usage based [pricing](https://www.ory.com/pricing)
Sign up for a
[free developer account](https://console.ory.sh/registration?utm_source=github&utm_medium=banner&utm_campaign=kratos-readme)
to get started.
### Self-host Ory Kratos
You can run Ory Kratos yourself for full control over infrastructure,
deployment, and customization.
The [install guide](https://www.ory.com/kratos/docs/install) explains how to:
- Install Kratos on Linux, macOS, Windows, and Docker
- Configure databases such as PostgreSQL, MySQL, and CockroachDB
- Deploy to Kubernetes and other orchestration systems
- Build Kratos from source
This guide uses the open source distribution to get you started without license
requirements. It is a great fit for individuals, researchers, hackers, and
companies that want to experiment, prototype, or run unimportant workloads
without SLAs. You get the full core engine, and you are free to inspect, extend,
and build it from source.
