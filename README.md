# PulsarEV — Motor Controller

> **Engineering scope:** Electric motor drive hardware, embedded motor-control software, and integration verification.  
> **Development status:** Ongoing (as stated in original README); source implementation and test status not verified.  
> **Hardware revision / MCU / firmware:** TBD — verify against committed engineering sources.  
> **Verification status:** No verification evidence assessed in this documentation update.

## About this repository

This is the Pulsar Team's 2026 Motor Controller engineering workspace. It is organized for traceable electronics R&D rather than presenting an unfinished project as production-ready.

### Engineering focus

Power stage, gate-drive interfaces, motor sensor feedback, PWM/control software, current/voltage sensing, startup/shutdown behavior, and verified fault handling.

## Start here

| Workspace | Entry point | Contents |
| --- | --- | --- |
| Hardware | [hardware/README.md](hardware/README.md) | Schematics, PCB, BOM, calculations and design reviews |
| Embedded software | [embedded/README.md](embedded/README.md) | MCU source, configuration and reproducible build notes |
| Documentation | [docs/README.md](docs/README.md) | Architecture, requirements, interfaces, decisions and validation |
| Testing | [tests/README.md](tests/README.md) | Verification plans, reports and test evidence |

## Engineering lifecycle

1. **Requirements:** Agree on constraints and acceptance criteria.
2. **Architecture:** Document hardware blocks, firmware responsibilities and interfaces.
3. **Implementation:** Commit native CAD/firmware source files with dependencies intact.
4. **Review:** Link issue, pull request and design rationale.
5. **Verification:** Record test conditions, revision, results and evidence.
6. **Release:** Tag verified hardware/firmware revisions only after explicit review.

## Quick start for contributors

```bash
git clone https://github.com/PulsarEV/2026-Pulsar-MotorSurucu.git
cd 2026-Pulsar-MotorSurucu
```

Next, read [onboarding](docs/development/onboarding.md), [requirements](docs/requirements/system-requirements.md), and the relevant hardware/firmware README. Toolchain commands have not yet been verified and are intentionally not invented.

## Development status

| Area | State |
| --- | --- |
| Requirements | Baseline pending confirmation |
| Hardware | Source/design revision to be confirmed |
| Firmware | Source/toolchain to be confirmed |
| Interface agreement | Draft documentation scaffold |
| Test evidence | Not supplied/verified here |

## Contributing and project safety

See [CONTRIBUTING.md](CONTRIBUTING.md). Do not change electrical limits, safety-critical logic or CAD designs based on undocumented assumptions. Power systems require controlled validation with qualified supervision.

**License:** No license is granted or selected by this documentation. Follow organization policy.
