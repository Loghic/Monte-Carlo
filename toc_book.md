# Metoda Monte Carlo – obsah skripta

Skriptum, autor Miroslav Virius (FJFI ČVUT). Obsah je přepsaný z fotografií. Čísla v závorkách jsou strany; kde chybí, byl okraj stránky na fotografii oříznutý.

- Předmluva (s. 3)
- Obsah (s. 5)

## 1 Úvodní příklady (s. 10)

- 1.1 Model pojišťovny (s. 10)
  - 1.1.1 Formulace úlohy (s. 10)
  - 1.1.2 Analytické řešení (s. 11)
  - 1.1.3 Řešení metodou Monte Carlo (s. 12)
- 1.2 Sčítání číselné řady metodou Monte Carlo (s. 13)
- 1.3 Shrnutí (s. 15)

## 2 Odhad chyby (s. 18)

- 2.1 Výpočet střední hodnoty při konečném rozptylu (s. 18)
  - 2.1.1 Chyba při výpočtu pravděpodobnosti (s. 19)
- 2.2 Odhad chyby pomocí centrální limitní věty (s. 20)
- 2.3 Odhad chyby při nekonečném rozptylu (s. 21)
- 2.4 Odhad pomocí závislých realizací (s. 21)
- 2.5 Závěrečné poznámky (s. 22)

## 3 Modelování náhodných veličin (s. 24)

- 3.1 Diskrétní náhodné veličiny (s. 24)
  - 3.1.1 Základní algoritmus (s. 25)
  - 3.1.2 Binomické rozdělení (s. 29)
  - 3.1.3 Poissonovo rozdělení (s. 31)
- 3.2 Spojité náhodné veličiny (s. 32)
  - 3.2.1 Základní algoritmus (s. 32)
  - 3.2.2 Zamítací metoda (s. 35)
  - 3.2.3 Zamítací metoda na neomezeném intervalu (s. 37)
  - 3.2.4 Uspořádané výběry (s. 38)
  - 3.2.5 Metoda superpozice (s. 39)
  - 3.2.6 Exponenciální rozdělení (s. 40)
  - 3.2.7 Rozdělení Γ (s. 42)
  - 3.2.8 Rozdělení B (s. 44)
  - 3.2.9 Normální rozdělení (s. 46)
- 3.3 Vícerozměrné náhodné veličiny (s. 49)
  - 3.3.1 Základní metoda (s. 50)
  - 3.3.2 Rovnoměrně rozdělená náhodná veličina na G ⊂ ℝⁿ
  - 3.3.3 Izotropní náhodné vektory
  - 3.3.4 n-rozměrná normální náhodná veličina

## 4 Náhodná čísla s rozdělením R(0, 1)

- 4.1 Co je to pseudonáhodná posloupnost
  - 4.1.1 Požadavky kladené na pseudonáhodnou posloupnost
  - 4.1.2 Hledáme pseudonáhodnou posloupnost
- 4.2 Testování kvality generátorů pseudonáhodných čísel
  - 4.2.1 Frekvenční test (test dvojic)
  - 4.2.2 Test sérií
  - 4.2.3 Pokerový test
  - 4.2.4 Test běhů
  - 4.2.5 Autokorelační test
  - 4.2.6 Maurerův univerzální statistický test
- 4.3 Lineární kongruenční generátory
  - 4.3.1 Příklady lineárních kongruenčních generátorů
  - 4.3.2 Nevýhody lineárních kongruenčních generátorů
- 4.4 Generátory založené na lineárních posuvných registrech
  - 4.4.1 Lineární posuvný registr se zpětnou vazbou
  - 4.4.2 Generátor Mersenne Twister
- 4.5 Některé další generátory pseudonáhodných čísel
  - 4.5.1 Zpožděné Fibonacciovy generátory
  - 4.5.2 Dobře rovnoměrně rozložené lineární generátory s dlouhou periodou
  - 4.5.3 Generátory ze skupiny Xorshift

## 5 Výpočet určitých integrálů

- 5.1 Základní metody pro výpočet integrálu v ℝ
  - 5.1.1 Integrál z omezené funkce na konečném intervalu
  - 5.1.2 Porovnání obou metod
- 5.2 Snižování rozptylu
  - 5.2.1 Vyjmutí hlavní části
  - 5.2.2 Skupinový výběr (vzorkování po intervalech)
  - 5.2.3 Relevantní výběr
- 5.3 Příklady
  - 5.3.1 Metoda vzorkování plochy
  - 5.3.2 Metoda vzorkování funkce
  - 5.3.3 Metoda vzorkování funkce s vyjmutím hlavní části
  - 5.3.4 Skupinový výběr
  - 5.3.5 Relevantní výběr
- 5.4 Integrály funkcí více proměnných
  - 5.4.1 Základní metody
  - 5.4.2 Snižování rozptylu
- 5.5 Nevlastní integrály
  - 5.5.1 Integrand se singularitou
  - 5.5.2 Integrály přes neomezenou oblast
  - 5.5.3 Příklady
- 5.6 Metoda Monte Carlo a klasické kvadraturní vzorce (s. 98)
  - 5.6.1 Porovnání (s. 99)
  - 5.6.2 Zrychlení konvergence (s. 100)

## 6 Markovovy řetězce a lineární rovnice (s. 102)

- 6.1 Řešení soustavy lineárních algebraických rovnic (s. 102)
  - 6.1.1 Odvození základního algoritmu (s. 102)
  - 6.1.2 Použitelnost základního algoritmu (s. 105)
  - 6.1.3 Odhad funkcionálu I_h = (h, x) (s. 106)
  - 6.1.4 Algoritmus (s. 107)
  - 6.1.5 Jiný odhad funkcionálu I_h (s. 108)
  - 6.1.6 Optimalizace rozptylu (s. 108)
  - 6.1.7 Příklad (s. 108)
