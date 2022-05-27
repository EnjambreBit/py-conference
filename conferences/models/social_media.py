from django.db import models


class SocialMedia(models.Model):
    TYPES = (
        ("web", "Website"),
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("instagram", "Instagram"),
        ("telegram", "Telegram"),
        ("youtube", "Youtube"),
        ("linkedin", "Linkedin"),
        ("github", "Github"),
        ("gitlab", "Gitlab"),
        ("reddit", "Reddit"),
        ("google", "Google"),
        ("pinterest", "Pinterest"),
        ("snapchat", "Snapchat"),
        ("tumblr", "Tumblr"),
        ("vine", "Vine"),
        ("flickr", "Flickr"),
        ("foursquare", "Foursquare"),
        ("peertube", "PeerTube"),
        ("other", "Other"),
    )
    profile = models.ForeignKey(
        "Profile", related_name="social_media", on_delete=models.CASCADE
    )
    type = models.CharField(max_length=100, choices=TYPES, default="web")
    type_other = models.CharField(max_length=100, default=None, blank=True, null=True)
    url = models.CharField(max_length=300, default=None, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "social_media"
        verbose_name = "Social media link"
        verbose_name_plural = "Social media links"

    def __str__(self):
        return f"{self.profile} - {self.type}"

    @property
    def type_name(self):
        if self.type == "other":
            return self.type
        return self.type_other
