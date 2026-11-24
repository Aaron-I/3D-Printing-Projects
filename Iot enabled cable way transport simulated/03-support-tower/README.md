# 03 – Support Tower with Solar Drive Mount: static stress and buckling

**Goal:** check the 5 m tower under rope tension, wind on the panel and self-weight, then check buckling.
**Dimensions:** `docs/dimensions.md` §3. **Loads:** `docs/design-assumptions.md`.

> A real tower of this size needs a qualified structural review of wind loading, connections, anchorage and foundation. This is a concept-stage study.

## A. Model
1. Parameters from `docs/dimensions.md`.
2. Base plate 800 × 800 × 12 with 4 × D20 holes. Leg centres 600 at the base, 300 at the top.
3. Legs: 4 × D48.3 × 3.2 tube from base to top. Braces D33.7 × 2.6 every 1000 mm in a lattice.
4. Top platform 500 × 400 × 10.
5. Solar panel 1650 × 990 × 35, tilted 15°, on a mounting rail (40 × 40 × 3) and arm. This is a mounting concept, not a verified drive mechanism.
6. Use `cad/reference_stl/support_tower_assembly_5000mm_concept.stl` only for layout.

## B. Static stress
| Setting | Value |
|---|---|
| Material | Structural steel (note the grade, E, yield) |
| Constraint | Fixed on the 4 base-plate bolt holes |
| Loads | (1) rope tension at the top platform, about 4.3 kN, in the sag direction; (2) wind on the panel about 1.1 kN horizontal at the panel centre; (3) self-weight and panel weight |
| Cases | Run rope, wind and weight separately, then the combined worst case with rope and wind in the same direction |
| Mesh | Solid mesh of the lattice is heavy. Use shell/tube modelling or a coarser mesh with local refinement at joints and the base plate |

## C. Buckling (Structural Buckling)
- Same constraints and combined loads as the worst case.
- Result is a load multiplier, and critical load = multiplier × applied load. Report the first mode and its shape.
- If the study is not available on your account, do a hand Euler calculation and label it "hand calculation". `tools/rope_load_calc.py` gives a leg-bay estimate.

## D. Hand check
Overturning at the base about 26.9 kN·m gives about 22 kN per leg, about 49 MPa axial in the legs (legs only, braces ignored). See `tools/output/hand_calc_output.txt`.

## E. Fill in
`results.md`, screenshots to `results/`.

## F. Interview points
- Why the worst case has rope and wind aligned
- What a buckling multiplier of 1 means
- Why brace spacing affects buckling
