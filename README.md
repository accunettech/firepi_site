# VigilPoint customer upgrade announcement

FirePi is now **VigilPoint**, a product of **Accunet Services, LLC**.

Tagline: **Know when it matters. Relax when it doesn't**

This static marketing update introduces the upcoming upgrade to existing FirePi
customers. It uses the approved navy, blue and slate brand palette, the shared V
mark, and screenshots of the working web and mobile interfaces with fictional
Riverside Glass Studio data. Green identifies health coverage, not primary actions.

## Preview

```sh
python3 -m http.server 8092 --bind 127.0.0.1
```

Open `http://127.0.0.1:8092`. The root, `/firepi/` and `/vigilpoint/` routes all show
the announcement, preserving previously shared FirePi links. No build service,
JavaScript, external font, analytics or CDN is required.

## Customer materials

- `share/vigilpoint-upgrade.html`: self-contained HTML attachment with embedded
  styling, logo and screenshots. Open it directly in a browser or attach it to
  an email. Screenshot links download the full preview image. It is a browser
  document, not an email-client template; many email clients strip HTML styling.
- `share/announcement.txt`: subject, preview text and customer email copy. Attach
  the self-contained overview when sending this version.

These files do not send messages or deploy the site. Customer distribution and
production hosting are managed separately from the repository update.
The page intentionally avoids unconfirmed launch dates, pricing, hardware
compatibility promises, production URLs and App Store links.

## Update and rebuild

Edit `templates/upgrade.html` and `assets/site.css`, then run:

```sh
python3 scripts/build.py
```

The script uses only Python's standard library. Commit the generated route files
and self-contained attachment with the template changes. Brand marks are copied
from the application repository's `src/firepi/static/brand/` SVGs. Screenshots in
`assets/screenshots/` show actual rendered UI, not invented application screens.
Only local-development environment labels were hidden for the captures; the
page discloses demonstration data and previews.

## Release checks before distribution

This is an **upcoming upgrade announcement**, not a claim that production service
or every described delivery channel is live today. The customer copy describes
the requested push → SMS → phone-call sequence and persistent team response.

Before distributing it, verify the actual rollout supports:

- Live iPhone/Android push, SMS and automated voice calling; voice escalation is
  not implemented in the current application. Push and SMS still use mocks in
  the local stack.
- All intended team members are subscribed and have notification permissions
  and valid destinations for each channel; delivery acceptance is not a handset
  delivery guarantee.
- The intended acknowledgement windows and continued escalation until team
  acknowledgement, including the equipment-recovery behavior. The current
  backend clears an alert on equipment recovery, and retries are bounded.
- Public HTTPS hosting, approved identity callbacks and native app distribution.
- Customer-specific hardware migration steps and timing.

Do not publish localhost URLs, demo tokens, private credentials or real customer
identities in screenshots. A missing device check-in establishes lost contact;
it does not distinguish power loss from loss of internet on its own.
