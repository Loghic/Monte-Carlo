# MEMC – Monte Carlo exercises

Practical, code-first notebooks for the Monte Carlo course (FJFI). Each notebook gives just enough theory to get the idea, then worked examples with code and plots.

The main code uses only the standard library (`random`, `math`) plus `matplotlib` for plots. Where it helps, a notebook also shows a NumPy / SciPy alternative (NumPy ships with matplotlib; SciPy is the optional `alt` extra).

## Contents

Czech notebooks are in `notebooks/cs/`; the English versions are in `notebooks/en/` with the same
structure (`extra/`, and `applications/` for Czech `aplikace/`). Each English notebook mirrors its
Czech twin cell for cell, with identifiers, printed output and prose translated. The table below lists
the Czech filenames; the English ones are the translated equivalents (`02_pojistovna` →
`02_insurance_company`, `aplikace/perkolace` → `applications/percolation`, and so on).

| # | Notebook | Topic |
|---|----------|-------|
| 0 | `00_opakovani.ipynb` | Refresher: expectation, variance, distributions, law of large numbers, Chebyshev, CLT, confidence intervals |
| 1 | `01_uvod_do_monte_carla.ipynb` | Monte Carlo basics: π (hit-or-miss, Buffon), integrals, error ∝ 1/√N, required N, volume of a ball |
| 2 | `02_pojistovna.ipynb` | Insurance company: model, CLT approximation vs simulation, ruin probability, confidence intervals (CLT, Chebyshev, Wilson), rare events, required capital, NumPy variant |
| 3 | `03_diskretni_rozdeleni.ipynb` | Discrete distributions: basic (linear) algorithm, reordering, bisection, Poisson (product of uniforms and inverse), geometric, NumPy variant |
| 4 | `04_spojita_rozdeleni.ipynb` | Continuous distributions: inverse transform (uniform, exponential, Cauchy, triangular, piecewise constant), why the LLN fails for Cauchy, numerical inversion, NumPy variant |
| 5 | `05_superpozice_a_usporadane_vybery.ipynb` | Mixtures (pick a component, then draw), mixture mean and variance, ordered samples in O(n), top-k of a huge sample, claim times, NumPy variant |
| 6 | `06_zamitaci_metoda.ipynb` | Rejection method: box version, envelope version, normal from a Cauchy envelope, choosing the constant M, what happens when M is wrong, NumPy batch variant |
| 7 | `07_snizovani_rozptylu.ipynb` | Variance reduction: sample mean vs hit-or-miss, antithetic variables, control variate, stratification, importance sampling (rare events, singularities), NumPy variant |
| 8 | `08_vzdalenost_v_kouli.ipynb` | Points in a ball: rejection vs polar coordinates, why r = U^(1/d), distance between two points, symmetry trick, higher dimensions |
| 9 | `09_pojistovna_kompletne.ipynb` | Insurance, finished: confidence intervals and their coverage, rare ruin by importance sampling, required capital from quantiles — uses the tools from 3-7 |

Notebook 2 introduces the insurance model and stops at the point where simulation beats the
CLT estimate; notebook 9 is the capstone that solves it properly.

### Extra notebooks

`notebooks/cs/extra/` holds material from the course scriptum that the practical lessons did
not cover. These are **not** numbered as lessons — the prefix is the *book chapter*.
(Material that is not in the scriptum at all lives in `notebooks/cs/aplikace/` instead.)

