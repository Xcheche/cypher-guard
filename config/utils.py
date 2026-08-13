from faker import Faker

fake = Faker()


def get_fake_profiles(count=10):
    """
    Build fake data matching the project's auth models:
    - User: email, password, is_active
    - Dashboard: first_name, last_name, nick_name, address, country, city
    """
    profiles = []
    for _ in range(count):
        profiles.append(
            {
                "email": fake.email(),
                "password": fake.password(length=12),
                "is_active": True,
                "first_name": fake.first_name()[:20],
                "last_name": fake.last_name()[:20],
                "nick_name": fake.user_name()[:10],
                "address": fake.street_address()[:100],
                "country": fake.country_code(),
                "city": fake.city()[:30],
            }
        )
    return profiles
