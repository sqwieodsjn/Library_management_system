from django.contrib import admin
from .models import Author, Category, Book, Member, BorrowRecord


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "email",
        "phone",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
    )

    ordering = (
        "full_name",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "created_at",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "available_copies",
        "price",
    )

    search_fields = (
        "title",
        "isbn",
    )

    list_filter = (
        "category",
        "author",
    )

    ordering = (
        "title",
    )

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "member_id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "is_active",
    )

    search_fields = (
        "member_id",
        "first_name",
        "last_name",
        "email",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "member_id",
    )

    
@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):

    list_display = (
        "member",
        "book",
        "borrow_date",
        "due_date",
        "return_date",
        "status",
    )

    search_fields = (
        "member__member_id",
        "book__title",
    )

    list_filter = (
        "status",
        "borrow_date",
    )

    ordering = (
        "-borrow_date",
    )