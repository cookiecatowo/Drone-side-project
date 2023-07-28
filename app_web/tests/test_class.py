from app_web.models.User import User

def test_user():
    user = User("skysky","moon.lion.star@gmail.com","0905619093")
    assert user.name == "skysky", "Error user name."
    assert user.email == "moon.lion.star@gmail.com", "Error user E-mail."
    assert user.phone == "0905619093", "Error user phone."