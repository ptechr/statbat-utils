from statbat_utils import remove_non_ascii

def test_remove_non_ascii():
    assert remove_non_ascii("Ronald Acuña Jr") == "Ronald Acuna Jr"
    assert remove_non_ascii([ "Ronald Acuña Jr" ]) == [ "Ronald Acuna Jr" ]