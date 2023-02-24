from simple_aggregator.modules.aggregator import Aggregator

def test_correct_report():
    a = Aggregator()
    a.add_event("2021-03-01 20:01")
    assert a.report() == {'2021-03-01-20': 1} 

def test_single_day():
    a = Aggregator()
    a.add_event("2021-03-01 20:31")
    a.add_event("2021-03-01 20:41")
    a.add_event("2021-03-01 20:51")
    assert a.report() == {'2021-03-01-20': 3} 

def test_multiple_hours():
    a = Aggregator()
    a.add_event("2021-03-01 20:31")
    a.add_event("2021-03-01 21:41")
    a.add_event("2021-03-01 22:51")
    assert a.report() == {'2021-03-01-20': 1, '2021-03-01-21': 1, '2021-03-01-22': 1} 

def test_correct_report_multiple_day():
    a = Aggregator()
    a.add_event("2021-03-21 20:31")
    a.add_event("2021-04-11 20:41")
    a.add_event("2021-05-23 20:55")
    a.add_event("2021-05-23 20:51")
    assert a.report() == {'2021-03-21-20': 1, '2021-04-11-20': 1, '2021-05-23-20' : 2} 
