# Grafici

In base a quanto richiesto da Marì, possiamo fare questi grafici:

## Associazione tra età di esordio e miglioramento clinico

Tabella di contingenza

- Tipo: istogramma con gruppo
- Asse X: [ esordio < 18, esordio ≥ 18]
- Asse Y: quantità

Quindi sostanzialmente avremmo due elementi sulla x, con due raggruppamenti (Sì/No) per il miglioramento clinico.

I due elementi sono:

- Esordio < 18
- Esordio ≥ 18

Dal db abbiamo il dato "Esordio in età adulta" dei genitori

Sulla tabella dei genitori abbiamo un dato che ci dice se c'è stato un miglioramento clinico in età adulta.

Parent::improvement_in_adulthood (boolean)

## Fenotipo dei genitori con FMF

Descrizione: Fenotipo dei genitori che soddisfano i criteri Eurofever/PRINTO 2019.

Istogramma non raggruppato, in cui le barre sono:

- Durata episodi
- Dolore osteoarticolare
- Tonsillite essudativa
- Cefalea
- Dolore addominale
- Aftosi
- Tonsillite eritematosa
- Dolore toracico
- Astenia
- ...

In sostanza, dobbiamo prendere la lista dei sintomi presenti in Parent e contare quante volte ciascun sintomo è presente tra i genitori con FMF.
