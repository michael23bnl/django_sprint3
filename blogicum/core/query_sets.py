from blog.models import Post, Category
from django.utils import timezone


def post_query():
    """Результат запроса к таблице blog_post."""
    query_set = (
        Post.objects.select_related(
            "category",
            "location",
            "author",
        )
        .only(
            "title",
            "text",
            "pub_date",
            "author__username",
            "category__title",
            "category__slug",
            "location__name",
        )
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )
    )
    return query_set


def category_query():
    """Результат запроса к таблице blog_category."""
    query_set = Category.objects.filter(is_published=True)
    return query_set
