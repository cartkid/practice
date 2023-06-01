from typing import List, Dict, Union
from dataclasses import dataclass


@dataclass
class SolarPanel:
    id: int
    serial_number: str
    manufacturer: Union[str, None]


@dataclass
class Defect:
    id: int
    solar_panel_id: int
    priority: str


def get_farm_panels_with_high_pri_defects(
    farm_panels: List[SolarPanel], defects: List[Defect]
) -> List[SolarPanel]:
    high_priority_defects = set(
        defect.solar_panel_id for defect in defects if defect.priority == "high"
    )
    return [panel for panel in farm_panels if panel.id in high_priority_defects]


def get_defects_per_manufacturer(
    farm_panels: List[SolarPanel], defects: List[Defect]
) -> Dict[str, int]:
    high_priority_defects = set(
        defect.solar_panel_id for defect in defects if defect.priority == "high"
    )

    manufacture_defect_count: Dict[str, int] = {}
    for panel in farm_panels:
        if panel.id in high_priority_defects and panel.manufacturer is not None:
            if panel.manufacturer in manufacture_defect_count:
                manufacture_defect_count[panel.manufacturer] += 1
            else:
                manufacture_defect_count[panel.manufacturer] = 1

    return manufacture_defect_count
