# Motor Controller — Embedded software

## Project status

An MCU codebase, compiler/toolchain, board revision and verified build command are not established by the current repository inventory.

| Item | Verified value |
| --- | --- |
| MCU and board revision | TBD |
| IDE / compiler | TBD |
| Build command | TBD — requires reproduction |
| Flash / debug procedure | TBD — requires controlled verification |
| Real-time architecture and peripheral map | TBD |

## Contributor workflow

1. Locate the actual MCU project before documenting build commands.
2. Keep generated code and user-maintained code boundaries intact.
3. Map GPIO, PWM, ADC, communication and interrupt usage only from committed sources.
4. Review fault handling, timing, hardware compatibility and watchdog behavior against evidence.
5. Document build logs and test results with commit and board revision.

Do not create placeholder drivers that could be mistaken for functioning device firmware.