# LinkedIn public-profile collection admission — 2026-09

- **Authority:** owner’s direct request: “grab profile url and parse” (2026-09-23).
- **Source / controller:** `https://www.linkedin.com/in/ablevt/` — public profile identified from the owner’s GitHub social-account metadata.
- **Access boundary:** one unauthenticated public request after a `robots.txt` / access-result check; no login, cookies, CAPTCHA solving, proxying, browser automation, retries after a block, or use of any endpoint beyond the profile URL.
- **Purpose:** reconcile current professional identity, project, employment, education, and publicly declared skill facts with the authority-platform evidence registry.
- **Accepted fields:** public headline, public summary, named roles/employers, date ranges, education/certifications, public project/portfolio links, and public skills only when visibly present.
- **Prohibited fields:** contact details, connections, messages, activity/feed content, inferred demographics, private/profile-hidden data, and any information behind authentication.
- **Destination / retention:** a bounded Markdown source excerpt and field-level parse receipt under this same `owner-profile-evidence/` directory; retained with the existing September 2026 research evidence until the related evidence register is superseded or archived.
- **Bounds:** maximum 2 network requests (robots/access check plus profile), 1 profile record, 1 MB response body, 60 seconds total, no monetary spend, no credentials.
- **Success criterion:** public profile content is accessible through a permitted response and accepted fields can be attributed directly to the profile URL with retrieval status.
- **Stop conditions:** robots/access denial, sign-in wall, CAPTCHA, rate limit, unexpected sensitive data, content that cannot be confidently attributed to the target profile, or any source-policy contradiction. Any stop condition is recorded as `BLOCKED` or `UNVERIFIED`, not inferred around.
