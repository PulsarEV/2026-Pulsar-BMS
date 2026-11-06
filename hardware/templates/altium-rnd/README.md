# PulsarEV Altium R&D template — hardware documentation

This directory is the engineering adoption guide for the **blank Altium Designer template** supplied in `Pulsar_Altium_ArGe_Bos_Proje_Sablonu.zip`.

## Included in the original ZIP

- `PULSAR_RnD_Template.PrjPcb`: project linking four design/library files
- `PULSAR_RnD_Template.SchDoc`: empty schematic
- `PULSAR_RnD_Template.PcbDoc`: design-elements-free PCB with 35 provisional design rules
- `PULSAR_Symbols.SchLib`: blank schematic library
- `PULSAR_Footprints.PcbLib`: blank PCB footprint library

**Important availability notice:** These GitHub commits contain the guide, source checksums, rules review and import utility; the five **native binary Altium design files have NOT yet been uploaded to GitHub**. The supplied ZIP must be used to import them safely. Never create fake blank text files with Altium extensions.

## Import

Place the original ZIP on your computer. From the repository root, run:

```bash
python hardware/tools/import_altium_template.py /path/to/Pulsar_Altium_ArGe_Bos_Proje_Sablonu.zip
```

Verified files will be copied to `hardware/templates/altium-rnd/source/`. The script does not overwrite existing files. After running, commit the added native files through the normal reviewed workflow.

Then open `source/PULSAR_RnD_Template.PrjPcb` in Altium Designer. Check that .SchDoc, .PcbDoc, .SchLib and .PcbLib load. In the PCB editor inspect **Design → Rules** and **Layer Stack Manager**; confirm the outline, material system, copper weight, layer stack, clearance, drill, DFM and component constraints before reusing. Run ERC and DRC for each actual design.

## Design status

The template is a blank structural starting point, **not a validated vehicle subsystem**. Rules were transferred from a BMS reference board; they require project-specific approval. No Altium GUI open/save or manufacturing verification was possible in the generation environment. See [rule review](PCB_RULES_REVIEW.md) and [integrity manifest](MANIFEST.sha256).
