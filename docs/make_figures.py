"""Regenerates the images used in README.md (docs/img/). Stdlib + matplotlib (+ Pillow for GIFs).

    uv run python docs/make_figures.py
"""
import math
import os
import random

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "figure.facecolor": "white"})
BLUE, RED, GREEN, ORANGE = "tab:blue", "tab:red", "tab:green", "tab:orange"


def save(fig, name, trim=False):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=110, bbox_inches="tight")
    plt.close(fig)
    if trim:                                    # crop the empty margin 3D axes leave behind
        from PIL import Image, ImageChops
        im = Image.open(path).convert("RGB")
        box = ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox()
        im.crop((max(box[0] - 12, 0), max(box[1] - 12, 0), min(box[2] + 12, im.width), min(box[3] + 12, im.height))).save(path)
    print("wrote", name)


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


# ---------------------------------------------------------------- 1. pi animation (hero)
def hero_pi():
    random.seed(3)
    N = 4000
    pts = [(random.random(), random.random()) for _ in range(N)]
    inside = [x * x + y * y <= 1 for x, y in pts]
    run, band, s = [], [], 0
    for i, ins in enumerate(inside, 1):
        s += ins
        p = s / i
        run.append(4 * p)
        band.append(8 * math.sqrt(max(p * (1 - p), 1e-12) / i))
    frames = sorted({int(10 * (N / 10) ** (k / 59)) for k in range(60)})

    fig, axes = plt.subplots(1, 2, figsize=(9, 3.9), gridspec_kw={"width_ratios": [1, 1.25]})
    t = [i / 200 * math.pi / 2 for i in range(201)]
    fig.subplots_adjust(left=0.04, right=0.985, bottom=0.17, top=0.88, wspace=0.16)

    def draw(n):
        for ax in axes:
            ax.clear()
        ax = axes[0]
        ax.scatter([x for (x, y), c in zip(pts[:n], inside[:n]) if c],
                   [y for (x, y), c in zip(pts[:n], inside[:n]) if c], s=5, c=GREEN, alpha=.7)
        ax.scatter([x for (x, y), c in zip(pts[:n], inside[:n]) if not c],
                   [y for (x, y), c in zip(pts[:n], inside[:n]) if not c], s=5, c=RED, alpha=.7)
        ax.plot([math.cos(a) for a in t], [math.sin(a) for a in t], "k", lw=1)
        ax.set_aspect("equal"); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
        ax.set_title(f"{n} random points", fontsize=10)
        ax = axes[1]
        idx = list(range(1, n + 1))
        lo = [r - b for r, b in zip(run[:n], band[:n])]
        hi = [r + b for r, b in zip(run[:n], band[:n])]
        ax.semilogx(idx, run[:n], color=BLUE, lw=1.4)
        ax.fill_between(idx, lo, hi, color=BLUE, alpha=.2, label="±2 standard errors (∝ 1/√N)")
        ax.axhline(math.pi, color="k", ls=":", label="π")
        ax.set_xlim(10, N); ax.set_ylim(2.5, 3.8)
        ax.set_xlabel("number of points N"); ax.set_ylabel("estimate of π")
        ax.set_title(f"π ≈ {run[n - 1]:.3f}   (error shrinks like 1/√N)", fontsize=10)
        ax.legend(loc="upper right", fontsize=8, frameon=False)

    anim = FuncAnimation(fig, lambda k: draw(frames[k]), frames=len(frames))
    anim.save(os.path.join(OUT, "hero_pi.gif"), writer=PillowWriter(fps=10), dpi=80)
    plt.close(fig)
    print("wrote hero_pi.gif")


