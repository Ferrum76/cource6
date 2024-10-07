from django.db import models

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок блога")
    content = models.TextField(verbose_name="Содержание блога")
    images = models.ImageField(upload_to="blog/images", verbose_name="Превью блога", blank=True, null=True)
    publish_at = models.DateField(verbose_name="Дата публикации", blank=True, null=True)
    count_views = models.IntegerField(verbose_name="Количество просмотров", default=0)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, verbose_name="Пользователь",
                             help_text="Укажите владельца продукта", **NULLABLE
                             )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        permissions = [
            ("can_edit", "может редактировать блог")
        ]