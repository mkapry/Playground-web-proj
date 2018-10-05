from django.contrib import admin
from .models import Course, HoleStats, Hole
from .models import Stats
from .models import Game


class StatsInline(admin.StackedInline):
    model = Stats
    extra = 1

class HoleInline(admin.StackedInline):
    model = Hole
    extra = 18
    max_num = 18

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [HoleInline]


admin.site.register(Stats)

class GameAdmin(admin.ModelAdmin):
    inlines = [StatsInline]
admin.site.register(Game, GameAdmin)
admin.site.register(Hole)
admin.site.register(HoleStats)
