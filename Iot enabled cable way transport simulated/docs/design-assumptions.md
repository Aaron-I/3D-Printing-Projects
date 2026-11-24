# Design assumptions

Everything below is a **placeholder** for this concept-stage study. Replace each value with your real design data, re-run `tools/rope_load_calc.py`, and note the date you changed it.

| Parameter | Value used | Marked | Notes |
|---|---|---|---|
| Payload | 20 kg | [ASSUMPTION] | Produce load |
| Pod mass (with sensors) | 6 kg | [ASSUMPTION] | |
| Carriage + hanger mass | 2 kg | [ASSUMPTION] | |
| Dynamic factor | 2.0 | [ASSUMPTION] | Applied once to gravity load. Do not also add it in Fusion. |
| **Design load** | **549 N** | derived | (20+6+2) kg × 9.81 × 2.0 |
| Rope span | 100 m | [ASSUMPTION] | |
| Mid-span sag (loaded) | 3.2 m | [ASSUMPTION] | |
| Vertical drop for motion check | 12 m | [ASSUMPTION] | |
| Slope angle | ___ ° | [ASSUMPTION] | Set from your terrain/design |
| Wind speed | 30 m/s | [ASSUMPTION] | |
| Panel drag coefficient | 1.2 | [ASSUMPTION] | |
| Air density | 1.225 kg/m³ | standard | |
| Aluminium | 6061-T6 | choice | Take E, yield, density from the Fusion library or a datasheet |
| Plastic | ___ (ABS / PA12 / PETG) | choose one | Copy E, yield, density from its datasheet |
| Tower steel | Structural steel (e.g. S235/E250) | choice | Verify grade |

Derived hand-check values are in `tools/output/hand_calc_output.txt`.

## Rules for this repo
- Replace `___` only with values from your own runs.
- Label analytical numbers as "hand calculation".
- If a study was not run, write "not run".
