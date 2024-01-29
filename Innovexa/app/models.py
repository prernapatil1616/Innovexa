from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.

class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_all_category(self):
        return Categories.objects.all().order_by('id')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("challenge_details", kwargs={'slug': self.slug})


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    STATUS = (
        ('PUBLISH', 'PUBLISH'),
        ('DRAFT', 'DRAFT'),
    )

    featured_image = models.ImageField(upload_to="featured_img", null=True)
    title = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=100, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("challenge_details", kwargs={'slug': self.slug})



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Challenge.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, Challenge)


class what_you_learn(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points


class Requirement(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    points = models.CharField(max_length=500)

    def __str__(self):
        return self.points


class SubmitForm(models.Model):
    title = models.CharField(max_length=130)
    repoUrl = models.URLField(max_length=130)
    liveUrl = models.URLField(max_length=130)
    feedback = models.TextField(max_length=130)

    def __str__(self):
        return self.title


