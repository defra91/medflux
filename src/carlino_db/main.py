# src/main.py

from .db import load_family_records, load_patient_records
import json
from .mappers.parent_mapper import map_parent
from .mappers.child_mapper import map_child

def main():
    
    family_records = load_family_records()
    patient_records = load_patient_records()

    print(f"Loaded {len(family_records)} family records from the database.")
    print(f"Loaded {len(patient_records)} patient records from the database.")

    parents = []
    children = []

    for family_record in family_records:
        parent = map_parent(family_record)
        parents.append(parent)

    for patient_record in patient_records:
        child = map_child(patient_record)
        children.append(child)

    from .writer import write_json
    write_json(parents, "parents.json")
    write_json(children, "children.json")

if __name__ == "__main__":
    main()