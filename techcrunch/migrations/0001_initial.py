# Generated by Django 4.2.11 on 2024-04-07 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(db_index=True, max_length=200, verbose_name='site_id')),
                ('slug', models.CharField(blank=True, max_length=500, null=True, verbose_name='slug')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_date')),
                ('image', models.CharField(blank=True, max_length=500, null=True, verbose_name='image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(db_index=True, max_length=200, verbose_name='site_id')),
                ('slug', models.CharField(blank=True, max_length=500, null=True, verbose_name='slug')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_date')),
                ('author_position', models.CharField(blank=True, max_length=200, null=True, verbose_name='author_position')),
                ('author_avatars', models.CharField(blank=True, max_length=500, null=True, verbose_name='author_avatars_links')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(db_index=True, max_length=200, verbose_name='site_id')),
                ('slug', models.CharField(blank=True, max_length=500, null=True, verbose_name='slug')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_date')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='DailyUpdateData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_items', models.TextField(blank=True, default='nothing', null=True, verbose_name='New_Articles')),
                ('category_items', models.TextField(blank=True, default='nothing', null=True, verbose_name='New_Category')),
                ('author_items', models.TextField(blank=True, default='nothing', null=True, verbose_name='New_Author')),
                ('search_date', models.DateTimeField(verbose_name='scrapped_date')),
                ('is_active', models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active')),
            ],
            options={
                'verbose_name': 'Daily Update Data',
                'verbose_name_plural': 'Daily Update Data',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=500, verbose_name='slug')),
                ('times_searched', models.IntegerField(blank=True, default=0, null=True, verbose_name='searching_times')),
            ],
            options={
                'verbose_name': 'keyword',
                'verbose_name_plural': 'keywords',
            },
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='URL_address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('status_code', models.IntegerField(blank=True, default=0, null=True, verbose_name='status_code')),
            ],
            options={
                'verbose_name': 'URL',
                'verbose_name_plural': 'URLs',
            },
        ),
        migrations.CreateModel(
            name='SearchByKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_pages', models.IntegerField(blank=True, default=5, null=True, verbose_name='max_pages')),
                ('new_articles', models.IntegerField(blank=True, default=0, null=True, verbose_name='new_articles')),
                ('scrapped_articles', models.TextField(blank=True, default='Nothing', null=True, verbose_name='scrapped_articles')),
                ('search_at', models.DateField(auto_now_add=True, null=True, verbose_name='search_at')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_by_keyword', to='techcrunch.keyword', verbose_name='keyword')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'search_by_keyword',
                'verbose_name_plural': 'search_by_keywords',
            },
        ),
        migrations.CreateModel(
            name='ArticleSearchByKeywordItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_scrapped', models.BooleanField(default=True, verbose_name='is_scrapped')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_search_by_keyword_items', to='techcrunch.article', verbose_name='article_searched_by_keyword')),
                ('search_by_keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_search_by_keyword_items', to='techcrunch.searchbykeyword')),
            ],
            options={
                'verbose_name': 'Articles Search By Keyword Item',
                'verbose_name_plural': 'Articles Search By Keyword Items',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='techcrunch.author', verbose_name='author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='techcrunch.category', verbose_name='category'),
        ),
    ]