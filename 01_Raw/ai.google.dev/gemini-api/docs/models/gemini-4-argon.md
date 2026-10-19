---
source_url: https://ai.google.dev/gemini-api/docs/models/gemini-4-argon?hl=fa
fetched_at: 2026-10-19T05:46:59.441848+00:00
title: "\u202bGemini 4 Argon \u00a0|\u00a0 Gemini API \u00a0|\u00a0 Google AI for Developers"
---

‫Gemini 4 Argon اکنون دردسترس است. [امتحان کنید](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa).

![](https://ai.google.dev/_static/images/translated.svg?hl=fa)

‫Google برای ترجمه محتوا به زبان ترجیحی شما از فناوری هوشواره استفاده می‌کند. ترجمه‌های هوشواره‌ای ممکن است اشتباه داشته باشند.

- [صفحه اصلی](https://ai.google.dev/?hl=fa)
- [Gemini API](https://ai.google.dev/gemini-api?hl=fa)
- [سندنگار](https://ai.google.dev/gemini-api/docs?hl=fa)

ارسال بازخورد

# ‫Gemini 4 Argon

‫Gemini 4 Argon (`gemini-4-argon`) مدل استدلال پرچم‌دار ما است که برای مهندسی نرم‌افزار پیچیده، حل مسائل عمیق ریاضی و علمی، عامل‌های چندمرحله‌ای خودکار، و رمزگشایی طولانی تا ۱ میلیون توکن ساخته شده است.

[امتحان کردن در Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-4-argon&hl=fa)

## اسناد

برای پوشش کامل ویژگی‌ها، تغییرات API، و راهنمایی‌های انتقال، به صفحه [جدیدترین مدل](https://ai.google.dev/gemini-api/docs/latest-model?hl=fa) مراجعه کنید.

## gemini-4-argon

| دارایی | شرح |
| --- | --- |
| id\_cardکد مدل | `gemini-4-argon` |
| ذخیرهانواع داده‌های پشتیبانی‌شده | **ورودی‌ها**  نوشتار، تصویر، ویدیو، صدا، و PDF  **خروجی**  نوشتار |
| token\_autoمحدودیت‌های نشان[[\*]](https://ai.google.dev/gemini-api/docs/tokens?hl=fa) | **پنجره بافت (محدودیت یکپارچه ورودی و خروجی نشانه)**  1,048,576  **حداکثر برونداد**  ‫۶۵٬۵۳۶ (هم‌زمان پیش‌فرض) / تا ۱٬۰۴۸٬۵۷۶ (با [رمزگشایی طولانی](https://ai.google.dev/gemini-api/docs/long-decode?hl=fa)) |
| handymanقابلیت‌ها | **[درک ویدیو با عامل هوش مصنوعی](https://ai.google.dev/gemini-api/docs/video-understanding?hl=fa#agentic-video-understanding)**  پشتیبانی‌شده (پیش‌فرض `static` است)  **[تولید صدا](https://ai.google.dev/gemini-api/docs/speech-generation?hl=fa)**  پشتیبانی نمی‌شود  **[ذخیره در حافظه نهان](https://ai.google.dev/gemini-api/docs/caching?hl=fa)**  پشتیبانی‌شده (فقط ضمنی)  توجه: ذخیره‌سازی صریح در حافظه نهان پشتیبانی نمی‌شود.  **[اجرای کد](https://ai.google.dev/gemini-api/docs/code-execution?hl=fa)**  پشتیبانی‌شده  **[استفاده از رایانه](https://ai.google.dev/gemini-api/docs/computer-use?hl=fa)**  پشتیبانی‌شده (پیش‌نمایش)  **[جستجوی فایل](https://ai.google.dev/gemini-api/docs/file-search?hl=fa)**  پشتیبانی‌شده  **[فراخوانی تابع](https://ai.google.dev/gemini-api/docs/function-calling?hl=fa)**  پشتیبانی‌شده  **[پایه‌مندسازی با Google Maps](https://ai.google.dev/gemini-api/docs/maps-grounding?hl=fa)**  پشتیبانی‌شده  **[تولید تصویر](https://ai.google.dev/gemini-api/docs/image-generation?hl=fa)**  پشتیبانی نمی‌شود  **[Live API](https://ai.google.dev/gemini-api/docs/live-api?hl=fa)**  پشتیبانی نمی‌شود  **[زمینه‌سازی جستجو](https://ai.google.dev/gemini-api/docs/google-search?hl=fa)**  پشتیبانی‌شده  **[بروندادهای ساختاریافته](https://ai.google.dev/gemini-api/docs/structured-output?hl=fa)**  پشتیبانی‌شده  **[درحال فکر کردن](https://ai.google.dev/gemini-api/docs/thinking?hl=fa)**  پشتیبانی‌شده (کم، متوسط، زیاد)  **[بافت نشانی وب](https://ai.google.dev/gemini-api/docs/url-context?hl=fa)**  پشتیبانی‌شده |
| ‫speedگزینه‌های مصرف | **[Batch API](https://ai.google.dev/gemini-api/docs/batch-api?hl=fa)**  پشتیبانی‌شده  **[استنتاج انعطاف‌پذیر](https://ai.google.dev/gemini-api/docs/flex-inference?hl=fa)**  پشتیبانی‌شده  **[استنباط اولویت](https://ai.google.dev/gemini-api/docs/priority-inference?hl=fa)**  پشتیبانی‌شده |
| ‫۱۲۳نسخه | برای جزئیات بیشتر، [الگوهای نسخه مدل](https://ai.google.dev/gemini-api/docs/models?hl=fa#model-versions) را بخوانید.  - پایدار: `gemini-4-argon` |
| calendar\_monthجدیدترین به‌روزرسانی | اکتبر ۲۰۲۶ |
| id\_cardکارت مدل | [کارت مدل](https://deepmind.google/models/model-cards/gemini-4-argon/?hl=fa) |

ارسال بازخورد

جز در مواردی که غیر از این ذکر شده باشد،‌محتوای این صفحه تحت مجوز [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/) است. نمونه کدها نیز دارای مجوز [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0) است. برای اطلاع از جزئیات، به [خطمشی‌های سایت Google Developers‏](https://developers.google.com/site-policies?hl=fa) مراجعه کنید. جاوا علامت تجاری ثبت‌شده Oracle و/یا شرکت‌های وابسته به آن است.

تاریخ آخرین به‌روزرسانی 2026-10-14 به‌وقت ساعت هماهنگ جهانی.

می‌خواهید موارد بیشتری را با ما درمیان بگذارید؟

[[["درک آسان","easyToUnderstand","thumb-up"],["مشکلم را برطرف کرد","solvedMyProblem","thumb-up"],["غیره","otherUp","thumb-up"]],[["اطلاعاتی که نیاز دارم وجود ندارد","missingTheInformationINeed","thumb-down"],["بیش‌ازحد پیچیده/ مراحل بسیار زیاد","tooComplicatedTooManySteps","thumb-down"],["قدیمی","outOfDate","thumb-down"],["مشکل ترجمه","translationIssue","thumb-down"],["مشکل کد / نمونه‌ها","samplesCodeIssue","thumb-down"],["غیره","otherDown","thumb-down"]],["تاریخ آخرین به‌روزرسانی 2026-10-14 به‌وقت ساعت هماهنگ جهانی."],[],[]]