| File | Topic |
|------|-------|
| `ch01_05_kdy_se_mc_vyplati.ipynb` | When MC is the right tool: summing a series, MC vs classical quadrature (crossover at d = 4), dependent realizations |
| `ch03_gamma_beta.ipynb` | Γ and B distributions: summed exponentials, Marsaglia–Tsang, order statistics, χ² = Γ(k/2, 1/2) |
| `ch04_generatory.ipynb` | Pseudorandom generators: LCG, the RANDU planes, Mersenne Twister |
| `ch04_testy_generatoru.ipynb` | Testing generators: χ², frequency, serial, poker, runs, autocorrelation |
| `ch06_markov_linearni_rovnice.ipynb` | Solving Ax = b by random walks (von Neumann–Ulam) |
| `ch06_prochazka_a_pde.ipynb` | Dirichlet and Poisson problems by random walks; walk on spheres |
| `ch07_hromadna_obsluha.ipynb` | Queueing (M/M/1): Δt model vs discrete-event model |
| `ch09_stochasticke_algoritmy.ipynb` | Miller–Rabin primality, simulated annealing |

### Applications

`notebooks/cs/aplikace/` holds worked real-world problems that go beyond the scriptum.
Descriptive names, no numbers.

| File | Topic |
|------|-------|
| `pojistovna_realisticky.ipynb` | Insurance with its simplifications removed one at a time: premiums arriving gradually, clustered claims (one crash, several parties), generalised Lundberg bound, payout delays, a finite claims-handling queue |
| `mcmc_metropolis.ipynb` | Metropolis algorithm: sampling when neither inverse transform nor rejection works; step size and autocorrelation time; burn-in and batch-means error bars; uniform point in a 20-dimensional ball |
| `osobni_rozpocet.ipynb` | Household budget as the insurance model: how big an emergency fund, reaching a savings goal before going negative (gambler's ruin), and which uncertainty actually drives the risk |
| `oceneni_opci.ipynb` | Option pricing: Black–Scholes as an exact check, antithetic variables, Asian options where no formula exists (control variate gives ~850x), barrier options |
| `vetvici_proces.ipynb` | Branching process: extinction probability as the smallest root of s = G(s), the phase transition at R0 = 1, and why most introductions die out anyway |
| `perkolace.ipynb` | Percolation: the p_c = 1/2 phase transition, exact by self-duality on the right rectangle, and the giant cluster |
| `planovani_projektu.ipynb` | Why projects run late: E[max] > max E, exact via harmonic numbers; critical path that moves, and where extra effort actually pays |
| `spolehlivost_systemu.ipynb` | System reliability: series/parallel exact formulas, diminishing returns of redundancy, rare failures via importance sampling |
| `bootstrap.ipynb` | Bootstrap: confidence intervals for any statistic without a formula, a coverage experiment, and the statistics where it genuinely fails |
| `run_na_banku.ipynb` | Self-exciting process: feedback in time, avalanche size 1/(1-n), why clusters need no external cause and where to intervene |

### Reference

- `notation.md` — symbols used in the notebooks, matched to the scriptum (bilingual).
- `toc_book.md` — contents of the scriptum.
- `plan.md` — what is still open.

## Setup with uv

1. Install [uv](https://docs.astral.sh/uv/) (once):

   ```bash
   # macOS
   brew install uv
   # or, any Unix
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. From this folder, create the environment and start JupyterLab:

   ```bash
   cd MEMC
   uv sync              # creates .venv with matplotlib + jupyterlab
   uv run jupyter lab   # opens JupyterLab in your browser
   ```

   Then open `notebooks/cs/00_opakovani.ipynb`. The kernel *Python 3 (ipykernel)* is the project's `.venv`, so no extra kernel setup is needed.

3. Optional SciPy alternatives (NumPy is already installed together with matplotlib):

   ```bash
   uv sync --extra alt
   ```

   Without this, the SciPy cells in later notebooks print a hint and the rest still runs.

### One-off run without syncing

```bash
uv run --with jupyterlab --with matplotlib jupyter lab
```

### Check that a notebook runs from top to bottom

```bash
uv run jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=600 notebooks/cs/00_opakovani.ipynb --output-dir /tmp
```

### VS Code instead of JupyterLab

Open the folder, run `uv sync`, open a notebook and pick the interpreter `.venv/bin/python` as its kernel.

## Notes

- Notebooks seed the random generator, so results are reproducible; change the seed to see the variation.
- Everything uses Python 3.10 or newer.
