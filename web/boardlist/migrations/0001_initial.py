# Generated by Django 4.0 on 2021-12-23 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0005_alter_board_visibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boardlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, null=True)),
                ('board', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boardlists', to='board.board')),
            ],
            options={
                'verbose_name': 'Boardlist',
                'verbose_name_plural': 'Boardlists',
            },
        ),
    ]
