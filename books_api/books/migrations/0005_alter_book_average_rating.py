# Generated by Django 3.2.7 on 2021-09-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_books_book_api_id_82a1ef_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
