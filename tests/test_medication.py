from scr.medication import Medication

def test_create_medication():
    med = Medication("Dipirona", "08:00")
    assert med.name == "Dipirona"
    assert med.time == "08:00"
    assert med.taken == False

def test_mark_as_taken():
    med = Medication("Dipirona", "08:00")
    med.mark_as_taken()
    assert med.taken == True

def test_invalid_name():
    med = Medication("", "08:00")
    assert med.name == ""