import unittest

from carlino_db.domain.episode_duration import EpisodeDuration
from carlino_db.domain.family import Family
from carlino_db.domain.parent import Parent
from carlino_db.domain.parental_role import ParentalRole
from carlino_db.domain.temperature_category import TemperatureCategory
from carlino_db.statistics.charts_calculator import calculate_parent_fmf_phenotype_chart


def make_parent(family_id: str, role: ParentalRole, *, abdominal_pain: bool = False, chest_pain: bool = False, headache: bool = False, osteoarticular_pain: bool = False, aphthosis_with_fever: bool = False, erythematous_tonsillitis: bool = False, exudative_tonsillitis: bool = False, asthenia: bool = False, respiratory_infections_chronic: bool = False, mutation: str = "MEFV") -> Parent:
    return Parent(
        family_id=family_id,
        parental_role=role,
        mutation=mutation,
        consanguinity=False,
        recurrent_fever=True,
        temperature_category=TemperatureCategory.ABOVE_OR_EQUAL_38,
        episode_duration=EpisodeDuration.BETWEEN_12_AND_72H,
        abdominal_pain=abdominal_pain,
        chest_pain=chest_pain,
        headache=headache,
        osteoarticular_pain=osteoarticular_pain,
        aphthosis_with_fever=aphthosis_with_fever,
        aphthosis_without_fever=False,
        erythematous_tonsillitis=erythematous_tonsillitis,
        exudative_tonsillitis=exudative_tonsillitis,
        cutaneous_manifestations=False,
        asthenia=asthenia,
        respiratory_infections_chronic=respiratory_infections_chronic,
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


class ParentFmfPhenotypeChartTests(unittest.TestCase):
    def test_calculate_parent_fmf_phenotype_chart(self):
        parent_1 = make_parent("f1", ParentalRole.MOTHER, abdominal_pain=True, headache=True)
        parent_2 = make_parent("f2", ParentalRole.FATHER, osteoarticular_pain=True, exudative_tonsillitis=True)

        chart = calculate_parent_fmf_phenotype_chart([
            Family(id="family-1", mother=parent_1, father=parent_2, children=[]),
        ])

        self.assertEqual(chart.title, "Fenotipo dei genitori con FMF")
        self.assertIsNotNone(chart.image_url)
        self.assertTrue(chart.image_url.startswith("data:image/png;base64,"))


if __name__ == "__main__":
    unittest.main()
