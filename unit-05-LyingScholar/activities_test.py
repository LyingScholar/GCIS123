import activities

def test_validate_password_abc():
    
    value = "abc"
    
    try:
        activities.validatePassword(value)
        assert False, "should have thrown error"
    except:
        assert True