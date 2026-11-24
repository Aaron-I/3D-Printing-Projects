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

