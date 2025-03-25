from cl20_module import hehe, count_regs


def test_hehe() -> None:
    assert hehe(3) == 0


def test_count_regs_use() -> None:
    assert count_regs("Orange", ["Wake", "Orange", "Orange", "Durham"]) == 2


def test_count_regs_edge() -> None:
    assert count_regs("Orange", []) == 0


def test_count_regs_mutate() -> None:
    cs: list[str] = ["Durham", "Wake", "Lee"]
    count_regs("Wake", cs)
    assert cs == ["Durham", "Wake", "Lee"]