- 6.2 Řešení integrálních rovnic (s. 109)
  - 6.2.1 Úvodní úvahy (s. 110)
  - 6.2.2 Základní odhad funkcionálu I_h (s. 111)
  - 6.2.3 Použitelnost odhadu ξ (s. 114)
  - 6.2.4 Poznámky (s. 115)
  - 6.2.5 Optimalizace rozptylu (s. 117)
  - 6.2.6 Randomizace základního odhadu (s. 118)
  - 6.2.7 Příklad (s. 119)
- 6.3 Náhodná procházka po síti a diferenciální rovnice (s. 120)
  - 6.3.1 Vnitřní Dirichletova úloha pro Laplaceovu rovnici (s. 120)
  - 6.3.2 Vnitřní Dirichletova úloha pro Poissonovu rovnici (s. 125)
  - 6.3.3 Neumannova úloha pro Laplaceovu rovnici (s. 126)
  - 6.3.4 Řešení smíšené úlohy pro parabolickou rovnici (s. 128)
  - 6.3.5 Poznámky (s. 130)
- 6.4 Náhodná procházka po sférách a Dirichletova úloha (s. 130)
  - 6.4.1 Základní odhad (s. 130)
  - 6.4.2 Použitelnost odhadu ξ_ε (s. 133)
  - 6.4.3 Randomizovaný odhad (s. 134)
  - 6.4.4 Příklady (s. 136)

## 7 Použití metody Monte Carlo v teorii hromadné obsluhy (s. 139)

- 7.1 Systém hromadné obsluhy (s. 139)
  - 7.1.1 Základní charakteristiky systému (s. 139)
  - 7.1.2 Popis systému hromadné obsluhy (s. 140)
- 7.2 Toky požadavků (s. 141)
- 7.3 Modelování systémů hromadné obsluhy (s. 142)
- 7.4 Vyhodnocování výsledků (s. 143)
- 7.5 Metoda rozštěpení (s. 146)
- 7.6 Příklad (s. 146)
  - 7.6.1 Model typu Δt (s. 147)
  - 7.6.2 Model diskrétních událostí (s. 148)

## 8 Modelování transportu záření

- 8.1 Předpoklady
  - 8.1.1 Rozbor uvedených předpokladů
- 8.2 Veličiny
- 8.3 Obecné schéma modelování interakce záření s látkou
  - 8.3.1 Klíčové aspekty procesu interakce
  - 8.3.2 Vlastní algoritmus
- 8.4 Metoda rozštěpení
- 8.5 Neanalogové modelování
- 8.6 Příklad: průchod neutronů nekonečnou deskou
- 8.7 Příklad: výpočet asymetrie detektoru
  - 8.7.1 Klíčové aspekty modelu
  - 8.7.2 Postup simulace
  - 8.7.3 Poznámky

## 9 Některé stochastické algoritmy

- 9.1 Určování prvočíselnosti
- 9.2 Simulované žíhání
  - 9.2.1 Motivace
  - 9.2.2 Formulace úlohy
  - 9.2.3 Algoritmus simulovaného žíhání
  - 9.2.4 Parametry algoritmu simulovaného žíhání
  - 9.2.5 Příklad: Problém obchodního cestujícího

## 10 Dodatek: Základní pojmy a věty

- 10.1 Náhodné jevy a náhodné veličiny
  - 10.1.1 Elementární jevy a jevové pole
  - 10.1.2 Pravděpodobnost
  - 10.1.3 Náhodná veličina
  - 10.1.4 Vícerozměrná náhodná veličina
- 10.2 Charakteristiky náhodných veličin
  - 10.2.1 Střední hodnota
  - 10.2.2 Rozptyl a směrodatná odchylka
  - 10.2.3 Momenty k-tého řádu
- 10.3 Příklady náhodných veličin
  - 10.3.1 Diskrétní náhodné veličiny
- 10.4 Náhodný proces
  - 10.4.1 Charakteristiky náhodného procesu
  - 10.4.2 Markovův náhodný proces
- 10.5 Zákony velkých čísel
- 10.6 Odchylka normální náhodné veličiny od střední hodnoty
- 10.7 Statistické odhady
  - 10.7.1 Parametrické odhady
  - 10.7.2 Příklady odhadů
  - 10.7.3 Neparametrické odhady
- 10.8 Statistické testy
  - 10.8.1 Obecné schéma statistického kritéria
  - 10.8.2 Test χ² (s. 206)
  - 10.8.3 Studentův test t (s. 207)
  - 10.8.4 Fisherův test F (s. 208)

## 11 Dodatek: Důkazy některých tvrzení (s. 210)

- 11.1 Pomocná tvrzení o diskrétních náhodných veličinách (s. 210)
  - 11.1.1 Bernoulliova veličina a náhodná čísla (s. 210)
  - 11.1.2 Binomická veličina (s. 212)
  - 11.1.3 Rozdělení součinu veličin γ ∼ R(0, 1) (s. 214)
- 11.2 Pomocná tvrzení o spojitých náhodných veličinách (s. 215)
  - 11.2.1 Transformace náhodné veličiny pomocí distribuční funkce (s. 215)
  - 11.2.2 Věty o zamítací metodě (s. 216)
  - 11.2.3 Rozdělení Γ, B a exponenciální rozdělení (s. 217)
  - 11.2.4 Normální rozdělení a izotropní vektory (s. 219)
- 11.3 Centrální momenty při nekonečném rozptylu (s. 220)
- 11.4 Náhodná procházka po sférách (s. 223)

## Závěr knihy

- Označení (s. 225)
- Literatura (s. 227)
- Rejstřík (s. 230)
