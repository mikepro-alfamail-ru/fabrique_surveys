# Generated by Django 2.2.10 on 2021-06-28 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_auto_20210629_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='useranswer', to='surveys.Question'),
        ),
    ]
