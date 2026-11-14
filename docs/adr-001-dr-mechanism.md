# ADR-001: Choose a supported DR mechanism per release and workload

**Status:** Proposed / requires product-version validation

## Context

The architecture requires an aggressive recovery point objective, application-group recovery, network mapping, and repeatable tests. Nutanix provides multiple protection and recovery capabilities whose feature sets and compatibility vary by AOS, Prism Central, license and topology.

## Decision

Do not assume NearSync, legacy Protection Domains, Leap, and Prism Central recovery plans are a single universally supported workflow. For each application, document the actual supported replication and orchestration combination using vendor documentation for the deployed release.

| Candidate | Evaluation |
| --- | --- |
| NearSync | Confirm target RPO, schedule constraints, supported AOS/PC versions, site pairing and networking |
| Protection Domains | Confirm whether this legacy mechanism is supported for the specific environment and what recovery automation is available |
| Prism Central DR / Leap recovery plans | Confirm supported protection type, category/app grouping, recovery network mapping and orchestration |
| Backup/restore | Assess as a separate data-protection layer; not a substitute for measured DR |

## Consequences

The blueprint remains portable, but deployment is blocked until a platform-specific compatibility record is approved. No unverified API calls or failover automation are included.

## Acceptance criteria

Record cluster versions, licensing, replication schedule, observed lag, target capacity, network maps, supported orchestration, failback method, and test evidence.