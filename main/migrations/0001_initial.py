# Generated by Django 4.1.4 on 2023-06-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField(blank=True, null=True)),
                ('visionMision', models.TextField(blank=True, null=True)),
                ('coreValues', models.TextField(blank=True, null=True)),
                ('takudzwa', models.ImageField(blank=True, default='default.jpg', max_length=200, null=True, upload_to='Pictures')),
                ('gracious', models.ImageField(blank=True, default='default.jpg', max_length=200, null=True, upload_to='Pictures')),
                ('carey', models.ImageField(blank=True, default='default.jpg', max_length=200, null=True, upload_to='Pictures')),
                ('nicole', models.ImageField(blank=True, default='default.jpg', max_length=200, null=True, upload_to='Pictures')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastUpadatedOn', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('part1', 'Carousel/HomeSlide'), ('part2', 'Products and Services'), ('services', 'Offered Services /Slides')], max_length=20, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='pics')),
                ('disc', models.TextField(null=True)),
                ('Homebutton', models.CharField(blank=True, choices=[('servicebtn', 'More Services'), ('Guidesbtn', '  More Projects Guides'), ('signUp', 'Sign Up Today'), ('contact', 'Contact Today'), ('learn', 'Learn More')], max_length=20)),
                ('createdOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('Updated', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
