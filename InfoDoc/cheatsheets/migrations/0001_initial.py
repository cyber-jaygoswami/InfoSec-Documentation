# Generated by Django 4.0.6 on 2022-07-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('cheatsheat_name', models.CharField(max_length=300)),
                ('pdf_file', models.FileField(upload_to='')),
            ],
        ),
    ]
