# Značení / Notation

Přepis oddílu **Označení** (s. 225) ze skripta *Metoda Monte Carlo* (M. Virius, FJFI ČVUT),
doplněný o poznámku, kde se sešity od skripta liší.

Transcribed from the **Označení** section (p. 225) of the course scriptum, with a note on
where these notebooks deviate.

## Náhodné veličiny a rozdělení / Random variables and distributions

| Symbol | Česky | English |
|---|---|---|
| ξ, ν, … | malá řecká písmena značí náhodné veličiny nebo jejich realizace | small Greek letters denote random variables or their realisations |
| γ | náhodné číslo s rozdělením R(0, 1), nebo jeho realizace | a random number with the R(0, 1) distribution, or its realisation |
| ξ ∼ f, ξ ∼ F | ξ má hustotu f, resp. distribuční funkci F; vpravo od ∼ může stát i jiný symbol rozdělení | ξ has density f, resp. distribution function F; another distribution symbol may stand to the right of ∼ |
| R(a, b) | rovnoměrné rozdělení na (a, b) | uniform distribution on (a, b) |
| R(G) | rovnoměrné rozdělení na množině G | uniform distribution on the set G |
| N(μ, σ) | normální rozdělení se střední hodnotou μ a **směrodatnou odchylkou** σ | normal distribution with mean μ and **standard deviation** σ |

> **Pozor:** druhý parametr je σ, **ne** σ². Tedy N(1, 2) má rozptyl 4.
> The second parameter is σ, **not** σ². So N(1, 2) has variance 4.

## Momenty a charakteristiky / Moments and characteristics

| Symbol | Česky | English |
|---|---|---|
| Eξ | střední hodnota náhodné veličiny ξ | mean value (expectation) of ξ |
| E(ξ \| B) | střední hodnota ξ za podmínky B | expectation of ξ given B |
| E₍ₓ₎ξ | střední hodnota ξ přes všechny hodnoty x | expectation of ξ over all values of x |
| Dξ | rozptyl (disperze) náhodné veličiny ξ | variance (dispersion) of ξ |
| σ_ξ | směrodatná odchylka, σ_ξ = √(Dξ) | standard deviation, σ_ξ = √(Dξ) |
| Cξ | kovarianční matice vícerozměrné náhodné veličiny ξ | covariance matrix of a multidimensional ξ |
| d_r | r-tý centrální absolutní moment | r-th central absolute moment |
| μ_r | r-tý obecný absolutní moment (kolem nuly) | r-th raw (ordinary) absolute moment (about zero) |
| R(τ), R(t, τ) | korelační funkce náhodného procesu | correlation function of a random process |

## Pravděpodobnost / Probability

| Symbol | Česky | English |
|---|---|---|
| P(A) | pravděpodobnost jevu A | probability of the event A |
| P(A \| B) | pravděpodobnost A za podmínky B | probability of A given B |

## Množiny a prostory / Sets and spaces

| Symbol | Česky | English |
|---|---|---|
| ℕ | přirozená čísla | natural numbers |
| ℕ₀ | přirozená čísla včetně nuly | natural numbers including zero |
| ℤ | celá čísla | integers |
| ℚ | racionální čísla | rational numbers |
| ℝ | reálná čísla | real numbers |
| ℝⁿ | n-tice reálných čísel | n-tuples of real numbers |
| ℂ | komplexní čísla | complex numbers |
| n̂ | množina {1, …, n} | the set {1, …, n} |
| V(G) | objem množiny G, V(G) = ∫_G dx | volume of the set G |
| ∂G | hranice množiny G | boundary of the set G |
| ℒ_p(G) | prostor funkcí integrovatelných s p-tou mocninou na G | space of functions p-th-power integrable on G |
| ℒ_∞(G) | prostor funkcí omezených na G | space of functions bounded on G |

## Matice a operátory / Matrices and operators

| Symbol | Česky | English |
|---|---|---|
| Aᵀ | transponovaná matice | transposed matrix |
| I | jednotková matice | identity matrix |
| ‖v‖_X | norma v v prostoru X | norm of v in the space X |
| ρ(A) | spektrální poloměr matice A | spectral radius of the matrix A |
| δ_ij | Kroneckerův symbol: δ_ij = 1 pro i = j, jinak 0 | Kronecker delta: δ_ij = 1 if i = j, else 0 |

## Ostatní / Miscellaneous

| Symbol | Česky | English |
|---|---|---|
| [x] | celá část čísla x | integer part of x |
| O(f(n)) | asymptotická horní mez | asymptotic upper bound (big O) |
| Ω(f(n)) | asymptotická dolní mez | asymptotic lower bound |

## Přetížené symboly / Overloaded symbols

Skriptum používá stejné písmeno ve více významech; rozliší je až kontext.
The scriptum reuses the same letter for several things; only context separates them.

- **R** — rovnoměrné rozdělení `R(a, b)`, korelační funkce `R(τ)`, a množina reálných čísel `ℝ`.
- **N** — normální rozdělení `N(μ, σ)`, a množina přirozených čísel `ℕ`.
  V sešitech navíc `N` často značí počet vzorků nebo počet intervalů.
  In the notebooks `N` also commonly denotes a sample count or a number of intervals.

## Kde se sešity liší / Where these notebooks differ

| Sešity / Notebooks | Skriptum | Proč / Why |
|---|---|---|
| X, Xᵢ | ξ | X je mezinárodně obvyklé a čte se snáz; ξ potkáte v přednáškách a ve skriptu. X is the international convention and reads more easily; you will meet ξ in lectures and in the book. |

V kódu se náhodné číslo z R(0, 1) jmenuje `gamma`. Jméno `g` je vyhrazené pro
**návrhovou hustotu** u zamítací metody a vážení podle důležitosti (sešity 6 a 7).

In the code a random number from R(0, 1) is named `gamma`. The name `g` is reserved for the
**proposal density** in the rejection method and importance sampling (notebooks 6 and 7).
