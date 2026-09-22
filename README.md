# License Picker

A small, offline Python CLI and library for comparing common open-source licenses and narrowing the catalog by practical requirements. It is designed to make an initial license discussion clearer without pretending to replace legal review.

> **Important:** License Picker provides concise educational summaries, not legal advice. Always read the full official license text before licensing a real project.

## Why it exists

Choosing a license often starts with a few concrete questions: Do I need an explicit patent grant? Do I want copyleft? Must redistributed copies retain notices? License Picker turns those questions into transparent filters and side-by-side facts that work locally and in scripts.

## Key features

- Built-in summaries for MIT, Apache-2.0, GPL-3.0, LGPL-3.0, MPL-2.0, BSD-3-Clause, and The Unlicense.
- Compare permissions, conditions, limitations, patent grants, notice requirements, and copyleft style.
- Filter by explicit patent grant, copyleft level, and notice requirement.
- Human-readable output or stable JSON for automation.
- Python API for embedding the same catalog and filters.
- No network calls, telemetry, credentials, runtime dependencies, or project-code execution.
- Clear errors and non-zero exit status for invalid license identifiers.

## Preview

```text
$ license-picker pick --patent-grant --copyleft none
Apache License 2.0 (apache-2.0)
  Copyleft: none
  Patent grant: yes
  Permissions: commercial use, modification, distribution, private use, patent use
  Conditions: include license, state significant changes, preserve notices
  Limitations: liability, warranty, trademark use
```

For screenshots, capture the terminal output above after installation; the project intentionally has no graphical interface.

## Requirements

- Python 3.10 or newer
- pip for installation

## Installation

From a clone:

```bash
git clone https://github.com/rad03i2/license-picker.git
cd license-picker
python -m pip install -e .
```

For development and tests:

```bash
python -m pip install -e . pytest
```

## Usage

List the catalog:

```bash
license-picker list
```

Inspect one license:

```bash
license-picker show apache-2.0
```

Compare licenses:

```bash
license-picker compare mit apache-2.0 mpl-2.0
```

Require an explicit patent grant without copyleft:

```bash
license-picker pick --patent-grant --copyleft none
```

Find entries that do not require retaining a notice:

```bash
license-picker pick --no-notice
```

Machine-readable output:

```bash
license-picker compare mit gpl-3.0 --json
```

Module execution is also supported:

```bash
python -m license_picker list
```

## Configuration

There is no configuration file and no environment variable is required. `pick` supports these filters:

| Option | Meaning |
|---|---|
| `--patent-grant` | Require an explicit patent grant in the summarized license |
| `--copyleft any` | Do not filter by copyleft |
| `--copyleft none` | Permissive/no copyleft |
| `--copyleft file` | File-level copyleft |
| `--copyleft library` | Library/weak copyleft |
| `--copyleft strong` | Strong copyleft |
| `--require-notice` | Require retention/inclusion of a notice or license text |
| `--no-notice` | Select entries without that summarized requirement |

## Python API

```python
from license_picker import compare, get_license, recommend

apache = get_license("apache-2.0")
permissive_with_patents = recommend(patent_grant=True, copyleft="none")
choices = compare(["mit", "apache-2.0"])
```

Returned values are immutable `License` dataclass instances and expose `to_dict()` for serialization.

## Project structure

```text
src/license_picker/
  __init__.py     Public API and version
  __main__.py     `python -m license_picker` entry point
  core.py         Catalog, lookup, comparison, filtering
  cli.py          CLI parsing, formatting, JSON and exit codes
tests/
  test_core.py    Engine tests
  test_cli.py     CLI behavior tests
.github/workflows/ci.yml
```

## Testing

```bash
python -m compileall -q src
pytest -q
license-picker list --json
```

GitHub Actions runs the same package on Ubuntu, Windows, and macOS with Python 3.10, 3.12, and 3.13.

## Security and privacy

All processing is local. License Picker does not read your repository, send data to a service, execute project files, or request secrets. See [SECURITY.md](SECURITY.md) for the reporting policy.

## Limitations

- The catalog is intentionally small and does not cover every OSI-approved, source-available, content, data, or proprietary license.
- Summaries simplify legal language and cannot capture every obligation or compatibility question.
- Filters express user-selected properties; they do not decide what license is legally suitable for a specific project.
- Patent, trademark, attribution, dependency-license compatibility, jurisdiction, contributor agreements, and relicensing can require professional review.
- The tool does not scan dependencies or an existing codebase for license compliance.

## Optional roadmap

Potential future work includes additional well-reviewed licenses, an interactive questionnaire, and exportable comparison tables. These are optional improvements, not currently implemented features.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Changes to license facts should be checked carefully against authoritative license texts and accompanied by tests.

## License

The License Picker **software itself** is released under the [MIT License](LICENSE). This does not mean the licenses described by the tool are MIT-licensed.

## Author

**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**

---

# License Picker — العربية

أداة Python صغيرة تعمل محليًا دون اتصال بالإنترنت، وتوفر واجهة أوامر ومكتبة برمجية لمقارنة مجموعة من تراخيص المصادر المفتوحة وتضييق الخيارات حسب متطلبات عملية. هدفها تسهيل النقاش الأولي حول اختيار الترخيص من دون الادعاء بأنها بديل عن المراجعة القانونية.

