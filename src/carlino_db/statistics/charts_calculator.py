import base64
from io import BytesIO

from ..charts import build_grouped_bar_chart, build_vertical_bar_chart
from ..domain.family import Family
from .models.statistics_chart import StatisticsChart


def calculate_charts(families: list[Family]) -> list[StatisticsChart]:
    """
    Calculate and return the statistics charts for the provided families.
    """
    return [
        calculate_adult_onset_improvement_chart(families),
        calculate_parent_fmf_phenotype_chart(families),
    ]


def _encode_chart_as_data_url(chart_figure) -> str:
    buffer = BytesIO()
    chart_figure.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
    buffer.seek(0)
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def calculate_adult_onset_improvement_chart(families: list[Family]) -> StatisticsChart:
    """
    Calculate and return a rendered statistics chart for the association between adult onset in parents and
    clinical improvement in adulthood.

    The chart is a grouped bar chart with two groups on the x-axis:
    - "Esordio < 18"
    - "Esordio ≥ 18"

    Each group contains two bars: "Sì" and "No" for clinical improvement.
    """

    chart_data: dict[str, dict[str, int]] = {
        "Esordio < 18": {"Sì": 0, "No": 0},
        "Esordio ≥ 18": {"Sì": 0, "No": 0},
    }

    for family in families:
        for parent in family.parents():
            if parent.onset_before_18 and not parent.onset_after_18:
                group_label = "Esordio < 18"
            elif parent.onset_after_18 and not parent.onset_before_18:
                group_label = "Esordio ≥ 18"
            elif parent.onset_after_18 and parent.onset_before_18:
                group_label = "Esordio ≥ 18"
            else:
                continue

            improvement_label = "Sì" if parent.improvement_in_adulthood else "No"
            chart_data[group_label][improvement_label] += 1

    title = "Associazione tra età di esordio e miglioramento clinico"
    description = (
        "Confronto tra genitori con esordio prima e dopo i 18 anni, in relazione al miglioramento clinico "
        "in età adulta."
    )

    labels = ["Esordio < 18", "Esordio ≥ 18"]
    series = [
        ("Sì", [chart_data["Esordio < 18"]["Sì"], chart_data["Esordio ≥ 18"]["Sì"]]),
        ("No", [chart_data["Esordio < 18"]["No"], chart_data["Esordio ≥ 18"]["No"]]),
    ]

    figure = build_grouped_bar_chart(
        labels=labels,
        series=series,
        xlabel="Categoria di esordio",
        colors=["#ca1103", "#69A74E"],
    )

    image_url = _encode_chart_as_data_url(figure)

    return StatisticsChart(
        title=title,
        description=description,
        image_url=image_url,
    )


def calculate_parent_fmf_phenotype_chart(families: list[Family]) -> StatisticsChart:
    """
    Build a chart with the phenotype frequencies among parents with FMF.

    The chart is ungrouped and counts how often each symptom is present in the parent records that satisfy
    the FMF criteria. Labels remain in Italian, while the implementation is in English.
    """

    symptom_definitions = [
        ("Febbbre ricorrente", "recurrent_fever"),
        ("Dolore addominale", "abdominal_pain"),
        ("Dolore toracico", "chest_pain"),
        ("Cefalea", "headache"),
        ("Dolore osteoarticolare", "osteoarticular_pain"),
        ("Aftosi con febbre", "aphthosis_with_fever"),
        ("Aftosi senza febbre", "aphthosis_without_fever"),
        ("Tonsillite eritematosa", "erythematous_tonsillitis"),
        ("Tonsillite essudativa", "exudative_tonsillitis"),
        ("Manifestazioni cutanee", "cutaneous_manifestations"),
        ("Astenia", "asthenia"),
        ("Infezioni respiratorie croniche", "respiratory_infections_chronic"),
        ("Febbre in età adulta", "fever_in_adulthood"),
        ("Amiloidosi familiare", "family_amyloidosis"),
        ("Tonsillectomia", "tonsillectomy"),
        ("Appendicectomia", "appendicectomy"),
        ("Infezioni respiratorie croniche familiari", "family_respiratory_infections_chronic"),
    ]

    counts: dict[str, int] = {label: 0 for label, _ in symptom_definitions}

    for family in families:
        for parent in family.parents():
            if not parent.mutation:
                continue

            for label, attribute_name in symptom_definitions:
                if getattr(parent, attribute_name, False):
                    counts[label] += 1

    labels = [label for label, _ in symptom_definitions]
    values = [counts[label] for label in labels]

    title = "Fenotipo dei genitori con FMF"
    description = (
        "Conteggio dei sintomi presenti tra i genitori con FMF. "
        "L'istogramma mostra la frequenza di ciascun segno fenotipico osservato."
    )

    figure = build_vertical_bar_chart(
        labels=labels,
        values=values,
        title=title,
        xlabel="Sintomo",
        color="#6c9eeb",
        rotation=60,
    )

    image_url = _encode_chart_as_data_url(figure)

    return StatisticsChart(
        title=title,
        description=description,
        image_url=image_url,
    )
