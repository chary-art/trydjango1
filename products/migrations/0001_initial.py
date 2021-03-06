# Generated by Django 3.1.7 on 2021-03-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('summary', models.TextField()),
                ('featured', models.BooleanField()),
                ('ady', models.CharField(max_length=120)),
                ('welayaty', models.CharField(max_length=120)),
                ('etraby', models.CharField(max_length=120)),
                ('salgysy', models.CharField(max_length=120)),
                ('bazar_ishguni', models.CharField(max_length=120)),
                ('maglumat', models.TextField(blank=True, null=True)),
                ('telefony', models.CharField(max_length=120)),
                ('ish_wagty', models.CharField(max_length=120)),
                ('surat', models.ImageField(upload_to='img/%y')),
                ('city', models.CharField(choices=[('city', 'Ashgabat'), ('city', 'Mary'), ('city', 'Balkan'), ('city', 'Turkmenabat'), ('city', 'Balkanabat')], default='green', max_length=6)),
            ],
        ),
    ]
