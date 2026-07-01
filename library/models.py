from django.db import models


class Author(models.Model):

    full_name = models.CharField(max_length=200)

    email = models.EmailField(
        blank=True,
        null=True,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    biography = models.TextField(
        blank=True,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.full_name


class Category(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(
        max_length=255
    )

    isbn = models.CharField(
        max_length=20,
        unique=True
    )

    publication_date = models.DateField()

    language = models.CharField(
        max_length=50
    )

    total_copies = models.PositiveIntegerField()

    available_copies = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

class Member(models.Model):

    member_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    joined_date = models.DateField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.member_id} - {self.first_name} {self.last_name}"


class BorrowRecord(models.Model):

    STATUS_CHOICES = [
        ("BORROWED", "Borrowed"),
        ("RETURNED", "Returned"),
        ("OVERDUE", "Overdue"),
    ]

    member = models.ForeignKey(
        Member,
        on_delete=models.PROTECT,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
    )

    borrow_date = models.DateField()

    due_date = models.DateField()

    return_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="BORROWED",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.member.member_id} - {self.book.title}"