# ---------------------------------------------------------------- 2. MCMC animation
def mcmc_gif():
    random.seed(5)
    W, MU, SD = (0.35, 0.65), (-2.0, 2.5), (0.8, 1.2)
    f = lambda x: sum(w * math.exp(-((x - m) / s) ** 2 / 2) / (s * math.sqrt(2 * math.pi))
                      for w, m, s in zip(W, MU, SD))
    x, fx, chain = 12.0, f(12.0), []                       # starts far from the target on purpose
    for _ in range(30000):
        y = x + random.gauss(0, 3.0)
        fy = f(y)
        if fy >= fx or random.random() < fy / fx:
            x, fx = y, fy
        chain.append(x)
    frames = sorted({int(20 * (30000 / 20) ** (k / 49)) for k in range(50)})
    grid = [-7 + 14 * i / 400 for i in range(401)]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    fig.subplots_adjust(left=0.09, right=0.98, bottom=0.17, top=0.9)

    def draw(n):
        ax.clear()
        w = 14 / 70
        ax.hist(chain[:n], bins=70, range=(-7, 7), weights=[1 / (n * w)] * n, color=BLUE, alpha=.55)
        ax.plot(grid, [f(g) for g in grid], RED, lw=1.8, label="target density")
        ax.plot([chain[n - 1]], [0], "v", color="k", ms=8)
        ax.set_xlim(-7, 13); ax.set_ylim(0, .36)
        ax.set_xlabel("x"); ax.set_ylabel("density")
        ax.set_title(f"Metropolis chain after {n} steps (it started at x = 12)", fontsize=10)
        ax.legend(loc="upper right", fontsize=8, frameon=False)

    anim = FuncAnimation(fig, lambda k: draw(frames[k]), frames=len(frames))
    anim.save(os.path.join(OUT, "mcmc.gif"), writer=PillowWriter(fps=9), dpi=80)
    plt.close(fig)
    print("wrote mcmc.gif")


# ---------------------------------------------------------------- 3. insurance: CLT vs simulation tail
def insurance():
    random.seed(1)
    N, p, L = 365, 0.05, 10_000
    lq = math.log(1 - p)

    def year():
        T, pos = 0.0, -1
        while True:
            pos += 1 + int(math.log(1 - random.random()) / lq)
            if pos >= N:
                return T
            T += L * math.sqrt(random.random())

    sample = sorted(year() for _ in range(300_000))
    mu, EX2 = 2 * L / 3, L * L / 2
    ET, sd = N * p * mu, math.sqrt(N * (p * EX2 - (p * mu) ** 2))
    Ks = [100_000 + 2_000 * i for i in range(61)]
    from bisect import bisect_right
    sim = [(len(sample) - bisect_right(sample, K)) / len(sample) for K in Ks]
    clt = [1 - phi((K - ET) / sd) for K in Ks]
    fig, ax = plt.subplots(figsize=(5.4, 3.7))
    ax.semilogy(Ks, [v if v > 0 else None for v in sim], color=BLUE, lw=2, label="simulation")
    ax.semilogy(Ks, clt, color=RED, ls="--", lw=2, label="normal (CLT) approximation")
    ax.set_xlabel("capital K"); ax.set_ylabel("P(ruin)")
    ax.set_title("The textbook approximation understates the risk", fontsize=10)
    ax.legend(frameon=False, fontsize=9)
    save(fig, "insurance_tail.png")


