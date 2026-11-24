"""
Hand-calculation helper for the IoT cableway concept models.

Every input marked [ASSUMPTION] is a placeholder. Replace it with your real
design value, re-run, and use the output ONLY as a sanity check on your
Fusion 360 simulations. These are not simulation results.

Run:  python tools/rope_load_calc.py
"""
import math

g = 9.81  # m/s^2

# ---------------- Inputs ----------------
# [ASSUMPTION] masses (kg)
payload_kg = 20.0
pod_kg = 6.0            # pod incl. sensors
carriage_kg = 2.0       # carriage + hanger
dyn_factor = 2.0        # dynamic amplification on gravity load
# [ASSUMPTION] cableway geometry
span_m = 100.0          # rope span between towers
sag_m = 3.2             # mid-span sag with load at centre
drop_h_m = 12.0         # vertical drop for the motion check
# [ASSUMPTION] wind on solar panel
wind_ms = 30.0
rho_air = 1.225
cd_panel = 1.2
panel_w_m, panel_h_m = 1.650, 0.990     # from dimensions.md
# Tower (mm) from dimensions.md
tower_h_mm = 5000.0
leg_od, leg_t = 48.3, 3.2
base_leg_centres = 600.0
brace_bay_mm = 1000.0
E_steel = 200e3         # MPa
# Axle
axle_d = 12.0
axle_span = 60.0        # gap between side plates, mm
# Pod floor
pod_in_x, pod_in_y, floor_t = 594.0, 394.0, 3.0   # mm
# Wheels (assumed solid aluminium discs)
wheel_m = 0.4
wheel_r = 0.040
wheel_groove_r_eff = 0.0355   # radius at groove bottom, m

# ---------------- Calculations ----------------
total_kg = payload_kg + pod_kg + carriage_kg
W = total_kg * g
P_design = W * dyn_factor
print("== Hanger / carriage design load ==")
print(f"Total suspended mass        : {total_kg:.1f} kg")
print(f"Static weight               : {W:.0f} N")
print(f"Design load (x{dyn_factor})        : {P_design:.0f} N")

# Rope: point load at mid-span, taut-string approximation (rope self-weight ignored)
H = P_design * span_m / (4 * sag_m)
V = P_design / 2
T_end = math.hypot(H, V)
print("\n== Rope tension (point load at mid-span) ==")
print(f"Horizontal component H      : {H:.0f} N")
print(f"Tension at end tower        : {T_end/1000:.2f} kN")

# Motion
v_ideal = math.sqrt(2 * g * drop_h_m)
I_total = 2 * 0.5 * wheel_m * wheel_r**2
k = I_total / wheel_groove_r_eff**2
v_roll = math.sqrt(2 * g * drop_h_m / (1 + k / total_kg))
print("\n== Descent speed over a %.0f m vertical drop ==" % drop_h_m)
print(f"Ideal v = sqrt(2gh)         : {v_ideal:.1f} m/s  (upper bound, no friction)")
print(f"With wheel inertia only     : {v_roll:.1f} m/s  (friction/drag will lower it further)")

# Wind
A = panel_w_m * panel_h_m
F_wind = 0.5 * rho_air * wind_ms**2 * cd_panel * A
print("\n== Wind on solar panel ==")
print(f"Panel area                  : {A:.3f} m^2")
print(f"Wind force                  : {F_wind/1000:.2f} kN at {wind_ms:.0f} m/s")

# Axle bending: full design load on ONE axle (conservative), simply supported, central load
M_axle = P_design * axle_span / 4
Z_axle = math.pi * axle_d**3 / 32
print("\n== Axle bending (conservative: whole load on one axle) ==")
print(f"Bending stress              : {M_axle / Z_axle:.0f} MPa")

# Tower leg axial stress from overturning (legs only, braces ignored)
A_leg = math.pi / 4 * (leg_od**2 - (leg_od - 2 * leg_t)**2)
I_leg = math.pi / 64 * (leg_od**4 - (leg_od - 2 * leg_t)**4)
M_ot = (H + F_wind) * tower_h_mm            # N*mm, rope and wind in same direction
F_leg = M_ot / base_leg_centres / 2         # two legs per side share the couple
print("\n== Tower leg (overturning, rope + wind aligned, legs only) ==")
print(f"Overturning moment at base  : {M_ot/1e6:.1f} kN*m")
print(f"Leg axial force             : {F_leg/1000:.1f} kN")
print(f"Leg axial stress            : {F_leg / A_leg:.0f} MPa  (leg area {A_leg:.0f} mm^2)")
P_cr = math.pi**2 * E_steel * I_leg / brace_bay_mm**2
print(f"Euler Pcr, one brace bay    : {P_cr/1000:.0f} kN (K=1, pinned ends; indicative only)")
print(f"Ratio Pcr / leg force       : {P_cr / F_leg:.1f}")

# Pod floor strip
p = P_design / (pod_in_x * pod_in_y)        # MPa
sigma_floor = 0.75 * p * pod_in_y**2 / floor_t**2
print("\n== Pod floor, 394 mm strip, simply supported (thin-strip estimate) ==")
print(f"Pressure on floor           : {p:.4f} MPa")
print(f"Bending stress              : {sigma_floor:.0f} MPa")
print("Compare with yield: Al 6061-T6 ~275 MPa, ABS ~40 MPa (check your datasheet).")
