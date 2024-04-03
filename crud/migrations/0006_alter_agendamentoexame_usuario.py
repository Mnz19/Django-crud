# Generated by Django 4.2.11 on 2024-04-03 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crud", "0005_alter_agendamentoexame_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agendamentoexame",
            name="usuario",
            field=models.ForeignKey(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
    ]
