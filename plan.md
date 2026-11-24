# Plan

Forward-looking only. Tick items off and delete them as they land; the record of what was
done lives in git history and in `docs/`, not here.

## Agreed conventions

- **Decimal separator is a dot**, English convention. Commas separate items only.
  Thousands are separated by **spaces**, never commas.
- **Notation follows the scriptum** (`notation.md`) for `γ` (uniform variate), `Dξ`
  (variance) and `N(μ, σ)` (second parameter is the standard deviation).
  Random variables stay `X`, not `ξ` — recorded as a deliberate deviation in `notation.md`.
- Three folders, one rule each: `notebooks/cs/` = numbered lessons mirroring the practical
  classes; `notebooks/cs/extra/` = scriptum chapters never taught, prefixed by **book
  chapter**; `notebooks/cs/aplikace/` = anything beyond the scriptum, descriptive names.
- Every notebook is standalone: it re-defines its own helpers, uses stdlib + matplotlib,
  and ends with a NumPy variant.

## 1. Notation sweep — done

Swept and verified: 83 markdown lines, 60 code edits, 0 remaining `U`-in-math or
`\operatorname{Var}`, all 12 Czech prepositions "U …" intact, all 9 notebooks still run.
Code `g` renamed to `gamma` where it meant the uniform variate; `g` now means only the
proposal density (nb 6, 7). `notation.md` records both.

## 2. Insurance split — done

`02_pojistovna.ipynb` trimmed to 14 cells (model → CLV → naive simulation → punchline:
the CLV estimate sits 8.5 standard errors outside the simulation's band).
`09_pojistovna_kompletne.ipynb` built: geometric skip, claim times from ordered samples,
CLV/Čebyšev/Wilson + coverage, importance sampling for rare ruin, required capital, NumPy.
Signposts added to nb 03, 04, 05.

Measured importance-sampling gain: 19x at K = 200 000, 433x at K = 250 000, and at
K = 300 000 plain MC gets 0 hits from 100 000 runs while weighting returns
1.77e-07 +- 7.6e-09.

## 3. Extras — done except ch 8

All in `notebooks/cs/extra/`, each verified by running it end to end:

- [x] `ch04_generatory.ipynb` — LCG, RANDU's 15 planes (viewed along the normal (9,-6,1)),
  Mersenne Twister.
- [x] `ch04_testy_generatoru.ipynb` — χ² implemented from scratch (checked against tables),
  frequency / serial / poker / runs / autocorrelation, second-order test.
  Payoff: RANDU passes every test except the 3-D serial one.
- [x] `ch09_stochasticke_algoritmy.ipynb` — Fermat vs Miller–Rabin on Carmichael numbers
  (0 % vs 90–99 % witnesses), simulated annealing on TSP.
- [x] `ch01_05_kdy_se_mc_vyplati.ipynb` — series by MC, MC vs quadrature (crossover measured
  at d = 4), dependent realizations (naive error bar underestimates ~6x at φ = 0.95).
- [x] `ch03_gamma_beta.ipynb` — Γ via summed exponentials and Marsaglia–Tsang (95–99.7 %
  acceptance), B via order statistics and Γ ratio, χ² = Γ(k/2, 1/2).
- [x] `ch07_hromadna_obsluha.ipynb` — M/M/1, Δt model vs discrete-event model (Δt bias
  measured as linear in Δt), warm-up transient, Little's law as a check.
- [x] `ch06_markov_linearni_rovnice.ipynb` — von Neumann–Ulam walk; cost per component is
  flat in n while iteration grows.
- [x] `ch06_prochazka_a_pde.ipynb` — Dirichlet and Poisson on a lattice, harmonic measure,
  walk-on-spheres (76–131x faster, no discretization error).

- [x] `aplikace/pojistovna_realisticky.ipynb` — the simple model's simplifications removed one
  at a time, each with an exact check or a limiting case that recovers the previous model:
  gradual premiums (timing matters), clustered claims at *identical* expected cost
  (~4x more ruin), Lundberg generalised via the cluster-size pgf, payout delays
  (which help: 20x less ruin at 90 days), and a finite claims-handling queue
  (M/M/1 anchor holds without clusters, becomes approximate with them).

- [ ] `ch08_transport_zareni.ipynb` — **parked**. Needs scriptum pages and physics context.

## 4. Applications — `notebooks/cs/aplikace/`

- [x] `pojistovna_realisticky.ipynb`
- [x] `mcmc_metropolis.ipynb` — closes the sampling gap; ch01_05 and ch09 both leaned on
  MCMC without ever teaching it. Verified against exact mixture moments and E||X||² = d/(d+2).
- [x] `osobni_rozpocet.ipynb` — budget as the insurance model, anchored by gambler's ruin.
  Headline: removing breakdown *uncertainty* takes ruin from 7% to 0%, while restaurants
  (which cost more on average) change nothing.

- [x] `oceneni_opci.ipynb` — Black–Scholes exact anchor; control variate on the Asian option
  gives **865x** variance reduction (correlation 0.99942).
- [x] `vetvici_proces.ipynb` — extinction = smallest root of s = G(s); phase transition at R0 = 1.
- [x] `perkolace.ipynb` — p_c = 1/2 exact, but only on the L x (L+1) rectangle; the square
  drifts (0.567 -> 0.513) and would have suggested a different p_c.
- [x] `planovani_projektu.ipynb` — E[max] = H_n exactly; critical path varies run to run
  (backend 56%, frontend 43%, databáze 1%), matching the sensitivity analysis.
- [x] `spolehlivost_systemu.ipynb` — (1-q^k)^B exact; at q = 1e-5 plain MC gets 0 hits from
  200 000 while weighting returns the right order from 50 000.
- [x] `bootstrap.ipynb` — coverage experiment shows ~90% not 95% on small skewed samples;
  fails outright for the maximum (9 distinct values from 4000 replications).
- [x] `run_na_banku.ipynb` — self-exciting feedback; avalanche size 1/(1-n) verified.

## 4. Open


- [ ] English notebooks in `notebooks/en/`, after the Czech ones are final.
