import pytest
from projectmain import new_account

def test_new_account():
    assert new_account("sarang",2222222222,222222222222,1,500,1234)==1

def test_show_account_details():
    assert new_account("sarang",1234)==1

def test_deposite():
    assert new_account("sarang",1234)==1

def test_withdraw():
    assert new_account("sarang",1234)==1

def test_show_balance():
    assert new_account("sarang",1234)==1

def test_delete_account():
    assert new_account("sarang",1234)==1