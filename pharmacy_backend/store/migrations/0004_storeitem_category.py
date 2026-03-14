from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_storeitem_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='category',
            field=models.CharField(
                choices=[
                    ('chemicals', 'Chemicals'),
                    ('glassware', 'Glassware'),
                    ('instruments', 'Instruments'),
                    ('computer', 'Computer Store'),
                    ('other', 'Other'),
                ],
                default='other',
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
