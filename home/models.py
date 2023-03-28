from django.db import models

from wagtail.models import Page, Orderable
from wagtail.admin.panels import MultiFieldPanel, InlinePanel, FieldPanel, FieldRowPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.fields import RichTextField, StreamField, StreamBlock
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class SectionBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    body = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, max_length=100)),
            ("text", blocks.RichTextBlock())
        ])
    )

    class Meta:
        block_counts = {
            'image': {"min_num": 1, "max_num": 1 },
            "body": {"min_num": 1, "max_num": 5}
        }

class HomePage(Page):
    hero_title = models.CharField(max_length=250)
    hero_text = models.CharField(max_length=250)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    home_page_text = models.CharField(max_length=255)
    other_sections = StreamField([
        ("section", SectionBlock())
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("hero_title"),
            FieldPanel("hero_text"),
            FieldPanel("hero_image")
        ], 
        heading="Hero section"),
        FieldPanel("home_page_text"),
        FieldPanel("other_sections"),
        InlinePanel("featured_menus", label="Featured Menu Items"),
        InlinePanel("gallery_images", label="Image Gallery"),
    ]
    

class FeaturedMenu(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="featured_menus")
    menu = models.ForeignKey(
        'home.MenuItem',
        on_delete=models.CASCADE,
        related_name="+"
    )
    panels = [
        FieldPanel("menu")
    ]

class BreadGalleryImages(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name="+"
    )
    panels = [
        FieldPanel("image")
    ]

@register_snippet
class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.CharField(max_length=250)

    panels = [
        FieldPanel("name"),
        FieldPanel("price"),
        FieldPanel("description")
    ]

    class Meta:
        verbose_name_plural = "Menu Items"

    def __str__(self):
        return self.name

class MenuPage(Page):
    menu_hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    menu_hero_text = models.CharField(max_length=250)
    
    content_panels = Page.content_panels + [
        FieldPanel("menu_hero_image"),
        FieldPanel("menu_hero_text"),
        InlinePanel("menu_items", label="Menu Items")
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

class MenuItems(Orderable):
    page = ParentalKey(MenuPage, on_delete=models.CASCADE, related_name="menu_items")
    menu = models.ForeignKey(
        'home.MenuItem',
        on_delete=models.CASCADE,
        related_name="+"
    )
    panels = [
        FieldPanel("menu")
    ]

@register_snippet
class ContactInfo(models.Model):
    title = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    panels = [
        FieldPanel("title"),
        FieldPanel("info")
    ]

    class Meta:
        verbose_name_plural = "Contact Info"

    def __str__(self) -> str:
        return self.title

class ContactPage(Page):
    page_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("page_image"),
        InlinePanel("contact_details", label="Contact Information")
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []


class ContactDetails(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name="contact_details")
    contact_info = models.ForeignKey(
        'home.ContactInfo',
        on_delete=models.CASCADE,
        related_name="+"
    )
    panels = [
        FieldPanel("contact_info")
    ]


class FormField(AbstractFormField):
    page = ParentalKey("FormPage", on_delete=models.CASCADE, related_name="form_fields")

class FormPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address", classname="col6"),
                FieldPanel("to_address", classname="col6")
            ]),
            FieldPanel("subject")
        ], "Email")
    ]