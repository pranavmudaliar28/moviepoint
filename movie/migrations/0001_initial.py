# Generated by Django 4.2.1 on 2023-05-18 02:50

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Latest Movies', 'Latest Movies'), ('Web-series', 'Web-series')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('poster', models.ImageField(upload_to='movie/poster/image/')),
                ('description', ckeditor.fields.RichTextField()),
                ('Releaseyear', models.IntegerField()),
                ('Downloadlink', models.URLField()),
                ('watchtralier', models.URLField()),
                ('IMDB_rating', models.FloatField()),
                ('current_season', models.CharField(max_length=250)),
                ('detail', models.CharField(max_length=250)),
                ('episode', models.CharField(max_length=250)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.category')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movie.session')),
            ],
        ),
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(max_length=250)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(choices=[('Action', 'Action'), ('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Drama', 'Drama'), ('Romance', 'Romance'), ('Sci-fi', 'Sci-fi'), ('Crime film', 'Crime film'), ('War', 'War'), ('Westerns', 'Westerns'), ('COMEDY', 'COMEDY'), ('Sports', 'Sports'), ('Adventure', 'Adventure'), ('Documentary', 'Documentary'), ('Romantic comedy', 'Romantic comedy'), ('Fiction', 'Fiction'), ('Mystery', 'Mystery'), ('Epic', 'Epic'), ('Dark comedy', 'Dark comedy'), ('Experimental', 'Experimental'), ('Animated film', 'Animated film'), ('Sports', 'Sports'), ('web-series', 'web-series'), ('Biographical', 'Biographical'), ('Disaster', 'Disaster'), ('Coming-of-age story', 'Coming-of-age story'), ('cartoon', 'cartoon'), ('Anime', 'Anime'), ('Road', 'Road'), ('Spy', 'Spy'), ('Silent', 'Silent'), ('Propaganda', 'Propaganda'), ('Dance film', 'Dance film')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='downloadlink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=250)),
                ('size', models.CharField(max_length=250)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
        migrations.CreateModel(
            name='All_season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('All_season', models.CharField(max_length=250)),
                ('detail', models.CharField(max_length=250)),
                ('episode', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=500)),
                ('poster', models.CharField(max_length=250)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
        ),
    ]
