# Generated by Django 4.2.11 on 2024-04-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crud", "0009_alter_agendamentoexame_horario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agendamentoexame",
            name="horario",
            field=models.CharField(
                choices=[
                    ("07:00", "07:00"),
                    ("08:00", "08:00"),
                    ("09:00", "09:00"),
                    ("10:00", "10:00"),
                    ("11:00", "11:00"),
                    ("13:00", "13:00"),
                    ("14:00", "14:00"),
                    ("15:00", "15:00"),
                    ("16:00", "16:00"),
                    ("17:00", "17:00"),
                ],
                max_length=5,
                verbose_name="Horário",
            ),
        ),
    ]
