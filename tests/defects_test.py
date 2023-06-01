from typing import List, Dict
import src.defects as defects


def test_get_farm_panels_with_high_pri_defects_one_defect():
    farm_panel = defects.SolarPanel(id=1, serial_number="abc123", manufacturer=None)
    defect = defects.Defect(id=123, solar_panel_id=1, priority="high")
    result: List[defects.SolarPanel] = defects.get_farm_panels_with_high_pri_defects(
        farm_panels=[farm_panel], defects=[defect]
    )
    assert result == [farm_panel]


def test_get_defects_per_manufacturer_one_issue_two_manufacturers():
    farm_panel1 = defects.SolarPanel(
        id=1, serial_number="abc123", manufacturer="bananas"
    )
    farm_panel2 = defects.SolarPanel(
        id=2, serial_number="abc124", manufacturer="apples"
    )
    defect = defects.Defect(id=123, solar_panel_id=1, priority="high")
    result: Dict[str, int] = defects.get_defects_per_manufacturer(
        farm_panels=[farm_panel1, farm_panel2], defects=[defect]
    )
    assert result == {"bananas": 1}


def test_get_defects_per_manufacturer_two_issues_from_one_of_two_manufacturers():
    farm_panel1 = defects.SolarPanel(
        id=1, serial_number="abc123", manufacturer="bananas"
    )
    farm_panel3 = defects.SolarPanel(
        id=3, serial_number="abc125", manufacturer="bananas"
    )
    farm_panel2 = defects.SolarPanel(
        id=2, serial_number="abc124", manufacturer="apples"
    )
    defect1 = defects.Defect(id=123, solar_panel_id=1, priority="high")
    defect2 = defects.Defect(id=124, solar_panel_id=3, priority="high")
    result: Dict[str, int] = defects.get_defects_per_manufacturer(
        farm_panels=[farm_panel1, farm_panel2, farm_panel3], defects=[defect1, defect2]
    )
    assert result == {"bananas": 2}
