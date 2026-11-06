# Contributing to PulsarEV Engineering

Engineering work is reviewed and traceable. This repository contains development assets, not an assertion of manufacturing readiness.

## Workflow

1. Read the root README, requirements, architecture and interface documents.
2. Open an issue describing the change, motivation, affected hardware/firmware and acceptance criteria.
3. Create a branch using `hardware/<topic>`, `firmware/<topic>`, `docs/<topic>`, `fix/<topic>` or `test/<topic>`.
4. Use descriptive commits, preferably Conventional Commits (e.g., `docs(hardware): clarify connector inventory`).
5. Update affected schematics, code, requirements, pin maps, BOM, revision history and test records together.
6. Open a pull request using the repository PR template; include evidence and known limitations.
7. Merge only after appropriate review.

## Hardware-specific rules

- Keep native CAD projects and library dependencies intact.
- Record electrical design changes and PCB revisions; do not rename Altium sources without validating project links.
- Never call a board verified or ready for manufacturing without documented checks and relevant evidence.
- Mark proposed protection features as proposed until implemented and tested.

## Firmware-specific rules

- Preserve MCU-generated code boundaries, real-time scheduling and interrupt behavior.
- Document target hardware revision, toolchain and reproducible build commands when confirmed.
- Never replace unverified hardware behavior with speculative drivers.

## Documentation and safety

Use explicit status labels: `Proposed`, `In progress`, `Verified`, `Blocked`, `Unknown`. Do not fabricate measurements or approvals.
Power systems and vehicle electronics require qualified supervision for potentially hazardous work.