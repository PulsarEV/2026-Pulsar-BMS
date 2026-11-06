# EDA Agent setup

This repository includes an MCP connection definition for [salitronic/eda-agent](https://github.com/salitronic/eda-agent). It is a shared configuration only: each engineer installs and runs the server on their own machine. It is not centrally hosted or automatically installed.

## Requirements

- Python 3.11 or newer.
- A locally installed, supported EDA application with its integration available:
  - Altium Designer on Windows.
  - KiCad 10 with its API.
  - EasyEDA Pro.
- A Copilot client that supports repository MCP configuration.

The server is experimental and can modify or delete content in the active EDA design. Review the upstream [README](https://github.com/salitronic/eda-agent#readme) and its current requirements before installing.

## Install locally

Clone and install the server in a location managed by you:

```shell
git clone https://github.com/salitronic/eda-agent
cd eda-agent
python -m pip install -e .
```

For Altium Designer, also run:

```shell
python -m eda_agent install-scripts
```

Then register and run the bundled Altium script as described by the upstream instructions. KiCad and EasyEDA Pro users must have their supported local application and integration ready.

The repository's `.mcp.json` launches `python -m eda_agent` with the `minimal` toolset. If Python is not on the MCP client's executable search path, configure the command to the Python executable in the environment where you installed the package, using your client's supported configuration.

## Connect and verify

1. Review the MCP configuration and the upstream project, then allow this repository's MCP server in your client only if you trust it.
2. Restart or refresh the client so it can start the local server. Confirm the `eda-agent` server connects and its tools are available.
3. Begin with a read-only query on a disposable or backed-up design. Confirm the active EDA project and inspect the server's response before proceeding.

Before any write, delete, or UI-automation operation, back up the design files, verify the active project, and require explicit user confirmation. Do not treat tool availability as approval to change a design. The server records full responses in a local activity log; review the upstream documentation for its location and handling.
