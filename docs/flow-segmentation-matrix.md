# Flow Network Security — segmentation intent

Category labels are illustrative and must match actual Prism Central categories. Begin in **monitor** mode and review logs before enforcing.

| Source | Destination | Service | Decision | Justification |
| --- | --- | --- | --- | --- |
| Approved ingress | Web | TCP 443 | Allow | TLS application entry |
| Web | Application | TCP 8443 | Allow | Internal application API |
| Application | Database | TCP 5432 | Allow | PostgreSQL connectivity |
| Admin jump host | Management | Approved management ports | Allow with MFA/approval | Privileged operations |
| Web | Database | Any | Deny | Prevent tier bypass |
| User subnet | Database | Any | Deny | Prevent direct data access |
| Any unexpected lateral flow | Any | Any | Deny after validation | Least privilege |

**Policy verification:** record observed flows, DNS/NTP/identity/backup/monitoring dependencies, and deny-test evidence. Confirm policy scope, priority and enforcement semantics in the installed Flow release.