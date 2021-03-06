# Generated by Django 2.1.2 on 2018-11-02 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strava_id', models.IntegerField()),
                ('activity_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strava_id', models.IntegerField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('auth_date', models.DateTimeField(auto_now_add=True, verbose_name='date authed')),
                ('last_logon_date', models.DateTimeField(auto_now_add=True, verbose_name='last logon')),
                ('bearer', models.TextField()),
                ('public', models.BooleanField()),
                ('picture_url', models.TextField()),
                ('user_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Efforts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pb', models.IntegerField()),
                ('efforts', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Athlete')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment_id', models.IntegerField()),
                ('name', models.TextField()),
                ('distance', models.IntegerField()),
                ('elevation', models.IntegerField()),
                ('type', models.TextField()),
                ('total_efforts', models.IntegerField()),
                ('total_athletes', models.IntegerField()),
                ('top_time', models.IntegerField()),
                ('tenth_time', models.IntegerField()),
                ('refresh_date', models.DateTimeField(auto_now_add=True, verbose_name='date refreshed')),
            ],
        ),
        migrations.AddField(
            model_name='efforts',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Segment'),
        ),
    ]
