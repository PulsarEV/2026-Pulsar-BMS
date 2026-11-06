# Motor Controller — Hardware engineering

## Purpose

Maintain native electronic design artifacts and their dependencies without breaking CAD project references.

## File inventory

| Artifact | Confirmed location | Status |
| --- | --- | --- |
| Altium .PrjPcb | TBD | Not found / unverified |
| .SchDoc / .PcbDoc | TBD | Not found / unverified |
| Component libraries and BOM | TBD | Not found / unverified |
| Calculations, simulation and manufacturing outputs | TBD | Not found / unverified |

## Hardware contributor workflow

1. Confirm project and revision with the subsystem owner.
2. Keep linked Altium files in a consistent relative structure; prefer native sources over screenshots.
3. Check component selection, supply/interface constraints and design assumptions.
4. Document ERC/DRC and design-review results only if actually executed.
5. Link evidence and hardware revision in the PR.

### Project-specific design review questions

Power stage, gate-drive interfaces, motor sensor feedback, PWM/control software, current/voltage sensing, startup/shutdown behavior, and verified fault handling.

**Warning:** The presence of a checklist is not proof of compliance or safety.