# bp-cryptografische-chips

## Background info
Dit is een korte lijst met enkele links naar achtergrond informatie:

* [SPECK](https://en.wikipedia.org/wiki/Speck_(cipher)): Dit is het ARX algoritme (Add-Rotate-XOR) dat onderzocht dient te worden. Zoals blijkt uit de beschrijving, kan dit cipher met verschillende blok-groottes werken. Dit zou flexibel moeten blijven en heeft voornamelijk betrekking tot het aantal rondes.
* [Power Analysis](https://en.wikipedia.org/wiki/Power_analysis): Dit artikel geeft een overzicht van verschillende soorten vermogen aanvallen en hoe deze (in grote lijnen) in zijn werk gaan.
* [Welch's t-test](https://en.wikipedia.org/wiki/Welch%27s_t-test): Dit artikel gaat over de T-test. Dit is de test die gebruikt wordt om te bepalen of een implementatie nog side-channel info lekt.
* [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight)
* [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)

## Running it

Gebruik `python -m unittest` in een python dir om unit testen uit te voeren. Embedded in de huidig meegeleverde `Makefile` met het commando `make test`.

Gebruik de handige cmdline parser package om aan `main.py` de juiste argumenten mee te geven, om die dan in de `BP_Speck` klasse te gebruiken. Zie main file en Makefile voor meer informatie. 