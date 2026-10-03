import unittest

from medflux.domain.child import Child
from medflux.domain.episode_duration import EpisodeDuration
from medflux.domain.family import Family
from medflux.domain.gender import Gender
from medflux.domain.parent import Parent
from medflux.domain.parental_role import ParentalRole
from medflux.domain.temperature_category import TemperatureCategory
from medflux.statistics.charts_calculator import calculate_phenotypic_concordance_chart


def make_child(family_id: str, mutation: str = "MEFV") -> Child:
    return Child(
        centre_id="centre-1",
        family_id=family_id,
        eurofever_id="eurofever-1",
        gender=Gender.MALE,
        country=None,
        onset_age_years=10,
        diagnosis_age_years=12,
        parents_consanguineous=None,
        familiality=None,
        mutation=mutation,
        fever=None,
        temperature_category=TemperatureCategory.ABOVE_OR_EQUAL_38,
        episode_duration=EpisodeDuration.BETWEEN_12_AND_72H,
        episodes_per_year=12,
        fever_trigger=None,
        abdominal_pain=True,
        chest_pain=True,
        headache=False,
        asthenia=False,
        has_tonsillitis=False,
        diarrhea=False,
        constipation=False,
        vomiting=False,
        abdominal_surgery=None,
        pericarditis=False,
        pleuritis=False,
        arthralgia=False,
        arthritis=False,
        myalgia=False,
        bone_pain=False,
        erysipelas_like=False,
        mucocutaneous=None,
        other_manifestations="",
        therapy=None,
        dosage_mg_day=0.0,
        therapy_response=None,
        side_effects=None,
        biological_therapy=False,
        amyloidosis=None,
        concomitant_diseases="",
        has_aphthosis=False,
        osteoarticular_pain=False,
    )


def make_parent(family_id: str, *, mutation: str = "MEFV") -> Parent:
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
        asthenia=False,
        has_tonsillitis=False,
        osteoarticular_pain=False,
        aphthosis_with_fever=False,
        aphthosis_without_fever=False,
        has_aphthosis=False,
        erythematous_tonsillitis=False,
        exudative_tonsillitis=False,
        cutaneous_manifestations=False,
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


class PhenotypicConcordanceChartTests(unittest.TestCase):
    def test_calculate_phenotypic_concordance_chart(self):
        child = make_child("f1")
        parent = make_parent("f1")
        family = Family(id="f1", mother=parent, father=None, children=[child])

        chart = calculate_phenotypic_concordance_chart([family])

        self.assertEqual(chart.title, "Concorrenze fenotipiche")
        self.assertIsNotNone(chart.image_url)
        self.assertTrue(chart.image_url.startswith("data:image/png;base64,"))

    def test_ignores_parent_with_different_mutation(self):
        child = make_child("f1", mutation="MEFV")
        matching_parent = make_parent("f1", mutation="MEFV")
        different_parent = make_parent("f1", mutation="OTHER")
        family = Family(id="f1", mother=matching_parent, father=different_parent, children=[child])

        chart = calculate_phenotypic_concordance_chart([family])

        self.assertIsNotNone(chart.image_url)
        self.assertTrue(chart.image_url.startswith("data:image/png;base64,"))


if __name__ == "__main__":
    unittest.main()
