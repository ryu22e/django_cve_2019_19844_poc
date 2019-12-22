# django_cve_2019_19844_poc
PoC for [CVE-2019-19844](https://www.djangoproject.com/weblog/2019/dec/18/security-releases/)

![](https://github.com/ryu22e/django_cve_2019_19844_poc/workflows/django_cve_2019_19844_poc/badge.svg)

## Setup

```python
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> User.objects.create_user('mike123', 'mike@example.org', 'test123')
```
