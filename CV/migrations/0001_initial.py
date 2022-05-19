# Generated by Django 4.0.4 on 2022-05-19 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Legends',
            fields=[
                ('L_id', models.AutoField(primary_key=True, serialize=False)),
                ('L_name', models.CharField(max_length=200)),
                ('L_codeName', models.CharField(max_length=100, unique=True)),
                ('L_title', models.CharField(max_length=100)),
                ('L_email', models.EmailField(max_length=254)),
                ('L_phone', models.CharField(max_length=100)),
                ('L_website', models.CharField(max_length=100)),
                ('L_address', models.CharField(max_length=200)),
                ('L_intro', models.CharField(max_length=200)),
                ('L_introDes', models.CharField(max_length=1000)),
                ('L_proPic', models.CharField(max_length=200)),
                ('L_FB', models.CharField(max_length=100)),
                ('L_Instagram', models.CharField(max_length=100)),
                ('L_LinkedIn', models.CharField(max_length=100)),
                ('L_GitHub', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('W_id', models.AutoField(primary_key=True, serialize=False)),
                ('W_name', models.CharField(max_length=100)),
                ('W_skill', models.CharField(max_length=100)),
                ('W_link', models.CharField(max_length=300)),
                ('W_pic', models.CharField(max_length=100)),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CV.legends')),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('WE_id', models.AutoField(primary_key=True, serialize=False)),
                ('WE_title', models.CharField(max_length=100)),
                ('WE_companyName', models.CharField(max_length=100)),
                ('WE_from', models.CharField(max_length=10)),
                ('WE_to', models.CharField(max_length=10)),
                ('WE_Details', models.CharField(max_length=300)),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CV.legends')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('S_id', models.AutoField(primary_key=True, serialize=False)),
                ('S_name', models.CharField(max_length=100)),
                ('S_power', models.IntegerField()),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CV.legends')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('E_title', models.CharField(max_length=100)),
                ('E_name', models.CharField(max_length=100)),
                ('E_from', models.CharField(max_length=10)),
                ('E_to', models.CharField(max_length=10)),
                ('E_details', models.CharField(max_length=300)),
                ('E_id', models.AutoField(primary_key=True, serialize=False)),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CV.legends')),
            ],
        ),
    ]
