from scipy.stats import fisher_exact

from ..domain.family import Family


def calculate_adult_onset_improvement_pvalue(families: list[Family]) -> float:
    """
    Calcola il p-value per l'associazione tra:
    - esordio < 18 vs ≥ 18
    - miglioramento clinico in età adulta (Sì/No)
    """

    # Tabella 2x2
    # a = esordio < 18 AND miglioramento sì
    # b = esordio < 18 AND miglioramento no
    # c = esordio ≥ 18 AND miglioramento sì
    # d = esordio ≥ 18 AND miglioramento no

    a = b = c = d = 0

    for family in families:
        for parent in family.parents():

            # Determina il gruppo di esordio
            if parent.onset_before_18 and not parent.onset_after_18:
                group = "<18"
            elif parent.onset_after_18:
                group = ">=18"
            else:
                continue

            # Determina miglioramento clinico
            improved = bool(parent.improvement_in_adulthood)

            # Popola la tabella
            if group == "<18":
                if improved:
                    a += 1
                else:
                    b += 1
            else:  # >=18
                if improved:
                    c += 1
                else:
                    d += 1

    # Costruzione matrice per Fisher
    contingency_table = [[a, b], [c, d]]

    # Fisher exact test (two-sided)
    _, p_value = fisher_exact(contingency_table, alternative="two-sided")

    return p_value


def calculate_symptom_pvalues(families: list[Family], symptom_keys: list[str]) -> dict[str, float]:
    """
    For each symptom, compute a Fisher exact test p-value for concordance
    between proband and parent with same mutation.
    """

    pvalues = {}

    for key in symptom_keys:
        # Contatori per la tabella 2x2
        a = b = c = d = 0

        for family in families:
            if not family.children:
                continue

            for proband in family.children:
                matching_parents = [parent for parent in family.parents() if parent.mutation == proband.mutation]
                if not matching_parents:
                    continue

                for parent in matching_parents:
                    proband_has = getattr(proband, key, False)
                    parent_has = getattr(parent, key, False)

                    if proband_has and parent_has:
                        a += 1
                    elif proband_has and not parent_has:
                        b += 1
                    elif not proband_has and parent_has:
                        c += 1
                    else:
                        d += 1

        # Tabella di contingenza
        table = [[a, b], [c, d]]

        # Fisher exact test
        _, pvalue = fisher_exact(table)

        pvalues[key] = pvalue

    return pvalues
