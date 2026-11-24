# IoT-Enabled Modular Cableway – Fusion 360 Mechanical Design & Simulation

Mechanical design and simulation work for an **IoT-enabled modular cableway transport system for hilly terrains**, a low-cost system for moving produce from remote hill farms to roadside collection points.

**Patent status:** Indian patent application no. 202641120616, filed Oct 2026, published, **awaiting examination**. This repo does not claim a grant. Confirm with the co-inventors what design detail may be public.

> **Status: concept stage.** Dimensions and loads are my own assumptions (see `docs/design-assumptions.md`). Results are filled in only from my own Fusion 360 runs. Nothing here is a validated or certified design.

## The system in brief
Pods descend by gravity-assisted motion along a rope. A low-power solar drive engages only on flat or uphill sections. Each pod carries a sensor package (load cell, GPS, IMU, RFID) relayed by an ESP32/LoRa gateway to a cloud hub and dashboard.

## The three mechanical subsystems

| # | Folder | Model | Simulation |
|---|---|---|---|
| 1 | `01-smart-cargo-pod/` | Pod with sensor bay, lug, vents, drain holes | Static stress with payload and dynamic factor, aluminium vs plastic |
| 2 | `02-carriage-hanger/` | Grooved wheels, side plates, axles, hanger straps | Gravity-driven slope motion study (check vs v = √(2gh)); stress on hanger and axle |
| 3 | `03-support-tower/` | 5 m steel tower, base plate, platform, solar panel mount | Static stress (rope tension + wind) and buckling |

## Progress tracker
Tick items only when the file is actually in the repo.

| Item | Pod | Carriage | Tower |
|---|---|---|---|
| Parametric model built (`cad/f3d`) | ☐ | ☐ | ☐ |
| STEP exported (`cad/step`) | ☐ | ☐ | ☐ |
| Drawing exported (`cad/drawings`) | ☐ | ☐ | ☐ |
| Simulation run | ☐ | ☐ | ☐ |
| Results table filled, screenshots saved | ☐ | ☐ | ☐ |
| Hand-check compared | ☐ | ☐ | ☐ |

## Repository layout
```
iot-cableway-fusion360/
├── README.md
├── .gitignore  .gitattributes          (Git LFS rules for CAD/STL)
├── docs/
│   ├── design-assumptions.md           every [ASSUMPTION] in one place
│   ├── dimensions.md                   dimensions and Fusion user parameters
│   ├── simulation-checklist.md         setup/QA checklist for every study
│   ├── fusion-platform-notes.md        what needs the Simulation Extension
│   └── github-publishing.md            how to publish this repo
├── cad/
│   ├── reference_stl/                  concept STL meshes (layout reference only)
│   ├── f3d/  step/  drawings/          YOUR Fusion models/exports go here
├── 01-smart-cargo-pod/    README.md (guide) · results.md · results/
├── 02-carriage-hanger/    README.md (guide) · results.md · results/
├── 03-support-tower/      README.md (guide) · results.md · results/
├── tools/
│   ├── rope_load_calc.py               hand-check calculations
│   └── output/hand_calc_output.txt     output of that script
└── resume/resume-notes.md              how this project appears on the resume
```

## How to use this repo
1. Read `docs/design-assumptions.md` and replace placeholders with your real values.
2. Run `python tools/rope_load_calc.py` to get hand-check numbers.
3. Rebuild each part in Fusion 360 from `docs/dimensions.md`, using `cad/reference_stl` only as a layout reference. The STLs are not editable parametric models and not suitable for FEA.
4. Follow each subsystem's `README.md` to simulate, then fill `results.md` from your own runs and add screenshots to `results/`.

## Honest scope notes
- STL meshes are simplified concepts (see `cad/reference_stl/README.txt`).
- A real 5 m tower needs a qualified structural design review before any construction.
- Hand calculations are sanity checks, not results.
