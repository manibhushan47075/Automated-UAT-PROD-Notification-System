from django.core.management.base import BaseCommand, CommandError
from notifier.services import send_notifications


class Command(BaseCommand):

    help = "Send UAT or PROD notification emails"

    def add_arguments(self, parser):
        parser.add_argument(
            "environment",
            type=str,
            help="UAT or PROD"
        )

    def handle(self, *args, **options):

        environment = options["environment"]

        self.stdout.write(
            self.style.SUCCESS(
                f"Sending {environment.upper()} notifications..."
            )
        )

        try:
            send_notifications(environment)

        except ValueError as e:
            raise CommandError(str(e))

        self.stdout.write(
            self.style.SUCCESS("Done!")
        )