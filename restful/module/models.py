__author__ = 'rrmerugu'
from django.template.defaultfilters import slugify

from mongoengine import SequenceField, EmbeddedDocument, ReferenceField, StringField, ListField, IntField, DateTimeField, BooleanField, Document, ObjectIdField, ValidationError
from datetime import datetime
import logging
logger = logging.getLogger(__name__)


class Blog(Document):
    blog_id = StringField()
    blog_title = StringField(max_length=100)
    blog_slug = StringField(max_length=120)
    blog_date = DateTimeField(default= datetime.now())
    blog_updated = DateTimeField(default=datetime.now())
    blog_content = StringField()

    def save(self, *args, **kwargs):
        self.blog_updated = datetime.now()
        self.blog_slug = slugify(self.blog_title)
        return super(Blog, self).save(*args, **kwargs)