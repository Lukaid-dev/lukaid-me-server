from django import forms

from django.contrib.admin.widgets import FilteredSelectMultiple

from apps.posts.models.post import Post
from apps.posts.models.post_tag import PostTag
from apps.posts.models.tag import Tag


class PostTagAdminForm(forms.ModelForm):
    class Meta:
        model = PostTag
        fields = "__all__"

    TagList = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(verbose_name="Tags", is_stacked=False),
        label="Tags",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["TagList"].initial = self.instance.tags.all()
        self.initial["TagList"] = self.fields["TagList"].initial

    def save(self, commit=True):
        obj = super().save(commit)
        if obj.pk:
            try:
                obj.tags.clear()
                obj.tags.add(*self.cleaned_data["TagList"])
            except (TypeError, ValueError):
                print("Error")
        return obj
