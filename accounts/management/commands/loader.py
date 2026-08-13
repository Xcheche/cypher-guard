from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from accounts.models import Dashboard
from config import utils as config_utils

User = get_user_model()


class Command(BaseCommand):
    help = "Load fake users and dashboards into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            nargs="?",
            default=10,
            type=int,
            help="Number of users to create",
        )

    def handle(self, *args, **options):
        count = options["count"]
        profiles = config_utils.get_fake_profiles(count)
        created = 0

        for profile in profiles:
            email = profile["email"]
            if User.objects.filter(email=email).exists():
                self.stdout.write(
                    self.style.WARNING(f"Skipping existing user: {email}")
                )
                continue

            user = User.objects.create_user(
                email=email,
                password=profile["password"],
                is_active=profile.get("is_active", True),
            )
            Dashboard.objects.create(
                user=user,
                first_name=profile["first_name"],
                last_name=profile.get("last_name") or None,
                nick_name=profile["nick_name"],
                address=profile.get("address") or None,
                country=profile.get("country") or "",
                city=profile.get("city") or None,
            )
            created += 1

        self.stdout.write(
            self.style.SUCCESS(f"Created {created} users with dashboards.")
        )


# To run the command, use:
# python manage.py loader <count>
# or without count to create 10 users by default: