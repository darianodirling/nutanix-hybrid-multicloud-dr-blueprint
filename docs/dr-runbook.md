# Disaster Recovery Validation Runbook

> **Safety:** Exercise in isolated networks first. Production failover/failback requires change approval and the vendor-supported workflow for the actual release.

## Preflight — record evidence

- [ ] Incident/exercise ID, date, change owner, business owner, and approvers recorded.
- [ ] RPO/RTO and workload criticality approved.
- [ ] Source and target AOS/AHV/Prism Central versions and DR licensing checked.
- [ ] Selected NearSync / Protection Domain / recovery-plan workflow confirmed as supported.
- [ ] Source/target cluster, CVM, storage, time sync and replication health checked.
- [ ] Latest consistent recovery point and lag timestamp recorded.
- [ ] Target CPU, memory, storage and network capacity confirmed.
- [ ] VM dependencies, boot order, secrets, certificates and external integrations inventoried.
- [ ] Recovery subnet/VLAN mappings and firewall/Flow policy reviewed.
- [ ] DNS, load-balancer, authentication and upstream/downstream dependencies mapped.
- [ ] Test recovery isolated from production identity, IP addresses, DNS and writable databases.
- [ ] Rollback/abort conditions and communications plan approved.

## Execute isolated test

1. Record T0 and current replication checkpoint; preserve screenshots/logs.
2. Initiate vendor-supported **test** recovery (not production cutover).
3. Boot database tier; check database consistency, storage mount and read/write health in isolation.
4. Boot application tier; verify service dependencies, certificates and internal endpoints.
5. Boot web tier; verify ingress, TLS, synthetic transactions and application logs.
6. Test allowed web→app and app→DB flows; verify prohibited east-west flows are blocked or logged as intended.
7. Measure RPO from the actual recovered data checkpoint and RTO to agreed business-ready state.
8. Verify monitoring, alerting, backups and audit trails at recovery site.
9. Document exceptions and business sign-off.
10. Tear down isolated test safely; confirm primary workload and replication remain healthy.

## Production failover (separate approved change)

- [ ] Incident commander authorizes failover; data owners accept data-loss risk.
- [ ] Split-brain prevention / source fencing verified before writable recovery.
- [ ] Follow supported orchestration for actual protection mechanism.
- [ ] Update DNS, routes and load-balancer targets only after validation.
- [ ] Validate customer journeys and security controls.
- [ ] Announce cutover, record timestamps and start heightened monitoring.

## Failback

- [ ] Confirm primary site is healthy and synchronized.
- [ ] Confirm supported reverse replication and data-consistency process.
- [ ] Approve maintenance window and write freeze as required.
- [ ] Execute vendor-supported failback; verify transactions and monitoring.
- [ ] Record lessons learned, observed RPO/RTO, and residual risks.

Use [evidence template](validation-evidence-template.md) for every exercise.