# ---------------------------------------------------------------- 4. variance reduction
def variance_reduction():
    random.seed(1)
    f = lambda x: math.exp(-x * x)
    Z = math.sqrt(math.pi) / 2 * math.erf(1)
    h = lambda x: 1 - x * x
    c = 0.668
    methods = {
        "hit-or-miss": lambda N: sum(random.random() < f(random.random()) for _ in range(N)) / N,
        "sample mean": lambda N: sum(f(random.random()) for _ in range(N)) / N,
        "antithetic": lambda N: sum(f(u) + f(1 - u) for u in (random.random() for _ in range(N // 2))) / N,
        "control variate": lambda N: sum(f(u) - c * (h(u) - 2 / 3) for u in (random.random() for _ in range(N))) / N,
        "stratified": lambda N: sum(f((i + random.random()) / N) for i in range(N)) / N,
    }
    Ns, R = [100, 300, 1000, 3000, 10_000], 150
    fig, ax = plt.subplots(figsize=(5.4, 3.7))
    for name, m in methods.items():
        se = []
        for N in Ns:
            xs = [m(N) for _ in range(R)]
            mm = sum(xs) / R
            se.append(math.sqrt(sum((x - mm) ** 2 for x in xs) / (R - 1)))
        ax.loglog(Ns, se, "o-", ms=3, label=name)
    ax.set_xlabel("number of points N"); ax.set_ylabel("standard error")
    ax.set_title("Same integral, same N: orders of magnitude apart", fontsize=10)
    ax.legend(frameon=False, fontsize=8, loc="lower left")
    save(fig, "variance_reduction.png")


# ---------------------------------------------------------------- 5. RANDU vs Mersenne Twister
def randu():
    random.seed(1)
    x, us = 1, []
    for _ in range(3002):
        x = 65539 * x % 2 ** 31
        us.append(x / 2 ** 31)
    mt = [random.random() for _ in range(3002)]
    fig = plt.figure(figsize=(8.2, 2.9))
    for k, (data, title, color) in enumerate(((us, "RANDU (IBM, 1960s):\nall points on 15 planes", RED),
                                              (mt, "Mersenne Twister (Python):\nsame viewing angle", GREEN))):
        ax = fig.add_subplot(1, 2, k + 1, projection="3d")
        ax.scatter(data[:3000], data[1:3001], data[2:3002], s=2, alpha=.5, color=color)
        ax.view_init(elev=0, azim=56.31)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
        ax.set_title(title, fontsize=10, y=0.98)
        ax.set_box_aspect((1, 1, 0.55))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=0.93, wspace=-0.1)
    save(fig, "randu.png", trim=True)


# ---------------------------------------------------------------- 6. percolation
def percolation():
    random.seed(1)
    L = 40
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.5))
    for ax, p in zip(axes, (0.40, 0.50, 0.60)):
        H = [[random.random() < p for _ in range(L - 1)] for _ in range(L)]
        V = [[random.random() < p for _ in range(L)] for _ in range(L - 1)]
        seen = [[False] * L for _ in range(L)]
        stack = [(r, 0) for r in range(L)]
        for r, c in stack:
            seen[r][c] = True
        while stack:
            r, c = stack.pop()
            for rr, cc, ok in ((r, c + 1, c < L - 1 and H[r][c]), (r, c - 1, c > 0 and H[r][c - 1]),
                               (r + 1, c, r < L - 1 and V[r][c]), (r - 1, c, r > 0 and V[r - 1][c])):
                if ok and not seen[rr][cc]:
                    seen[rr][cc] = True
                    stack.append((rr, cc))
        for r in range(L):
            for c in range(L - 1):
                if H[r][c]:
                    wet = seen[r][c] and seen[r][c + 1]
                    ax.plot([c, c + 1], [r, r], color=BLUE if wet else "0.84", lw=1.1 if wet else .5, zorder=2 if wet else 1)
        for r in range(L - 1):
            for c in range(L):
                if V[r][c]:
                    wet = seen[r][c] and seen[r + 1][c]
                    ax.plot([c, c], [r, r + 1], color=BLUE if wet else "0.84", lw=1.1 if wet else .5, zorder=2 if wet else 1)
        through = any(seen[r][L - 1] for r in range(L))
        ax.set_title(f"p = {p:.2f}: {'flows through' if through else 'blocked'}", fontsize=10)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
        for s in ax.spines.values():
            s.set_visible(False)
    save(fig, "percolation.png")


# ---------------------------------------------------------------- 7. projects slip: E[max] = H_n
def project_slip():
    random.seed(2)
    ns = [1, 2, 3, 5, 10, 20, 50]
    sim = [sum(max(random.expovariate(1) for _ in range(n)) for _ in range(30_000 // max(1, n // 4))) /
           (30_000 // max(1, n // 4)) for n in ns]
    nn = list(range(1, 51))
    fig, ax = plt.subplots(figsize=(5.4, 3.7))
    ax.plot(nn, [sum(1 / k for k in range(1, n + 1)) for n in nn], color=RED, lw=2, label="exact: $H_n$")
    ax.plot(ns, sim, "o", color=BLUE, label="simulation")
    ax.axhline(1, color="k", ls="--", lw=1, label="plan from averages")
    ax.set_xlabel("parallel tasks (each takes 1 on average)"); ax.set_ylabel("expected project duration")
    ax.set_title("Why projects run late: waiting for the slowest", fontsize=10)
    ax.legend(frameon=False, fontsize=9)
    save(fig, "project_slip.png")


if __name__ == "__main__":
    hero_pi()
    mcmc_gif()
    insurance()
    variance_reduction()
    randu()
    percolation()
    project_slip()
