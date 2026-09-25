# LinkedIn public-profile retrieval receipt — 2026-09

- **Target:** `https://www.linkedin.com/in/ablevt/`
- **Authority:** owner’s direct request: “grab profile url and parse” (2026-09-23).
- **Purpose:** professional-evidence reconciliation only.
- **Access check:** `GET https://www.linkedin.com/robots.txt` returned HTTP `200`; body size `120,190` bytes; SHA-256 `1eaa886c2898f40d5515d38552dddab29b48333c6a3adb5097572ad6309d709c`.
- **Rule evaluation:** Python standard-library `urllib.robotparser` returned `allowed=False` for `*`, `curl`, `Defuddle`, and `Mozilla/5.0` against the target path.
- **Result:** `BLOCKED` — no target profile request, authentication attempt, browser automation, CAPTCHA handling, proxying, or retry occurred.
- **Collected profile fields:** none.
- **Correct next source:** an owner-provided LinkedIn profile export/PDF/text, or an owner-authenticated export through LinkedIn’s own account tools. That supplied artifact can be parsed locally under the existing evidence contract.
- **Bounded request count:** 1/2 used; zero profile-page requests; no credentials; no monetary cost.
