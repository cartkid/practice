from typing import List, Dict, Union
from dataclasses import dataclass
import pytest


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
    high_priority_panel_defects = set()
    for defect in defects:
        if defect.priority != "high":
            continue
        high_priority_panel_defects.add(defect.solar_panel_id)

    farm_panels_with_high_pri_defects: List[SolarPanel] = []
    for panel in farm_panels:
        if panel.id in high_priority_panel_defects:
            farm_panels_with_high_pri_defects.append(panel)

    return farm_panels_with_high_pri_defects


def get_defects_per_manufacturer(
    farm_panels: List[SolarPanel], defects: List[Defect]
) -> Dict[str, int]:
    high_priority_defects = set()
    for defect in defects:
        if defect.priority != "high":
            continue
        high_priority_defects.add(defect.solar_panel_id)

    manufacture_defect_count: Dict[str, int] = {}
    for panel in farm_panels:
        if panel.id in high_priority_defects and panel.manufacturer is not None:
            if panel.manufacturer in manufacture_defect_count:
                manufacture_defect_count[panel.manufacturer] += 1
            else:
                manufacture_defect_count[panel.manufacturer] = 1

    return manufacture_defect_count


def test_get_farm_panels_with_high_pri_defects_one_defect():
    farm_panel = SolarPanel(id=1, serial_number="abc123", manufacturer=None)
    defect = Defect(id=123, solar_panel_id=1, priority="high")
    result: List[SolarPanel] = get_farm_panels_with_high_pri_defects(
        farm_panels=[farm_panel], defects=[defect]
    )
    assert result == [farm_panel]


def test_get_defects_per_manufacturer_one_issue_two_manufacturers():
    farm_panel1 = SolarPanel(id=1, serial_number="abc123", manufacturer="bananas")
    farm_panel2 = SolarPanel(id=2, serial_number="abc124", manufacturer="apples")
    defect = Defect(id=123, solar_panel_id=1, priority="high")
    result: Dict[str, int] = get_defects_per_manufacturer(
        farm_panels=[farm_panel1, farm_panel2], defects=[defect]
    )
    assert result == {"bananas": 1}


def test_get_defects_per_manufacturer_two_issues_from_one_of_two_manufacturers():
    farm_panel1 = SolarPanel(id=1, serial_number="abc123", manufacturer="bananas")
    farm_panel3 = SolarPanel(id=3, serial_number="abc125", manufacturer="bananas")
    farm_panel2 = SolarPanel(id=2, serial_number="abc124", manufacturer="apples")
    defect = Defect(id=123, solar_panel_id=1, priority="high")
    defect = Defect(id=124, solar_panel_id=3, priority="high")
    result: Dict[str, int] = get_defects_per_manufacturer(
        farm_panels=[farm_panel1, farm_panel2, farm_panel3], defects=[defect]
    )
    assert result == {"bananas": 2}


pytest.main()
