# 01 – Smart Cargo Pod: static stress, aluminium vs plastic

**Goal:** compare aluminium and plastic for the pod body under payload with a dynamic factor.
**Dimensions:** `docs/dimensions.md` §1. **Loads:** `docs/design-assumptions.md`.

## A. Model (Design workspace)
1. Units mm. Add the pod parameters from `docs/dimensions.md`.
2. Sketch a 600 × 400 rectangle, extrude 350, fillet vertical edges R10, then Shell (inside) to 3 mm, open face on top.
3. Lid: 600 × 400 × 3 plate with matching corner radius.
4. Lug: a 40 × 60 × 12 vertical plate with a D12 hole, joined to the pod at its attachment point.
5. Cut 4 vent slots (80 × 10) on each long side and 4 × D6 drain holes in the floor.
6. Sensor bay: 120 × 80 × 40 pocket or box under the lid for load cell, GPS, IMU, RFID and ESP32/LoRa.
7. Assign aluminium to the body (copy the design for the plastic run).
8. Save to `cad/f3d/`, export STEP to `cad/step/`.

Use `cad/reference_stl/cargo_pod_*.stl` only as a visual reference (Insert → Insert Mesh).

## B. Simulate (Simulation workspace → New Study → Static Stress)
| Setting | Value |
|---|---|
| Study Materials | Run 1: Aluminium 6061. Run 2: your chosen plastic with datasheet properties |
| Constraint | Pin constraint on the lug hole's inner cylindrical face (Fixed if Pin is not offered; note it is stiffer than real) |
| Gravity | On, in the hanging direction (pod self-weight only) |
| Payload | Pressure on the inner floor face = `design load / floor area` (549 N / (594 × 394 mm) ≈ 0.0023 MPa). Do not add gravity for the payload again, because the dynamic factor is already in the 549 N |
| Electronics | Extra force or remote mass on the sensor bay floor |
| Mesh | Start about 3 mm, refine to ≤ 1.5 mm at the lug and corners. For 3 mm walls consider shell elements |

Run at least three mesh sizes and record peak von Mises stress for each.

## C. Read and check
- von Mises stress (and location), displacement, safety factor, mass
- Reaction force at the lug must equal the applied load
- Compare with the hand check in `tools/output/hand_calc_output.txt`
- If floor deflection is large compared with the wall thickness, a linear study is not valid there. Use Nonlinear Static Stress, or add ribs / thicken the floor and report that as a finding

## D. Fill in
`results.md`, then screenshots to `results/`.

## E. Interview points
- Why that constraint, and what it ignores
- Why a flat unribbed plastic floor deflects much more (E is much lower)
- What a safety factor is, and why stress at a sharp corner is a singularity
