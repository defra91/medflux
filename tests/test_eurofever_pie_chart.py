import unittest

from carlino_db.domain.episode_duration import EpisodeDuration
from carlino_db.domain.family import Family
from carlino_db.domain.parent import Parent
from carlino_db.domain.parental_role import ParentalRole
from carlino_db.domain.temperature_category import TemperatureCategory
from carlino_db.statistics.charts_calculator import calculate_eurofever_mutations_pie_chart


def make_parent(family_id: str, mutation: str) -> Parent:
    return Parent(
        family_id=family_id,
        parental_role=ParentalRole.MOTHER,
        mutation=mutation,
        consanguinity=False,
        recurrent_fever=True,
        temperature_category=TemperatureCategory.ABOVE_OR_EQUAL_38,
        episode_duration=EpisodeDuration.BETWEEN_12_AND_72H,
        abdominal_pain=True,
        chest_pain=True,
        headache=False,
        osteoarticular_pain=False,
        aphthosis_with_fever=False,
        aphthosis_without_fever=False,
        erythematous_tonsillitis=False,
        exudative_tonsillitis=False,
        cutaneous_manifestations=False,
        asthenia=False,
        respiratory_infections_chronic=False,
        fever_in_adulthood=False,
        family_amyloidosis=False,
        onset_before_18=True,
        onset_after_18=False,
        episodes_per_year=12,
        tonsillectomy=False,
        appendicectomy=False,
        improvement_in_adulthood=False,
        family_respiratory_infections_chronic=False,
    )


class EurofeverPieChartTests(unittest.TestCase):
    def test_calculate_eurofever_mutations_pie_chart(self):
        families = [
            Family(id="f1", mother=make_parent("f1", "M694V"), father=make_parent("f1", "M694V"), children=[]),
            Family(id="f2", mother=make_parent("f2", "V726A"), father=None, children=[]),
        ]

        chart = calculate_eurofever_mutations_pie_chart(families)

        self.assertEqual(chart.title, "Distribuzione mutazioni Eurofever")
        self.assertTrue(chart.image_url.startswith("data:image/png;base64,"))


if __name__ == "__main__":
    unittest.main()
