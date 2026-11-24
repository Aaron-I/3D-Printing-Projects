# Dimensions (mm) – concept-stage choices

These are my concept sizes, not taken from the patent. Change them here first if your design differs, then update the models and rerun the simulations. The same values are in `cad/reference_stl/dimensions_manifest.json`.

## 1. Smart Cargo Pod
| Feature | Value |
|---|---|
| Body (L × W × H) | 600 × 400 × 350 |
| Wall thickness | 3 |
| Corner radius | R10 |
| Lid | 600 × 400 × 3 |
| Lug (vertical plate) | 40 × 60 × 12, hole D12 |
| Vent slots | 4 × (80 × 10) on each long side |
| Drain holes | 4 × D6 |
| Sensor bay | 120 × 80 × 40, under the lid |

## 2. Carriage and Hanger Assembly
| Feature | Value |
|---|---|
| Wheels | 2 × D80 × 30, U-groove R4.5 |
| Wheel pitch | 100 |
| Side plates | 2 × 200 × 120 × 8, 60 gap between them |
| Axles | 2 × D12 × 100 (one per wheel) |
| Hanger straps | 2 × 150 × 40 × 6, holes 120 apart, straddling the lug |
| Pins | D12 |
| Spacers | OD20 × 15 |

## 3. Support Tower with Solar Drive Mount
| Feature | Value |
|---|---|
| Height | 5000 |
| Leg centres | 600 at base, 300 at top |
| Legs | 4 × D48.3 × 3.2 tube |
| Braces | D33.7 × 2.6 tube, every 1000 |
| Base plate | 800 × 800 × 12, 4 × D20 holes |
| Top platform | 500 × 400 × 10 |
| Solar panel | 1650 × 990 × 35, tilted 15° |
| Panel rail / arm | 40 × 40 × 3 square tube, rail 1650, arm 900 (mounting concept only) |

## Fusion 360 user parameters
Add these under Modify → Change Parameters (units mm unless shown):

```
pod_L = 600 mm        pod_W = 400 mm       pod_H = 350 mm
pod_wall = 3 mm       pod_fillet = 10 mm
lug_w = 40 mm  lug_h = 60 mm  lug_t = 12 mm  lug_hole = 12 mm
wheel_D = 80 mm  wheel_w = 30 mm  groove_R = 4.5 mm  wheel_pitch = 100 mm
plate_L = 200 mm  plate_H = 120 mm  plate_t = 8 mm  plate_gap = 60 mm
axle_D = 12 mm  axle_L = 100 mm
strap_L = 150 mm  strap_w = 40 mm  strap_t = 6 mm  strap_hole_pitch = 120 mm
tower_H = 5000 mm  leg_base = 600 mm  leg_top = 300 mm
leg_OD = 48.3 mm  leg_t = 3.2 mm  brace_OD = 33.7 mm  brace_t = 2.6 mm
bay = 1000 mm  base_plate = 800 mm  base_plate_t = 12 mm  base_hole = 20 mm
panel_L = 1650 mm  panel_W = 990 mm  panel_t = 35 mm  panel_tilt = 15 deg
```

> The STL package has no dimension sheets. If you made PNG drawings, put them in `cad/drawings/`.
