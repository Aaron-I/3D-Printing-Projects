# 02 – Carriage and Hanger: slope motion study and stress

**Goal:** (1) check the carriage's descent speed on a slope against v = √(2gh); (2) check stress in the hanger straps, pins and axles.
**Dimensions:** `docs/dimensions.md` §2.

## A. Model
1. Parameters from `docs/dimensions.md`.
2. Wheel: revolve a D80 × 30 profile with a U-groove R4.5 (sketch the profile, revolve about the axis).
3. Side plates: 2 × 200 × 120 × 8, 60 apart, with axle holes at 100 pitch.
4. Axles: 2 × D12 × 100. Spacers OD20 × 15. Pins D12.
5. Hanger straps: 2 × 150 × 40 × 6, holes 120 apart, straddling the pod lug.
6. Assemble: wheels on axles (revolute joints), axles through plates, straps pinned at the lug hole.
7. Add the rope as a straight D-sized rod at the slope angle (set in `docs/design-assumptions.md`), grounded, to sit in the wheel groove.

## B. Motion study (gravity on a slope)
- Tools: Motion Study (basic) or Event Simulation (Simulation Extension).
- Ground the rope, give the wheels revolute joints, set up groove–rope contact if the tool supports it, gravity on.
- Run a few seconds. Plot carriage velocity at the bottom of the drop `h`.
- **Compare with v = √(2gh).** That value assumes frictionless sliding, so it is an upper bound. A real result is lower because of wheel inertia and friction. In `tools/output/hand_calc_output.txt` wheel inertia alone changes v by only about 1%, so most of any larger gap is friction/contact modelling. State which.
- If contact will not solve, use the Python energy balance and label it "analytical".

## C. Stress (Static Stress)
- Parts: straps, pins, axles (and plates if wanted).
- Constraint: wheel bearing faces on the axles (or the plate holes).
- Load: design load (549 N) vertical at the strap pin holes.
- Hand check: axle bending ~49 MPa if the whole load is on one axle with a 60 mm span (conservative).
- Run mesh refinement as in `docs/simulation-checklist.md`.

## D. Fill in
`results.md`, screenshots to `results/`.

## E. Interview points
- Why v = √(2gh) is an upper bound
- Role of the wheel groove and rope contact
- Why the axle check is conservative
