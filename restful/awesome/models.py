import logging
from datetime import datetime

from bson import ObjectId
from django.template.defaultfilters import slugify
from mongoengine import StringField, DateTimeField, Document

logger = logging.getLogger(__name__)


class Blog(Document):
    blog_id = StringField()
    blog_title = StringField(max_length=100)
    blog_slug = StringField(max_length=120)
    blog_date = DateTimeField(default=datetime.now())
    blog_updated = DateTimeField(default=datetime.now())
    blog_content = StringField()

    def save(self, *args, **kwargs):
        if self.blog_id is None:
            self.blog_id = str(ObjectId())
        self.blog_updated = datetime.now()
        self.blog_slug = slugify(self.blog_title)
        return super(Blog, self).save(*args, **kwargs)

        # TODO - Add clean() or validations() for update
