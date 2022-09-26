from django.contrib import admin
from conferences.models.attendance_talk import AttendanceTalk
from rangefilter.filters import DateRangeFilter
from conferences.filters.dropdown_filter import RelatedDropdownFilter



class AttendanceTalkAdmin(admin.ModelAdmin):
    model = AttendanceTalk
    list_display = (
        'id',
        'profile',
        'talk_room',
    )
    search_fields = (
        "profile",
        "talk_room__talk",
        "talk_room__room",
    )
    autocomplete_fields = (
        "profile",
        "talk_room",
    )
    list_filter = (
        ("talk_room__talk", RelatedDropdownFilter),
        #("date", DateRangeFilter),
    )
