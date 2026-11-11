import math

H, L1, L2, L3 = 6.7, 5, 4.2, 5

def ik(x, y, z, phi_deg):
    r = math.hypot(x, y)
    phi = math.radians(phi_deg)
    th0 = math.atan2(y, x)

    wr = r - L3 * math.cos(phi)
    wz = (z - H) - L3 * math.sin(phi)
    d = math.hypot(wr, wz)
    EPS = 1e-6
    if not (abs(L1 - L2) <= d <= (L1 + L2) + EPS):
        raise ValueError("Target is unreachable")

    cos_th2 = (d**2 - L1**2 - L2**2) / (2 * L1 * L2)
    th2 = -math.acos(max(-1, min(1, cos_th2)))

    beta = math.atan2(wz, wr)
    gama =  math.atan2(L2 * math.sin(th2), L1 + L2 * math.cos(th2))

    th1 = beta - gama
    th3 = phi - th1 - th2
    return [math.degrees(th0), math.degrees(th1), math.degrees(th2), math.degrees(th3)]

def fk(th0_deg, th1_deg, th2_deg, th3_deg):
    th0, th1, th2, th3 = map(math.radians, [th0_deg, th1_deg, th2_deg, th3_deg])
    r = L1 * math.cos(th1) + L2 * math.cos(th1 + th2) + L3 * math.cos(th1 + th2 + th3)
    z = H + L1 * math.sin(th1) + L2 * math.sin(th1 + th2) + L3 * math.sin(th1 + th2 + th3)
    return [r * math.cos(th0), r * math.sin(th0), z]

ang = ik(10, 5, 5, 30)
pos = fk(*ang)

print(ang)
print(pos)