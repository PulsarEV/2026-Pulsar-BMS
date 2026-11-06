# Provisional Altium PCB rules — engineering review

Origin: source `SPARK_BMS_V01.PcbDoc`. The blank target PCB contains **35 native rule records**, excluding project-specific `Polygon_outline` and duplicate `DiffPairsRouting_1`.

| Group | Source rule names |
| --- | --- |
| Electrical | Clearance, ShortCircuit, UnRoutedNet, NetAntennae |
| Routing | Width, RoutingVias, RoutingCorners, RoutingLayers, RoutingTopology, RoutingPriority, DiffPairsRouting |
| Planes & polygons | LayerPairs, PlaneClearance, PlaneConnect, PolygonConnect, UnpouredPolygon |
| Components & fanout | ComponentClearance, Height, Fanout_BGA, Fanout_LCC, Fanout_SOIC, Fanout_Small, Fanout_Default |
| Solder & silkscreen | SolderMaskExpansion, PasteMaskExpansion, MinimumSolderMaskSliver, SilkToBoardRegionClearance, SilkToSilkClearance, SilkToSolderMaskClearance |
| Drill | HoleSize, HoleToHoleClearance |
| Testpoints | AssemblyTestpoint, AssemblyTestPointUsage, FabricationTestpoint, FabricationTestPointUsage |

Source general clearance: **7.874 mil (~0.20 mm)**. Source hole-to-hole clearance: **11.811 mil (~0.30 mm)**. Source component clearance: **10 mil (~0.254 mm)**. These describe the uploaded reference; **they are not universally approved spacing or manufacturing specifications**.

Before a real project, review the voltage classes, creepage/clearance and insulation requirements, supplier DFM limits, current capability, layer stack, copper weight, solder mask, thermal behavior and test methods. Do not declare electrical safety or fabrication readiness without documented evidence.