> **تنبيه مهم:** الملخصات تعليمية وليست استشارة قانونية. اقرأ دائمًا النص الرسمي الكامل للترخيص قبل اعتماده في مشروع حقيقي.

## لماذا هذا المشروع؟

غالبًا يبدأ اختيار الترخيص بأسئلة واضحة: هل أحتاج إلى منح صريح لحقوق براءات الاختراع؟ هل أريد copyleft؟ هل يجب الاحتفاظ بإشعار الترخيص عند التوزيع؟ تحول الأداة هذه الأسئلة إلى مرشحات واضحة ومعلومات قابلة للمقارنة محليًا أو ضمن الأتمتة.

## الميزات الرئيسية

- ملخصات مدمجة لـ MIT وApache-2.0 وGPL-3.0 وLGPL-3.0 وMPL-2.0 وBSD-3-Clause وThe Unlicense.
- مقارنة الصلاحيات والشروط والقيود ومنح البراءات ومتطلبات الإشعار ونمط copyleft.
- تصفية حسب منح البراءات ودرجة copyleft ومتطلبات الإشعار.
- إخراج مقروء للمستخدم أو JSON للأتمتة.
- Python API لاستخدام المحرك داخل برامج أخرى.
- لا اتصال بالشبكة، ولا telemetry، ولا مفاتيح API، ولا اعتماديات تشغيل خارجية، ولا تنفيذ لكود المشاريع.
- أخطاء واضحة ورمز خروج غير صفري عند إدخال معرف ترخيص غير صحيح.

## المعاينة

```text
license-picker pick --patent-grant --copyleft none
```

يعرض الأمر التراخيص المدمجة التي تطابق الشرطين مع الصلاحيات والشروط والقيود. لا توجد واجهة رسومية؛ ويمكن أخذ لقطة شاشة من الطرفية عند الحاجة لعرض المشروع.

## المتطلبات والتثبيت

يتطلب Python 3.10 أو أحدث.

```bash
git clone https://github.com/rad03i2/license-picker.git
cd license-picker
python -m pip install -e .
```

وللتطوير والاختبارات:

```bash
python -m pip install -e . pytest
```

## الاستخدام

```bash
license-picker list
license-picker show apache-2.0
license-picker compare mit apache-2.0 mpl-2.0
license-picker pick --patent-grant --copyleft none
license-picker pick --no-notice
license-picker compare mit gpl-3.0 --json
python -m license_picker list
```

## الإعداد

لا تحتاج الأداة إلى ملف إعداد أو متغيرات بيئة. يدعم أمر `pick` مرشحات منح البراءات، وcopyleft بالقيم `any` و`none` و`file` و`library` و`strong`، وكذلك `--require-notice` و`--no-notice`.

## Python API

```python
from license_picker import compare, get_license, recommend

apache = get_license("apache-2.0")
choices = recommend(patent_grant=True, copyleft="none")
comparison = compare(["mit", "apache-2.0"])
```

النتائج عبارة عن كائنات `License` غير قابلة للتغيير وتوفر `to_dict()` للتسلسل.

## بنية المشروع

- `src/license_picker/core.py`: الكتالوج ومحرك البحث والتصفية والمقارنة.
- `src/license_picker/cli.py`: واجهة الأوامر وJSON ومعالجة الأخطاء.
- `tests/`: اختبارات المحرك والواجهة.
- `.github/workflows/ci.yml`: اختبارات متعددة الأنظمة وإصدارات Python.

## الاختبارات

```bash
python -m compileall -q src
pytest -q
license-picker list --json
```

يضبط GitHub Actions مصفوفة اختبار على Ubuntu وWindows وmacOS مع Python 3.10 و3.12 و3.13.

## الأمان والخصوصية

كل المعالجة محلية. لا تقرأ الأداة مستودعك، ولا ترسل بيانات إلى خدمة خارجية، ولا تنفذ ملفات المشروع، ولا تطلب أسرارًا أو بيانات اعتماد. راجع [SECURITY.md](SECURITY.md) للتفاصيل.

## القيود

- الكتالوج محدود عمدًا ولا يشمل كل التراخيص المتاحة.
- الملخصات تبسط النصوص القانونية ولا تغطي كل التزامات الترخيص أو حالات التوافق.
- المرشحات لا تحدد قانونيًا ما هو الترخيص المناسب لمشروع معين.
- قضايا البراءات والعلامات التجارية والتوافق بين تراخيص الاعتماديات وإعادة الترخيص قد تحتاج مراجعة متخصصة.
- الأداة لا تفحص اعتماديات المشروع أو الكود الحالي للتحقق من الامتثال.

## تطوير اختياري مستقبلًا

يمكن مستقبلًا إضافة تراخيص موثقة أخرى، واستبيان تفاعلي، وتصدير جداول مقارنة. هذه أفكار اختيارية وليست ميزات موجودة حاليًا.

## المساهمة

راجع [CONTRIBUTING.md](CONTRIBUTING.md). يجب التحقق بعناية من أي تعديل على معلومات التراخيص وإضافة اختبارات مناسبة.

## الترخيص

برنامج License Picker نفسه منشور تحت [ترخيص MIT](LICENSE). هذا لا يعني أن التراخيص التي تصفها الأداة منشورة تحت MIT.

## المؤلف

**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**
