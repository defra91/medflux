import unittest

from carlino_db.domain.episode_duration import EpisodeDuration
from carlino_db.domain.family import Family
from carlino_db.domain.parent import Parent
from carlino_db.domain.parental_role import ParentalRole
from carlino_db.domain.temperature_category import TemperatureCategory
from carlino_db.statistics.charts_calculator import calculate_adult_onset_improvement_chart


def make_parent(family_id: str, role: ParentalRole, *, onset_before_18: bool, onset_after_18: bool, improvement_in_adulthood: bool) -> Parent:
    return Parent(
        family_id=family_id,
        parental_role=role,
        mutation="MUT",
        consanguinity=False,
        recurrent_fever=False,
        temperature_category=TemperatureCategory.NOT_PRESENT,
        episode_duration=EpisodeDuration.UNKNOWN,
        abdominal_pain=False,
        chest_pain=False,
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
        onset_before_18=onset_before_18,
        onset_after_18=onset_after_18,
        episodes_per_year=0,
        tonsillectomy=False,
        appendicectomy=False,
        improvement_in_adulthood=improvement_in_adulthood,
        family_respiratory_infections_chronic=False,
    )


class AdultOnsetImprovementChartTests(unittest.TestCase):
    def test_calculate_adult_onset_improvement_chart(self):
        parent_group_before_18_yes = make_parent("f1", ParentalRole.MOTHER, onset_before_18=True, onset_after_18=False, improvement_in_adulthood=True)
        parent_group_before_18_no = make_parent("f2", ParentalRole.FATHER, onset_before_18=True, onset_after_18=False, improvement_in_adulthood=False)
        parent_group_after_18_yes = make_parent("f3", ParentalRole.MOTHER, onset_before_18=False, onset_after_18=True, improvement_in_adulthood=True)
        parent_group_after_18_no = make_parent("f4", ParentalRole.FATHER, onset_before_18=False, onset_after_18=True, improvement_in_adulthood=False)

        families = [
            Family(id="f1", mother=parent_group_before_18_yes, father=None, children=[]),
            Family(id="f2", mother=parent_group_before_18_no, father=None, children=[]),
            Family(id="f3", mother=parent_group_after_18_yes, father=None, children=[]),
            Family(id="f4", mother=parent_group_after_18_no, father=None, children=[]),
        ]

        chart = calculate_adult_onset_improvement_chart(families)

        self.assertEqual(chart.title, "Associazione tra età di esordio e miglioramento clinico")
        self.assertIsNotNone(chart.image_url)
        self.assertTrue(chart.image_url.startswith("data:image/png;base64,"))


if __name__ == "__main__":
    unittest.main()
