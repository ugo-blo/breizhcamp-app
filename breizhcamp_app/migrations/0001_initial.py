# Generated by Django 4.2 on 2023-05-01 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter an artist name', max_length=200, verbose_name='Artist name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a release genre (e.g. IDM, Ambient, Techno, etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a song title', max_length=200, verbose_name='Song title')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='breizhcamp_app.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a release title', max_length=200, verbose_name='Release title')),
                ('release_date', models.DateField(blank=True, null=True)),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='breizhcamp_app.artist')),
                ('genre', models.ManyToManyField(help_text='Select a genre for this release', to='breizhcamp_app.genre')),
                ('song', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='breizhcamp_app.song')),
            ],
            options={
                'ordering': ['release_date', 'title'],
            },
        ),
    ]
