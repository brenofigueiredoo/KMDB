from django.core.management.base import BaseCommand
from users.models import User
import ipdb
from django.core.management import CommandError


class Command(BaseCommand):
    help = "Create admin users"

    def add_arguments(self, parser):
        parser.add_argument("--username")
        parser.add_argument("--password")
        parser.add_argument("--email")

    def handle(self, *args, **kwargs):

        username = kwargs["username"]
        password = kwargs["password"]
        email = kwargs["email"]

        default_username = "admin"
        default_password = "admin1234"
        default_email = "@example.com"

        return_data = {}

        if username:
            return_data["username"] = username
        else:
            return_data["username"] = default_username

        if password:
            return_data["password"] = password
        else:
            return_data["password"] = default_password

        if email:
            return_data["email"] = email

        if not email and username:
            return_data["email"] = username + default_email

        if not email and not username:
            return_data["email"] = default_username + default_email

        verify_username = User.objects.filter(username=return_data["username"])
        verify_email = User.objects.filter(email=return_data["email"])

        if verify_username:
            raise CommandError("Username `admin` already taken.")

        if verify_email:
            raise CommandError("Email `admin@example.com` already taken.")

        User.objects.create_superuser(**return_data)

        self.stdout.write(self.style.SUCCESS("Admin `admin` successfully created!"))
