# Copyright © Michal Čihař <michal@weblate.org>

# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.0.6 on 2024-06-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0010_alter_subscription_notification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="notification",
            field=models.CharField(
                choices=[
                    (
                        "RepositoryNotification",
                        "Operation was performed in the repository",
                    ),
                    ("LockNotification", "Component was locked or unlocked"),
                    ("LicenseNotification", "License was changed"),
                    ("ParseErrorNotification", "Parse error occurred"),
                    ("NewStringNotificaton", "String is available for translation"),
                    (
                        "NewContributorNotificaton",
                        "Contributor made their first translation",
                    ),
                    ("NewSuggestionNotificaton", "Suggestion was added"),
                    ("LanguageTranslatedNotificaton", "Language was translated"),
                    ("ComponentTranslatedNotificaton", "Component was translated"),
                    ("NewCommentNotificaton", "Comment was added"),
                    ("MentionCommentNotificaton", "You were mentioned in a comment"),
                    (
                        "LastAuthorCommentNotificaton",
                        "Your translation received a comment",
                    ),
                    ("TranslatedStringNotificaton", "String was edited by user"),
                    ("ApprovedStringNotificaton", "String was approved"),
                    ("ChangedStringNotificaton", "String was changed"),
                    (
                        "NewTranslationNotificaton",
                        "New language was added or requested",
                    ),
                    (
                        "NewComponentNotificaton",
                        "New translation component was created",
                    ),
                    ("NewAnnouncementNotificaton", "Announcement was published"),
                    ("NewAlertNotificaton", "New alert emerged in a component"),
                    ("MergeFailureNotification", "Repository operation failed"),
                    ("PendingSuggestionsNotification", "Pending suggestions exist"),
                    ("ToDoStringsNotification", "Unfinished strings exist"),
                ],
                max_length=100,
            ),
        ),
    ]
