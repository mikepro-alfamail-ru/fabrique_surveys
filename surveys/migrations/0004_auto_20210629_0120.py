# Generated by Django 2.2.10 on 2021-06-28 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0003_auto_20210629_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answervariant',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answervariant', to='surveys.Question'),
        ),
    ]
