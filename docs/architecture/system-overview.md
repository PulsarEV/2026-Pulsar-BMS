# Motor Controller — System architecture

**Status:** Initial scope statement. No verified electrical or firmware block diagram was available during the repository reorganization.

## Purpose and boundary

Electric motor drive hardware, embedded motor-control software, and integration verification.

**Areas requiring confirmed architecture:** Power stage, gate-drive interfaces, motor sensor feedback, PWM/control software, current/voltage sensing, startup/shutdown behavior, and verified fault handling.

## Required architecture evidence

- Approved system block diagram and electrical boundary
- Power distribution and protection descriptions
- MCU/peripheral assignments, if firmware exists
- External connector and communication interface definitions
- Safety assumptions and required isolation/monitoring considerations
- Version mapping between hardware and firmware
- Review references and open engineering decisions

Do not add an apparently factual architecture diagram until connections are supported by schematic or approved specification.