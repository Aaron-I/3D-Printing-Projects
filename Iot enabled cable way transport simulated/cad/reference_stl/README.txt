Concept-stage STL package
==========================

Units: millimetres (mm). STL files are unitless; import into Fusion 360 and set
the document/design units to mm.

Contents
--------
- cargo_pod_*.stl: pod body, lid, lug and sensor bay, plus assembly
- carriage_*.stl: carriage/hanger assembly and representative components
- support_tower_*.stl / tower_*.stl: tower assembly and representative components

Important modelling notes
-------------------------
These are simplified concept meshes derived from the supplied dimension sheets
and the dimensions stated with them. They are intended for CAD layout,
visualization and early fit checks only.

Some features are represented schematically rather than as manufacturing-ready
geometry:
- Several bolt/axle/pin holes are shown with collars or are not boolean-cut.
- The pod is assembled from wall panels; the vent openings are represented as
  gaps in the long walls.
- The carriage wheel groove is approximated by a faceted revolved profile.
- The tower is a simplified tapered lattice; the solar panel support is a
  mounting concept, not a verified drive mechanism.
- Welds, fasteners, tolerances, edge treatments, drainage details and detailed
  interfaces are not fully modelled.

Do not use these meshes as fabrication or structural approval. The 5 m tower
requires a qualified structural design review, including wind loading,
buckling, connection design, anchorage and foundation checks. Verify all
dimensions and interfaces against the actual design before manufacture.

Coordinate conventions
----------------------
Cargo pod: X=600 length, Y=400 width, Z=350 height.
Carriage: X is wheel spacing direction; Z is vertical in the side-view layout.
Tower: Z is vertical; base plate is centred at Z=-6; ground reference is Z=0.

Files are separate STL meshes; assemblies are concatenated multi-component
meshes. For editable parametric work, recreate or remodel the parts in Fusion
360 using the supplied dimensions rather than treating STL as native feature history.
