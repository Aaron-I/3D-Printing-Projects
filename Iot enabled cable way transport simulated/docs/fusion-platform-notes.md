# Platform: Autodesk Fusion (Fusion 360), Simulation workspace

Modelling, assemblies and simulation all happen in Fusion.

| Study | Used for | Availability (verify on your account) |
|---|---|---|
| Static Stress (linear) | Pod, hanger, axle, tower | Base Fusion |
| Structural Buckling | Tower | Simulation Extension (token-based in base, included in extension) |
| Event Simulation | Carriage motion | Simulation Extension |
| Nonlinear Static Stress | Only if pod deflection is large | Simulation Extension |

- Check which study types are enabled on your own account (Simulation workspace → New Study). Plans change, and I could not confirm what the student/education licence includes today.
- The Simulation Extension has a free 14-day trial for existing Fusion subscribers. Build the models first, then start the trial.
- Fallbacks if a study type is unavailable: hand Euler calculation for buckling, and a Python/spreadsheet energy balance for carriage speed. Label them clearly as hand calculations, not FEA.
- Menu names differ between versions; use the search bar (S).
