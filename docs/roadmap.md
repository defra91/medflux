# Roadmap

## Obiettivo del progetto

Creare un sistema completo per:

- leggere il database clinico fornito da Carlino (file Excel)
- convertirlo in oggetti di dominio puliti
- calcolare statistiche cliniche e genetiche
- generare un report professionale in HTML → PDF
- includere sezioni utili per analisi clinica, genetica e diagnostica

## Task

### Lettura del database clinico

- Lettura dei fogli Excel
- Validazione delle colonne
- Conversione delle righe in oggetti di dominio (Parent, Child, Family)

### Modellazione del dominio

- Definizione delle classi di dominio (Parent, Child, Family)
- Gestione degli enumeratori (enum) per campi specifici del dominio
- Costruzione delle famiglie a partire dai singoli oggetti di dominio (Parent, Child)

### View-model del report

- Creazione di view-model specifici per le diverse sezioni del report (clinica, genetica, diagnostica)
- Mappatura dei dati di dominio nei view-model per il rendering del report
- Validazione dei view-model prima della generazione del reportreport_viewmodel_builder

### Template HTML

- Creazione dei template HTML per le diverse sezioni del report
- Integrazione dei view-model nei template per il rendering dinamico
- Creazione di template aggiuntivi per sezioni specifiche del report

### Stile e layout

- Definizione dello stile generale del report (CSS)
- Gestione del layout delle diverse sezioni
- Personalizzazione dello stile per sezioni specifiche del report
- Integrazione Sass per la gestione avanzata degli stili e del layout

### Produzione del PDF

- Generazione del PDF a partire dai template HTML
- Configurazione delle opzioni di layout e stile per il PDF
- Gestione delle pagine, intestazioni e piè di pagina
- Ottimizzazione della qualità e delle dimensioni del PDF

### Calcolo delle statistiche

#### Cohort Statistics Summary

- Numero delle famiglie
- Numero dei membri
- Distribuzione ruoli
- Distribuzione mutazioni
- Frequenza dei sintomi
- Indicatori clinici aggregati


#### Family Registry

- Tabella completa delle famiglie
- Ruoli
- Mutazioni
- Probando
- Sintomi principali

#### Genetic Variant Summary

- Elenco varianti genetiche
- Frequenza delle varianti genetiche
- Famiglie coinvolte
- Probando associati

#### Phenotype Distribution

- Sintomi più frequenti
- Sintomi rari
- Correlazioni tra sintomi

#### Proband Overview

- Elenco probandi
- Mutazioni
- Sintomi
- Età di esordio

#### Clinical Indicators Summary

- Febbre ricorrente
- Tonsilliti
- Dolori osteoarticolari
- Manifestazioni cutanee
- Infezioni respiratorie
- Appendicectomia / tonsillectomia

#### Appendix: Raw Clinical Data

- Tabella completa dei dati grezzi
- Codici delle variabili
- Note cliniche
