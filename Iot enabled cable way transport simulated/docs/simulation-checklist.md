# Simulation checklist (use for every study)

**Before solving**
- [ ] Design units are mm; model matches `docs/dimensions.md`
- [ ] Small features (D6 drains, tiny fillets) suppressed unless they matter
- [ ] Material assigned via Study Materials and its properties noted
- [ ] Constraints reflect the real support, and the choice is noted
- [ ] Loads from `docs/design-assumptions.md`; dynamic factor applied **once**
- [ ] Gravity direction set
- [ ] Mesh settings noted (element size, local refinement)

**After solving**
- [ ] Reaction force equals total applied load
- [ ] Deformed shape looks physically sensible
- [ ] Mesh convergence: 3 mesh sizes, peak stress changes < ~5% between the last two
- [ ] Stress singularities (sharp re-entrant corners, point loads) identified and not quoted as peaks
- [ ] Linear study valid? If deflection exceeds about half the wall thickness (thin plates), use nonlinear or redesign
- [ ] Compared with the hand check in `tools/output/hand_calc_output.txt`
- [ ] Screenshots saved to the project's `results/` folder
- [ ] `results.md` filled only from this run
