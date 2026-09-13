from .gender import Gender
from .country import Country
from dataclasses import dataclass
from .temperature_category import TemperatureCategory
from .mutation import Mutation
from .optional_bool import OptionalBool
from .fever_trigger import FeverTrigger


@dataclass
class Child:
    """
    Represents a child in the domain model.
    """
    
    centre_id: str          
    family_id: str
    eurofever_id: str     
    gender: Gender      
    country: Country             

    onset_age_years: int      
    diagnosis_age_years: int  

    parents_consanguineous: OptionalBool
    familiality: OptionalBool 

    mutation: Mutation

    fever: OptionalBool       
    temperature_category: TemperatureCategory
    episode_duration_days: int    
    episodes_per_year: int        
    fever_trigger: FeverTrigger          

    abdominal_pain: bool             
    diarrhea: bool    
    constipation: bool
    vomiting: bool    
    abdominal_surgery: bool          

    chest_pain: bool  
    pericarditis: bool
    pleuritis: bool   

    arthralgia: bool  
    arthritis: bool   
    myalgia: bool     
    bone_pain: bool   

    erysipelas_like: bool            
    mucocutaneous: bool              
    other_manifestations: str 

    therapy: bool     
    dosage_mg_day: float      
    therapy_response: bool           
    side_effects: bool
    biological_therapy: bool         

    amyloidosis: bool 
    concomitant_diseases: str 