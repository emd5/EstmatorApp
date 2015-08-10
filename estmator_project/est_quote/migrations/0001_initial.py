# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('est_client', '0001_initial'),
        ('est_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('counts', models.IntegerField(null=True, blank=True)),
                ('mins_piece', models.IntegerField()),
                ('mult_dollies', models.IntegerField()),
                ('m_cart', models.IntegerField()),
                ('l_cart', models.IntegerField()),
                ('p_cart', models.IntegerField()),
                ('s_pack', models.IntegerField()),
                ('category', models.ForeignKey(to='est_quote.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('company', models.ForeignKey(to='est_client.Company')),
                ('contact', models.ForeignKey(to='est_client.Client')),
                ('user', models.ForeignKey(to='est_profile.UserProfile')),
            ],
        ),
    ]