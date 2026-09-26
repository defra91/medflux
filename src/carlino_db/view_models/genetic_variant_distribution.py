from dataclasses import dataclass


@dataclass
class GeneticVariantDistributionVM:
    proband_distribution: dict[str, dict]
    parent_distribution: dict[str, dict]
