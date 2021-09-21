# Generated by Django 3.2.7 on 2021-09-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('published_date', models.PositiveSmallIntegerField(null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('ratings_count', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('authors', models.ManyToManyField(to='books.Author')),
                ('categories', models.ManyToManyField(blank=True, to='books.Category')),
            ],
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['api_id'], name='books_book_api_id_82a1ef_idx'),
        ),
    ]
