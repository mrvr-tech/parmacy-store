from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create test users for Store Keeper and Lab Users'

    def handle(self, *args, **options):
        # Create Store Keeper (Admin)
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user(
                username='admin',
                password='admin123',
                email='admin@pharmacy.com',
                first_name='Store',
                last_name='Keeper',
                role='store'
            )
            self.stdout.write(
                self.style.SUCCESS(
                    '✓ Created Store Keeper: admin / admin123'
                )
            )
        else:
            self.stdout.write('Store Keeper already exists')

        # Create Lab Users (Lab 1 to Lab 17)
        for i in range(1, 18):
            username = f'lab{i}'
            password = f'lab{i}123'
            lab_name = f'Lab {i}'
            
            if not User.objects.filter(username=username).exists():
                lab_user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=f'lab{i}@pharmacy.com',
                    first_name=f'Lab',
                    last_name=f'User {i}',
                    role='lab',
                    lab_name=lab_name
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✓ Created {lab_name}: {username} / {password}'
                    )
                )
            else:
                self.stdout.write(f'{lab_name} already exists')

        self.stdout.write(
            self.style.SUCCESS(
                '\n📋 All test users created successfully!\n'
                '📝 Store Keeper: admin / admin123\n'
                '🔬 Lab Users: lab1/lab1123 ... lab17/lab17123'
            )
        )
