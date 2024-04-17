# Generated by Django 5.0.4 on 2024-04-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('InProgress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
                ('resolution_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]