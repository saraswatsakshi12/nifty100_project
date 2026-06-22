from src.etl.loader import ExcelLoader


def test_loader_class():

    assert ExcelLoader != None



def test_loader_object():

    obj = ExcelLoader("dummy.xlsx")

    assert obj.path=="dummy.xlsx"